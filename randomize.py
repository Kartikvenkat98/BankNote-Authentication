import random as rdm
fid = open("bank.csv", "r")
li = fid.readlines()
fid.close()
print(li)

rdm.shuffle(li)
print(li)

fid = open("shuffled_bank.csv", "w")
fid.writelines(li)
fid.close()
