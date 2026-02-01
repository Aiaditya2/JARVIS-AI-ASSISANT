# -*- coding: utf-8 -*-
"""
Test script to verify encoding fixes work correctly
"""

import sys
import codecs

# Setup UTF-8 encoding
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

def test_hindi_text():
    """Test printing Hindi text"""
    print("=" * 50)
    print("Testing Hindi Text Encoding")
    print("=" * 50)
    
    hindi_texts = [
        "समय बताओ",
        "तारीख बताओ",
        "मौसम बताओ",
        "नमस्ते! मैं JARVIS हूं",
        "सहायता"
    ]
    
    print("\nHindi Commands:")
    for i, text in enumerate(hindi_texts, 1):
        try:
            print(f"{i}. {text}")
        except UnicodeEncodeError as e:
            print(f"{i}. ERROR: {e}")
            return False
    
    print("\n[OK] All Hindi text displayed correctly!")
    return True

def test_jarvis_imports():
    """Test importing JARVIS modules"""
    print("\n" + "=" * 50)
    print("Testing JARVIS Module Imports")
    print("=" * 50)
    
    try:
        from jarvis.utils.encoding import setup_utf8_encoding, safe_print
        from jarvis.core.command_processor import CommandProcessor
        
        print("[OK] Encoding utilities imported")
        print("[OK] Command processor imported")
        
        # Test command processor with Hindi
        processor = CommandProcessor()
        print(f"[OK] Command processor initialized")
        print(f"  Hindi commands: {len(processor.hindi_commands)}")
        
        # Test processing Hindi command
        result = processor.process("समय बताओ")
        if result:
            print(f"[OK] Hindi command processed: {result}")
        
        return True
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("\nJARVIS Encoding Test")
    print("=" * 50)
    
    # Test 1: Hindi text display
    test1 = test_hindi_text()
    
    # Test 2: JARVIS imports
    test2 = test_jarvis_imports()
    
    # Summary
    print("\n" + "=" * 50)
    print("Test Summary")
    print("=" * 50)
    
    if test1 and test2:
        print("[SUCCESS] All tests passed! Encoding is working correctly.")
        print("\nYou can now run JARVIS without encoding errors.")
    else:
        print("[ERROR] Some tests failed. Check the errors above.")
        print("\nIf you see encoding errors:")
        print("1. Make sure you're using UTF-8 encoding")
        print("2. Run: chcp 65001 (in Windows CMD)")
        print("3. Check ENCODING_FIX.md for more details")

if __name__ == "__main__":
    main()
