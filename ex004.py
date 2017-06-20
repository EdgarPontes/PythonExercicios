a = input('Digite algo: ')
print("O tipo primitivo desse valor é {},\nSó tem espaços? {},\nÉ um número? {},\nÉ alfabetico? {},\n"
      "É alfanumérico? {},\nEstá em maiúscula: {},\nEstá em minúscula? {},\nEstá capitalizado? {},\n"
      .format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isalpha(), a.isupper(), a.islower(), a.istitle()))
