# FSPD - Tabalho Prático 2

## Como executar

Primeiramente deve-se executar o seguinte comando para criação das stubs e para tornar os arquivos de clientes e servidores executáveis:

```make
make config
```

Para executar os servidores e clientes, os comandos `make` são iguais aos descritos na documentação do trabalho:

- `make run_serv_arm arg=<port>`: executa o servidor da primeira parte, no porto especificado em \<port>.
- `make run_cli_arm arg=<addr>`: executa o cliente da primeira parte, que se conecta ao servidor o qual está escutando no endereço especificado em \<addr>.
- `make run_serv_comp arg1=<port> arg2=<addr1> arg3=<addr2>`: executa o servidor da segunda parte no porto especificado em \<port>, e executa os servidores do Siga no endereço \<addr1> e Matrícula no endereço \<addr2>.
- `make run_cli_comp arg=<addr>`: executa o cliente da segunda parte, que se conecta ao servidor o qual está escutando no endereço especificado em \<addr>.

Para deletar as stubs e pasta `__pycache__` gerados durante a execução (e pelo comando `make config`) basta executar o comando `make clean`.

## Pontos de atenção

No servidor/cliente implementados na primeira parte, não há persistência de dados: uma vez que o servidor é encerrado, todos os registros daquela seção são descartados.

Caso seja executado o comando `T` pelo cliente da segunda parte, todos os três servidores e o cliente são encerrados, porém os clientes da parte um (que podem estar executando) não são encerrados. Dessa forma, caso algum desses clientes que ainda estão executando tentem enviar uma requisição ao servidor, a mensagem de erro **"error while sending request, closing client..."** é exibida, e o cliente que enviou o comando é encerrado.
