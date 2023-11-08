caracter = input("Cual es el caracter ")
if "A" <= caracter <= "Z":
  print("Mayuscula")
elif "a" <= caracter <= "z":
  print("Minuscula")
elif caracter == "Ñ" or caracter == "ñ":
  print("eñe")
else:
  print("No es una letra")