# -- coding: utf-8 --
s='{"key":"{key}","value":"{value}"}'
l=[{'key':'k1','value':'111'},{'key':'k2','value':'222'}]
isIN=True
s1=None
for i in range(2):
    for k,v in l[i].items():
        #if  str in s:
        if  "{"+k+"}" in s and isIN:
            s1=s.replace("{"+k+"}",v)
            isIN=False
        if "{" + k + "}" in s1 and (not isIN):
            s1 = s1.replace("{" + k + "}", v)
            isIN=True
    print(s1)
