#!/usr/bin/env python3

import ftplib
import os
import sys

def conectar_ftp(host, porta, usuario, senha):
    try:
        # Criando uma instância do objeto FTP
        ftp = ftplib.FTP()
        
        # Conectando ao servidor FTP
        ftp.connect(host, porta)
        
        # Realizando login no servidor FTP
        ftp.login(usuario, senha)
        
        print("Conexão FTP bem-sucedida!")

        return ftp
    except Exception as e:
        print("Ocorreu um erro durante a conexão FTP:", e)
        return None

def enviar_arquivo_ftp(ftp, caminho_arquivo, nome_arquivo):
    try:
        # Abrindo o arquivo local para leitura binária
        with open(caminho_arquivo, 'rb') as arquivo:
            # Enviando o arquivo para o servidor FTP
            ftp.storbinary('STOR ' + nome_arquivo, arquivo)
        
        print("Arquivo '{}' enviado com sucesso para o servidor FTP.".format(nome_arquivo))
    except Exception as e:
        print("Ocorreu um erro durante o envio do arquivo FTP:", e)

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso: {} <host> <porta> <usuário> <senha> <diretório remoto> <arquivo local>".format(sys.argv[0]))
        sys.exit(1)

    host = sys.argv[1]
    porta = int(sys.argv[2])
    usuario = sys.argv[3]
    senha = sys.argv[4]
    diretorio_remoto = sys.argv[5]
    caminho_arquivo_local = sys.argv[6]
    nome_arquivo = os.path.basename(caminho_arquivo_local)

    ftp = conectar_ftp(host, porta, usuario, senha)
    if ftp:
        ftp.cwd(diretorio_remoto)  # Navega para o diretório remoto
        enviar_arquivo_ftp(ftp, caminho_arquivo_local, nome_arquivo)
        ftp.quit()
