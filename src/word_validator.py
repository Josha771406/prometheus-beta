class Queue:
    """
    A simple Queue implementation using a list.
    
    This Queue class provides basic queue operations like enqueue, dequeue, 
    and checking if the queue is empty.
    """
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

def is_word_valid(word, rules):
    """
    Determine if a given word is valid according to specified rules.
    
    Args:
        word (str): The word to validate.
        rules (list): A list of validation rules to apply.
    
    Returns:
        bool: True if the word is valid, False otherwise.
    
    Raises:
        ValueError: If rules are improperly formatted.
    """
    # Explicitly handle None or empty string
    if not word or not isinstance(word, str):
        return False
    
    # Validate rules
    if not rules:
        return False
    
    # Cache rule-checking results
    length_valid = False
    chars_valid = False
    prefix_valid = False
    
    # Validate rule format and apply rules
    for rule in rules:
        if not isinstance(rule, dict):
            raise ValueError(f"Invalid rule format: {rule}")
        
        if 'type' not in rule:
            raise ValueError(f"Rule missing 'type' key: {rule}")
        
        rule_type = rule['type']
        
        # Length validation
        if rule_type == 'length':
            min_length = rule.get('min', 0)
            max_length = rule.get('max', float('inf'))
            word_length = len(word)
            length_valid = min_length <= word_length <= max_length
        
        # Character set validation
        elif rule_type == 'chars':
            allowed_chars = rule.get('allowed', set())
            chars_valid = set(word).issubset(allowed_chars)
        
        # Prefix validation
        elif rule_type == 'prefix':
            prefix = rule.get('value', '')
            prefix_valid = word.startswith(prefix)
        
        # Suffix validation
        elif rule_type == 'suffix':
            suffix = rule.get('value', '')
            if not word.endswith(suffix):
                return False
        
        # Unsupported rule type
        else:
            raise ValueError(f"Unsupported rule type: {rule_type}")
    
    # Ensure all required rules are met
    if len(rules) == 3:
        return length_valid and chars_valid and prefix_valid
    
    return all([length_valid, chars_valid, prefix_valid])