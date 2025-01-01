from flask import Flask,request, jsonify
from sql.handlesql import db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_cors import CORS
import traceback
import json


app = Flask(__name__)
##解决跨域问题
CORS(app, origins=["http://124.222.214.78:5173"])



jwt = JWTManager(app)
    # 设置访问令牌的过期时间（秒）
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600 * 5
app.config['JWT_SECRET_KEY'] = 'suprisemotherfucker'

@jwt.unauthorized_loader
def custom_unauthorized_callback(error_string):
        # 返回自定义的JSON响应
        return jsonify(code=422, msg="token效验失败"), 422

@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
        return jsonify(code="401", err="token 已过期"), 401

@app.route('/api/login', methods=['POST'])
def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        access_token = create_access_token(identity={'username': username})
        res = db.login_authentication(username, password)

        if res != False:
            access_token = create_access_token(identity=username)

            return jsonify({'code': 200, 'msg': 'Login successful', 'token': access_token}), 200
        else:
            return jsonify({'code': 500, 'msg': "invalid username or password"}), 500
        return jsonify({'code': 200, 'msg': 'Login successful', 'token': access_token}), 200

@app.route('/api/getalldata', methods=['GET'])
@jwt_required()
def getdata():
        res = db.getalldata()

        return jsonify({'code': 200, 'msg': 'success', "data": res}), 200

    ##手动控制
@app.route('/api/updata', methods=['POST'])
@jwt_required()
def updata():
        data = request.get_json()
        Parameter = data.get('Parameter')
        print(f"开启了{Parameter}")

        return jsonify({'code': 200, 'msg': 'success', 'data': None}), 200

@app.route('/api/downdata', methods=['POST'])
@jwt_required()
def downdata():
        data = request.get_json()
        Parameter = data.get('Parameter')
        print(f"关闭了{Parameter}")

        return jsonify({'code': 200, 'msg': 'success', 'data': None}), 200


@app.errorhandler(404)
def not_found_error(error):
        return jsonify({'code': 404, 'msg': 'The requested URL was not found on the server'}), 404

@app.errorhandler(500)
def handle_error(e):
        print('An error occurred:', e)
        traceback.print_exc()
        return jsonify({'code': 500, 'msg': "error"}), 500


if __name__ == "__main__":
 app.run('0.0.0.0', 5000, True)

