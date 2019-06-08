import base64
from multiprocessing import Process
def decodeGua(cipher):
    codes = {}
    gua = '乾﹑坤﹑屯﹑蒙﹑需﹑讼﹑师﹑比﹑小畜﹑履﹑泰﹑否﹑同人﹑大有﹑谦﹑豫﹑随﹑蛊﹑临﹑观﹑噬嗑﹑贲﹑剥﹑复﹑无妄﹑大畜﹑颐﹑大过﹑坎﹑离﹑咸﹑恒﹑遯﹑大壮﹑晋﹑明夷﹑家人﹑睽﹑蹇﹑解﹑损﹑益﹑夬﹑姤﹑萃﹑升﹑困﹑井﹑革﹑鼎﹑震﹑艮﹑渐﹑归妹﹑丰﹑旅﹑巽﹑兑﹑涣﹑节﹑中孚﹑小过﹑既济﹑未济'
    number = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9,+,/'
    number_list = number.split(',')
    gua_list = gua.split('﹑')
    for key,value in zip(gua_list,number_list):
        codes[key] = value
    for (key,value) in codes.items():
        cipher = cipher.replace(key,value)
    bytes001 = base64.b64decode(cipher.encode('utf-8'))
    print(str(bytes001, 'utf-8'))



def main():
    str = '大过随坤大壮乾师坎乾大过遯坤睽乾比随乾谦遯乾未济乾比遯乾离乾乾小过乾比噬嗑乾坎遯坤困乾蒙损乾无妄遯坤渐乾师家人乾颐乾乾涣乾蒙随乾随遯坤师乾蒙坎乾同人乾乾鼎乾需噬嗑乾大有革乾艮乾蒙同人乾大有革乾艮乾蒙小畜乾大有乾乾艮乾蒙随乾蛊随坤坤乾蒙需乾同人乾乾震乾需小畜乾蛊随乾革乾蒙需乾随革乾丰乾需小畜乾随革乾丰乾需需乾随随乾鼎乾需随乾蛊乾乾革乾需无妄乾谦随坤屯乾蒙遯乾'
    decodeGua(str)




if __name__ == '__main__':
    main()