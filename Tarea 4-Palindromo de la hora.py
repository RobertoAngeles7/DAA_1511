contador_palindromos = 0
for hora in range(0,24):    
    convertir_str_hora=str(hora).zfill(2)
    for minuto in range(0,60):
        convertir_str_minuto=str(minuto).zfill(2)
        if convertir_str_hora == convertir_str_minuto[::-1]:
            contador_palindromos = contador_palindromos +1
            c = convertir_str_hora + (":") + convertir_str_minuto
            print (c)
print("Total de palindromos: ", contador_palindromos)