#方法一
'''
import re

str1=input()
ret_greed = re.findall('( *\D*)(-?\+?\d+).*',str1)
# ret_search = re.search('(-?\+?)',ret_greed[0][0].replace(" ","")).group()
# print(ret_greed)
# print(ret_greed[0][1])
match = ret_greed[0][0].replace(" ","")
# print(match)
if match == "-" or match == "+" or match == "":
    newstr = match + ret_greed[0][1]
    print(max(min(eval(newstr), 2**31 - 1), -2**31))
else:
    print("0")
'''


#方法二  C语言版本
'''
int myAtoi(char* str) {      //定义一个指针字符串
    
    int len=strlen(str);
    if(len==0){
        return 0;
    }
    int i=0;
    while(str[i]==' '){
       
        i++;
    }
    
    if(str[i]!='+'&&str[i]!='-'&&str[i]<'0'&&str[i]>'9'){
        return 0;
    }
    
    double *a=(double *)malloc(sizeof(double)*(len));   //分配内存地址
    double sum=0;
    int flag=1;
    if(str[i]=='+'){//正数
         i++;
    }else if(str[i]=='-'){//负数
         i++;
         flag=-1;
    }
    
    int k=0;
    while(str[i]>='0'&&str[i]<='9'){
        *a=str[i]-'0';
        sum=sum*10+(*a);
        a++;  //寻址
        i++;
    }
            
    if(flag==-1){
        sum=sum*(-1);
    }
    
    if(sum<INT_MIN){
        return INT_MIN;
    }else if(sum>INT_MAX){
        return INT_MAX;
    }else{
        return (int)sum;
    }

}

'''


