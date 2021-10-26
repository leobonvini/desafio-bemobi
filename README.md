# Descrição

A aplicação realiza a leitura de logs referentes aos registros de mudança de status dos usuários de um serviço.

## Instalação

A aplicação foi desenvolvida em Python, que pode ser obtido no [link](https://www.python.org/).

## Execução

O arquivo deve ser renomeado para "log.txt" e usuário deve executar o comando:

```
python log_count.py
```
Outra alternativa é adicionar no parâmetro da função GetLogData() o nome do seu arquivo. 

É possível testar a aplicação através de um arquivo populado pseudoaleatoriamente, para isso, execute:

```
python populate.py
```
Será gerado um arquivo de 10 mil registros, para alterar esse número, basta adicionar o quantidade esperada de linhas no parâmetro da função 
PopulateLogFile().

## Autor
Leonardo Bonvini Rosa Junior