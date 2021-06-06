# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
TextReader = st.text_input("Shannon Fano Encoder", "Hello hitty")

dictionary={}
for i in set(TextReader):
    dictionary[i]=round(TextReader.count(i)/len(TextReader),3)
d=dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))# creation of sorted probability values
values=list(d.values())




dictionary1={}
for i in set(TextReader):
    dictionary1[i]=''

keylist=list(d)


values1=list(dictionary1.values())
dic=dict(zip(keylist, values1))


values2=list(dic.values())


def ShannonFano(d, begin, end):
    if(begin==end):
        return 
    a=begin
    z=end
    suml=0.0
    sumr=0.0
    
    while(a<=z):
        if(suml<=sumr):
            suml+=values[a]
            a+=1
        else:
            sumr+=values[z]
            z-=1
    for i in range(begin,a):
        values2[i]+='0'
    for i in range(a,end+1): 
        values2[i]+='1'

    ShannonFano(d, begin, a-1)
    ShannonFano(d, a, end)
    
ShannonFano(d,0,len(d)-1)

dic=dict(zip(keylist, values2))
st.write(f" Key value: {dic}")

x=''
for i in TextReader:
    x+=dic[i]
print(x)

st.write(f"Result: {x}")


st.markdown("""---""")


def decoder(data):
    newdic = {}
    for i in dic: # new dinctionary that replaces keys and values between each other
        newdic[dic[i]] = i
    begin = 0
    current = 0
    str1 = ''
    while current < len(data) + 1: # running on each x digit
        try:
            str1 += newdic[str(data[begin:current])] # writes into the string decoded letters
            begin = current
        except KeyError:
            current+= 1
    return str1

st.write(f"Shannon Fano decoding")
st.write(f"Encoded string: {x}")
st.write(f"Result: {decoder(x)}")
#huffman encode

st.markdown("""---""")

string = st.text_input("Huffman Encoder", "Hello hitty1")
text=string
class Tree(object):
    def __init__(self, l=None, r=None):
        self.l = l
        self.r = r
    def __str__(self):
        return '%s_%s' % (self.l, self.r)
    def nodes(self):
        return (self.l, self.r)
    def descendant(self):
        return (self.l, self.r)
    
def huffman_encoding(x, left=True, string=''):
    if type(x) is str:
        return {x: string}
    (l, r) = x.descendant()
    dic = dict()
    dic.update(huffman_encoding(l, True, string + '0'))
    dic.update(huffman_encoding(r, False, string + '1'))
    return dic

prob = {}
for i in string:
    if i in prob:
        prob[i] += 1
    else:
        prob[i] = 1
prob = sorted(prob.items(), key=lambda x: x[1], reverse=True)
nodes = prob
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = Tree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
huffmanCode = huffman_encoding(nodes[0][0])

diction={}
for (char, frequency) in prob:
    diction[char]=huffmanCode[char]
st.write(f"Key value: {diction}")

d = {}
for i in text:
    if i in d:
        d[i]+= 1
    else:
        d[i] = 1
for (char, frequency) in prob:
    print(char, round(d[char]/len(text),3))
res=''

for s in text:
    s=huffmanCode[s]
    res+=s
st.write(res)

st.markdown("""---""")
#huffman decoding 
diction1 = dict([(value, key) for key, value in diction.items()])
def huffmanDecode (dic, t):
    res = ""
    while t:
        for i in dic:
            if t.startswith(i):
                res += dic[i]
                t = t[len(i):]
    return res
res1=huffmanDecode(diction1,res)
st.write(f"Huffman decoding")
st.write(f"Encoded string: {res}")
st.write(f"Result: {res1}")
st.markdown("""---""")
#hamming encode
def Hamming15(x):
    d3=int(x[0])
    d5=int(x[1])
    d6=int(x[2])
    d7=int(x[3])
    d9=int(x[4])
    d10=int(x[5])
    d11=int(x[6])
    d12=int(x[7])
    d13=int(x[8])
    d14=int(x[9])
    d15=int(x[10])
    p1 = (d3 + d5 + d7 + d9 + d11+ d13 + d15) % 2
    p2 = (d3 + d6 + d7 + d10 + d11 + d14 + d15) % 2
    p4 = (d5 + d6 + d7 + d12 +d13+ d14 + d15) % 2
    p8 = (d9 +d10 +d11+ d12 + d13 + d14 + d15) % 2
    p0 = (p1+ p2 + d3 + p4 +d5 +d6+ d7+ p8+ d9+ d10 +d11 +d12 +d13 +d14 + d15 ) % 2
    return str(p0)+str(p1)+str(p2)+str(d3)+str(p4)+str(d5)+str(d6)+str(d7)+str(p8)+str(d9)+str(d10)+str(d11)+str(d12)+str(d13)+str(d14)+str(d15)

def Hamming7(x2):
    d3=bool(int(x2[0]))
    d5=bool(int(x2[1]))
    d6=bool(int(x2[2]))
    d7=bool(int(x2[3]))
    p1 = int(d3 ^ d5 ^ d7) 
    p2 = int(d3 ^ d6 ^ d7) 
    p4 = int(d5 ^ d6 ^ d7) 
    p0 = int(p1 ^ p2 ^ d3 ^ p4 ^ d5 ^ d6 ^ d7)
    return str(p0)+str(p1)+str(p2)+x2[0]+str(p4)+x2[1]+x2[2]+x2[3]

def Encode15(TextReader):
    e=''
    while len(TextReader) >= 11:
        lim = TextReader[0:11]
        e+=Hamming15(lim)
        TextReader = TextReader[11:]
        Encode15(TextReader)
    return e    


string15= st.text_input("Hamming encoder 15/11", "10101000000011110001001011001001110")
st.write(Encode15(string15))
def Encode7(TextReader):
    e=''
    while len(TextReader) >= 4:
        lim = TextReader[0:4]
        e+=Hamming7(lim)
        TextReader = TextReader[4:]
        Encode7(TextReader)
    return e   


string7= st.text_input("Hamming encoder 7/4", "101010000000111100010010110010011101011")
st.write(Encode7(string7))

st.markdown("""---""")

# hamming decode
init_blocks = []
for i in range(0, len(TextReader), 8):
    init_blocks.append(TextReader[i: i + 8])
for index, block in enumerate(init_blocks):
    print('b' + str(index),block)
    
def ErrorGen7(percent, bitstring):
    b=[]
    bitstring2=list(bitstring)
    x=len(bitstring)/8 
    y=round(x*percent)
    for i in range(y):
        e=random.randint(1,x)
        last=e*8
        first=e*8-8
        be=random.randint(first,last)
        if bitstring2[be] == '0':
            bitstring2[be]='1'
        else:
            bitstring2[be]='0'
        for j in range(first,last):
            b+=bitstring2[j]
       
    return b    

