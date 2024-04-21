--
-- Autogenerated by Thrift
--
-- DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
-- @generated
--


require 'Thrift'
require 'media_service_ttypes'

UserReviewServiceClient = __TObject.new(__TClient, {
  __type = 'UserReviewServiceClient'
})

function UserReviewServiceClient:UploadUserReview(req_id, user_id, review_id, timestamp, carrier)
  self:send_UploadUserReview(req_id, user_id, review_id, timestamp, carrier)
  self:recv_UploadUserReview(req_id, user_id, review_id, timestamp, carrier)
end

function UserReviewServiceClient:send_UploadUserReview(req_id, user_id, review_id, timestamp, carrier)
  self.oprot:writeMessageBegin('UploadUserReview', TMessageType.CALL, self._seqid)
  local args = UploadUserReview_args:new{}
  args.req_id = req_id
  args.user_id = user_id
  args.review_id = review_id
  args.timestamp = timestamp
  args.carrier = carrier
  args:write(self.oprot)
  self.oprot:writeMessageEnd()
  self.oprot.trans:flush()
end

function UserReviewServiceClient:recv_UploadUserReview(req_id, user_id, review_id, timestamp, carrier)
  local fname, mtype, rseqid = self.iprot:readMessageBegin()
  if mtype == TMessageType.EXCEPTION then
    local x = TApplicationException:new{}
    x:read(self.iprot)
    self.iprot:readMessageEnd()
    error(x)
  end
  local result = UploadUserReview_result:new{}
  result:read(self.iprot)
  self.iprot:readMessageEnd()
end

function UserReviewServiceClient:ReadUserReviews(req_id, user_id, start, stop, carrier)
  self:send_ReadUserReviews(req_id, user_id, start, stop, carrier)
  return self:recv_ReadUserReviews(req_id, user_id, start, stop, carrier)
end

function UserReviewServiceClient:send_ReadUserReviews(req_id, user_id, start, stop, carrier)
  self.oprot:writeMessageBegin('ReadUserReviews', TMessageType.CALL, self._seqid)
  local args = ReadUserReviews_args:new{}
  args.req_id = req_id
  args.user_id = user_id
  args.start = start
  args.stop = stop
  args.carrier = carrier
  args:write(self.oprot)
  self.oprot:writeMessageEnd()
  self.oprot.trans:flush()
end

function UserReviewServiceClient:recv_ReadUserReviews(req_id, user_id, start, stop, carrier)
  local fname, mtype, rseqid = self.iprot:readMessageBegin()
  if mtype == TMessageType.EXCEPTION then
    local x = TApplicationException:new{}
    x:read(self.iprot)
    self.iprot:readMessageEnd()
    error(x)
  end
  local result = ReadUserReviews_result:new{}
  result:read(self.iprot)
  self.iprot:readMessageEnd()
  if result.success ~= nil then
    return result.success
  elseif result.se then
    error(result.se)
  end
  error(TApplicationException:new{errorCode = TApplicationException.MISSING_RESULT})
end
UserReviewServiceIface = __TObject:new{
  __type = 'UserReviewServiceIface'
}


UserReviewServiceProcessor = __TObject.new(__TProcessor
, {
 __type = 'UserReviewServiceProcessor'
})

function UserReviewServiceProcessor:process(iprot, oprot, server_ctx)
  local name, mtype, seqid = iprot:readMessageBegin()
  local func_name = 'process_' .. name
  if not self[func_name] or ttype(self[func_name]) ~= 'function' then
    iprot:skip(TType.STRUCT)
    iprot:readMessageEnd()
    x = TApplicationException:new{
      errorCode = TApplicationException.UNKNOWN_METHOD
    }
    oprot:writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
    x:write(oprot)
    oprot:writeMessageEnd()
    oprot.trans:flush()
  else
    self[func_name](self, seqid, iprot, oprot, server_ctx)
  end
end

