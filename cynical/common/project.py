'''
Generates a new random project name
'''

import logging
import random
import re


def execute():
    found = False
    words = []
    code = ''
    names = []

    # Read al words into a list
    with open('/usr/share/dict/words', 'r') as w:
        for line in w.readlines():
            words.append(line.strip())

    while not found:
        # Generates a new code and creates a regex
        code = ''.join(random.choices('bcdfghjklmnpqrstvwxyz', k=4))
        regex = f'^{code[0]}.*{code[1]}.*{code[2]}.*{code[3]}'
        p = re.compile(regex, re.IGNORECASE)

        for word in words:
            if p.match(word):
                found = True
                names.append(word)

    return code, names


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info('Cynical Common Project - Start')

    try:
        code, names = execute()

        print(f'Code: {code}')
        for name in names:
            print(f'Name: {name}')

    except Exception as e:
        logger.exception(e)


    logger.info('Cynical Common Project - Finish')

    execute()
