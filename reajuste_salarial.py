salario = int(input()) 

if 0 < salario <= 600:
  salario_novo = salario + (salario * 0.17)
  reajuste = salario_novo - salario
  percentual = 17
  print(f'''
  Novo salario: {salario_novo: .2f}
  Reajuste ganho: {reajuste: .2f}                                                                                    
  Em percentual: {percentual} %
  ''')
elif 600 < salario <= 900:
  salario_novo = salario + (salario * 0.13)
  reajuste = salario_novo - salario
  percentual = 13
  print(f'''
  Novo salario: {salario_novo: .2f}
  Reajuste ganho: {reajuste: .2f}                                                                                   
  Em percentual: {percentual} %
  ''')
elif 900 < salario <= 1500:
  salario_novo = salario + (salario * 0.12)
  reajuste = salario_novo - salario
  percentual = 12
  print(f'''
  Novo salario: {salario_novo: .2f}
  Reajuste ganho: {reajuste: .2f}                                                                                   
  Em percentual: {percentual} %
  ''')
elif 1500 < salario <= 2000:
  salario_novo = salario + (salario * 0.10)
  reajuste = salario_novo - salario
  percentual = 10
  print(f'''
  Novo salario: {salario_novo: .2f}
  Reajuste ganho: {reajuste: .2f}                                                                                    
  Em percentual: {percentual} %
  ''')
else:
  salario_novo = salario + (salario * 0.05)
  reajuste = salario_novo - salario
  percentual = 5
  print(f'''
  Novo salario: {salario_novo: .2f}
  Reajuste ganho: {reajuste: .2f}                                                                                   
  Em percentual: {percentual} %
  ''')
   