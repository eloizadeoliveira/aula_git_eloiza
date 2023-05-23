Texto = input('digite seu texto:')

def asda(texto):
    textoDividido = Texto.split(" ")
    ContadorPalavras = len(textoDividido)
    return(ContadorPalavras)


print("seu texto tem "+ str(asda(Texto)) +" palavras")


#capturar texto usuario
#dividir texto em palavras
#calcular nmero de palavras
#exibir resultado calculado para o usuario