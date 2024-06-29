def format_to_currency(value: str) -> str:
    """ 
        Format a number to currency format
    """

    return f'{int(value):,.0f}'.replace(",", ".")
