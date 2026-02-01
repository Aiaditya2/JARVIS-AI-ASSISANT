# JARVIS Quick Start Guide

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Choose Your LLM Backend

#### Option A: Ollama (Easiest - Recommended)

```bash
# Install Ollama
# Windows: Download from https://ollama.com
# Linux/Mac: curl -fsSL https://ollama.com/install.sh | sh

# Pull a small model
ollama pull llama3.2:1b
```

#### Option B: llama.cpp (Most Efficient)

```bash
pip install llama-cpp-python

# Download a GGUF model
mkdir models
# Visit https://huggingface.co/models?search=gguf
# Download a Q4_K_M model (e.g., TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf)
# Place it in the models/ directory
```

### Step 3: Run JARVIS

```bash
# Basic usage
python -m jarvis.main --language hi-IN --model-type ollama --model-name llama3.2:1b

# Or use the example
python examples/basic_usage.py
```

## 📱 Android Setup

### Prerequisites

1. Install Buildozer:
```bash
pip install buildozer
```

2. Install Android SDK and NDK (Buildozer will help with this)

### Build APK

```bash
buildozer android debug
```

The APK will be in `bin/` directory.

## 🎯 Local LLM Recommendations

### For 2-4 GB RAM:
- **Ollama**: `llama3.2:1b` or `phi3:mini`
- **llama.cpp**: TinyLlama Q4_K_M (~1.5GB)

### For 4-8 GB RAM:
- **Ollama**: `gemma2:2b` or `llama3.2:3b`
- **llama.cpp**: Phi-3-mini Q4_K_M (~2.5GB)

### For 8+ GB RAM:
- **Ollama**: `llama3.2` or `mistral`
- **Transformers**: Any 7B model with 8-bit quantization

## 🔧 Troubleshooting

### Voice Recognition Issues

- **No microphone detected**: Install `pyaudio` properly
- **Hindi not recognized**: Ensure internet connection for Google Speech Recognition
- **Offline mode**: Install PocketSphinx for offline recognition

### LLM Issues

- **Ollama not found**: Make sure Ollama service is running (`ollama serve`)
- **Model not found**: Pull the model first (`ollama pull <model>`)
- **Out of memory**: Use a smaller model or Q4 quantization

### Android Issues

- **Build fails**: Check Android SDK/NDK installation
- **App crashes**: Check logs with `adb logcat`
- **No voice**: Grant microphone permission in Android settings

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [examples/](examples/) for code examples
- Customize commands in `jarvis/core/command_processor.py`
