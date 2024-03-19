def inverter_string(string):
    string_invertida = ''
    for caracter in string:
        string_invertida = caracter + string_invertida
    return string_invertida

#string pre-definida
string = "Estágio Ribeirão Preto - 2024"
print("String pré-definida:", (string))
print("String invertida:", inverter_string(string))  

#string manualmente
string_digitada = input("\nDigite uma string: ")
print("String invertida:", inverter_string(string_digitada))
