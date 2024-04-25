#define NODE 0
#define CORES 28
#define HALF 32
#define CONTS 32
#define FREQ_STEP_DES 8
#define MAXSTEP 23

#include <vector>
#include <sstream>
#include <fstream>
#include <iostream>
#include <unistd.h>
#include <string>
#include <cstdlib>
#include <time.h>
#include <cmath>
#include <cassert>

bool train = true;

int core_state[HALF*2];			
bool exec_slowdown[CONTS];
bool exec_okay[CONTS];
int cpus[CONTS];
int cidx = 0;
bool upscaled[CONTS];
bool have_new_sample; 	//If false, do not make new decisions based on this sample. Makes controller robust to the reporting rate.

// Setup and node state
std::string container_name_actual[CONTS];
int num_containers, num_flows, lim[CONTS];

// ContainerState should only contain the latency values.
struct containerState {
    float upscale_desired;
    float exec_desired;
    float avg_exec;
};
containerState _ctr[CONTS];

// File names for the various things needed
std::string _cname[CONTS];      // Container name
std::string _snames[CONTS];     // Stats file names
std::string _fnames[CONTS];     // Frequency file names
std::string _limFile = "workload_qos_profile";	// Change this to the file generated by set_service_targets.cpp

// Resource change
std::string stats1 = "/home/cc/paper_setup/shared/";	// Change this to the location where the containers map the reporting files.
std::string cpufreq1 = "/sys/devices/system/cpu/cpu";
std::string cpufreq2 = "/cpufreq/scaling_setspeed";
uint32_t FREQ_ARRAY[24] = {800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000, 2800000, 2900000, 3000000, 3100000};

bool changed_core[CONTS];

// Temporary variables
float maxViolation[CONTS];

// variables for cluster state
int cont_to_cluster[CONTS];         // container to cluster
int num_clusters;                   
int cluster_freqStep[CONTS];        // cluster to freqStep


void read_profile() {
  std::ifstream fpo(_limFile);
  std::string tmpStr;
  int idx;
  float exec, upscale;
  std::string name;

  while(std::getline(fpo, tmpStr)) {
    std::stringstream linestream(tmpStr);
    linestream >> idx >> name >> exec >> upscale;
    if(idx < num_containers) {
	_ctr[idx].exec_desired = 2.0*exec;
	_ctr[idx].upscale_desired = 1.1*upscale;
    }
  }
  fpo.close();
}

/*
 * Functions for starting off with a predefined parititoning.
 */
int next = 0;
void init_cores(int idx, int cores) {
  int start = next;
  for(int i=0; i<cores; i++) {
    core_state[start] = idx; core_state[HALF+start] = idx;
    start++;
  }
  next = start;
  cpus[idx] = cores; lim[idx] = cores; changed_core[idx] = true;
}

void init_cluster() {
  next = 0;	// Reset pointer
  for(int i=0; i<CORES; i++) {
    core_state[i] = -1; core_state[i+HALF] = -1;
  }
  for(int i=CORES; i<HALF; i++) { 
    core_state[i] = -2; core_state[i+HALF] = -2;
  }
}

/* 
 * Functions for setting the allocations to the files/counters.
*/
inline std::string get_cpu_list(int i, bool isBg = false) {
    std::string str = "";
    bool first = true;
    if(isBg) {
        for(int c=0; c<HALF*2; c++) {
	  if(core_state[c] == -1) {
	    if(first) {
	      str += std::to_string(c);
              first = false;
	    } else {
              str += "," + std::to_string(c);
	    }
	  }
	}
    } else {
	int owner = i;
	//std::cout << "Inside: " << owner << " ---> " << _cname[i] << "\n";
        for(int c=0; c<HALF*2; c++) {
	  if(core_state[c] == owner) {
	    if(first) {
	      str += std::to_string(c);
              first = false;
	    } else {
              str += "," + std::to_string(c);
	    }
	  }
	}
    }
    return str;
} 

