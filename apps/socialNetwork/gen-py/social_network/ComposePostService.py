#
# Autogenerated by Thrift Compiler (0.12.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def ComposePost(self, flow, timestamp, edge, req_id, username, user_id, text, media_ids, media_types, post_type, carrier):
        """
        Parameters:
         - flow
         - timestamp
         - edge
         - req_id
         - username
         - user_id
         - text
         - media_ids
         - media_types
         - post_type
         - carrier

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def ComposePost(self, flow, timestamp, edge, req_id, username, user_id, text, media_ids, media_types, post_type, carrier):
        """
        Parameters:
         - flow
         - timestamp
         - edge
         - req_id
         - username
         - user_id
         - text
         - media_ids
         - media_types
         - post_type
         - carrier

        """
        self.send_ComposePost(flow, timestamp, edge, req_id, username, user_id, text, media_ids, media_types, post_type, carrier)
        self.recv_ComposePost()

    def send_ComposePost(self, flow, timestamp, edge, req_id, username, user_id, text, media_ids, media_types, post_type, carrier):
        self._oprot.writeMessageBegin('ComposePost', TMessageType.CALL, self._seqid)
        args = ComposePost_args()
        args.flow = flow
        args.timestamp = timestamp
        args.edge = edge
        args.req_id = req_id
        args.username = username
        args.user_id = user_id
        args.text = text
        args.media_ids = media_ids
        args.media_types = media_types
        args.post_type = post_type
        args.carrier = carrier
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ComposePost(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ComposePost_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.se is not None:
            raise result.se
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["ComposePost"] = Processor.process_ComposePost

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_ComposePost(self, seqid, iprot, oprot):
        args = ComposePost_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ComposePost_result()
        try:
            self._handler.ComposePost(args.flow, args.timestamp, args.edge, args.req_id, args.username, args.user_id, args.text, args.media_ids, args.media_types, args.post_type, args.carrier)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ServiceException as se:
            msg_type = TMessageType.REPLY
            result.se = se
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ComposePost", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class ComposePost_args(object):
    """
    Attributes:
     - flow
     - timestamp
     - edge
     - req_id
     - username
     - user_id
     - text
     - media_ids
     - media_types
     - post_type
     - carrier

    """


    def __init__(self, flow=None, timestamp=None, edge=None, req_id=None, username=None, user_id=None, text=None, media_ids=None, media_types=None, post_type=None, carrier=None,):
        self.flow = flow
        self.timestamp = timestamp
        self.edge = edge
        self.req_id = req_id
        self.username = username
        self.user_id = user_id
        self.text = text
        self.media_ids = media_ids
        self.media_types = media_types
        self.post_type = post_type
        self.carrier = carrier

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BYTE:
                    self.flow = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.edge = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.req_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.media_ids = []
                    (_etype110, _size107) = iprot.readListBegin()
                    for _i111 in range(_size107):
                        _elem112 = iprot.readI64()
                        self.media_ids.append(_elem112)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.media_types = []
                    (_etype116, _size113) = iprot.readListBegin()
                    for _i117 in range(_size113):
                        _elem118 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.media_types.append(_elem118)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.post_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.MAP:
                    self.carrier = {}
                    (_ktype120, _vtype121, _size119) = iprot.readMapBegin()
                    for _i123 in range(_size119):
                        _key124 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val125 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.carrier[_key124] = _val125
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ComposePost_args')
        if self.flow is not None:
            oprot.writeFieldBegin('flow', TType.BYTE, 1)
            oprot.writeByte(self.flow)
            oprot.writeFieldEnd()
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 2)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.edge is not None:
            oprot.writeFieldBegin('edge', TType.I16, 3)
            oprot.writeI16(self.edge)
            oprot.writeFieldEnd()
        if self.req_id is not None:
            oprot.writeFieldBegin('req_id', TType.I64, 4)
            oprot.writeI64(self.req_id)
            oprot.writeFieldEnd()
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 5)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 6)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 7)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.media_ids is not None:
            oprot.writeFieldBegin('media_ids', TType.LIST, 8)
            oprot.writeListBegin(TType.I64, len(self.media_ids))
            for iter126 in self.media_ids:
                oprot.writeI64(iter126)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.media_types is not None:
            oprot.writeFieldBegin('media_types', TType.LIST, 9)
            oprot.writeListBegin(TType.STRING, len(self.media_types))
            for iter127 in self.media_types:
                oprot.writeString(iter127.encode('utf-8') if sys.version_info[0] == 2 else iter127)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.post_type is not None:
            oprot.writeFieldBegin('post_type', TType.I32, 10)
            oprot.writeI32(self.post_type)
            oprot.writeFieldEnd()
        if self.carrier is not None:
            oprot.writeFieldBegin('carrier', TType.MAP, 11)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.carrier))
            for kiter128, viter129 in self.carrier.items():
                oprot.writeString(kiter128.encode('utf-8') if sys.version_info[0] == 2 else kiter128)
                oprot.writeString(viter129.encode('utf-8') if sys.version_info[0] == 2 else viter129)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ComposePost_args)
ComposePost_args.thrift_spec = (
    None,  # 0
    (1, TType.BYTE, 'flow', None, None, ),  # 1
    (2, TType.I64, 'timestamp', None, None, ),  # 2
    (3, TType.I16, 'edge', None, None, ),  # 3
    (4, TType.I64, 'req_id', None, None, ),  # 4
    (5, TType.STRING, 'username', 'UTF8', None, ),  # 5
    (6, TType.I64, 'user_id', None, None, ),  # 6
    (7, TType.STRING, 'text', 'UTF8', None, ),  # 7
    (8, TType.LIST, 'media_ids', (TType.I64, None, False), None, ),  # 8
    (9, TType.LIST, 'media_types', (TType.STRING, 'UTF8', False), None, ),  # 9
    (10, TType.I32, 'post_type', None, None, ),  # 10
    (11, TType.MAP, 'carrier', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 11
)


class ComposePost_result(object):
    """
    Attributes:
     - se

    """


    def __init__(self, se=None,):
        self.se = se

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.se = ServiceException()
                    self.se.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ComposePost_result')
        if self.se is not None:
            oprot.writeFieldBegin('se', TType.STRUCT, 1)
            self.se.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ComposePost_result)
ComposePost_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'se', [ServiceException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

