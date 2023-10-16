from flask import Flask, request

from app.ibm_watson import create_assistant_session, send_message_to_assistant

assistant_id = 'xxxxxxxx'
apikey = 'xxxxxxx'
url = 'xxxxxxx'

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send():
	user_input = request.args.get('user_input')
	session_id = create_assistant_session(assistant_id)
	assistant_response = send_message_to_assistant(assistant_id, session_id, user_input)
	return assistant_response

