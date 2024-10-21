# AI Assistant

Welcome to the **AI Assistant** project! This innovative application leverages the power of artificial intelligence to provide users with real-time weather updates and the latest news headlines, all through a simple voice interface. 

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)

## Features

- **Voice Recognition**: Interact with the assistant using natural language.
- **Weather Updates**: Get real-time weather information for any city.
- **Latest News**: Stay informed with the top headlines from around the world.
- **User-Friendly Interface**: Simple and intuitive design for ease of use.

## Technologies Used

This project is built using the following technologies:

- **Python**: The core programming language for the application.
- **Requests**: For making HTTP requests to external APIs.
- **SpeechRecognition**: To convert spoken language into text.
- **gTTS (Google Text-to-Speech)**: For converting text responses back into speech.
- **OpenWeatherMap API**: To fetch weather data.
- **NewsAPI**: To retrieve the latest news articles.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:Sudeep458/AI_Assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AI_Assistant
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file in the root directory and add your API keys:
   ```bash
   WEATHER_API_KEY=your_openweathermap_api_key
   NEWS_API_KEY=your_newsapi_key
   ```
   
## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. When prompted, speak your query (e.g., "What's the weather in New York?" or "Tell me the latest news.").
3. Listen to the AI Assistant's response!

## How It Works

The AI Assistant uses voice recognition to capture user queries and then processes these queries to fetch data from external APIs. The weather information is retrieved from OpenWeatherMap, while news headlines are fetched from NewsAPI. The assistant responds with text-to-speech, providing an engaging user experience.

## Example Queries

1. "What's the weather like in Bengaluru?"
2. "Give me today's top news."
3. "Tell me about the weather in Yelahanka."


