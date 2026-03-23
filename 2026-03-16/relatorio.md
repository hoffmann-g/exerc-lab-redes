# Identificação de pacotes DHCP

Data: 23 de março de 2026
Grupo: João Sbardelotto e Guilherme Hoffmann

#### Detalhes dos pacotes DHCP

- Discover - DHCPDISCOVER
    - Transaction ID: 0x00003d1d
    - MAC Address: 00:0b:82:01:fc:42

- Offer - DHCPOFFER
    - Transaction ID: 0x00003d1d
    - MAC Address: 00:0b:82:01:fc:42
    - Offered IP: 192.168.0.10
    - Subnet Mask: 255.255.255.0
    - Renewal Time: 30 minutes (1800 seconds)
    - Rebinding Time: 52 minutes, 30 seconds (3150 seconds)
    - IP Address Lease Time: 1 hour (3600 seconds)
    - DHCP Server Identifier: 192.168.0.1

- Request - DHCPREQUEST
    - Transaction ID: 0x00003d1d
    - MAC Address: 00:0b:82:01:fc:42
    - Requested IP: 192.168.0.10
    - Client Identifier
        - MAC Address: 00:0b:82:01:fc:42
        - Hardware Type: Ethernet (1)

- Acknowledge - DHCPACK
    - Transaction ID: 0x00003d1d
    - MAC Address: 00:0b:82:01:fc:42
    - Assigned IP: 192.168.0.10

---

#### Flag dos pacotes DHCP
- Discover - DHCPDISCOVER- 0x0000 (Unicast)
- Offer - DHCPOFFER- 0x0000 (Unicast)
- Request - DHCPREQUEST- 0x0000 (Unicast)
- Acknowledge - DHCPACK- 0x0000 (Unicast)

---

#### Protocolo de transporte utilizado:
    - UDP (User Datagram Protocol)
    Explicação: É um protocolo leve e eficiente para a troca de mensagens em redes locais.

---

#### Ordem das mensagens:
1. O cliente envia um pacote DHCPDISCOVER para localizar servidores DHCP disponíveis.
2. O servidor responde com um pacote DHCPOFFER, oferecendo um endereço IP e outras configurações de rede.
3. O cliente responde com um pacote DHCPREQUEST, solicitando o endereço IP oferecido pelo servidor.
4. O servidor confirma a atribuição do endereço IP com um pacote DHCPACK, finalizando o processo de configuração de rede para o cliente.

Porém, em caso de IP já estar em uso, o servidor pode responder com um pacote DHCPNAK, indicando que a solicitação do cliente foi negada e que ele deve iniciar o processo de descoberta novamente, ou até mesmo, consistir apenas de DHCPREQUEST e DHCPACK, caso o cliente já tenha um endereço IP válido e esteja renovando sua concessão.

---

#### Endereços de enlace, rede e transporte:
    - Endereço de enlace (MAC): 00:0b:82:01:fc:42
    - Endereço de rede (IP): 192.168.0.10
    - Endereço de transporte (UDP): Porta 67 (servidor DHCP) e Porta 68 (cliente DHCP)
    Explicação: O endereço de enlace é utilizado para a comunicação dentro da rede local, enquanto o endereço de rede é utilizado para a comunicação entre redes. O endereço de transporte é utilizado para identificar as portas de comunicação entre o cliente e o servidor DHCP.

#### Informações que devem constar em cada mensagem:
- DHCPDISCOVER:
    - Transaction ID: Identificador único para correlacionar mensagens.
    - MAC Address: Identificação do cliente.
- DHCPOFFER:
    - Transaction ID: Correlaciona com o DHCPDISCOVER.
    - MAC Address: Identificação do cliente.
    - Offered IP: Endereço IP oferecido ao cliente.
    - Subnet Mask: Máscara de sub-rede para a configuração de rede.
    - Renewal Time: Tempo para o cliente renovar a concessão.
    - Rebinding Time: Tempo para o cliente tentar renovar a concessão com qualquer servidor.
    - IP Address Lease Time: Tempo total da concessão do endereço IP.
    - DHCP Server Identifier: Identificação do servidor DHCP.
- DHCPREQUEST:
    - Transaction ID: Correlaciona com o DHCPDISCOVER e DHCPOFFER.
    - MAC Address: Identificação do cliente.
    - Requested IP: Endereço IP solicitado pelo cliente.
    - Client Identifier: Identificação do cliente, geralmente o endereço MAC.
- DHCPACK:
    - Transaction ID: Correlaciona com as mensagens anteriores.
    - MAC Address: Identificação do cliente.
    - Assigned IP: Endereço IP atribuído ao cliente.