/**
 * Autogenerated by Thrift Compiler (0.12.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef Ping4Service_H
#define Ping4Service_H

#include <thrift/TDispatchProcessor.h>
#include <thrift/async/TConcurrentClientSyncInfo.h>
#include "social_network_types.h"

namespace social_network {

#ifdef _MSC_VER
  #pragma warning( push )
  #pragma warning (disable : 4250 ) //inheriting methods via dominance 
#endif

class Ping4ServiceIf {
 public:
  virtual ~Ping4ServiceIf() {}
  virtual void Ping(const int8_t flow, const int64_t timestamp, const int16_t level, const int64_t req_id) = 0;
};

class Ping4ServiceIfFactory {
 public:
  typedef Ping4ServiceIf Handler;

  virtual ~Ping4ServiceIfFactory() {}

  virtual Ping4ServiceIf* getHandler(const ::apache::thrift::TConnectionInfo& connInfo) = 0;
  virtual void releaseHandler(Ping4ServiceIf* /* handler */) = 0;
};

class Ping4ServiceIfSingletonFactory : virtual public Ping4ServiceIfFactory {
 public:
  Ping4ServiceIfSingletonFactory(const ::apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf>& iface) : iface_(iface) {}
  virtual ~Ping4ServiceIfSingletonFactory() {}

  virtual Ping4ServiceIf* getHandler(const ::apache::thrift::TConnectionInfo&) {
    return iface_.get();
  }
  virtual void releaseHandler(Ping4ServiceIf* /* handler */) {}

 protected:
  ::apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf> iface_;
};

class Ping4ServiceNull : virtual public Ping4ServiceIf {
 public:
  virtual ~Ping4ServiceNull() {}
  void Ping(const int8_t /* flow */, const int64_t /* timestamp */, const int16_t /* level */, const int64_t /* req_id */) {
    return;
  }
};

typedef struct _Ping4Service_Ping_args__isset {
  _Ping4Service_Ping_args__isset() : flow(false), timestamp(false), level(false), req_id(false) {}
  bool flow :1;
  bool timestamp :1;
  bool level :1;
  bool req_id :1;
} _Ping4Service_Ping_args__isset;

class Ping4Service_Ping_args {
 public:

  Ping4Service_Ping_args(const Ping4Service_Ping_args&);
  Ping4Service_Ping_args& operator=(const Ping4Service_Ping_args&);
  Ping4Service_Ping_args() : flow(0), timestamp(0), level(0), req_id(0) {
  }

  virtual ~Ping4Service_Ping_args() throw();
  int8_t flow;
  int64_t timestamp;
  int16_t level;
  int64_t req_id;

  _Ping4Service_Ping_args__isset __isset;

  void __set_flow(const int8_t val);

  void __set_timestamp(const int64_t val);

  void __set_level(const int16_t val);

  void __set_req_id(const int64_t val);

