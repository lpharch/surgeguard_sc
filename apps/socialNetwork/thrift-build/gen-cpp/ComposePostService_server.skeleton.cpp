// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "ComposePostService.h"
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TSimpleServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

using namespace  ::social_network;

class ComposePostServiceHandler : virtual public ComposePostServiceIf {
 public:
  ComposePostServiceHandler() {
    // Your initialization goes here
  }

  void ComposePost(const int8_t flow, const int64_t timestamp, const int16_t edge, const int64_t req_id, const std::string& username, const int64_t user_id, const std::string& text, const std::vector<int64_t> & media_ids, const std::vector<std::string> & media_types, const PostType::type post_type, const std::map<std::string, std::string> & carrier) {
    // Your implementation goes here
    printf("ComposePost\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  ::apache::thrift::stdcxx::shared_ptr<ComposePostServiceHandler> handler(new ComposePostServiceHandler());
  ::apache::thrift::stdcxx::shared_ptr<TProcessor> processor(new ComposePostServiceProcessor(handler));
  ::apache::thrift::stdcxx::shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  ::apache::thrift::stdcxx::shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  ::apache::thrift::stdcxx::shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

