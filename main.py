from src.corte_lote import maincorte
from src.bdremove import mainbdremove
import os

#Pede ao usuário as informações necessárias para a execução do programa
#Como mesmo a remoção de 0% de borda pode causar variações mínimas nas proporções, é necessário que o usuário escolha se deseja remover as bordas ou não
dirinicial=str(input("Digite o nome da pasta em que as fotos estão localizadas: ")) 
largura_resolucao = int(input("Digite a largura desejada para as fotos cortadas: "))
altura_resolucao = int(input("Digite a altura desejada para as fotos cortadas: "))
remover=bool(input("Deseja remover as bordas das imagens? (True/False): "))

#Executa o ciclo de atividades, de acordo com a escolha do usuário
if remover:
    porcentagem = int(input("Digite a porcentagem de borda que deseja remover: "))
    mainbdremove(dirinicial,porcentagem)
    maincorte(largura_resolucao, altura_resolucao, 'outputBD') #Nome da pasta onde as imagens sem bordas estão padronizado pois será apagada
    #Apaga a pasta com a foto inteira, sem bordas, pois não é mais necessária
    for arq in os.listdir('outputBD'):
        os.remove(f'outputBD/{arq}')
    os.rmdir('outputBD')
else:
    maincorte(largura_resolucao, altura_resolucao, dirinicial)