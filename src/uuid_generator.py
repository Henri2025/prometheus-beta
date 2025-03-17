import time
import random
import hashlib

def generate_uuid():
    """
    Generate a version 4 UUID without using external libraries.
    
    Returns:
        str: A UUID in standard 8-4-4-4-12 format (e.g., '550e8400-e29b-4214-a569-0000deadbeef')
    """
    # Current timestamp
    timestamp = int(time.time() * 1000)
    
    # Random components
    random_part1 = random.getrandbits(48)
    random_part2 = random.getrandbits(16)
    
    # Use hashlib to add more uniqueness and randomness
    hash_input = f"{timestamp}{random_part1}{random_part2}".encode('utf-8')
    hash_obj = hashlib.sha1(hash_input)
    hash_hex = hash_obj.hexdigest()
    
    # Create UUID in standard format
    uuid_parts = [
        hash_hex[:8],                 # 8 chars
        hash_hex[8:12],               # 4 chars
        f"4{hash_hex[12:15]}",         # Version 4 UUID starts with '4'
        f"{hex(int(hash_hex[15:18], 16) & 0x3 | 0x8)[2:].zfill(4)}", # variant bits, ensure 4 chars
        hash_hex[18:30]               # 12 chars
    ]
    
    return '-'.join(uuid_parts)