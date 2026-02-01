"""
Basic usage example for JARVIS
"""

from jarvis.main import JARVIS

def main():
    # Initialize JARVIS with Hindi support
    jarvis = JARVIS(
        language="hi-IN",  # Hindi
        model_type="ollama",
        model_name="llama3.2:1b"
    )
    
    # Run interactive mode
    print("JARVIS is ready! Speak in Hindi or English.")
    print("Say 'exit' to quit.\n")
    
    jarvis.run_interactive()

if __name__ == "__main__":
    main()
