from flask import Flask, request, jsonify, render_template
from bot import StoryBot

app = Flask(__name__, template_folder='templates')
story_bot = StoryBot(name="Storyteller", system="Once upon a time...")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint for handling chat requests.
    """
    data = request.json
    user_input = data.get('user_input', '')
    response = story_bot.chat(user_input)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
