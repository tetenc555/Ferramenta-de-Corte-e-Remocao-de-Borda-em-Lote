import os
from PIL import Image

def cortar_imagem(imagem, largura, altura):
    #Abre a imagem e pega informações para os cálculos
    img = Image.open(imagem)
    largura_original, altura_original = img.size
    quantidade_horizontal = largura_original // largura
    quantidade_vertical = altura_original // altura

    #Cria um vetor para armazenar as imagens cortadas
    imagens_cortadas = []

    #Corta a imagem em partes iguais, mantendo a resolução especificada até a quantidade possivel
    for y in range(quantidade_vertical):
        for x in range(quantidade_horizontal):
            box = (x * largura, y * altura, (x + 1) * largura, (y + 1) * altura)
            nova_imagem = img.crop(box)
            imagens_cortadas.append(nova_imagem)

    #Se a imagem não for divisível perfeitamente pela resolução especificada, adiciona o restante da imagem no lado direito e inferior
    #Isso pode resultar em uma perda pequena do ponto inferior direito, onde não é possivel manter alguma das resoluções na pedida pelo usuário
    if largura_original % largura != 0:
        for y in range(quantidade_vertical):
            box = (quantidade_horizontal * largura, y * altura, largura_original, (y + 1) * altura)
            nova_imagem = img.crop(box)
            imagens_cortadas.append(nova_imagem)

    if altura_original % altura != 0:
        for x in range(quantidade_horizontal):
            box = (x * largura, quantidade_vertical * altura, (x + 1) * largura, altura_original)
            nova_imagem = img.crop(box)
            imagens_cortadas.append(nova_imagem)

    return imagens_cortadas


def maincorte (largura_resolucao, altura_resolucao):
    #Diretório contendo as imagens com bordas removidas
    diretorio = 'outputBD/'  

    #Lista todos os arquivos de imagem no diretório
    arquivos_imagens = [f for f in os.listdir(diretorio) if f.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG'))]

    os.makedirs('output/', exist_ok=True)
    #Roda a função em cada imagem, corta e salva as partes cortadas
    for imagem in arquivos_imagens:
        imagens_cortadas = cortar_imagem(os.path.join(diretorio, imagem), largura_resolucao, altura_resolucao)
        #Salvando as imagens cortadas
        for i, img in enumerate (imagens_cortadas):
            os.chdir('output/')
            img.save(f'ic_{i}_{imagem}.jpg')
            os.chdir("..")
            
    print("Corte realizado com sucesso! :3")