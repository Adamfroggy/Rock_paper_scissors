# StoryBot

StoryBot is a conversational AI bot that generates stories based on user input. It utilizes the power of pre-trained language models to create engaging narratives, making it a fun tool for storytelling and creative exploration.

## Table of Contents

- [Introduction](#introduction)
- [License](#license)
- [Citation](#citation)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [References](#references)

## Introduction
Welcome to StoryBot, your creative companion in the world of storytelling! 📖✨

StoryBot is an AI-powered chatbot designed to unleash your imagination by generating captivating stories based on your prompts. Whether you're looking to embark on epic adventures, explore mysterious realms, or delve into the depths of fantasy, StoryBot is here to bring your ideas to life.

# What is StoryBot?
StoryBot harnesses the power of state-of-the-art language models to craft rich and immersive narratives in response to user input. With its ability to maintain context and remember previous interactions, StoryBot offers a seamless storytelling experience, allowing for multiple revisions and endless creative possibilities.

# Why StoryBot?
Inspiration on Demand: Need a spark of inspiration? Simply ask StoryBot to weave a tale, and watch as it conjures up worlds filled with wonder and excitement.
Engaging Conversations: Dive into interactive conversations with StoryBot, where each exchange unfolds a new chapter in your story.
Memory and Continuity: Explore the depths of your imagination without losing track of the plot, as StoryBot remembers past interactions and maintains continuity across conversations.

# How to Use StoryBot
Using StoryBot is easy and intuitive:

1. Installation: Clone the repository and install the required dependencies.
2. Interaction: Run StoryBot in the terminal or integrate it into your applications using the provided API.
3. Prompting: Enter your story prompts or questions, and let StoryBot work its magic.
4. Exploration: Engage in dynamic storytelling sessions, revise and refine your stories, and explore endless narrative possibilities.

## Features

- **Interactive Chat**: Users can engage with the bot in real-time by providing prompts or questions.
- **Story Generation**: The bot generates stories based on the user's input and maintains context across interactions.
- **Memory Module**: StoryBot remembers previous interactions, allowing for multiple revisions of the same story.
- **API Integration**: StoryBot can be integrated into web applications using a Flask-based API.

# Get Started
Ready to embark on your storytelling journey with StoryBot? Follow the installation instructions in the Installation section and unleash your creativity!

# Contributors
StoryBot is made possible by the contributions of passionate developers and storytellers like you. Join our community and become a part of the creative journey!

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/storybot.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the bot:

    ```
    python app.py
    ```

## Usage

### Command Line Interface (CLI)

Run the bot in the terminal:


Interact with the bot by entering prompts or questions.

### API Integration

The bot provides an API endpoint for interaction. Send a POST request to `http://localhost:5000/chat` with a JSON payload containing the user's input:

```json
{
    "user_input": "Tell me a story about dragons."
}

Memory Module
StoryBot remembers previous interactions and maintains context across conversations. This allows for multiple revisions of the same story based on user input.

Examples

CLI Example

$ python app.py
>>> Tell me a story about a haunted house.
Once upon a time, in a dark and stormy night, there was a haunted house...

# API Example
import requests

url = 'http://localhost:5000/chat'
data = {'user_input': 'Tell me a story about a haunted forest.'}
response = requests.post(url, json=data)
print(response.json()['response'])

```

# License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

# Citation

If you use or find inspiration from this project, please consider citing it using the provided [CITATION](CITATION) file.

# Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

# Code of Conduct

We aim to foster an inclusive and respectful community. Please review our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct.



