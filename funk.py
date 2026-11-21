def omgång(s1,s2,vinnaren):

    s1_vinner=[["sten","sax"],["sax","påse"],["påse","sten"]]
    s2_vinner=[["sax","sten"],["påse","sax"],["sten","påse"]]

    val=[]

    print("")
    print(" ---- NY OMGÅNG ---- ")
    print("")
    val.append(input(s1+" det är din tur! Välj sten, sax eller påse: "))
    print("")
    print("\n"*20)
    val.append(input(s2+" det är din tur! Välj sten, sax eller påse: "))

    if val[0]==val[-1]:
        print("")
        print("Ni valde samma, kör om......")
        print("")
    for alternativ in s1_vinner:
        if alternativ==val:
            print("")
            print("Grattis",s1,"du vann en omgång!!")
            print("")
            return vinnaren.append(s1)
    for alternativ in s2_vinner:
        if alternativ==val:
            print("")
            print("Grattis",s2,"du vann en omgång!!")
            print("")
            return vinnaren.append(s2)

 

def köra(s1,s2,vinnaren):
    while len(vinnaren)<3:
       omgång(s1,s2,vinnaren)

    if vinnaren.count(s1)>vinnaren.count(s2):
       print("GRATTIS",s1,"DU VANN TOTALT ÖVER",s2,"MED 2-1 OCH ÄR DÄRMED MYCKET BÄTTRE <3")
       print("")
    else: 
       print("GRATTIS",s2,"DU VANN TOTALT ÖVER",s1,"MED 2-1 OCH ÄR DÄRMED MYCKET BÄTTRE <3")
       print("")
