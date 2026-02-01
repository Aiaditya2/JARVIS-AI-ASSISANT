# JARVIS - Just A Rather Very Intelligent System

A local AI assistant with Hindi voice support and Android integration, optimized for low RAM usage.

## 🌟 Features

- 🗣️ **Hindi Voice Recognition** - Full support for Hindi speech input
- 🔊 **Hindi Text-to-Speech** - Natural Hindi voice output
- 🤖 **Local LLM Integration** - Runs completely offline
- 📱 **Android Support** - Native Android app with Kivy
- 💾 **Low RAM Usage** - Optimized for systems with limited memory
- 🔧 **Modular Architecture** - Easy to extend and customize

## 📋 Local LLM Recommendations (Low RAM / High Power)

### Best Options for Low RAM Systems:

#### 1. **Ollama** (Recommended - Easiest Setup)
- **Models**: `llama3.2:1b`, `phi3:mini`, `gemma2:2b`
- **RAM Usage**: ~2-4 GB
- **Installation**: 
  ```bash
  # Install Ollama
  curl -fsSL https://ollama.com/install.sh | sh
  
  # Pull a model
  ollama pull llama3.2:1b
  ```
- **Pros**: Easy setup, automatic quantization, good performance
- **Cons**: Requires Ollama service running

#### 2. **llama.cpp with GGUF Models** (Most Efficient)
- **Models**: Q4_K_M or Q5_K_M quantized GGUF models
- **RAM Usage**: ~1.5-3 GB
- **Recommended Models**:
  - `TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf`
  - `phi-3-mini-4k-instruct.Q4_K_M.gguf`
  - `gemma-2b-it.Q4_K_M.gguf`
- **Download**: From [Hugging Face](https://huggingface.co/models?search=gguf)
- **Pros**: Lowest RAM usage, fastest inference
- **Cons**: Requires manual model download

#### 3. **Transformers with 8-bit Quantization**
- **Models**: `microsoft/Phi-3-mini-4k-instruct`, `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- **RAM Usage**: ~3-5 GB
- **Pros**: Easy to use, good model selection
- **Cons**: Higher RAM usage than llama.cpp

### Model Comparison:

| Model | Size | RAM Usage | Speed | Quality |
|-------|------|-----------|-------|---------|
| llama3.2:1b (Ollama) | 1.3B | ~2GB | Fast | Good |
| phi3:mini (Ollama) | 3.8B | ~3GB | Medium | Very Good |
| TinyLlama Q4_K_M | 1.1B | ~1.5GB | Very Fast | Good |
| Phi-3-mini Q4_K_M | 3.8B | ~2.5GB | Medium | Very Good |

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Microphone (for voice input)
- 2-4 GB RAM (for LLM)
- For Android: Android SDK, Buildozer (for building APK)

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "JARVIS AI ASSISANT"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install system dependencies** (Linux):
   ```bash
   # For speech recognition
   sudo apt-get install portaudio19-dev python3-pyaudio
   
   # For offline recognition (optional)
   sudo apt-get install pocketsphinx
   ```

4. **Setup LLM backend** (choose one):

   **Option A: Ollama (Recommended)**
   ```bash
   # Install Ollama
   curl -fsSL https://ollama.com/install.sh | sh
   
   # Pull a small model
   ollama pull llama3.2:1b
   ```

   **Option B: llama.cpp**
   ```bash
   pip install llama-cpp-python
   
   # Download a GGUF model to models/ directory
   mkdir models
   # Download model from Hugging Face
   ```

5. **Configure** (optional):
   Edit `config/config.yaml` to customize settings.

## 📱 Android Setup

### Building Android APK

1. **Install Buildozer**:
   ```bash
   pip install buildozer
   ```

2. **Create buildozer.spec** (see example in repo)

3. **Build APK**:
   ```bash
   buildozer android debug
   ```

### Android Requirements

- Android 5.0+ (API 21+)
- Microphone permission
- Internet permission (for Google Speech Recognition fallback)

## 🎯 Usage

### Basic Usage

```python
from jarvis.main import JARVIS

# Initialize JARVIS
jarvis = JARVIS(
    language="hi-IN",  # Hindi
    model_type="ollama",
    model_name="llama3.2:1b"
)

# Run interactive mode
jarvis.run_interactive()
```

### Command Line

```bash
# Hindi mode with Ollama
python -m jarvis.main --language hi-IN --model-type ollama --model-name llama3.2:1b

# English mode
python -m jarvis.main --language en-US --model-type ollama --model-name llama3.2:1b

# Android mode
python -m jarvis.main --android
```

### Android App

```bash
# Run Kivy app
python -m jarvis.android.kivy_app
```

## 🗂️ Project Structure

```
JARVIS AI ASSISANT/
├── jarvis/
│   ├── __init__.py
│   ├── main.py                 # Main JARVIS class
│   ├── core/
│   │   ├── __init__.py
│   │   ├── voice_recognizer.py  # Voice recognition
│   │   ├── tts_engine.py        # Text-to-speech
│   │   ├── llm_handler.py       # LLM integration
│   │   └── command_processor.py # Command processing
│   └── android/
│       ├── __init__.py
│       ├── android_voice.py     # Android voice handler
│       └── kivy_app.py          # Kivy Android app
├── config/
│   └── config.yaml              # Configuration file
├── models/                      # LLM models (if using llama.cpp)
├── requirements.txt
└── README.md
```

## 🔧 Configuration

Edit `config/config.yaml` to customize:

- Language settings
- LLM backend and model
- Voice recognition parameters
- Android settings

## 🎤 Supported Commands

### Hindi Commands:
- "समय बताओ" - Get current time
- "तारीख बताओ" - Get current date
- "मौसम बताओ" - Get weather
- "सहायता" - Show help

### English Commands:
- "time" - Get current time
- "date" - Get current date
- "weather" - Get weather
- "help" - Show help

Custom commands can be added via `CommandProcessor.register_command()`.

## 🛠️ Development

### Adding New Commands

```python
from jarvis.core.command_processor import CommandProcessor

processor = CommandProcessor()

def my_command(text):
    return "Command executed!"

processor.register_command("mycommand", my_command)
```

### Adding New LLM Backend

Extend `LLMHandler` class in `jarvis/core/llm_handler.py`.

## 📝 Notes

- **Voice Recognition**: Uses Google Speech Recognition by default (requires internet). For offline, configure PocketSphinx.
- **TTS**: Uses system TTS. For better Hindi TTS, consider using gTTS (requires internet) or Festival TTS with Hindi voices.
- **LLM**: Start with Ollama for easiest setup. For lowest RAM, use llama.cpp with Q4 quantized models.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License

## 🙏 Acknowledgments

- Ollama for easy LLM deployment
- llama.cpp for efficient inference
- SpeechRecognition library
- Kivy for Android support
