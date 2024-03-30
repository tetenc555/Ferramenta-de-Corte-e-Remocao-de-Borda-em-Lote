from src.corte_lote import maincorte
from src.bdremove import mainbdremove
import os

dirinicial=str(input("Digite o nome da pasta em que as fotos estão localizadas: ")) 
porcentagem = int(input("Digite a porcentagem de borda que deseja remover: "))
largura_resolucao = int(input("Digite a largura da resolução desejada: "))
altura_resolucao = int(input("Digite a altura da resolução desejada: "))

mainbdremove(dirinicial,porcentagem)
maincorte(largura_resolucao, altura_resolucao)
for arq in os.listdir('outputBD'):
    os.remove(f'outputBD/{arq}')
os.rmdir('outputBD')