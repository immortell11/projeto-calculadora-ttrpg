# Calculadora de estatísticas de um personagem de um RPG de mesa do gênero fantasia

# Pontos de Vida
while True:
  pv = int(input('Por favor, insira quantos pontos de vida iniciais o seu personagem possui: '))
  vig = int(input('Por favor, insira quanto de vigor o seu personagem possui: '))
  while True:
    nivel = int(input('Por favor, insira o nível do seu personagem (de 1 a 20): '))
    if nivel > 20:
      print('Valor inválido. Insira um número menor ou igual a 20.')
      continue
    elif nivel < 1:
      print('Valor inválido. Insira um número maior que 0.')
      continue
    else:
      pv_final = pv + vig + (vig * (nivel - 1))
      print(f'Seu personagem possui {pv_final} pontos de vida.')
      break

# Pontos de Energia
  pe = int(input('Por favor, insira quantos pontos de energia o seu personagem possui: '))
  fol = int(input('Por favor, insira quanto de fôlego o seu personagem possui: '))
  pe_final = pe + fol + (fol * (nivel - 1))
  print(f'Seu personagem possui {pe_final} pontos de energia.')

# Magias
  n_magias = 3 + (nivel - 1)
  if nivel >= 5:
    print(f'Seu personagem possui {n_magias} magias, sendo {nivel - 4} delas aprimoradas.')
  elif nivel >= 9:
    print(f'Seu personagem possui {n_magias} magias, sendo {nivel - 4} delas aprimoradas e {nivel - 8} aperfeiçoadas.')
  else:
    print(f'Seu personagem possui {n_magias} magias.')

# Habilidades
  n_habil = nivel // 2
  if nivel == [3,5,7,9,11,13,15,17,19]:
    n_habil - 0.5
  if nivel == 1:
    print('Seu personagem não possui nenhuma habilidade.')
  else:
    print(f'Seu personagem possui {n_habil} habilidade(s)')

  restart = input("Gostaria de calcular outro personagem? (s/n): ").strip().lower()

  if restart.lower() != 's':
    print('Tchau!')
    break
