"""
Utility modules for JARVIS
"""

from jarvis.utils.encoding import (
    setup_utf8_encoding,
    safe_encode,
    safe_decode,
    safe_print,
    normalize_hindi_text
)

__all__ = [
    'setup_utf8_encoding',
    'safe_encode',
    'safe_decode',
    'safe_print',
    'normalize_hindi_text'
]
