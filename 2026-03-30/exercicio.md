Pontifícia Universidade Católica do Rio Grande do Sul
Escola Politécnica
Laboratório de Redes de Computadores
Monitoração do Protocolo HTTP e HTTPS
Objetivo
Monitorar pacotes dos protocolos de aplicação HTTP e HTTPS, identificar a
constituição do cabeçalho (header), o encapsulamento pelos demais protocolos da
pilha e o fluxo de comunicação entre origem e destino.
Descrição
Utilize o Wireshark para capturar pacotes do protocolo HTTP e HTTPS:
Para cada protocolo, identifique:
• O encapsulamento do protocolo pelos demais níveis da pilha TCP/IP

1. Observe e descreva como o protocolo é encapsulado por todos os
   demais níveis da pilha;
2. Observe e responda se todas as informações do cabeçalho, do
   protocolo de aplicação e dos demais níveis, podem ser acessadas em
   texto aberto ou estão criptografadas.
3. Caso o cabeçalho esteja em texto, responda as questões a seguir:
   a) Qual é a versão do protocolo HTTP que está sendo usada?
   b) Qual é a linguagem que seu browser indica que pode aceitar?
   c) Qual é o endereço IP de seu computador e do servidor?
   d) Quando foi a última vez que o arquivo HTML que você está
   usando foi modificado no servidor?
   e) Que informações mantidas nesses protocolos possibilitam
   identificar o navegador e o servidor web?
   f) Dê um reload na página e informe se ela estava em cache no
   seu browser.
   Dicas
   HTTP
   • Exemplo: http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html
