def between(num1,num2,num3):
    return num2 < num1 < num3
def dict_of_numbers():
    d = {}
    num_no_ch=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    cha= ["twen","thir","for","fif"]
    t =  "ty"
    c = 1
    j=1
    d[0]="zero"
    while True:
        for i in range(1,20):
            if between(i,0,13):
                d[i]=num_no_ch[i-1]
            elif i <= 19:
                if 16 <= i:
                    if i == 18:
                        d[i]=num_no_ch[c+1]+"een"
                    else:
                        d[i]=num_no_ch[c+1]+"teen"
                elif 12 < i:
                    if i == 14:
                        d[i]="fourteen"
                    else:
                        d[i]=cha[j]+"teen"
                j += 1
                c += 1
        j = -1
        
        for i in range(20,100):
            if i <= 99:
                if i % 10 == 0:
                    if i <= 50:
                        d[i]=cha[j+1]+t
                    elif i == 80:
                        d[i]=num_no_ch[j+2]+"y"
                    else:
                        d[i]=num_no_ch[j+2]+t 
                    j += 1
                    c = -1
                elif i <= 59:        
                    d[i]=cha[j]+t+"-"+num_no_ch[c]
                elif between(i,80,90):
                    d[i]=num_no_ch[j+1]+"y-"+num_no_ch[c]
                else:
                    d[i]=num_no_ch[j+1]+t+"-"+num_no_ch[c]
                
                c+=1
        return d




                    
                    
                        


            

                
                
            
        
        
        