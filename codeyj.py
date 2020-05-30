import re

alphabet="1234567890ABCDEFGHIJKLMNOPQRSTUVWSYZ-. *"
bars=["WNNNW","NWNNW","WWNNN","NNWNW","WNWNN","NWWNN","NNNWW","WNNWN","NWNWN","NNWWN"]
spaces=[2,3,4,1]
#code yj规则1：对尾部为010的编码，去掉10
#code yj Rule 1: If the end of a code is 010, remove the 10
codeyjRule1=r".*010$"   
#code yj规则2/3：如果一个编码的尾部为0110，其下一个编码头部为110，则去掉两个11中间的0
#code yj Rule 2/3: If the end of a code is 0110, and the head of the next code is 110, remove the 0 between two codes 
codeyjRule2=r".*0110$"  
codeyjRule3=r"^110.*"

def encode39(char): #转化为code39码/convert a char to code 39
    i=alphabet.find(char)
    encodedchar=""
    tspace=0
    for bar in bars[i%10]:
        if bar=='W':
            encodedchar=encodedchar+'11'
        elif bar=='N':
            encodedchar=encodedchar+'1'
        tspace+=1
        if tspace==spaces[int(i/10)]:
            encodedchar=encodedchar+'00'
        else:
            encodedchar=encodedchar+'0'
    return encodedchar

def code2img(code,codewidth=2,imgheight=50):    #将二进制码转换为图片/covert binary code to picture
    imgrow=[]
    for c in code:
        if c=='1':
            for i in range(codewidth):
                imgrow.append(0)
        elif c=='0':
            for i in range(codewidth):
                imgrow.append(255)
    
    bimg=[]
    for i in range(imgheight):
        bimg.append(imgrow)

    return bimg

def codeyjencode(string):   #将字符串转化为Code yj编码/convert string to code yj 
    uncodedstr=string
    encodedstrList=[]
    for c in uncodedstr:
        if re.match(codeyjRule1,encode39(c))==None:
            encodedstrList.append(encode39(c))
        else:
            encodedstrList.append(encode39(c)[:-2])
    if not len(encodedstrList)==1:
        for i in range(len(encodedstrList)-1):
            if not re.match(codeyjRule2,encodedstrList[i])==None:
                if not re.match(codeyjRule3,encodedstrList[i+1])==None:
                    encodedstrList[i]=encodedstrList[i][:-1]
                    break
    encodedstrList.append('1')
    return "".join(encodedstrList)