void do_all_allocations() {
    // Enforce core allocations
    // Each cluster must have at least one core to avoid pathological cond
    for(int i=0; i<num_clusters; i++) {
        if(changed_core[i] && cpus[i] > 0) {
            std::string str = ("docker update --cpuset-cpus " + get_cpu_list(i) + " ");
            for(int it=0; it<num_containers; it++) {
		if(cont_to_cluster[it] == i) {
		  if(get_cpu_list(i) == "") {
			printf("No cores allocated to cluster %d container %d\n", i, it);
			exit(-1);
		  }
		  //std::cout << str << container_name_actual[it] << "\n";
                  system((str + container_name_actual[it]).c_str());
		}
	    }
        }
    }
}

/*
 * Functions to update internal variables used for state assignment. do_all_allocations() depends on the output of this
 */
inline void update_freq(int i, int step) {
  if(step < 0)
      return;
  cluster_freqStep[i] = step;

  // Write to freq files.
  for(int c=0; c<CORES; c++) {
    if(core_state[c] == i) {
      FILE* fp = fopen(_fnames[c].c_str(), "w");
      if(fp == nullptr) {
          std::cout << "Could not open freq file with name " << _fnames[c] << "\n";
          exit(-1);
        }
        fprintf(fp, "%i", FREQ_ARRAY[step]);
        fflush(fp);
        fclose(fp);
      }
    }
}

void add_core(int owner) {
  for(int i=cidx; i<CORES; i++) {
    if(core_state[i] == -1) {
      // Found idle core, reallocate.
      changed_core[owner] = 1;
      core_state[i] = owner; core_state[i+HALF] = owner;
      cidx++;
      cpus[owner]++;
      return;
    }
  }
  for(int i=0; i<cidx; i++) {
    if(core_state[i] == -1) {
      // Found idle core, reallocate.
      changed_core[owner] = 1;
      core_state[i] = owner; core_state[i+HALF] = owner;
      cidx++;
      cpus[owner]++;
      return;
    }
  }
}

void yield_core(int owner) {
  changed_core[owner] = 1;
  for(int i=cidx; i<CORES; i++) {
    if(core_state[i] == owner) {
      // Found idle core, reallocate.
      core_state[i] = -1; core_state[i+HALF] = -1;
      cpus[owner]--;
      cidx++;
      return;
    }
  }
  for(int i=0; i<cidx; i++) {
    if(core_state[i] == owner) {
      // Found idle core, reallocate.
      core_state[i] = -1; core_state[i+HALF] = -1;
      cidx++;
      cpus[owner]--;
      return;
    }
  }
}
/*
 * Functions which read system state and provide inputs for core inc./dec. functions
 */
void read_stats_file() {
  float blah1, blah2, blah3, blah4;
  int same = 0, read = 0;
  for(int i=0; i<num_clusters; i++) {
    exec_slowdown[i] = false;
    exec_okay[i] = false;
    maxViolation[i] = 0;
  }
  have_new_sample = true;
  // Check whether we are reading the same numbers as last time, and if yes, don't change anything. 
  // Read all the stats files.
  for(int i=0; i<num_containers; i++) {
    bool issame = false; 

    int owner = cont_to_cluster[i];
    std::ifstream fp(_snames[i]);
    if(fp.fail()) {
        _ctr[i].avg_exec = -1;
        exec_okay[owner] = false;
    } 
    else {
      std::string tmpStr;
      std::getline(fp, tmpStr);
      if(tmpStr.size() < 5) {
        exec_okay[owner] = false;
        continue;
      }
      read++;
      std::stringstream linestream(tmpStr);
      linestream >> blah2 >> blah3 >> blah1;
      if(blah3 == _ctr[i].avg_exec) {
        same++;
        issame = true;
      }
      _ctr[i].avg_exec = blah3;

      float exec_metric = (_ctr[i].avg_exec)/(_ctr[i].exec_desired);

      // Containers with very small avg exec time (mongodb) can naturally have wild variations, do not upscale them
      if(_ctr[i].exec_desired < 0.002) { 
        exec_okay[owner] = false;
        exec_slowdown[owner] = false;
      } else {
        if(exec_metric > 1.05 && !issame)
          exec_slowdown[owner] = true;
        if(exec_metric < 0.95 && !issame)
          exec_okay[owner] = true; 
        if(exec_metric > maxViolation[owner])
          maxViolation[owner] = exec_metric;
      }
      fp.close();
    }
  }
  for(int i=0; i<num_clusters; i++) {
    if(exec_slowdown[i] && exec_okay[i])
      exec_okay[i] = false;
  }
  if(read == same)	have_new_sample = false;
}

