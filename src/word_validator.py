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
    
    # Validate each rule
    rule_results = []
    for rule in rules:
        # Validate rule format
        if not isinstance(rule, dict):
            raise ValueError(f"Invalid rule format: {rule}")
        
        if 'type' not in rule:
            raise ValueError(f"Rule missing 'type' key: {rule}")
        
        rule_type = rule['type']
        result = False
        
        # Length validation
        if rule_type == 'length':
            min_length = rule.get('min', 0)
            max_length = rule.get('max', float('inf'))
            result = min_length <= len(word) <= max_length
        
        # Character set validation
        elif rule_type == 'chars':
            allowed_chars = rule.get('allowed', set())
            result = all(char in allowed_chars for char in word)
        
        # Prefix validation
        elif rule_type == 'prefix':
            prefix = rule.get('value', '')
            result = word.startswith(prefix)
        
        # Suffix validation
        elif rule_type == 'suffix':
            suffix = rule.get('value', '')
            result = word.endswith(suffix)
        
        # Unsupported rule type
        else:
            raise ValueError(f"Unsupported rule type: {rule_type}")
        
        rule_results.append(result)
    
    # If only one rule, return its result
    if len(rule_results) == 1:
        return rule_results[0]
    
    # For multiple rules, require all to be true
    return all(rule_results)