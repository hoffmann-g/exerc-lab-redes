# Lab — Subredes IPv4 + Roteamento Estático (GNS3)

## Topologia
```
PC1 — Switch1 — R1 — R2 — R3 — Switch2 — PC2
                 \         /
                  R4 ----- 
```

## Endereço público único: 203.0.113.0/24 (subdividido com VLSM)

| Subrede | Rede/Máscara        | Hosts úteis | Uso                 |
|---------|---------------------|-------------|---------------------|
| LAN1    | 203.0.113.0/29      | .1–.6       | PC1, Switch1, R1    |
| LAN2    | 203.0.113.8/29      | .9–.14      | PC2, Switch2, R3    |
| R1↔R2   | 203.0.113.16/30     | .17–.18     | enlace              |
| R2↔R3   | 203.0.113.20/30     | .21–.22     | enlace              |
| R1↔R4   | 203.0.113.24/30     | .25–.26     | enlace              |
| R3↔R4   | 203.0.113.28/30     | .29–.30     | enlace              |

## Endereços por interface
- **R1**: f0/0 .1 (LAN1) | f0/1 .17 (R2) | f1/0 .25 (R4)
- **R2**: f0/0 .18 (R1) | f0/1 .21 (R3)
- **R3**: f0/0 .22 (R2) | f0/1 .29 (R4) | f1/0 .9 (LAN2)
- **R4**: f0/0 .26 (R1) | f0/1 .30 (R3)
- **PC1**: .2  gw .1   |  **PC2**: .10  gw .9

## Ordem de configuração
1. Cole `R1.txt`, `R2.txt`, `R3.txt`, `R4.txt` no console de cada roteador.
2. Configure os PCs com `PCs-VPCS.txt`.
3. Os nomes de interface (f0/0, f1/0...) dependem do modelo de roteador no GNS3 —
   ajuste se o seu usar Gi0/0, e0/0, etc. Confira com `show ip interface brief`.

## Validação (ping) — gere tráfego e registre as saídas
- PC1: `ping 203.0.113.10`  (PC1 -> PC2, atravessa toda a rede)
- PC2: `ping 203.0.113.2`
- Em cada roteador, pingue todas as outras subredes, ex. de R1:
  `ping 203.0.113.10`, `ping 203.0.113.30`, `ping 203.0.113.22`
- Verifique a tabela: `show ip route` (deve listar conectadas C + estáticas S)
- `show ip interface brief` (todas "up/up")

## Relatório (o que incluir)
- Print da topologia no GNS3.
- Tabela de endereçamento (acima) e justificativa das máscaras (/30 nos enlaces ponto-a-ponto = só 2 hosts; /29 nas LANs).
- `show running-config` e `show ip route` de cada roteador.
- Resultados dos pings (PC↔PC e roteador↔subredes) com prints.
- Conclusão: confirmar conectividade total entre as 6 subredes.
