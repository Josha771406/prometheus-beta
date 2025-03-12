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
    if not word or not isinstance(word, str):
        return False
    
    # Pre-process and validate rules
    validated_rules = []
    for rule in rules:
        if not isinstance(rule, dict):
            raise ValueError(f"Invalid rule format: {rule}")
        
        validated_rules.append(rule)
    
    # Apply each rule sequentially
    for rule in validated_rules:
        # Check existence of required keys
        if 'type' not in rule:
            raise ValueError(f"Rule missing 'type' key: {rule}")
        
        rule_type = rule['type']
        
        # Length validation
        if rule_type == 'length':
            min_length = rule.get('min', 0)
            max_length = rule.get('max', float('inf'))
            if not (min_length <= len(word) <= max_length):
                return False
        
        # Character set validation
        elif rule_type == 'chars':
            allowed_chars = rule.get('allowed', set())
            if not all(char in allowed_chars for char in word):
                return False
        
        # Prefix validation
        elif rule_type == 'prefix':
            prefix = rule.get('value', '')
            if not word.startswith(prefix):
                return False
        
        # Suffix validation
        elif rule_type == 'suffix':
            suffix = rule.get('value', '')
            if not word.endswith(suffix):
                return False
        
        # Unsupported rule type
        else:
            raise ValueError(f"Unsupported rule type: {rule_type}")
    
    return True