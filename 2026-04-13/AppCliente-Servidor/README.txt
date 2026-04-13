Autores: João Sbardelotto e Lucas Maciel

Configurar as portas e IP acessando diretamente os arquivos .py

Em um Computador rodar 

python3 Servidor.py

Com isso o Servidor estará esperando conexões tanto TCP quanto UDP no IP e portas expecificado

Em um segundo Computador rodar 

python3 Client.py

logo após o programa ira pedir para escolher uma conexão TCP(1) ou UDP(2) 
após escolher o programa enviara o conteúdo do arquivo animacao.txt, para substituir a animação faça cada linha cercada por " e cada frame separado por ;