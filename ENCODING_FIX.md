# Encoding Fix for Windows

## Problem

The error `return codecs.charmap_encode(input,self.errors,encoding_table)[0]` occurs on Windows when Python tries to encode Unicode characters (like Hindi text) using the default Windows encoding (cp1252), which doesn't support these characters.

## Solution

I've implemented several fixes:

### 1. UTF-8 Encoding Declarations
All Python files with Hindi text now have:
```python
# -*- coding: utf-8 -*-
```

### 2. Windows Console Encoding Fix
The code now automatically:
- Sets Windows console to UTF-8 (code page 65001)
- Wraps stdout/stderr with UTF-8 encoders
- Handles encoding errors gracefully

### 3. Safe Encoding Utilities
Created `jarvis/utils/encoding.py` with helper functions:
- `setup_utf8_encoding()` - Configures UTF-8 for Windows
- `safe_encode()` - Safely encodes text
- `safe_decode()` - Safely decodes bytes
- `safe_print()` - Safely prints Unicode text
- `normalize_hindi_text()` - Normalizes Hindi text

## Manual Fix (if needed)

If you still encounter encoding errors, run this in PowerShell/CMD before starting JARVIS:

```powershell
chcp 65001
```

Or set it permanently:
```powershell
# In PowerShell (as Administrator)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

## Testing

Run the test script to verify encoding is working:
```bash
python test_setup.py
```

## Files Modified

- `jarvis/main.py` - Added UTF-8 setup
- `jarvis/core/command_processor.py` - Added encoding fix
- `jarvis/core/tts_engine.py` - Added safe encoding for TTS
- `jarvis/utils/encoding.py` - New encoding utilities
- `examples/custom_commands.py` - Added encoding fix

## Additional Notes

- The TTS engine now has fallback handling for encoding issues
- All logging now uses UTF-8 encoding
- Hindi text is normalized before processing
