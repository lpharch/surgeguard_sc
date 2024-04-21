--
-- Autogenerated by Thrift
--
-- DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
-- @generated
--


require 'Thrift'
require 'media_service_ttypes'

PlotServiceClient = __TObject.new(__TClient, {
  __type = 'PlotServiceClient'
})

function PlotServiceClient:WritePlot(req_id, plot_id, plot, carrier)
  self:send_WritePlot(req_id, plot_id, plot, carrier)
  self:recv_WritePlot(req_id, plot_id, plot, carrier)
end

function PlotServiceClient:send_WritePlot(req_id, plot_id, plot, carrier)
  self.oprot:writeMessageBegin('WritePlot', TMessageType.CALL, self._seqid)
  local args = WritePlot_args:new{}
  args.req_id = req_id
  args.plot_id = plot_id
  args.plot = plot
  args.carrier = carrier
  args:write(self.oprot)
  self.oprot:writeMessageEnd()
  self.oprot.trans:flush()
end

function PlotServiceClient:recv_WritePlot(req_id, plot_id, plot, carrier)
  local fname, mtype, rseqid = self.iprot:readMessageBegin()
  if mtype == TMessageType.EXCEPTION then
    local x = TApplicationException:new{}
    x:read(self.iprot)
    self.iprot:readMessageEnd()
    error(x)
  end
  local result = WritePlot_result:new{}
  result:read(self.iprot)
  self.iprot:readMessageEnd()
end

function PlotServiceClient:ReadPlot(req_id, plot_id, carrier)
  self:send_ReadPlot(req_id, plot_id, carrier)
  return self:recv_ReadPlot(req_id, plot_id, carrier)
end

function PlotServiceClient:send_ReadPlot(req_id, plot_id, carrier)
  self.oprot:writeMessageBegin('ReadPlot', TMessageType.CALL, self._seqid)
  local args = ReadPlot_args:new{}
  args.req_id = req_id
  args.plot_id = plot_id
  args.carrier = carrier
  args:write(self.oprot)
  self.oprot:writeMessageEnd()
  self.oprot.trans:flush()
end

function PlotServiceClient:recv_ReadPlot(req_id, plot_id, carrier)
  local fname, mtype, rseqid = self.iprot:readMessageBegin()
  if mtype == TMessageType.EXCEPTION then
    local x = TApplicationException:new{}
    x:read(self.iprot)
    self.iprot:readMessageEnd()
    error(x)
  end
  local result = ReadPlot_result:new{}
  result:read(self.iprot)
  self.iprot:readMessageEnd()
  if result.success ~= nil then
    return result.success
  elseif result.se then
    error(result.se)
  end
  error(TApplicationException:new{errorCode = TApplicationException.MISSING_RESULT})
end
PlotServiceIface = __TObject:new{
  __type = 'PlotServiceIface'
}


PlotServiceProcessor = __TObject.new(__TProcessor
, {
 __type = 'PlotServiceProcessor'
})

function PlotServiceProcessor:process(iprot, oprot, server_ctx)
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

function PlotServiceProcessor:process_WritePlot(seqid, iprot, oprot, server_ctx)
  local args = WritePlot_args:new{}
  local reply_type = TMessageType.REPLY
  args:read(iprot)
  iprot:readMessageEnd()
  local result = WritePlot_result:new{}
  local status, res = pcall(self.handler.WritePlot, self.handler, args.req_id, args.plot_id, args.plot, args.carrier)
  if not status then
    reply_type = TMessageType.EXCEPTION
    result = TApplicationException:new{message = res}
  elseif ttype(res) == 'ServiceException' then
    result.se = res
  else
    result.success = res
  end
  oprot:writeMessageBegin('WritePlot', reply_type, seqid)
  result:write(oprot)
  oprot:writeMessageEnd()
  oprot.trans:flush()
end

function PlotServiceProcessor:process_ReadPlot(seqid, iprot, oprot, server_ctx)
  local args = ReadPlot_args:new{}
  local reply_type = TMessageType.REPLY
  args:read(iprot)
  iprot:readMessageEnd()
  local result = ReadPlot_result:new{}
  local status, res = pcall(self.handler.ReadPlot, self.handler, args.req_id, args.plot_id, args.carrier)
  if not status then
    reply_type = TMessageType.EXCEPTION
    result = TApplicationException:new{message = res}
  elseif ttype(res) == 'ServiceException' then
    result.se = res
  else
    result.success = res
  end
  oprot:writeMessageBegin('ReadPlot', reply_type, seqid)
  result:write(oprot)
  oprot:writeMessageEnd()
  oprot.trans:flush()
