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
    def StorePost(self, flow, timestamp2, edge, req_id, post, carrier):
        """
        Parameters:
         - flow
         - timestamp2
         - edge
         - req_id
         - post
         - carrier

        """
        pass

    def ReadPost(self, flow, timestamp2, edge, req_id, post_id, carrier):
        """
        Parameters:
         - flow
         - timestamp2
         - edge
         - req_id
         - post_id
         - carrier

        """
        pass

    def ReadPosts(self, flow, timestamp2, edge, req_id, post_ids, carrier):
        """
        Parameters:
         - flow
         - timestamp2
         - edge
         - req_id
         - post_ids
         - carrier

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def StorePost(self, flow, timestamp2, edge, req_id, post, carrier):
        """
        Parameters:
         - flow
         - timestamp2
         - edge
         - req_id
         - post
         - carrier

        """
        self.send_StorePost(flow, timestamp2, edge, req_id, post, carrier)
        self.recv_StorePost()

    def send_StorePost(self, flow, timestamp2, edge, req_id, post, carrier):
        self._oprot.writeMessageBegin('StorePost', TMessageType.CALL, self._seqid)
        args = StorePost_args()
        args.flow = flow
        args.timestamp2 = timestamp2
        args.edge = edge
        args.req_id = req_id
        args.post = post
        args.carrier = carrier
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_StorePost(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = StorePost_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.se is not None:
            raise result.se
        return

    def ReadPost(self, flow, timestamp2, edge, req_id, post_id, carrier):
        """
        Parameters:
         - flow
         - timestamp2
         - edge
         - req_id
         - post_id
         - carrier

        """
        self.send_ReadPost(flow, timestamp2, edge, req_id, post_id, carrier)
        return self.recv_ReadPost()

    def send_ReadPost(self, flow, timestamp2, edge, req_id, post_id, carrier):
        self._oprot.writeMessageBegin('ReadPost', TMessageType.CALL, self._seqid)
        args = ReadPost_args()
        args.flow = flow
        args.timestamp2 = timestamp2
        args.edge = edge
        args.req_id = req_id
        args.post_id = post_id
        args.carrier = carrier
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ReadPost(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ReadPost_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.se is not None:
            raise result.se
        raise TApplicationException(TApplicationException.MISSING_RESULT, "ReadPost failed: unknown result")

    def ReadPosts(self, flow, timestamp2, edge, req_id, post_ids, carrier):
        """
        Parameters:
         - flow
         - timestamp2
         - edge
         - req_id
         - post_ids
         - carrier

        """
        self.send_ReadPosts(flow, timestamp2, edge, req_id, post_ids, carrier)
        return self.recv_ReadPosts()

    def send_ReadPosts(self, flow, timestamp2, edge, req_id, post_ids, carrier):
        self._oprot.writeMessageBegin('ReadPosts', TMessageType.CALL, self._seqid)
        args = ReadPosts_args()
        args.flow = flow
        args.timestamp2 = timestamp2
        args.edge = edge
        args.req_id = req_id
        args.post_ids = post_ids
        args.carrier = carrier
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ReadPosts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ReadPosts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.se is not None:
            raise result.se
        raise TApplicationException(TApplicationException.MISSING_RESULT, "ReadPosts failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["StorePost"] = Processor.process_StorePost
        self._processMap["ReadPost"] = Processor.process_ReadPost
        self._processMap["ReadPosts"] = Processor.process_ReadPosts

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

    def process_StorePost(self, seqid, iprot, oprot):
        args = StorePost_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = StorePost_result()
        try:
            self._handler.StorePost(args.flow, args.timestamp2, args.edge, args.req_id, args.post, args.carrier)
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
        oprot.writeMessageBegin("StorePost", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_ReadPost(self, seqid, iprot, oprot):
        args = ReadPost_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ReadPost_result()
        try:
            result.success = self._handler.ReadPost(args.flow, args.timestamp2, args.edge, args.req_id, args.post_id, args.carrier)
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
        oprot.writeMessageBegin("ReadPost", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_ReadPosts(self, seqid, iprot, oprot):
        args = ReadPosts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ReadPosts_result()
        try:
            result.success = self._handler.ReadPosts(args.flow, args.timestamp2, args.edge, args.req_id, args.post_ids, args.carrier)
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
        oprot.writeMessageBegin("ReadPosts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class StorePost_args(object):
    """
    Attributes:
     - flow
     - timestamp2
     - edge
     - req_id
     - post
     - carrier

    """


    def __init__(self, flow=None, timestamp2=None, edge=None, req_id=None, post=None, carrier=None,):
        self.flow = flow
        self.timestamp2 = timestamp2
        self.edge = edge
        self.req_id = req_id
        self.post = post
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
                    self.timestamp2 = iprot.readI64()
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
                if ftype == TType.STRUCT:
                    self.post = Post()
                    self.post.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.MAP:
                    self.carrier = {}
                    (_ktype131, _vtype132, _size130) = iprot.readMapBegin()
                    for _i134 in range(_size130):
                        _key135 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val136 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.carrier[_key135] = _val136
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
        oprot.writeStructBegin('StorePost_args')
        if self.flow is not None:
            oprot.writeFieldBegin('flow', TType.BYTE, 1)
            oprot.writeByte(self.flow)
            oprot.writeFieldEnd()
        if self.timestamp2 is not None:
            oprot.writeFieldBegin('timestamp2', TType.I64, 2)
            oprot.writeI64(self.timestamp2)
            oprot.writeFieldEnd()
        if self.edge is not None:
            oprot.writeFieldBegin('edge', TType.I16, 3)
            oprot.writeI16(self.edge)
            oprot.writeFieldEnd()
        if self.req_id is not None:
            oprot.writeFieldBegin('req_id', TType.I64, 4)
            oprot.writeI64(self.req_id)
            oprot.writeFieldEnd()
        if self.post is not None:
            oprot.writeFieldBegin('post', TType.STRUCT, 5)
            self.post.write(oprot)
            oprot.writeFieldEnd()
        if self.carrier is not None:
            oprot.writeFieldBegin('carrier', TType.MAP, 6)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.carrier))
            for kiter137, viter138 in self.carrier.items():
                oprot.writeString(kiter137.encode('utf-8') if sys.version_info[0] == 2 else kiter137)
                oprot.writeString(viter138.encode('utf-8') if sys.version_info[0] == 2 else viter138)
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
all_structs.append(StorePost_args)
StorePost_args.thrift_spec = (
    None,  # 0
    (1, TType.BYTE, 'flow', None, None, ),  # 1
    (2, TType.I64, 'timestamp2', None, None, ),  # 2
    (3, TType.I16, 'edge', None, None, ),  # 3
    (4, TType.I64, 'req_id', None, None, ),  # 4
    (5, TType.STRUCT, 'post', [Post, None], None, ),  # 5
    (6, TType.MAP, 'carrier', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 6
)


class StorePost_result(object):
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
        oprot.writeStructBegin('StorePost_result')
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
all_structs.append(StorePost_result)
StorePost_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'se', [ServiceException, None], None, ),  # 1
)


class ReadPost_args(object):
    """
    Attributes:
     - flow
     - timestamp2
     - edge
     - req_id
     - post_id
     - carrier

    """


    def __init__(self, flow=None, timestamp2=None, edge=None, req_id=None, post_id=None, carrier=None,):
        self.flow = flow
        self.timestamp2 = timestamp2
        self.edge = edge
        self.req_id = req_id
        self.post_id = post_id
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
                    self.timestamp2 = iprot.readI64()
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
                if ftype == TType.I64:
                    self.post_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.MAP:
                    self.carrier = {}
                    (_ktype140, _vtype141, _size139) = iprot.readMapBegin()
                    for _i143 in range(_size139):
                        _key144 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val145 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.carrier[_key144] = _val145
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
        oprot.writeStructBegin('ReadPost_args')
        if self.flow is not None:
            oprot.writeFieldBegin('flow', TType.BYTE, 1)
            oprot.writeByte(self.flow)
            oprot.writeFieldEnd()
        if self.timestamp2 is not None:
            oprot.writeFieldBegin('timestamp2', TType.I64, 2)
            oprot.writeI64(self.timestamp2)
            oprot.writeFieldEnd()
        if self.edge is not None:
            oprot.writeFieldBegin('edge', TType.I16, 3)
            oprot.writeI16(self.edge)
            oprot.writeFieldEnd()
        if self.req_id is not None:
            oprot.writeFieldBegin('req_id', TType.I64, 4)
            oprot.writeI64(self.req_id)
            oprot.writeFieldEnd()
        if self.post_id is not None:
            oprot.writeFieldBegin('post_id', TType.I64, 5)
            oprot.writeI64(self.post_id)
            oprot.writeFieldEnd()
        if self.carrier is not None:
            oprot.writeFieldBegin('carrier', TType.MAP, 6)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.carrier))
            for kiter146, viter147 in self.carrier.items():
                oprot.writeString(kiter146.encode('utf-8') if sys.version_info[0] == 2 else kiter146)
                oprot.writeString(viter147.encode('utf-8') if sys.version_info[0] == 2 else viter147)
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
all_structs.append(ReadPost_args)
ReadPost_args.thrift_spec = (
    None,  # 0
    (1, TType.BYTE, 'flow', None, None, ),  # 1
    (2, TType.I64, 'timestamp2', None, None, ),  # 2
    (3, TType.I16, 'edge', None, None, ),  # 3
    (4, TType.I64, 'req_id', None, None, ),  # 4
    (5, TType.I64, 'post_id', None, None, ),  # 5
    (6, TType.MAP, 'carrier', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 6
)


class ReadPost_result(object):
    """
    Attributes:
     - success
     - se

    """


    def __init__(self, success=None, se=None,):
        self.success = success
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
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Post()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
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
        oprot.writeStructBegin('ReadPost_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
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
all_structs.append(ReadPost_result)
ReadPost_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Post, None], None, ),  # 0
    (1, TType.STRUCT, 'se', [ServiceException, None], None, ),  # 1
)


class ReadPosts_args(object):
    """
    Attributes:
     - flow
     - timestamp2
     - edge
     - req_id
     - post_ids
     - carrier

    """


    def __init__(self, flow=None, timestamp2=None, edge=None, req_id=None, post_ids=None, carrier=None,):
        self.flow = flow
        self.timestamp2 = timestamp2
        self.edge = edge
        self.req_id = req_id
        self.post_ids = post_ids
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
                    self.timestamp2 = iprot.readI64()
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
                if ftype == TType.LIST:
                    self.post_ids = []
                    (_etype151, _size148) = iprot.readListBegin()
                    for _i152 in range(_size148):
                        _elem153 = iprot.readI64()
                        self.post_ids.append(_elem153)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.MAP:
                    self.carrier = {}
                    (_ktype155, _vtype156, _size154) = iprot.readMapBegin()
                    for _i158 in range(_size154):
                        _key159 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val160 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.carrier[_key159] = _val160
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
        oprot.writeStructBegin('ReadPosts_args')
        if self.flow is not None:
            oprot.writeFieldBegin('flow', TType.BYTE, 1)
            oprot.writeByte(self.flow)
            oprot.writeFieldEnd()
        if self.timestamp2 is not None:
            oprot.writeFieldBegin('timestamp2', TType.I64, 2)
            oprot.writeI64(self.timestamp2)
            oprot.writeFieldEnd()
        if self.edge is not None:
            oprot.writeFieldBegin('edge', TType.I16, 3)
            oprot.writeI16(self.edge)
            oprot.writeFieldEnd()
        if self.req_id is not None:
            oprot.writeFieldBegin('req_id', TType.I64, 4)
            oprot.writeI64(self.req_id)
            oprot.writeFieldEnd()
        if self.post_ids is not None:
            oprot.writeFieldBegin('post_ids', TType.LIST, 5)
            oprot.writeListBegin(TType.I64, len(self.post_ids))
            for iter161 in self.post_ids:
                oprot.writeI64(iter161)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.carrier is not None:
            oprot.writeFieldBegin('carrier', TType.MAP, 6)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.carrier))
            for kiter162, viter163 in self.carrier.items():
                oprot.writeString(kiter162.encode('utf-8') if sys.version_info[0] == 2 else kiter162)
                oprot.writeString(viter163.encode('utf-8') if sys.version_info[0] == 2 else viter163)
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
all_structs.append(ReadPosts_args)
ReadPosts_args.thrift_spec = (
    None,  # 0
    (1, TType.BYTE, 'flow', None, None, ),  # 1
    (2, TType.I64, 'timestamp2', None, None, ),  # 2
    (3, TType.I16, 'edge', None, None, ),  # 3
    (4, TType.I64, 'req_id', None, None, ),  # 4
    (5, TType.LIST, 'post_ids', (TType.I64, None, False), None, ),  # 5
    (6, TType.MAP, 'carrier', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 6
)


class ReadPosts_result(object):
    """
    Attributes:
     - success
     - se

    """


    def __init__(self, success=None, se=None,):
        self.success = success
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
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype167, _size164) = iprot.readListBegin()
                    for _i168 in range(_size164):
                        _elem169 = Post()
                        _elem169.read(iprot)
                        self.success.append(_elem169)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
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
        oprot.writeStructBegin('ReadPosts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter170 in self.success:
                iter170.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
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
all_structs.append(ReadPosts_result)
ReadPosts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [Post, None], False), None, ),  # 0
    (1, TType.STRUCT, 'se', [ServiceException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

