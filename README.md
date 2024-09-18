# DLLExample

Esta atividade demonstra como foi criada uma DLL em C++ e utilizada em um script Python usando a biblioteca `ctypes`.

## Estrutura do Projeto

- `dll-atividade.cpp`: Contém a implementação das funções exportadas pela DLL.
- `dll-atividade.h`: Contém as declarações.
- `main.py`: Script Python que utiliza a DLL, definindo os tipos de argumentos e chamando as funções.

## Requisitos Usados

- Visual Studio 2022
- Visual Studio Code 
- Python 3.12.6

## Compilação da DLL

1. No Visual Studio 2022 foi criado o escopo de um projeto de DLL em C++.
2. Foram adicionados os arquivos `dll-atividade.cpp` e `dll-atividade.h` ao projeto.
4. Compile o projeto para gerar o arquivo `dll-atividade.dll`, no visual studio pode-se utilizar o atalho Crt+B para a compilação.

## Uso da DLL no Python

1. O arquivo `dll-atividade.dll` está em um diretório acessível, `"PATH/dll-atividade/x64/Debug/dll-atividade.dll"`
2. No script Python (`main.py`), a DLL é carregada usando `ctypes.CDLL` e são defidos os tipos de argumentos e o tipo de retorno das funções.

