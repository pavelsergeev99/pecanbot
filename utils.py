import logging

import text

async def generate_pecanbot_count(prompt) -> int:
    if isinstance(prompt, int):
        try:
            print(prompt)
            return prompt // text.text_pecanbon_price
        except Exception as e:
            logging.error(e)       
    else:
        return 0