  bool operator == (const Ping4Service_Ping_args & rhs) const
  {
    if (!(flow == rhs.flow))
      return false;
    if (!(timestamp == rhs.timestamp))
      return false;
    if (!(level == rhs.level))
      return false;
    if (!(req_id == rhs.req_id))
      return false;
    return true;
  }
  bool operator != (const Ping4Service_Ping_args &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const Ping4Service_Ping_args & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class Ping4Service_Ping_pargs {
 public:


  virtual ~Ping4Service_Ping_pargs() throw();
  const int8_t* flow;
  const int64_t* timestamp;
  const int16_t* level;
  const int64_t* req_id;

  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class Ping4Service_Ping_result {
 public:

  Ping4Service_Ping_result(const Ping4Service_Ping_result&);
  Ping4Service_Ping_result& operator=(const Ping4Service_Ping_result&);
  Ping4Service_Ping_result() {
  }

  virtual ~Ping4Service_Ping_result() throw();

  bool operator == (const Ping4Service_Ping_result & /* rhs */) const
  {
    return true;
  }
  bool operator != (const Ping4Service_Ping_result &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const Ping4Service_Ping_result & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class Ping4Service_Ping_presult {
 public:


  virtual ~Ping4Service_Ping_presult() throw();

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);

};

class Ping4ServiceClient : virtual public Ping4ServiceIf {
 public:
  Ping4ServiceClient(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) {
    setProtocol(prot);
  }
  Ping4ServiceClient(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) {
    setProtocol(iprot,oprot);
  }
 private:
  void setProtocol(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) {
  setProtocol(prot,prot);
  }
  void setProtocol(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) {
    piprot_=iprot;
    poprot_=oprot;
    iprot_ = iprot.get();
    oprot_ = oprot.get();
  }
 public:
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> getInputProtocol() {
    return piprot_;
  }
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> getOutputProtocol() {
    return poprot_;
  }
  void Ping(const int8_t flow, const int64_t timestamp, const int16_t level, const int64_t req_id);
  void send_Ping(const int8_t flow, const int64_t timestamp, const int16_t level, const int64_t req_id);
  void recv_Ping();
 protected:
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> piprot_;
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> poprot_;
  ::apache::thrift::protocol::TProtocol* iprot_;
  ::apache::thrift::protocol::TProtocol* oprot_;
};

class Ping4ServiceProcessor : public ::apache::thrift::TDispatchProcessor {
 protected:
  ::apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf> iface_;
  virtual bool dispatchCall(::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, const std::string& fname, int32_t seqid, void* callContext);
 private:
  typedef  void (Ping4ServiceProcessor::*ProcessFunction)(int32_t, ::apache::thrift::protocol::TProtocol*, ::apache::thrift::protocol::TProtocol*, void*);
  typedef std::map<std::string, ProcessFunction> ProcessMap;
  ProcessMap processMap_;
  void process_Ping(int32_t seqid, ::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, void* callContext);
 public:
  Ping4ServiceProcessor(::apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf> iface) :
    iface_(iface) {
    processMap_["Ping"] = &Ping4ServiceProcessor::process_Ping;
  }

  virtual ~Ping4ServiceProcessor() {}
};

class Ping4ServiceProcessorFactory : public ::apache::thrift::TProcessorFactory {
 public:
  Ping4ServiceProcessorFactory(const ::apache::thrift::stdcxx::shared_ptr< Ping4ServiceIfFactory >& handlerFactory) :
      handlerFactory_(handlerFactory) {}

  ::apache::thrift::stdcxx::shared_ptr< ::apache::thrift::TProcessor > getProcessor(const ::apache::thrift::TConnectionInfo& connInfo);

 protected:
  ::apache::thrift::stdcxx::shared_ptr< Ping4ServiceIfFactory > handlerFactory_;
};

class Ping4ServiceMultiface : virtual public Ping4ServiceIf {
 public:
  Ping4ServiceMultiface(std::vector<apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf> >& ifaces) : ifaces_(ifaces) {
  }
  virtual ~Ping4ServiceMultiface() {}
 protected:
  std::vector<apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf> > ifaces_;
  Ping4ServiceMultiface() {}
  void add(::apache::thrift::stdcxx::shared_ptr<Ping4ServiceIf> iface) {
    ifaces_.push_back(iface);
  }
 public:
  void Ping(const int8_t flow, const int64_t timestamp, const int16_t level, const int64_t req_id) {
    size_t sz = ifaces_.size();
    size_t i = 0;
    for (; i < (sz - 1); ++i) {
      ifaces_[i]->Ping(flow, timestamp, level, req_id);
    }
    ifaces_[i]->Ping(flow, timestamp, level, req_id);
  }

};

// The 'concurrent' client is a thread safe client that correctly handles
// out of order responses.  It is slower than the regular client, so should
// only be used when you need to share a connection among multiple threads
class Ping4ServiceConcurrentClient : virtual public Ping4ServiceIf {
 public:
  Ping4ServiceConcurrentClient(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) {
    setProtocol(prot);
  }
  Ping4ServiceConcurrentClient(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) {
    setProtocol(iprot,oprot);
  }
 private:
  void setProtocol(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) {
  setProtocol(prot,prot);
  }
  void setProtocol(apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) {
    piprot_=iprot;
    poprot_=oprot;
    iprot_ = iprot.get();
    oprot_ = oprot.get();
  }
 public:
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> getInputProtocol() {
    return piprot_;
  }
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> getOutputProtocol() {
    return poprot_;
  }
  void Ping(const int8_t flow, const int64_t timestamp, const int16_t level, const int64_t req_id);
  int32_t send_Ping(const int8_t flow, const int64_t timestamp, const int16_t level, const int64_t req_id);
  void recv_Ping(const int32_t seqid);
 protected:
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> piprot_;
  apache::thrift::stdcxx::shared_ptr< ::apache::thrift::protocol::TProtocol> poprot_;
  ::apache::thrift::protocol::TProtocol* iprot_;
  ::apache::thrift::protocol::TProtocol* oprot_;
  ::apache::thrift::async::TConcurrentClientSyncInfo sync_;
};

#ifdef _MSC_VER
  #pragma warning( pop )
#endif

} // namespace

#endif
