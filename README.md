# Vocalix

Vocalix is a modular, voice-controlled Python AI assistant powered by Google Gemma 3n-e4b-it via NVIDIA’s Build API. It supports speech recognition, system automation, web browsing, media playback, and real-time conversational AI.

## Features
- **Voice Control**: Hardware microphone input integration using `SpeechRecognition`.
- **Conversational AI**: Real-time LLM inference via the NVIDIA Gemma API.
- **System Automation**: Launch and terminate installed Windows applications programmatically.
- **Web & Knowledge Search**: Integrated Wikipedia lookup and Bing web search.
- **Media Playback**: Automates file explorer and local media execution.
- **Offline TTS**: Text-to-speech synthesis using `pyttsx3`.

## Tech Stack
- **Python 3.x**
- **SpeechRecognition**: Audio capture and processing
- **pyttsx3**: Text-to-Speech engine
- **AppOpener**: Windows application automation
- **wikipedia**: API wrapper for knowledge queries
- **requests**: HTTP client for LLM API integration

## Prerequisites
This project requires an NVIDIA API key to access the Gemma model.
1. Create an account at [NVIDIA Build](https://build.nvidia.com)
2. Generate an API key for the [Google Gemma 3n-e4b-it](https://build.nvidia.com/google/gemma-3n-e4b-it) model.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Basilbaasi/Vocalix---AI.git
cd Vocalix---AI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment variables. Create a `.env` file in the root directory:
```env
NVIDIA_API_KEY=your_nvidia_api_key_here
NVIDIA_API_BASE_URL=https://integrate.api.nvidia.com/v1
```

## Usage

Start the assistant by running the main script:
```bash
python main.py
```

### Example Voice Commands
- *"Vocalix, open YouTube"*
- *"Vocalix, what is machine learning?"*
- *"Vocalix, play music"*
- *"Vocalix, search pandas on the web"*

## Media & Demo

- **Demo Video:** [Watch the Vocalix live demonstration on LinkedIn](https://www.linkedin.com/posts/basilck_python-ai-voiceassistant-activity-7354211469388849153-FYhw)

## License
This project is licensed under the MIT License.

---
*Built by Basil C K. Powered by Google Gemma LLM via NVIDIA Build Platform.*
