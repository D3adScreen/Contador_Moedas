def EX1_Nivel_1 (valor):
        if valor>=0.01 and valor<=20:
            print(valor)
            a=valor//2
            ab=valor%2
            ab=round(ab,2)
            b=ab//1
            bb=ab%1
            bb=round(bb,2)
            c=bb//0.50
            cb=bb%0.50
            cb=round(cb,2)
            d=cb//0.20
            db=cb%0.20
            db=round(db,2)
            e=db//0.10
            eb=db%0.10
            eb=round(eb,2)
            f=eb//0.05
            fb=eb%0.05
            fb=round(fb,2)
            g=fb//0.02
            gb=fb%0.02
            gb=round(gb,2)
            h=gb//0.01
            hb=gb%0.01
            hb=round(hb,2)
            dic={"2€":a,"1€":b,"50cent":c,"20cent":d,"10cent":e,"5cent":f,"2cent":g,"1cent":h}
            return(dic)
        else:
            print("O valor tem de estar entre 0.01 e 20")

valor=float(input("Escreva um valor entre 0.01 e 20: "))   
ex=EX1_Nivel_1 (valor)
print(ex)
    