function UserReviewServiceProcessor:process_UploadUserReview(seqid, iprot, oprot, server_ctx)
  local args = UploadUserReview_args:new{}
  local reply_type = TMessageType.REPLY
  args:read(iprot)
  iprot:readMessageEnd()
  local result = UploadUserReview_result:new{}
  local status, res = pcall(self.handler.UploadUserReview, self.handler, args.req_id, args.user_id, args.review_id, args.timestamp, args.carrier)
  if not status then
    reply_type = TMessageType.EXCEPTION
    result = TApplicationException:new{message = res}
  elseif ttype(res) == 'ServiceException' then
    result.se = res
  else
    result.success = res
  end
  oprot:writeMessageBegin('UploadUserReview', reply_type, seqid)
  result:write(oprot)
  oprot:writeMessageEnd()
  oprot.trans:flush()
end

function UserReviewServiceProcessor:process_ReadUserReviews(seqid, iprot, oprot, server_ctx)
  local args = ReadUserReviews_args:new{}
  local reply_type = TMessageType.REPLY
  args:read(iprot)
  iprot:readMessageEnd()
  local result = ReadUserReviews_result:new{}
  local status, res = pcall(self.handler.ReadUserReviews, self.handler, args.req_id, args.user_id, args.start, args.stop, args.carrier)
  if not status then
    reply_type = TMessageType.EXCEPTION
    result = TApplicationException:new{message = res}
  elseif ttype(res) == 'ServiceException' then
    result.se = res
  else
    result.success = res
  end
  oprot:writeMessageBegin('ReadUserReviews', reply_type, seqid)
  result:write(oprot)
  oprot:writeMessageEnd()
  oprot.trans:flush()
end

-- HELPER FUNCTIONS AND STRUCTURES

UploadUserReview_args = __TObject:new{
  req_id,
  user_id,
  review_id,
  timestamp,
  carrier
}

function UploadUserReview_args:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 1 then
      if ftype == TType.I64 then
        self.req_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 2 then
      if ftype == TType.I64 then
        self.user_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 3 then
      if ftype == TType.I64 then
        self.review_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 4 then
      if ftype == TType.I64 then
        self.timestamp = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 5 then
      if ftype == TType.MAP then
        self.carrier = {}
        local _ktype207, _vtype208, _size206 = iprot:readMapBegin() 
        for _i=1,_size206 do
          local _key210 = iprot:readString()
          local _val211 = iprot:readString()
          self.carrier[_key210] = _val211
        end
        iprot:readMapEnd()
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function UploadUserReview_args:write(oprot)
  oprot:writeStructBegin('UploadUserReview_args')
  if self.req_id ~= nil then
    oprot:writeFieldBegin('req_id', TType.I64, 1)
    oprot:writeI64(self.req_id)
    oprot:writeFieldEnd()
  end
  if self.user_id ~= nil then
    oprot:writeFieldBegin('user_id', TType.I64, 2)
    oprot:writeI64(self.user_id)
    oprot:writeFieldEnd()
  end
  if self.review_id ~= nil then
    oprot:writeFieldBegin('review_id', TType.I64, 3)
    oprot:writeI64(self.review_id)
    oprot:writeFieldEnd()
  end
  if self.timestamp ~= nil then
    oprot:writeFieldBegin('timestamp', TType.I64, 4)
    oprot:writeI64(self.timestamp)
    oprot:writeFieldEnd()
  end
  if self.carrier ~= nil then
    oprot:writeFieldBegin('carrier', TType.MAP, 5)
    oprot:writeMapBegin(TType.STRING, TType.STRING, ttable_size(self.carrier))
    for kiter212,viter213 in pairs(self.carrier) do
      oprot:writeString(kiter212)
      oprot:writeString(viter213)
    end
    oprot:writeMapEnd()
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

UploadUserReview_result = __TObject:new{
  se
}

