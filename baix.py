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

def baixar_arquivos_ftp(ftp, diretorio_remoto, diretorio_local):
    try:
        # Navegando para o diretório remoto
        ftp.cwd(diretorio_remoto)
        
        # Listando arquivos no diretório remoto
        arquivos_remotos = ftp.nlst()

        # Baixando arquivos um por um
        for arquivo in arquivos_remotos:
            caminho_local = os.path.join(diretorio_local, arquivo)
            with open(caminho_local, 'wb') as arquivo_local:
                ftp.retrbinary('RETR ' + arquivo, arquivo_local.write)
            print("Arquivo '{}' baixado com sucesso.".format(arquivo))
        
        print("Todos os arquivos foram baixados com sucesso.")
    except Exception as e:
        print("Ocorreu um erro durante o download dos arquivos FTP:", e)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Uso: {} <host> <porta> <usuário> <senha> <diretório remoto>".format(sys.argv[0]))
        sys.exit(1)

    host = sys.argv[1]
    porta = int(sys.argv[2])
    usuario = sys.argv[3]
    senha = sys.argv[4]
    diretorio_remoto = sys.argv[5]
    diretorio_local = "./downloads"  # Diretório local onde os arquivos serão salvos

    if not os.path.exists(diretorio_local):
        os.makedirs(diretorio_local)

    ftp = conectar_ftp(host, porta, usuario, senha)
    if ftp:
        baixar_arquivos_ftp(ftp, diretorio_remoto, diretorio_local)
        ftp.quit()
