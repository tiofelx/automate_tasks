# Automatizar Tarefas

Este é um script Python que oferece três funcionalidades principais: renomear arquivos em um diretório com um prefixo específico, enviar e-mails usando o servidor SMTP do Gmail, e fazer backup de arquivos de um diretório para outro.

## Funcionalidades

1. **Renomear Arquivos**:
   - A função `rename_files` renomeia todos os arquivos em um diretório adicionando um prefixo ao nome original.

2. **Enviar E-mails**:
   - A função `send_email` envia um e-mail usando o servidor SMTP do Gmail. Certifique-se de fornecer as credenciais de e-mail do remetente de forma segura.

3. **Fazer Backup de Arquivos**:
   - A função `backup_files` copia todos os arquivos de um diretório de origem para um diretório de destino, criando o diretório de destino se ele não existir.

## Requisitos

- Python 3.x
- Bibliotecas Python necessárias:
  - `smtplib` (para enviar e-mails)
  - `email.mime` (para criar mensagens MIME)
  - `shutil` (para operações de cópia de arquivos)
  - `os` (para operações de sistema)

## Como Usar

1. **Configuração de E-mail**:
   - Antes de usar a função de enviar e-mails, configure as variáveis de ambiente para o e-mail do remetente e senha:
     ```
     export SENDER_EMAIL=seu_email@gmail.com
     export SENDER_PASSWORD=sua_senha
     ```

2. **Execução do Script**:
   - Clone este repositório e navegue até o diretório onde o script está localizado.
   - Execute o script Python:
     ```
     python main.py
     ```

3. **Exemplo de Uso**:
   ```python
   # Exemplo de uso das funções
   if __name__ == "__main__":
       # Renomear arquivos
       rename_files('/caminho/do/diretorio', 'prefixo_')

       # Enviar e-mail
       sender_email = os.getenv('SENDER_EMAIL')
       sender_password = os.getenv('SENDER_PASSWORD')
       receiver_email = 'email_destinatario@gmail.com'
       subject = 'Assunto do Email'
       body = 'Corpo do email'
       send_email(sender_email, sender_password, receiver_email, subject, body)

       # Fazer backup de arquivos
       backup_files('/caminho/do/diretorio_origem', '/caminho/do/diretorio_backup')
