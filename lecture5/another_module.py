from selenium.webdriver.support import expected_conditions

import modules as m
import strings as s

expected_conditions.element_to_be_clickable()

print ('JUST IMPORTED MODULE')

if __name__ == '__main__':
    print(f'My favourite student is {s.NAME} {m.LASTNAME}')