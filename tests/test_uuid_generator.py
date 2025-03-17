import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_format():
    """Test that the generated UUID matches the standard format."""
    uuid = generate_uuid()
    
    # Regex for UUID v4 format
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set()
    num_uuids = 1000
    
    for _ in range(num_uuids):
        uuids.add(generate_uuid())
    
    assert len(uuids) == num_uuids, "UUIDs are not unique"

def test_uuid_version():
    """Test that the UUID version is 4."""
    uuid = generate_uuid()
    version_char = uuid.split('-')[2][0]
    
    assert version_char == '4', f"UUID version should be 4, got {version_char}"

def test_uuid_variant():
    """Test that the UUID variant is correct."""
    uuid = generate_uuid()
    variant_char = uuid.split('-')[3][0]
    
    assert variant_char in ['8', '9', 'a', 'b'], f"Invalid variant: {variant_char}"

def test_uuid_length():
    """Test that the UUID length is correct."""
    uuid = generate_uuid()
    
    assert len(uuid) == 36, f"UUID length should be 36, got {len(uuid)}"