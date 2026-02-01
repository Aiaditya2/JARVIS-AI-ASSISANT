# -*- coding: utf-8 -*-
"""
Text-to-Speech Engine with Hindi Support
"""

import pyttsx3
import threading
import logging
import sys
from typing import Optional

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        import codecs
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        if hasattr(sys.stderr, 'buffer'):
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except Exception:
        pass

logger = logging.getLogger(__name__)


class TTSEngine:
    """Text-to-Speech engine supporting multiple languages including Hindi"""
    
    def __init__(self, language: str = "hi"):
        """
        Initialize TTS engine
        
        Args:
            language: Language code (hi for Hindi, en for English)
        """
        try:
            self.engine = pyttsx3.init()
            self.language = language
            self.setup_voice()
        except Exception as e:
            logger.error(f"Failed to initialize TTS engine: {e}")
            self.engine = None
    
    def setup_voice(self):
        """Configure voice settings"""
        if not self.engine:
            return
        
        try:
            voices = self.engine.getProperty('voices')
            
            # Try to find Hindi voice
            if self.language == "hi":
                for voice in voices:
                    if 'hindi' in voice.name.lower() or 'hi' in voice.id.lower():
                        self.engine.setProperty('voice', voice.id)
                        logger.info(f"Using Hindi voice: {voice.name}")
                        break
            
            # Set speech rate and volume
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
        except Exception as e:
            logger.warning(f"Could not setup voice: {e}")
    
    def speak(self, text: str, async_mode: bool = True):
        """
        Convert text to speech
        
        Args:
            text: Text to speak
            async_mode: If True, speak in background thread
        """
        if not self.engine:
            logger.error("TTS engine not initialized")
            return
        
        def _speak():
            try:
                # Ensure text is properly encoded
                if isinstance(text, bytes):
                    text_utf8 = text.decode('utf-8')
                else:
                    text_utf8 = text
                
                # Handle encoding issues with pyttsx3
                try:
                    self.engine.say(text_utf8)
                    self.engine.runAndWait()
                except UnicodeEncodeError:
                    # Fallback: encode to ASCII with error handling
                    text_safe = text_utf8.encode('ascii', 'ignore').decode('ascii')
                    if text_safe:
                        self.engine.say(text_safe)
                        self.engine.runAndWait()
                    else:
                        logger.warning("Could not convert text to speech due to encoding issues")
            except Exception as e:
                logger.error(f"Error in TTS: {e}")
        
        if async_mode:
            thread = threading.Thread(target=_speak, daemon=True)
            thread.start()
        else:
            _speak()
    
    def set_language(self, language: str):
        """Change TTS language"""
        self.language = language
        self.setup_voice()
