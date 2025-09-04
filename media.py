nota1=float(input("digite uma nota"))
nota2=float(input("digite mais uma nota" ))
nota3=float(input("digite mais uma nota"))
nota4=float(input("digite a ultima nota"))
media=(nota1+nota2+nota3+nota4)/4
print(media)

if media>7.0:
    print(f"media:{media}- aprovado")
elif media<5.0 <7.0:
    print (f"media:{media}-recuperacao")
else:
    print("5.0")
