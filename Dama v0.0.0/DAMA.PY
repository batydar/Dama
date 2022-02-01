satır1={"B","S","X","X","X","X","X","X"}
satır2={"B","B","B","B","B","B","B","B"}
satır3={"B","B","B","B","B","B","B","B"}
satır4={"X","X","X","X","X","X","X","X"}
satır5={"X","X","X","X","X","X","X","X"}
satır6={"S","S","S","S","S","S","S","S"}
satır7={"S","S","S","S","S","S","S","S"}
satır8={"X","X","X","X","X","X","X","X"}

def beyazhareket():
    user_input=input("Hangi taşı hareket ettireceksiniz ('satır','sütün') şeklinde yazınız\n")
    seçilentaş=user_input.split(",")
    if seçilentaş[0]=="1":
        if seçilentaş[1]=="1":    
            if satır1[0]=="B":
                user_input=input("Taşı hangi yöne hareket ettireceksin (sağ, sol, üst, aşağı)\n")
                if user_input=="sağ":
                    if satır1[1]=="X" or satır1[1]=="S":
                        if satır1[1]=="X":
                            satır1[0]="X"
                            satır1[1]="B"
                        else:
                            if satır1[2]!="S":
                                satır1[1]="X"
                                satır1[2]="B"
                            else:
                                print("Bu hareketi yapamazsıız")


beyazhareket()
print(satır1)
print(satır2)
print(satır3)
print(satır4)
print(satır5)
print(satır6)
print(satır7)
print(satır8)