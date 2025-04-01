from flask import Flask, request, jsonify
from models import db, GuestbookMessage

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize DB
db.init_app(app)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = GuestbookMessage.query.all()
    return jsonify([msg.to_dict() for msg in messages])

@app.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    new_message = GuestbookMessage(name=data['name'], message=data['message'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
