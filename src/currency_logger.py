import logging
from typing import Union

def format_currency_log(
    amount: Union[int, float], 
    currency: str = '$', 
    locale: str = 'en_US'
) -> str:
    """
    Format a number with a currency symbol and log it.

    Args:
        amount (Union[int, float]): The monetary amount to format and log
        currency (str, optional): Currency symbol. Defaults to '$'.
        locale (str, optional): Locale for formatting. Defaults to 'en_US'.

    Returns:
        str: Formatted currency string

    Raises:
        ValueError: If amount is not a number
        TypeError: If currency is not a string
    """
    # Validate inputs
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    
    if not isinstance(currency, str):
        raise TypeError("Currency must be a string")

    # Format the number with two decimal places
    try:
        formatted_amount = f"{currency}{amount:,.2f}"
    except Exception as e:
        raise ValueError(f"Could not format amount: {e}")

    # Log the formatted amount
    logging.info(f"Currency Log: {formatted_amount}")

    return formatted_amount