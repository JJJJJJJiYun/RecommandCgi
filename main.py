import json
import traceback

import grpc
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.protobuf.json_format import MessageToDict
from grpc._channel import _Rendezvous

from pb.action import action_pb2, action_pb2_grpc
from pb.item import item_pb2, item_pb2_grpc
from pb.recommand import recommand_pb2, recommand_pb2_grpc

app = Flask(__name__)


@app.route('/recommand', methods=['GET'])
def recommand():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = recommand_pb2_grpc.RecommandServiceStub(channel)
        params = get_request_params()
        try:
            response = client.Recommand(
                recommand_pb2.RecommandRequest(user_id=request.headers.get("USER_ID"), page=int(params['page']),
                                               page_size=int(params['pageSize'])))
            resp_dict = MessageToDict(response)
            return generate_response_by_grpc_response({
                'list': resp_dict['items'] if 'items' in resp_dict else [],
                'pageInfo': generate_page_info(resp_dict['pageInfo'])
            })
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


@app.route('/setDefaultRecommandItems', methods=['POST'])
def set_default_recommand_items():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = recommand_pb2_grpc.RecommandServiceStub(channel)
        params = get_request_params()
        try:
            client.SetDefaultRecommandItems(
                recommand_pb2.SetDefaultRecommandItemsRequest(item_ids=params['itemIds']))
            return generate_response_by_grpc_response("")
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


@app.route('/getItemList', methods=['GET'])
def get_item_list():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = item_pb2_grpc.ItemServiceStub(channel)
        params = get_request_params()
        try:
            response = client.GetItemList(
                item_pb2.GetItemListRequest(item_type=item_pb2.ItemType.Value(params['itemType'].upper()),
                                            page=int(params['page']),
                                            page_size=int(params['pageSize']))
            )
            resp_dict = MessageToDict(response)
            return generate_response_by_grpc_response({
                'list': resp_dict['items'],
                'pageInfo': generate_page_info(resp_dict['pageInfo'])
            })
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


@app.route('/getItem', methods=['GET'])
def get_item():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = item_pb2_grpc.ItemServiceStub(channel)
        params = get_request_params()
        try:
            response = client.GetItem(
                item_pb2.GetItemRequest(item_type=item_pb2.ItemType.Value(params['itemType'].upper()), id=params['id'])
            )
            resp_dict = MessageToDict(response)
            return generate_response_by_grpc_response({
                'item': resp_dict
            })
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


@app.route('/action', methods=['GET'])
def record_action():
    with grpc.insecure_channel('localhost:50052') as channel:
        client = action_pb2_grpc.ActionServiceStub(channel)
        params = get_request_params()
        try:
            client.RecordAction(
                action_pb2.RecordActionRequest(user_id=request.headers.get("USER_ID"),
                                               item_id=params['itemId'], action='read',
                                               item_type=action_pb2.ItemType.Value(params['itemType'].upper())))
            return generate_response_by_grpc_response("")
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


def get_request_params():
    if request.method == 'GET':
        params = request.args.to_dict()
    elif request.method == 'POST' and "application/json" in request.headers.get("Content-Type", type=str):
        params = json.loads(request.data)
    else:
        params = request.form
    return params


def generate_response_by_grpc_response(data, code=0, msg="ok"):
    return jsonify({
        'code': code,
        'msg': msg,
        'data': data
    })


def generate_page_info(page_info):
    return {
        'page': page_info['page'],
        'pageSize': page_info['pageSize'],
        'total': page_info['total'] if 'total' in page_info else 0,
        'totalPage': page_info['totalPage'] if 'totalPage' in page_info else 0
    }


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run("localhost", "8888")
