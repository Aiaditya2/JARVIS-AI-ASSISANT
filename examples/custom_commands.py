# -*- coding: utf-8 -*-
"""
Example of adding custom commands to JARVIS
"""

import sys
import codecs

# Fix encoding for Windows
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

from jarvis.main import JARVIS

def main():
    # Initialize JARVIS
    jarvis = JARVIS(
        language="hi-IN",
        model_type="ollama",
        model_name="llama3.2:1b"
    )
    
    # Register custom command
    def greet_command(text):
        return "नमस्ते! मैं JARVIS हूं, आपकी कैसे मदद कर सकता हूं?"
    
    jarvis.command_processor.register_command("greet", greet_command)
    jarvis.command_processor.hindi_commands["नमस्ते"] = "greet"
    
    # Test command
    response = jarvis.process_command("नमस्ते")
    print(f"Response: {response}")
    jarvis.speak(response)

if __name__ == "__main__":
    main()
