#!/usr/bin/env python3
"""
Test script for flexhash wheel
"""

def test_flexhash():
    """Test basic flexhash functionality"""
    try:
        import flexhash
        
        # Test basic functionality
        test_data = b'test'
        result = flexhash.hash(test_data)
        
        # Verify result
        if len(result) != 32:
            raise ValueError(f"Expected 32 bytes, got {len(result)}")
        
        # Test consistency
        result2 = flexhash.hash(test_data)
        if result != result2:
            raise ValueError("Hash function is not deterministic")
        
        print("✓ flexhash test passed")
        return True
        
    except Exception as e:
        print(f"✗ flexhash test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sys
    success = test_flexhash()
    sys.exit(0 if success else 1)