/*
 * Calculations for the core algorithm.
 */
void increase_resources() {
    // Completely operates on clusterid
    // This functions has to be changed between versions
    float max = -1;
    int maxIdx = -1;

    for(int i=0; i<num_clusters; i++) {
        upscaled[i] = false;
    }

    while(1) {
        max = -1;
        for(int i=0; i<num_clusters; i++) {
	  if(exec_slowdown[i] && !upscaled[i]) {
	    if(maxViolation[i] > max) {
              max = maxViolation[i];
              maxIdx = i;
            }
          }
        }
        if(max < 0) // Nothing to upscale any more
          return;
        
        int owner = maxIdx;
        upscaled[owner] = true;
	float sel = (float)rand()/(float)RAND_MAX;
	if(sel < 0.5 && cluster_freqStep[owner] < MAXSTEP) {
	  // Upscale frequency by 1 pt.
          update_freq(owner, MAXSTEP);
        }
	else {
          add_core(owner);
        } 
    } 
    return;
}

void recover_resources() {
    // Completely operates on clusterid
    for(int i=0; i<num_clusters; i++) {
      if(exec_okay[i]) {
       float select = (float)rand()/(float)RAND_MAX;
       bool fallthrough = false;
       if(select < 0.5) {
         if(cluster_freqStep[i] > FREQ_STEP_DES)  
             update_freq(i, cluster_freqStep[i] -1);
         else
             fallthrough = true;
       } 
       if((select >= 0.5) || fallthrough) {
         // cores
         if(cpus[i] > lim[i])
          yield_core(i);
       } 
      }
    }
}

/*
 * Initialization and profile update functions
 */
void set_up_names() {
    int t_num_clusters, t_num_containers;

    std::ifstream file("/home/cc/paper_setup/config/config_cluster");	// Change to name of the config file.

    // First read the file and find the actual container names. Write them into file "container_names". Not needed if container names match what is provided in the config file.
    std::string line, line2;
    std::getline(file, line);

    t_num_containers = std::stoi(line);
    std::getline(file, line);
    t_num_clusters = std::stoi(line);
    for(int i=0; i<t_num_containers; i++) {
      std::getline(file, line);
      std::stringstream linestream(line);

      std::string data, name;
      int id, this_node;

      linestream >> id >> this_node >> name >> data;
      if(this_node != NODE)
        continue;

      std::system(("docker inspect --format '{{.Name}}' $(docker ps -q) | grep " +  name + ">> container_names").c_str());
    }
    file.close();
}