end

-- HELPER FUNCTIONS AND STRUCTURES

WritePlot_args = __TObject:new{
  req_id,
  plot_id,
  plot,
  carrier
}

function WritePlot_args:read(iprot)
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
        self.plot_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 3 then
      if ftype == TType.STRING then
        self.plot = iprot:readString()
      else
        iprot:skip(ftype)
      end
    elseif fid == 4 then
      if ftype == TType.MAP then
        self.carrier = {}
        local _ktype257, _vtype258, _size256 = iprot:readMapBegin() 
        for _i=1,_size256 do
          local _key260 = iprot:readString()
          local _val261 = iprot:readString()
          self.carrier[_key260] = _val261
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

function WritePlot_args:write(oprot)
  oprot:writeStructBegin('WritePlot_args')
  if self.req_id ~= nil then
    oprot:writeFieldBegin('req_id', TType.I64, 1)
    oprot:writeI64(self.req_id)
    oprot:writeFieldEnd()
  end
  if self.plot_id ~= nil then
    oprot:writeFieldBegin('plot_id', TType.I64, 2)
    oprot:writeI64(self.plot_id)
    oprot:writeFieldEnd()
  end
  if self.plot ~= nil then
    oprot:writeFieldBegin('plot', TType.STRING, 3)
    oprot:writeString(self.plot)
    oprot:writeFieldEnd()
  end
  if self.carrier ~= nil then
    oprot:writeFieldBegin('carrier', TType.MAP, 4)
    oprot:writeMapBegin(TType.STRING, TType.STRING, ttable_size(self.carrier))
    for kiter262,viter263 in pairs(self.carrier) do
      oprot:writeString(kiter262)
      oprot:writeString(viter263)
    end
    oprot:writeMapEnd()
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

WritePlot_result = __TObject:new{
  se
}

function WritePlot_result:read(iprot)
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

function WritePlot_result:write(oprot)
  oprot:writeStructBegin('WritePlot_result')
  if self.se ~= nil then
    oprot:writeFieldBegin('se', TType.STRUCT, 1)
    self.se:write(oprot)
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

ReadPlot_args = __TObject:new{
  req_id,
  plot_id,
  carrier
}

function ReadPlot_args:read(iprot)
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
        self.plot_id = iprot:readI64()
      else
        iprot:skip(ftype)
      end
    elseif fid == 3 then
      if ftype == TType.MAP then
        self.carrier = {}
        local _ktype265, _vtype266, _size264 = iprot:readMapBegin() 
        for _i=1,_size264 do
          local _key268 = iprot:readString()
          local _val269 = iprot:readString()
          self.carrier[_key268] = _val269
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

function ReadPlot_args:write(oprot)
  oprot:writeStructBegin('ReadPlot_args')
  if self.req_id ~= nil then
    oprot:writeFieldBegin('req_id', TType.I64, 1)
    oprot:writeI64(self.req_id)
    oprot:writeFieldEnd()
  end
  if self.plot_id ~= nil then
    oprot:writeFieldBegin('plot_id', TType.I64, 2)
    oprot:writeI64(self.plot_id)
    oprot:writeFieldEnd()
  end
  if self.carrier ~= nil then
    oprot:writeFieldBegin('carrier', TType.MAP, 3)
    oprot:writeMapBegin(TType.STRING, TType.STRING, ttable_size(self.carrier))
    for kiter270,viter271 in pairs(self.carrier) do
      oprot:writeString(kiter270)
      oprot:writeString(viter271)
    end
    oprot:writeMapEnd()
    oprot:writeFieldEnd()
  end
  oprot:writeFieldStop()
  oprot:writeStructEnd()
end

ReadPlot_result = __TObject:new{
  success,
  se
}

function ReadPlot_result:read(iprot)
  iprot:readStructBegin()
  while true do
    local fname, ftype, fid = iprot:readFieldBegin()
    if ftype == TType.STOP then
      break
    elseif fid == 0 then
      if ftype == TType.STRING then
        self.success = iprot:readString()
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

function ReadPlot_result:write(oprot)
  oprot:writeStructBegin('ReadPlot_result')
  if self.success ~= nil then
    oprot:writeFieldBegin('success', TType.STRING, 0)
    oprot:writeString(self.success)
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
return PlotServiceClient, PlotServiceProcessor