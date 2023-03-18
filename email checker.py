#sami606713@gmail.com
k=0
j=0
while(True):
    email=input("enter email")
    if(len(email)>=6):
        if(email[0].isalpha()):
            if("@" in email and email.count("@")==1):
                if(email[-3]=="." or email[-4]=="."):
                    for i in email:
                        if(i==i.isspace()):
                            k=1
                        elif(i==i.isupper()):
                            email.lower()
                        elif("@" or "." or "_" not in email):
                            j=1
                        else:
                            continue
                    print("correct email")
                    with open("sami.txt","a+") as f:
                        f.write(f"incoming email is={email}\n")

                else:
                    print("wrong email")
            else:
                print("wrong email")
        else:
            print("wrong email")
    else:
        print("wrong email")