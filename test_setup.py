# -*- coding: utf-8 -*-
"""
Test script to verify JARVIS setup
"""

import sys
import codecs
import importlib

# Fix encoding for Windows
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if hasattr(sys.stderr, 'buffer'):
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    try:
        import os
        os.system('chcp 65001 > nul 2>&1')
    except:
        pass

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    modules = [
        "speech_recognition",
        "pyttsx3",
        "yaml"
    ]
    
    failed = []
    for module in modules:
        try:
            importlib.import_module(module)
            print(f"[OK] {module}")
        except ImportError:
            print(f"[FAIL] {module} - NOT INSTALLED")
            failed.append(module)
    
    return len(failed) == 0

def test_llm_backends():
    """Test LLM backend availability"""
    print("\nTesting LLM backends...")
    
    backends = {
        "ollama": "ollama",
        "transformers": "transformers",
        "llama_cpp": "llama_cpp"
    }
    
    available = []
    for name, module in backends.items():
        try:
            importlib.import_module(module)
            print(f"[OK] {name} backend available")
            available.append(name)
        except ImportError:
            print(f"[SKIP] {name} backend not available")
    
    if not available:
        print("\n⚠ WARNING: No LLM backend found!")
        print("Install at least one:")
        print("  - pip install ollama")
        print("  - pip install transformers torch")
        print("  - pip install llama-cpp-python")
    
    return available

def test_jarvis_modules():
    """Test JARVIS modules"""
    print("\nTesting JARVIS modules...")
    
    try:
        from jarvis.core.voice_recognizer import VoiceRecognizer
        from jarvis.core.tts_engine import TTSEngine
        from jarvis.core.llm_handler import LLMHandler
        from jarvis.core.command_processor import CommandProcessor
        from jarvis.main import JARVIS
        print("[OK] All JARVIS modules imported successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Error importing JARVIS modules: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("JARVIS Setup Test")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test LLM backends
    llm_backends = test_llm_backends()
    
    # Test JARVIS modules
    jarvis_ok = test_jarvis_modules()
    
    # Summary
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    
    if imports_ok and jarvis_ok:
        print("[SUCCESS] Core setup is correct!")
        if llm_backends:
            print(f"[INFO] {len(llm_backends)} LLM backend(s) available")
            print("\nYou can now run JARVIS:")
            print("  python -m jarvis.main --language hi-IN --model-type ollama")
        else:
            print("[WARNING] Install an LLM backend to use JARVIS")
    else:
        print("[ERROR] Setup incomplete. Please install missing dependencies.")
        print("\nRun: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
