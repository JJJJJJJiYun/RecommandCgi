# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb.action import action_pb2 as pb_dot_action_dot_action__pb2


class ActionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RecordAction = channel.unary_unary(
        '/action.ActionService/RecordAction',
        request_serializer=pb_dot_action_dot_action__pb2.RecordActionRequest.SerializeToString,
        response_deserializer=pb_dot_action_dot_action__pb2.EmptyMessage.FromString,
        )


class ActionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RecordAction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ActionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RecordAction': grpc.unary_unary_rpc_method_handler(
          servicer.RecordAction,
          request_deserializer=pb_dot_action_dot_action__pb2.RecordActionRequest.FromString,
          response_serializer=pb_dot_action_dot_action__pb2.EmptyMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'action.ActionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
