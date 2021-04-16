import random
import string
import os

togen = int(input('List Amount to Generate: '))
usernamelen = int(input('Username Lenght: '))
passwordlen = int(input('Password Lenght: '))

amountdone = 0
while amountdone < togen:
    username = str(''.join(random.choices(string.ascii_letters + string.digits, k=usernamelen)))
    password = str(''.join(random.choices(string.ascii_letters + string.digits, k=passwordlen)))



    with open(os.path.abspath('UsernameList.txt'), 'a+') as Savefile:
        Savefile.seek(0)
        data = Savefile.read(100)
        if len(data) > 0:
            Savefile.write("\n")
        Savefile.write(username + ':' + password)
        amountdone += 1
        Savefile.close()
else:
    print('List Generated')