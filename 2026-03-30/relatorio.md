# Monitoramento HTTP e HTTPS — Respostas

## HTTP

### Encapsulamento

`[Protocols in frame: eth:ethertype:ip:tcp:http]`

O protocolo HTTP é encapsulado por TCP (camada de transporte), que é encapsulado por IPv4 (camada de rede), que é encapsulado por Ethernet II (camada de enlace) — correspondendo às camadas Aplicação → Transporte → Rede → Enlace da pilha TCP/IP.

### Texto aberto ou criptografado?

Todas as informações estão em **texto aberto** (plaintext). Cabeçalhos HTTP, TCP e IP são plenamente legíveis no Wireshark sem qualquer descriptografia.

### a) Versão do protocolo HTTP

**HTTP/1.1** — visível na linha de requisição `GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1` e na linha de resposta `HTTP/1.1 200 OK`.

### b) Linguagem aceita pelo browser

O request foi feito com **`curl/8.18.0`**, que não envia o header `Accept-Language`. O único header de preferência presente é `Accept: */*`, indicando que aceita qualquer tipo de conteúdo. Um browser enviaria, por exemplo, `Accept-Language: pt-BR,pt;q=0.9,en;q=0.8`.

### c) Endereços IP

- IP do **computador (cliente):** `10.132.241.183`
- IP do **servidor:** `128.119.245.12`

### d) Última modificação do arquivo

`Last-Modified: Tue, 28 Oct 2025 05:59:01 GMT`

### e) Identificação de navegador e servidor

- **Navegador:** identificado pelo header `User-Agent: curl/8.18.0` presente na requisição
- **Servidor:** identificado pelo header `Server: Apache/2.4.62 (AlmaLinux) OpenSSL/3.5.1 mod_fcgid/2.3.9 mod_perl/2.0.12 Perl/v5.32.1` presente na resposta

### f) Cache no reload

Como o request foi feito via `curl`, não há mecanismo de cache. A requisição não inclui `If-None-Match` nem `If-Modified-Since`, e o servidor sempre retorna `200 OK` com o conteúdo completo.

---

## HTTPS

*(a preencher)*