void initialize() {
    for(int i=0; i<CONTS; i++) {
        upscaled[i] = false;
	cluster_freqStep[i] = 7;
    }

    for(int i=0; i<CONTS; i++) {
        _fnames[i] = cpufreq1+std::to_string(i)+cpufreq2;
    }
    init_cluster();

    int t_num_clusters, t_num_containers;
    std::ifstream file("/home/cc/paper_setup/config/config_social_cluster");
    std::ifstream file2("container_names");
    std::string line, line2;
    std::getline(file, line);

    t_num_containers = std::stoi(line);
    std::getline(file, line);
    t_num_clusters = std::stoi(line);

    num_clusters = 0; num_containers = 0;
    // Read the input file and set up things.
    int cnt=0; float discard;
    for(int i=0; i<t_num_containers; i++) {
      std::getline(file, line);
      std::stringstream linestream(line);
        
      int id, this_node;
      std::string name;
      int clusterID; int num_cores;

      linestream >> id >> this_node >> name;
      if(this_node != NODE)
        continue;
      
      std::getline(file2, line2); 
      _cname[cnt] = name;
      container_name_actual[cnt] = line2;
      
      linestream >> _ctr[cnt].exec_desired >> discard;
      linestream >> clusterID >> num_cores;

      cont_to_cluster[cnt] = clusterID;
      _ctr[cnt].avg_exec = _ctr[cnt].exec_desired;
      _snames[cnt] = stats1+name;

      init_cores(clusterID, num_cores);
      if(clusterID > num_clusters)
        num_clusters = clusterID;
      
      num_containers++;
      cnt++;
    }
    num_clusters++;
    file.close();
    file2.close();

    do_all_allocations();
}


void decide() {
  read_stats_file();
  if(have_new_sample) {
    recover_resources();
    increase_resources();
    do_all_allocations();
  }
}

/*
 * Main() function
 */
int main(int argc, char* argv[]) {
    int core_sum = 0;
    float full_sum = 0;
    float full_time = 0;
    int cnt_sanity = 0;

    float warmup = 30000;
    bool warmed = false;

    for(int i=0; i<CONTS; i++) {
      cpus[i] = 0;
    }
    set_up_names();
    initialize();
    read_profile();

    int i=0;
    struct timespec ts1, ts2, ts3;
    clock_gettime(CLOCK_REALTIME, &ts1);
   
    // Warm for 30s and then poll for 60s.
    do {
       clock_gettime(CLOCK_REALTIME, &ts2);
	i++;
       for(int ii=0; ii<num_clusters; ii++) {
           changed_core[ii] = false;
           upscaled[ii] = false;
       }
       decide();
       usleep(100000);	// Every 100ms

       core_sum = 0;
       for(int ii=0; ii<HALF*2; ii++) {
	   if(core_state[ii] >= 0) {
	    core_sum++;
	   }
       }
	clock_gettime(CLOCK_REALTIME, &ts3);
	if ((ts3.tv_sec-ts1.tv_sec)*1000 + (ts3.tv_nsec-ts1.tv_nsec)/1000000.0 < warmup) {
	  full_sum += core_sum*((ts3.tv_sec-ts2.tv_sec)*1000000 + (ts3.tv_nsec-ts2.tv_nsec)/1000.0);
	  full_time += 1*((ts3.tv_sec-ts2.tv_sec)*1000000 + (ts3.tv_nsec-ts2.tv_nsec)/1000.0);
	} else {
	  if(!warmed) {
	    warmed = true;
	    printf("Resetting cluster\n");
	    init_cluster();
	    do_all_allocations();
 	    train = false;
    	    printf("Warmup Phase: CoreUsage (us-cores): %f, avg cores used: %f\n", full_sum, full_sum/full_time);
	    full_sum = 0; full_time = 0;
	  }
	  full_sum += core_sum*((ts3.tv_sec-ts2.tv_sec)*1000000 + (ts3.tv_nsec-ts2.tv_nsec)/1000.0);
	  full_time += 1*((ts3.tv_sec-ts2.tv_sec)*1000000 + (ts3.tv_nsec-ts2.tv_nsec)/1000.0);
	}
   } while (((ts3.tv_sec-ts1.tv_sec)*1000+(ts3.tv_nsec-ts1.tv_nsec)/1000000.0) < 90000);  
    printf("CoreUsage (us-cores): %f, avg cores used: %f\n", full_sum, full_sum/full_time);
    return -1;
}