function UploadUserReview_result:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 1 then
      if ftype == TType.STRUCT then
        self.se = ServiceException:new{}
        self.se:read(iprot)
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function UploadUserReview_result:write(oprot)
  oprot:writeStructBegin('UploadUserReview_result')
  if self.se ~= nil then
    oprot:writeFieldBegin('se', TType.STRUCT, 1)
    self.se:write(oprot)
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

ReadUserReviews_args = __TObject:new{
  req_id,
  user_id,
  start,
  stop,
  carrier
}

function ReadUserReviews_args:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 1 then
      if ftype == TType.I64 then
        self.req_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 2 then
      if ftype == TType.I64 then
        self.user_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 3 then
      if ftype == TType.I32 then
        self.start = iprot:readI32()
      else
        iprot:skip(ftype)
      end
    elseif fid == 4 then
      if ftype == TType.I32 then
        self.stop = iprot:readI32()
      else
        iprot:skip(ftype)
      end
    elseif fid == 5 then
      if ftype == TType.MAP then
        self.carrier = {}
        local _ktype215, _vtype216, _size214 = iprot:readMapBegin() 
        for _i=1,_size214 do
          local _key218 = iprot:readString()
          local _val219 = iprot:readString()
          self.carrier[_key218] = _val219
        end
        iprot:readMapEnd()
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function ReadUserReviews_args:write(oprot)
  oprot:writeStructBegin('ReadUserReviews_args')
  if self.req_id ~= nil then
    oprot:writeFieldBegin('req_id', TType.I64, 1)
    oprot:writeI64(self.req_id)
    oprot:writeFieldEnd()
  end
  if self.user_id ~= nil then
    oprot:writeFieldBegin('user_id', TType.I64, 2)
    oprot:writeI64(self.user_id)
    oprot:writeFieldEnd()
  end
  if self.start ~= nil then
    oprot:writeFieldBegin('start', TType.I32, 3)
    oprot:writeI32(self.start)
    oprot:writeFieldEnd()
  end
  if self.stop ~= nil then
    oprot:writeFieldBegin('stop', TType.I32, 4)
    oprot:writeI32(self.stop)
    oprot:writeFieldEnd()
  end
  if self.carrier ~= nil then
    oprot:writeFieldBegin('carrier', TType.MAP, 5)
    oprot:writeMapBegin(TType.STRING, TType.STRING, ttable_size(self.carrier))
    for kiter220,viter221 in pairs(self.carrier) do
      oprot:writeString(kiter220)
      oprot:writeString(viter221)
    end
    oprot:writeMapEnd()
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

ReadUserReviews_result = __TObject:new{
  success,
  se
}

function ReadUserReviews_result:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 0 then
      if ftype == TType.LIST then
        self.success = {}
        local _etype225, _size222 = iprot:readListBegin()
        for _i=1,_size222 do
          local _elem226 = Review:new{}
          _elem226:read(iprot)
          table.insert(self.success, _elem226)
        end
        iprot:readListEnd()
      else
        iprot:skip(ftype)
      end
    elseif fid == 1 then
      if ftype == TType.STRUCT then
        self.se = ServiceException:new{}
        self.se:read(iprot)
      else
        iprot:skip(ftype)
      end
    else
      iprot:skip(ftype)
    end
    iprot:readFieldEnd()
  end
  iprot:readStructEnd()
end

function ReadUserReviews_result:write(oprot)
  oprot:writeStructBegin('ReadUserReviews_result')
  if self.success ~= nil then
    oprot:writeFieldBegin('success', TType.LIST, 0)
    oprot:writeListBegin(TType.STRUCT, #self.success)
    for _,iter227 in ipairs(self.success) do
      iter227:write(oprot)
    end
    oprot:writeListEnd()
    oprot:writeFieldEnd()
  end
  if self.se ~= nil then
    oprot:writeFieldBegin('se', TType.STRUCT, 1)
    self.se:write(oprot)
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end
return UserReviewServiceClient, UserReviewServiceProcessor