import logging

import text

async def generate_pecanbot_count(prompt) -> int:
    if isinstance(prompt, int):
        print(prompt)
        return prompt // text.text_pecanbon_price
    else:
        return 0