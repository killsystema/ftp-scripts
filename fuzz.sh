#!/bin/bash

# Endereço IP e porta
IP="ALVO"
PORTA="PORTA"

# Função para executar os comandos e imprimir as respostas
executar_comandos() {
    # Estabelecer a conexão com o servidor usando netcat
    nc -v $IP $PORTA

    # Loop para ler cada linha do arquivo e enviar os comandos
    while IFS= read -r comando; do
        if [ -n "$comando" ]; then
            echo "Enviando comando: $comando"
            # Enviar comando para o servidor usando netcat e imprimir a resposta
            resposta=$(echo "$comando" | nc $IP $PORTA)
            echo "Resposta: $resposta"
        else
            echo "Enviando comando vazio"
            resposta=$(echo "" | nc $IP $PORTA)
            echo "Resposta: $resposta"
        fi
    done < "$1"
}

# Verificar se um arquivo foi passado como argumento
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <arquivo_comandos>"
    exit 1
fi

# Verificar se o arquivo de comandos existe
if [ ! -f "$1" ]; then
    echo "Arquivo '$1' não encontrado."
    exit 1
fi

# Chamada da função para executar os comandos
executar_comandos "$1"
