#3
def es_palindromo(cad):
	tam=len(cad)
	con=tam-1
	cad2=""
	while con>=0:
		cad2=cad2+cad[con]
		con=con-1 
	else:
		if cad==cad2:
			print True
		else:
			print False

cadena=raw_input("Ingrese la Palabra: ")
es_palindromo(cadena)