import os
from PIL import Image
def removeborda(imagem, porcentagem):
    #Define img como a imagem parametrizada
    img = Image.open(imagem)
    
    #Define proporções originais e novas a partir da porcentagem
    largura_original, altura_original = img.size

    #Calcula a nova largura e altura a partir da porcentagem
    #Obrigada Cauã e Miguel (mencionados no readme) pela ajuda com o cálculo
    #A raiz quadrada é usada para manter a proporção da imagem, por isso, pode haver uma variação mínuscula de proporção entre as imagens
    largura = int(largura_original * (((100-porcentagem) / 100)**0.5))
    altura = int(altura_original * (((100-porcentagem) / 100)**0.5))
    
    #Cria um vetor com valores de comeco e fim para cortar a imagem, os calculando a partir da relacao das novas proporções com as originais, divindo por 2 para centralizar
    caixa = (((largura_original - largura) // 2), ((altura_original - altura) // 2), ((largura_original + largura) // 2), ((altura_original + altura) // 2))
    
    #Obtem nova imagem a partir do crop da antiga com o vetor criado
    nova_img = img.crop(caixa)
    return nova_img

def mainbdremove(dir,porcentagem):
    #Define o diretorio e o valor da porcentagem a ser removida
    diretorio = f'{dir}/'

    #Define cada imagem no diretório
    arquivos_imagens = [f for f in os.listdir(diretorio) if f.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG'))]
    #Cria pasta output caso não exista
    os.makedirs('outputBD/', exist_ok=True)

    #Executa o corte para cada imagem
    for imagem in arquivos_imagens:
        nv=removeborda(os.path.join(diretorio, imagem), (porcentagem))
        #Salva a nova imagem na pasta output
        os.chdir('outputBD/')
        nv.save(f'{imagem}_{porcentagem}%borderremoved.jpg')
        os.chdir("..")

    print("Bordas removidas com sucesso! ;)")