import subprocess

#Only use trusted inputs when using shell = True
# p1 = subprocess.run('dir', shell = True, stdout = subprocess.PIPE)#, text = True)#,s capture_output=True)

# print(p1) #return argument and returncode
# print(p1.args) #what argument was run
# print(p1.returncode)  #0 means a succesful run
# print(p1.stdout) #standard out is being passed out to console hence our stdout shows None

# print(p1.stdout)

#Use a list to submit multiple command arguments
#subprocess.run(['dir'])

# with open('output.txt', 'w') as f:
#     p1 = subprocess.run('dir', shell=True, stdout=f)

###################
#Now let's try to catch an error.

p1 = subprocess.run(['cat', 'text.txt'], shell=True) #stderr=subprocess.DEVNULL)

p2 = subprocess.run('dir', input = p1.stdout)

#HOW TO CONCATENATE SHELL COMMANDS IN LINUX

p3 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)

print(p1.returncode)
print(p1.stderr)
