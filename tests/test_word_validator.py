import pytest
from src.word_validator import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    q = Queue()
    assert q.is_empty() == True
    
    q.enqueue(1)
    assert q.is_empty() == False
    
    item = q.dequeue()
    assert item == 1
    assert q.is_empty() == True

def test_queue_dequeue_error():
    """Test that dequeuing from an empty queue raises an error."""
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_word_valid_length_rules():
    """Test word validation with length rules."""
    rules = [
        {'type': 'length', 'min': 3, 'max': 5}
    ]
    assert is_word_valid('cat', rules) == True
    assert is_word_valid('hello', rules) == True
    assert is_word_valid('hi', rules) == False
    assert is_word_valid('elephant', rules) == False

def test_word_valid_chars_rules():
    """Test word validation with character set rules."""
    rules = [
        {'type': 'chars', 'allowed': set('abcdefg')}
    ]
    assert is_word_valid('cafe', rules) == True
    assert is_word_valid('aged', rules) == True
    assert is_word_valid('hello', rules) == False
    assert is_word_valid('123', rules) == False

def test_word_valid_prefix_rules():
    """Test word validation with prefix rules."""
    rules = [
        {'type': 'prefix', 'value': 're'}
    ]
    assert is_word_valid('research', rules) == True
    assert is_word_valid('return', rules) == True
    assert is_word_valid('hello', rules) == False

def test_word_valid_suffix_rules():
    """Test word validation with suffix rules."""
    rules = [
        {'type': 'suffix', 'value': 'ing'}
    ]
    assert is_word_valid('going', rules) == True
    assert is_word_valid('running', rules) == True
    assert is_word_valid('hello', rules) == False

def test_word_valid_multiple_rules():
    """Test word validation with multiple combined rules."""
    rules = [
        {'type': 'length', 'min': 3, 'max': 5},
        {'type': 'chars', 'allowed': set('abcdefg')},
        {'type': 'prefix', 'value': 're'}
    ]
    assert is_word_valid('read', rules) == True
    assert is_word_valid('reap', rules) == False
    assert is_word_valid('realms', rules) == False
    assert is_word_valid('hello', rules) == False

def test_word_valid_edge_cases():
    """Test edge cases for word validation."""
    # Empty word and empty rules
    assert is_word_valid('', []) == False
    assert is_word_valid(None, []) == False

def test_invalid_rule_format():
    """Test error handling for invalid rule formats."""
    with pytest.raises(ValueError):
        is_word_valid('hello', [{'wrong_key': 'value'}])
    
    with pytest.raises(ValueError):
        is_word_valid('hello', [{'type': 'unknown'}])
    
    with pytest.raises(ValueError):
        is_word_valid('hello', [1, 2, 3])  # Invalid rule type