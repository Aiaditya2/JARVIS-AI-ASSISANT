# -*- coding: utf-8 -*-
"""
Main JARVIS Application
Entry point for the JARVIS assistant
"""

import logging
import sys
import codecs
from typing import Optional
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    # Set UTF-8 encoding for stdout/stderr
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if hasattr(sys.stderr, 'buffer'):
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    # Set console code page to UTF-8
    try:
        import os
        os.system('chcp 65001 > nul 2>&1')
    except:
        pass

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from jarvis.core.voice_recognizer import VoiceRecognizer
from jarvis.core.tts_engine import TTSEngine
from jarvis.core.llm_handler import LLMHandler
from jarvis.core.command_processor import CommandProcessor
from jarvis.android.android_voice import AndroidVoiceHandler

# Setup UTF-8 encoding first
from jarvis.utils.encoding import setup_utf8_encoding
setup_utf8_encoding()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class JARVIS:
    """Main JARVIS assistant class"""
    
    def __init__(
        self,
        language: str = "hi-IN",
        model_type: str = "ollama",
        model_name: str = "llama3.2:1b",
        use_android: bool = False
    ):
        """
        Initialize JARVIS
        
        Args:
            language: Language code (hi-IN for Hindi, en-US for English)
            model_type: LLM backend type
            model_name: LLM model name
            use_android: Use Android voice handler
        """
        self.language = language
        self.use_android = use_android
        
        # Initialize components
        logger.info("Initializing JARVIS...")
        
        if use_android:
            self.voice_handler = AndroidVoiceHandler()
            self.tts = None  # Use Android TTS
        else:
            self.voice_recognizer = VoiceRecognizer(language=language)
            self.tts = TTSEngine(language=language.split("-")[0])
        
        self.llm = LLMHandler(model_type=model_type, model_name=model_name)
        self.command_processor = CommandProcessor()
        
        logger.info("JARVIS initialized successfully")
    
    def process_command(self, text: str) -> str:
        """
        Process a command and return response
        
        Args:
            text: Input command text
            
        Returns:
            Response string
        """
        # First try command processor
        response = self.command_processor.process(text)
        
        # If no command matched, use LLM
        if response is None:
            prompt = f"User: {text}\nAssistant:"
            response = self.llm.generate(prompt)
        
        return response
    
    def speak(self, text: str):
        """Speak response"""
        if self.use_android and self.voice_handler:
            self.voice_handler.speak_hindi(text)
        elif self.tts:
            self.tts.speak(text)
    
    def listen_and_respond(self):
        """Listen for command and respond"""
        if self.use_android:
            def on_recognized(text: str):
                logger.info(f"Recognized: {text}")
                response = self.process_command(text)
                self.speak(response)
            
            self.voice_handler.start_listening_hindi(on_recognized)
        else:
            text = self.voice_recognizer.listen_once()
            if text:
                logger.info(f"Recognized: {text}")
                response = self.process_command(text)
                logger.info(f"Response: {response}")
                self.speak(response)
                return response
        return None
    
    def run_interactive(self):
        """Run in interactive mode"""
        logger.info("JARVIS is ready. Say 'exit' to quit.")
        
        if not self.use_android:
            while True:
                try:
                    response = self.listen_and_respond()
                    if response and "exit" in response.lower():
                        break
                except KeyboardInterrupt:
                    logger.info("Interrupted by user")
                    break
                except Exception as e:
                    logger.error(f"Error in interactive mode: {e}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="JARVIS AI Assistant")
    parser.add_argument(
        "--language",
        default="hi-IN",
        help="Language code (default: hi-IN for Hindi)"
    )
    parser.add_argument(
        "--model-type",
        default="ollama",
        choices=["ollama", "transformers", "llama_cpp"],
        help="LLM backend type"
    )
    parser.add_argument(
        "--model-name",
        default="llama3.2:1b",
        help="LLM model name"
    )
    parser.add_argument(
        "--android",
        action="store_true",
        help="Use Android voice handler"
    )
    
    args = parser.parse_args()
    
    jarvis = JARVIS(
        language=args.language,
        model_type=args.model_type,
        model_name=args.model_name,
        use_android=args.android
    )
    
    jarvis.run_interactive()


if __name__ == "__main__":
    main()
