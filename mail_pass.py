import random
import string

def randommail():
    harfler = string.ascii_lowercase
    mail=''.join(random.choice(harfler) for i in range(20))
    gmail=mail+"@gmail.com"
    return gmail
i=0
while i<=10:
    
    print(randommail())
    i=i+1


def randompass():
    harfler = string.digits
    password=''.join(random.choice(harfler) for i in range(8))
    return password

i=0
while i<=10:
    
    print(randompass())
    i=i+1