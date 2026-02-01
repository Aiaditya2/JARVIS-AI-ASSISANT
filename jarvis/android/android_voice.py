"""
Android Voice Integration Module
Handles Hindi voice recognition and TTS on Android devices
"""

import logging
from typing import Optional, Callable
import json

logger = logging.getLogger(__name__)


class AndroidVoiceHandler:
    """Handles voice operations on Android devices"""
    
    def __init__(self, use_kivy: bool = True):
        """
        Initialize Android voice handler
        
        Args:
            use_kivy: Use Kivy for Android app (True) or ADB bridge (False)
        """
        self.use_kivy = use_kivy
        self.callback: Optional[Callable] = None
        
        if use_kivy:
            self._init_kivy()
        else:
            self._init_adb()
    
    def _init_kivy(self):
        """Initialize Kivy for Android app"""
        try:
            from kivy.app import App
            from kivy.uix.button import Button
            from jnius import autoclass
            
            # Android classes
            self.PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.Intent = autoclass('android.content.Intent')
            self.RecognizerIntent = autoclass('android.speech.RecognizerIntent')
            self.SpeechRecognizer = autoclass('android.speech.SpeechRecognizer')
            self.Locale = autoclass('java.util.Locale')
            
            logger.info("Kivy Android voice initialized")
        except ImportError:
            logger.warning("Kivy not available, using fallback")
            self.use_kivy = False
        except Exception as e:
            logger.error(f"Kivy initialization error: {e}")
            self.use_kivy = False
    
    def _init_adb(self):
        """Initialize ADB bridge for communication"""
        logger.info("Using ADB bridge for Android communication")
        # ADB-based implementation would go here
    
    def start_listening_hindi(self, callback: Callable[[str], None]):
        """
        Start listening for Hindi voice input on Android
        
        Args:
            callback: Function to call with recognized text
        """
        self.callback = callback
        
        if self.use_kivy:
            self._start_kivy_listening()
        else:
            logger.warning("Android voice not available in non-Kivy mode")
    
    def _start_kivy_listening(self):
        """Start listening using Kivy/Android APIs"""
        try:
            activity = self.PythonActivity.mActivity
            
            # Create Hindi locale
            hindi_locale = self.Locale("hi", "IN")
            
            # Create intent for speech recognition
            intent = self.Intent(self.RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(
                self.RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                self.RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )
            intent.putExtra(
                self.RecognizerIntent.EXTRA_LANGUAGE,
                hindi_locale.toString()
            )
            intent.putExtra(
                self.RecognizerIntent.EXTRA_MAX_RESULTS,
                1
            )
            
            # Start activity for result
            activity.startActivityForResult(intent, 1)
            logger.info("Started Hindi voice recognition on Android")
        except Exception as e:
            logger.error(f"Error starting Android listening: {e}")
    
    def speak_hindi(self, text: str):
        """
        Speak text in Hindi on Android
        
        Args:
            text: Text to speak
        """
        if self.use_kivy:
            self._speak_kivy(text)
        else:
            logger.warning("Android TTS not available in non-Kivy mode")
    
    def _speak_kivy(self, text: str):
        """Speak using Android TTS"""
        try:
            from jnius import autoclass
            
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            Locale = autoclass('java.util.Locale')
            
            activity = self.PythonActivity.mActivity
            tts = TextToSpeech(activity, None)
            
            # Set Hindi locale
            hindi_locale = Locale("hi", "IN")
            tts.setLanguage(hindi_locale)
            
            # Speak
            tts.speak(text, TextToSpeech.QUEUE_FLUSH, None)
            logger.info(f"Speaking: {text}")
        except Exception as e:
            logger.error(f"Error in Android TTS: {e}")
