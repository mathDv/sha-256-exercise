# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import binascii

from Crypto.Hash import SHA256
__author__ = "mdv"
__date__ = "$Apr 29, 2016 11:41:02 PM$"

if __name__ == "__main__":

################################################################################
    print ("Trabalho 4 - SHA - PyCrypto")
print ("Autor - Matheus Duarte Vasconcelos")
print ("DISCIPLINA DE CRIPTOGRAFIA\n")
################################################################################
#based on: https://pythonhelp.wordpress.com/2012/09/25/filas-e-pilhas-em-python/
class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
 
    def vazia(self):
        return len(self.dados) == 0
################################################################################


################################################################################
################################################################################
#tarefa 1
#funcao para ler arquivo ("video_03.mp4") em blocos de 1024
count_blocos=1
file = open("../video_03.mp4", "rb")
bytesFrames = []
p = Pilha()
while True:
    bloco = file.read(1024)
    if not bloco:
        print ("CountBloco: ", count_blocos)
        break
    p.empilha(bloco)#coloca na pilha
    count_blocos+=1
h = SHA256.new()
block_n = p.desempilha()        #ler ultimo bloco
h.update(block_n)               #calcula hash do ultimo bloco

count =1
while True:
    block_n = p.desempilha()        #ler ultimo bloco
    if not block_n:
        print ("Count: ", count)
        print ("FIM DA PILHA")
        break
    block_next = block_n+binascii.unhexlify(h.hexdigest())
    h = SHA256.new()
    h.update(block_next)               #calcula hash do ultimo bloco
    print ("Hash do ultimo bloco", h.hexdigest())
    count +=1
quit()#descomentar esta linha para calcular hash do video de emxemplo
################################################################################

################################################################################
#funcao para ler arquivo de teste ("video05.mp4") em blocos de 1024
count_blocos=1
file = open("../video05.mp4", "rb")
bytesFrames = []
p = Pilha()
while True:
    bloco = file.read(1024)
    if not bloco:
        print ("CountBloco: ", count_blocos)
        break
    p.empilha(bloco)#coloca na pilha
    count_blocos+=1
h = SHA256.new()
block_n = p.desempilha()        #ler ultimo bloco
h.update(block_n)               #calcula hash do ultimo bloco
count =1
while True:
    block_n = p.desempilha()        #ler ultimo bloco
    if not block_n:
        print ("Count: ", count)
        print ("FIM DA PILHA")
        break
    block_next = block_n+binascii.unhexlify(h.hexdigest())
    h = SHA256.new()
    h.update(block_next)               #calcula hash do ultimo bloco
    print ("Hash do ultimo bloco", h.hexdigest())
    count +=1
################################################################################
print ("---------------------------END OF FILE------------------------------")
print ("--------------------------------------------------------------------")
quit()

