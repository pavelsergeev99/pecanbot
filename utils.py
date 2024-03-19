import logging

import text

async def generate_pecanbot_count(prompt) -> int:
    if isinstance(int(prompt), int):
        return int(prompt) // text.text_pecanbon_price
    else:
        return 0