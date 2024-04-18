

import random

lucky_number = random.randint(1 ,100) # משנה עם ערכים ובחירה רנדומלית בינהם


fortune_number = random.randint(1 ,3) # מספרים רנדומלי לשימוש בתנאים הבאים

fortune_text = '' # משתנה ריק בתנאים נכניס בו משפטים

if fortune_number == 1:
    fortune_text = ' you will hace a great day'
if fortune_number == 2:
    fortune_text = ' you will hace a goddddd day'
if fortune_number == 3:
    fortune_text = ' you will hace a woww day'

print(f' {fortune_text} your lucky number is {lucky_number}') # ואז אפשר להכניס פעלים למשפט f - הדפסת משפטת עם פועל המשתנה