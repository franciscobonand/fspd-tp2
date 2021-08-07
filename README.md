# FSPD - Tabalho Prático 2

## Como executar

1. Execute o comando `make config`. Ao fazer isso, os arquivos `.py` serão definidos como executáveis. Esse comando Makefile executa os seguintes comandos:

```make
chmod +x svc_arm.py
chmod +x cln_arm.py
chmod +x svc_comp.py
chmod +x cln_comp.py
```

2. Para executar os servidores e clientes, os comandos `make` são iguais aos descritos na documentação do trabalho:

- `make run_serv_arm arg=<port>`: executa o servidor da primeira parte, no porto especificado em \<port>.
- `make run_cli_arm arg=<addr>`: executa o cliente da primeira parte, que se conecta ao servidor o qual está escutando no endereço especificado em \<addr>.
- `make run_serv_comp arg1=<port> arg2=<addr1> arg3=<addr2>`: executa o servidor da segunda parte no porto especificado em \<port>, e executa os servidores do Siga no endereço \<addr1> e Matrícula no endereço \<addr2>.
- `make run_cli_comp arg=<addr>`: executa o cliente da segunda parte, que se conecta ao servidor o qual está escutando no endereço especificado em \<addr>.

## Ressalvas

No servidor/cliente implementados na primeira parte, não há persistência de dados: uma vez que o servidor é encerrado, todos os registros daquela seção são descartados.

Nos servidores implementados na segunda parte, foram criados mocks de registros para que as consultas do cliente retornem os resultados esperados (não é feita uma consulta a um banco de dados/arquivo local). Com isso em mente, tem-se as seguintes consultas podem ser feitas para avaliar as respostas esperadas:  

- `C,1`: retorna registro de estudante que possui todas as informações (nome, matrícula, curso e créditos).
- `C,2`: retorna registro de estudante que possui todas as informações (nome, matrícula, curso e créditos).
- `C,3`: retorna registro de estudante que possui apenas informações do Siga (nome e matrícula).
- `C,*`: onde "*" são os demais números exceto os anteriormente citados. Nesses casos, não há registros.
