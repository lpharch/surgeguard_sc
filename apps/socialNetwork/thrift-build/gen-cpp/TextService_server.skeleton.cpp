// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "TextService.h"
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TSimpleServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

using namespace  ::social_network;

class TextServiceHandler : virtual public TextServiceIf {
 public:
  TextServiceHandler() {
    // Your initialization goes here
  }

  void ComposeText(TextServiceReturn& _return, const int8_t flow, const int64_t timestamp, const int16_t edge, const int64_t req_id, const std::string& text, const std::map<std::string, std::string> & carrier) {
    // Your implementation goes here
    printf("ComposeText\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  ::apache::thrift::stdcxx::shared_ptr<TextServiceHandler> handler(new TextServiceHandler());
  ::apache::thrift::stdcxx::shared_ptr<TProcessor> processor(new TextServiceProcessor(handler));
  ::apache::thrift::stdcxx::shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  ::apache::thrift::stdcxx::shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  ::apache::thrift::stdcxx::shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

