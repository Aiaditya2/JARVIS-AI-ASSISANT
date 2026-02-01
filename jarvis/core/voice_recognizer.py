# -*- coding: utf-8 -*-
"""
Voice Recognition Module with Hindi Support
Supports both English and Hindi speech recognition
"""

import speech_recognition as sr
import threading
import sys
from typing import Optional, Callable
import logging

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


class VoiceRecognizer:
    """Handles voice recognition in multiple languages including Hindi"""
    
    def __init__(self, language: str = "hi-IN"):
        """
        Initialize voice recognizer
        
        Args:
            language: Language code (hi-IN for Hindi, en-US for English)
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        self.is_listening = False
        self.callback: Optional[Callable] = None
        
        # Adjust for ambient noise
        logger.info("Adjusting for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def recognize_audio(self, audio) -> Optional[str]:
        """
        Recognize speech from audio
        
        Args:
            audio: AudioData object
            
        Returns:
            Recognized text or None
        """
        try:
            # Try Google Speech Recognition (works offline with some models)
            text = self.recognizer.recognize_google(audio, language=self.language)
            logger.info(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Recognition service error: {e}")
            # Fallback to offline recognition
            try:
                text = self.recognizer.recognize_sphinx(audio)
                return text
            except:
                return None
    
    def listen_once(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Listen for a single command
        
        Args:
            timeout: Timeout in seconds
            phrase_time_limit: Maximum phrase length
            
        Returns:
            Recognized text or None
        """
        try:
            with self.microphone as source:
                logger.info("Listening...")
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
            return self.recognize_audio(audio)
        except sr.WaitTimeoutError:
            logger.warning("Listening timeout")
            return None
        except Exception as e:
            logger.error(f"Error in listen_once: {e}")
            return None
    
    def start_continuous_listening(self, callback: Callable[[str], None]):
        """
        Start continuous listening in background
        
        Args:
            callback: Function to call with recognized text
        """
        self.callback = callback
        self.is_listening = True
        
        def listen_loop():
            while self.is_listening:
                text = self.listen_once()
                if text and self.callback:
                    self.callback(text)
        
        thread = threading.Thread(target=listen_loop, daemon=True)
        thread.start()
        logger.info("Started continuous listening")
    
    def stop_listening(self):
        """Stop continuous listening"""
        self.is_listening = False
        logger.info("Stopped listening")
    
    def set_language(self, language: str):
        """Change recognition language"""
        self.language = language
        logger.info(f"Language set to: {language}")
