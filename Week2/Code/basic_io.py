#comentarios
#input file

f = open('../Sandbox/test.txt', 'r')

for line in f:
    print line,
    
f.close()

#same but skip blank lines:
f = open('../Sandbox/test.txt', 'r')

for line in f:
    if len(line.strip()) > 0:
        print line,
f.close()

#output file

list_to_save = range(100)

f = open('../Sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n')
f.close()

#storing objects

my_dictionary = {"akey": 10, "another key": 11}

import pickle

f = open('../Sandbox/testp.p','wb')
pickle.dump(my_dictionary, f)
f.close()

#load data again
f= open('../Sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close

print another_dictionary