import text

async def generate_pecanbot_count(prompt) -> int:
    prompt_type = type(prompt)
    if (prompt_type == "<class 'int'>" or prompt_type == "<class 'float'>"):
         return int(prompt) // text.text_pecanbon_price
    else:
         return 0