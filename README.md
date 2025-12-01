# Mi-Projecto-Seguranca-Python
Este projeto foi desenvolvido em ambiente 100% controlado e educacional, como parte de um laboratório de segurança informática.   O objetivo é compreender o funcionamento de malwares simulados (Ransomware e Keylogger), praticar sua implementação em Python e refletir sobre medidas de defesa e prevenção.
---
Projetos revisados e estudados

Ransomware Simulado
Vimos como um script pode criptografar e descriptografar arquivos e gerar uma mensagem de “resgate”.

###Implementação
- Criação de arquivos de teste.
- Script em Python utilizando a biblioteca `cryptography.fernet`.
- Função para criptografar e descriptografar.
- Mensagem simulada de resgate exibida ao usuário.

### Evidências
- Arquivos de teste
  - Arquivos em texto aberto (não criptografados)

<img width="639" height="146" alt="image" src="https://github.com/user-attachments/assets/0452b07d-cb3a-4264-b797-0cdbfbd660dc" />
<img width="797" height="115" alt="image" src="https://github.com/user-attachments/assets/927902c2-03e4-4c92-9453-a0aa2e4fddf1" />

  - Execução script python (Ransomware_simulado.py)

    <img width="495" height="204" alt="image" src="https://github.com/user-attachments/assets/bf28d711-fcd6-454a-ba13-cb72b11f0d8d" />

  - Arquivos criptografados

<img width="1251" height="500" alt="image" src="https://github.com/user-attachments/assets/173ece04-0564-4c71-a56a-849da2cc4c3e" />

- Execução script python (descriptografar.py)

<img width="722" height="456" alt="image" src="https://github.com/user-attachments/assets/f445ec85-645c-4b36-8e1d-97f7c7a35ee4" />
<img width="804" height="467" alt="image" src="https://github.com/user-attachments/assets/eadf7edd-efe6-499c-b68b-f071bd1ace62" />


--------

Keylogger Simulado
### Objetivo
Capturar teclas digitadas e armazená-las em um arquivo `.txt`, além de implementar envio automático por e-mail.

### Implementação
- Uso da biblioteca `pynput` para captura de teclas.
- Armazenamento em arquivo `log.txt`.
- Envio automático via SMTP (`smtplib`).
- Execução em máquina virtual Kali Linux, apenas para fins educacionais.

### Evidências

- Arquivo com dados capturados.

<img width="874" height="428" alt="image" src="https://github.com/user-attachments/assets/7b0997eb-7f27-43e9-82f3-b7e40adc1143" />

<img width="1246" height="418" alt="image" src="https://github.com/user-attachments/assets/5e3640cc-73fa-457e-9606-f1328367955a" />


---


## Reflexão sobre Defesa

Durante o laboratório, foram estudadas medidas de defesa contra malwares:

- **Antivírus e Firewall**: proteção contra execução e comunicação não autorizada.  
- **Sandboxing**: execução de programas suspeitos em ambientes isolados.  
- **Conscientização do Usuário**: evitar abrir anexos suspeitos e cair em golpes de engenharia social.  
- **Monitoramento de Logs**: identificar comportamentos anômalos no sistema.  

Essas práticas são fundamentais para mitigar riscos e proteger sistemas reais.

---

## Conclusões
- Foi possível compreender, na prática, como funcionam Ransomware e Keylogger.  
- Os exercícios mostraram como malwares exploram vulnerabilidades técnicas e humanas.  
- A experiência reforça a importância de testes em laboratório para entender ameaças e fortalecer defesas.  

---

⚠️ Aviso Importante
Este repositório e todo o material aqui disponibilizado têm exclusivamente fins educacionais e de pesquisa em ambiente controlado.
Os exemplos de código e simulações de malware (Ransomware e Keylogger) foram desenvolvidos para estudo em laboratório de segurança informática, não devendo ser utilizados em ambientes públicos ou privados sem autorização.

Declaração de responsabilidade:
O autor não se responsabiliza por qualquer dano, perda de dados ou uso indevido decorrente da execução dos scripts fora de um ambiente seguro e controlado.
A utilização deste material em sistemas reais, sem consentimento, pode ser considerada atividade ilegal.
