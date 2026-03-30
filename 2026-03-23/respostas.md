# Monitoramento DNS — Respostas

## 3.1 Captura DNS com Wireshark

### Consulta DNS inicial (moodle.pucrs.br)

- **IP de origem:** 192.168.0.23
- **IP de destino:** 192.168.0.1
- **Protocolo de aplicação:** DNS
- **Porta de origem:** 50235
- **Porta de destino:** 53
- **Tipo de mensagem DNS:** Standard query (consulta padrão)
- **Tipo de registro DNS:** A (Host Address — endereço IPv4)
- **Endereço a ser resolvido:** moodle.pucrs.br

### Resposta DNS correspondente

- **Número do pacote:** 322
- **IP de origem:** 192.168.0.1
- **IP de destino:** 192.168.0.23
- **Protocolo de aplicação:** DNS
- **Porta de origem:** 53
- **Porta de destino:** 50235
- **Tipo de mensagem DNS:** Standard query response (resposta padrão)
- **Tipo de registro DNS:** A (Host Address — endereço IPv4)
- **Endereços resolvidos:** moodle.pucrs.br → 104.18.7.39 e 104.18.6.39

### Requisição HTTP GET

- `GET /online/ HTTP/1.1` — solicita o recurso `/online/` via HTTP 1.1
- `Host: grandshinyoldpathway.neverssl.com` — identifica o servidor de destino
- `Connection: keep-alive` — mantém a conexão TCP aberta para reuso
- `Upgrade-Insecure-Requests: 1` — cliente prefere HTTPS se disponível
- `User-Agent: Mozilla/5.0 (X11; Linux x86_64)...` — identifica o navegador e sistema operacional
- `Accept: text/html,...` — tipos de conteúdo aceitos pelo cliente
- `Accept-Encoding: gzip, deflate` — algoritmos de compressão suportados
- `Accept-Language: en-US,en;q=0.9` — idiomas preferidos para o conteúdo

### Resposta HTTP

- `HTTP/1.1 200 OK` — requisição bem-sucedida
- `Date: Mon, 30 Mar 2026 18:58:27 GMT` — data/hora em que a resposta foi gerada
- `Server: Apache/2.4.66` — software do servidor web
- `Upgrade: h2,h2c` — servidor oferece suporte a HTTP/2
- `Connection: Upgrade, Keep-Alive` — mantém a conexão viva e sinaliza suporte ao upgrade
- `Last-Modified: Wed, 29 Jun 2022 00:23:22 GMT` — data da última modificação do recurso
- `ETag: "8be-..."` — identificador único da versão do recurso, usado para cache
- `Accept-Ranges: bytes` — servidor aceita requisições parciais do conteúdo
- `Vary: Accept-Encoding` — a resposta pode variar conforme o encoding do cliente
- `Content-Encoding: gzip` — corpo da resposta comprimido com gzip
- `Content-Length: 1173` — tamanho em bytes do corpo comprimido
- `Keep-Alive: timeout=5, max=100` — conexão ativa por até 5 segundos ou 100 requisições
- `Content-Type: text/html; charset=UTF-8` — conteúdo retornado é HTML em UTF-8

---

## 3.2 Captura DNS com nslookup

### Endereço IP de www.iitb.ac.in

O endereço IP de www.iitb.ac.in é **103.21.124.133**.

### Servidor DNS que forneceu a resposta

O servidor DNS que respondeu foi **192.168.0.1** (gateway/roteador local), na porta 53.

### A resposta foi autoritativa?

Não. A resposta foi **não autoritativa** (`Non-authoritative answer`), o que significa que o servidor DNS local não é a autoridade original para o domínio iitb.ac.in — ele obteve a resposta de outro servidor e a retornou a partir do seu cache. Um servidor autoritativo é aquele diretamente responsável pela zona DNS do domínio consultado.

### Servidor de nomes autoritativo para iitb.ac.in

Os servidores autoritativos para o domínio iitb.ac.in são:

- dns1.iitb.ac.in
- dns2.iitb.ac.in
- dns3.iitb.ac.in

O primeiro retornado foi **dns1.iitb.ac.in**. Para obter seu endereço IP, basta realizar uma nova consulta DNS pelo nome `dns1.iitb.ac.in`, cujo resultado é **103.21.125.129**.
