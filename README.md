# Ferramenta de Corte e Remoção de Borda em lote

Escrito em Python pra processamento facilitado e rápido! Testado num enviroment Conda com Python 3.11.5

Obrigada Cauã Moreno e Miguel Dias pela ajuda no cálculo de fórmulas e lógica geral!

## Como usar
1. Clone o repositório
2. Instale a biblioteca Pillow caso ainda não a tenha
3. Crie uma pasta com o lote de fotos a processar, no mesmo caminho que o script
4. Execute o arquivo main com as propriedades preferidas!

Vale ressaltar que: 
- No caso de processamento de foto única, basta colocar apenas uma foto no diretório inicial
- O output todo sairá em uma unica pasta, indicando nome da foto original + qual parte da foto aquele corte representa

## Problemas conhecidos
- Dependendo do tamanho da imagem, pode haver perda de uma pequena parte do canto inferior direito. Essa perda será menor que qualquer um das duas resoluções inseridas.
- A proporção poderá sofrer uma modificação minuscula na remoção de bordas. Essa modificação é quase nula e acontece apenas em alguns casos.
