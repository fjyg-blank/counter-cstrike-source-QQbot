from flask import Flask, request
import api
app = Flask(__name__)
@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type')=='private':
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        api.keyword(message, uid)
    if request.get_json().get('message_type')=='group':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        msgid = request.get_json().get('message_id')
        times=request.get_json().get('time')
        api.keyword(msgid,message,uid,gid,times)
    return 'OK'
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)
