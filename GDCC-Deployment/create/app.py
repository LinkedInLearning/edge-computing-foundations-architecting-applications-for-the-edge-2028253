from flask import Flask, request, redirect, render_template_string, jsonify
from models import db, GuestbookMessage

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize DB
db.init_app(app)

# Route for the homepage (Landing page)
@app.route('/')
def home():
    # Retrieve all messages from the database to display on the homepage
    messages = GuestbookMessage.query.all()
    return render_template_string('''
        <h1>Welcome to the Guestbook!</h1>
        <form method="POST" action="/messages">
            <label for="name">Your Name:</label>
            <input type="text" name="name" required>
            <label for="message">Your Message:</label>
            <textarea name="message" required></textarea>
            <button type="submit">Post Message</button>
        </form>
        <h2>Messages</h2>
        <ul>
            {% for msg in messages %}
                <li><strong>{{ msg.name }}</strong>: {{ msg.message }}</li>
            {% endfor %}
        </ul>
    ''', messages=messages)

# Route for posting messages
@app.route('/messages', methods=['POST'])
def post_message():
    # Get data from the form
    name = request.form['name']
    message = request.form['message']

    # Add the new message to the database
    new_message = GuestbookMessage(name=name, message=message)
    db.session.add(new_message)
    db.session.commit()

    # Redirect back to the homepage after posting
    return redirect('/')

# Optional: API route for getting messages as JSON (for example, to integrate with a frontend)
@app.route('/api/messages', methods=['GET'])
def api_get_messages():
    messages = GuestbookMessage.query.all()
    return jsonify([msg.to_dict() for msg in messages])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

