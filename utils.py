import text

def generate_pecanbot_count(prompt) -> int:
    if isinstance(prompt, int):
        return prompt // text.text_pecanbon_price
    else:
        return 0