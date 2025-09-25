#!/usr/bin/env python3
"""
Debug script to help diagnose import issues
"""
import sys
import os
from pathlib import Path

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")

# Check if we're in the right directory
if Path("flexhash").exists():
    print("✓ flexhash directory found")
    flexhash_files = list(Path("flexhash").iterdir())
    print(f"Files in flexhash/: {[f.name for f in flexhash_files]}")
    
    # Look for compiled extensions
    so_files = list(Path("flexhash").glob("*.so")) + list(Path("flexhash").glob("*.pyd"))
    if so_files:
        print(f"✓ Found compiled extensions: {[f.name for f in so_files]}")
    else:
        print("✗ No compiled extensions found (.so/.pyd files)")
else:
    print("✗ flexhash directory not found")

print("\n" + "="*50)
print("Attempting import...")

try:
    import flexhash
    print("✓ Successfully imported flexhash")
    
    # Test the hash function
    test_data = b"test"
    result = flexhash.hash(test_data)
    print(f"✓ Hash function works: {result.hex()}")
    
except ImportError as e:
    print(f"✗ Import failed: {e}")
    
    # Try importing the C extension directly
    try:
        from flexhash import _flexhash
        print("✓ C extension _flexhash imports directly")
    except ImportError as e2:
        print(f"✗ C extension _flexhash import failed: {e2}")
        
        # Check if the module file exists
        import flexhash
        flexhash_path = Path(flexhash.__file__).parent
        print(f"flexhash package path: {flexhash_path}")
        
        extension_files = list(flexhash_path.glob("_flexhash*"))
        if extension_files:
            print(f"Found extension files: {extension_files}")
        else:
            print("No _flexhash extension files found")

except Exception as e:
    print(f"✗ Unexpected error: {e}")