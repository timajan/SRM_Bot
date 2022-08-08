def create_text(name):
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read().replace("NAME", name)

    return text


subject = "Senior Engineers supply from 20$/h"
domain = 'https://app.hubspot.com'
email_field = '?interaction=email'
