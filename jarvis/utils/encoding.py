# -*- coding: utf-8 -*-
"""
Encoding utilities for handling Unicode text, especially Hindi
"""

import sys
import codecs
import logging

logger = logging.getLogger(__name__)


def setup_utf8_encoding():
    """Setup UTF-8 encoding for Windows console"""
    if sys.platform == 'win32':
        try:
            # Set console code page to UTF-8
            import os
            os.system('chcp 65001 > nul 2>&1')
        except:
            pass
        
        # Fix stdout/stderr encoding
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        if hasattr(sys.stderr, 'buffer'):
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
        
        logger.info("UTF-8 encoding configured for Windows")


def safe_encode(text: str, encoding: str = 'utf-8') -> bytes:
    """
    Safely encode text to bytes
    
    Args:
        text: Text to encode
        encoding: Target encoding (default: utf-8)
        
    Returns:
        Encoded bytes
    """
    if isinstance(text, bytes):
        return text
    try:
        return text.encode(encoding)
    except UnicodeEncodeError:
        # Fallback to ASCII with error handling
        return text.encode('ascii', 'ignore')


def safe_decode(data: bytes, encoding: str = 'utf-8') -> str:
    """
    Safely decode bytes to text
    
    Args:
        data: Bytes to decode
        encoding: Source encoding (default: utf-8)
        
    Returns:
        Decoded text
    """
    if isinstance(data, str):
        return data
    try:
        return data.decode(encoding)
    except UnicodeDecodeError:
        # Try with error handling
        return data.decode(encoding, errors='ignore')


def safe_print(text: str):
    """
    Safely print Unicode text
    
    Args:
        text: Text to print
    """
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback: print ASCII representation
        try:
            print(text.encode('ascii', 'ignore').decode('ascii'))
        except:
            print("(Unable to display text due to encoding issues)")


def normalize_hindi_text(text: str) -> str:
    """
    Normalize Hindi text for processing
    
    Args:
        text: Hindi text to normalize
        
    Returns:
        Normalized text
    """
    if not isinstance(text, str):
        text = safe_decode(text) if isinstance(text, bytes) else str(text)
    
    # Remove zero-width characters and normalize
    import unicodedata
    text = unicodedata.normalize('NFKC', text)
    
    return text.strip()
