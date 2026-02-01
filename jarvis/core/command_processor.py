# -*- coding: utf-8 -*-
"""
Command Processor Module
Handles command recognition and execution
"""

import re
import logging
import sys
from typing import Dict, Callable, Optional, List

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


class CommandProcessor:
    """Processes and executes voice commands"""
    
    def __init__(self):
        self.commands: Dict[str, Callable] = {}
        self.hindi_commands: Dict[str, str] = {}  # Hindi to English mapping
        self._register_default_commands()
    
    def _register_default_commands(self):
        """Register default commands"""
        # Hindi command mappings
        self.hindi_commands = {
            "समय बताओ": "time",
            "तारीख बताओ": "date",
            "मौसम बताओ": "weather",
            "गाना बजाओ": "play music",
            "वीडियो चलाओ": "play video",
            "खोलो": "open",
            "बंद करो": "close",
            "सहायता": "help"
        }
        
        # Register command handlers
        self.register_command("time", self._get_time)
        self.register_command("date", self._get_date)
        self.register_command("weather", self._get_weather)
        self.register_command("help", self._show_help)
    
    def register_command(self, command: str, handler: Callable):
        """
        Register a new command
        
        Args:
            command: Command keyword
            handler: Function to execute
        """
        self.commands[command] = handler
        logger.info(f"Registered command: {command}")
    
    def process(self, text: str) -> Optional[str]:
        """
        Process command text and execute
        
        Args:
            text: Input command text
            
        Returns:
            Response string or None
        """
        # Normalize text
        text = text.lower().strip()
        
        # Check if it's a Hindi command
        for hindi, english in self.hindi_commands.items():
            if hindi in text or text.startswith(hindi):
                text = english
        
        # Try to match commands
        for command, handler in self.commands.items():
            if command in text:
                try:
                    result = handler(text)
                    return result
                except Exception as e:
                    logger.error(f"Error executing command {command}: {e}")
                    return f"Error executing command: {str(e)}"
        
        # If no command matched, return None (will be handled by LLM)
        return None
    
    def _get_time(self, text: str) -> str:
        """Get current time"""
        from datetime import datetime
        now = datetime.now()
        return f"Current time is {now.strftime('%I:%M %p')}"
    
    def _get_date(self, text: str) -> str:
        """Get current date"""
        from datetime import datetime
        now = datetime.now()
        return f"Today is {now.strftime('%B %d, %Y')}"
    
    def _get_weather(self, text: str) -> str:
        """Get weather information"""
        # Placeholder - implement with weather API
        return "Weather information not available. Please configure weather API."
    
    def _show_help(self, text: str) -> str:
        """Show available commands"""
        commands_list = ", ".join(self.commands.keys())
        return f"Available commands: {commands_list}"
