import logging

import text

async def generate_pecanbot_count(prompt) -> int:
    try:
        if isinstance(int(prompt), int):
            return int(prompt) // text.text_pecanbon_price
    except Exception as e:
            logging.error(e)
            return 0