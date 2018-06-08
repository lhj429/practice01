s = '/usr/local/bin/python'

s_list = s.split("/")
s_list = s_list[1:]

for i in range(0, len(s_list)):
    s_list[i] = "\'" + s_list[i] + "\'"

for i in range(0, len(s_list)):
    if(i==len(s_list)-1):
        print(s_list[i])
    else:
        print(s_list[i], end=",")

print("\'" + s[0:14] + "\', " + "\'" + s[15:] + "\'")
