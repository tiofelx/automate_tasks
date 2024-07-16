import os
import shutil
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para renomear arquivos
def rename_files(directory, prefix):
    try:
        if not os.path.exists(directory):
            logging.error(f"O diretório {directory} não existe.")
            return
        for filename in os.listdir(directory):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, prefix + filename)
            os.rename(old_path, new_path)
        logging.info(f"Arquivos em {directory} renomeados com o prefixo {prefix}")
    except Exception as e:
        logging.error(f"Erro ao renomear arquivos: {e}")

# Função para enviar e-mails
def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        logging.info("Email enviado com sucesso!")
    except Exception as e:
        logging.error(f"Falha ao enviar email: {e}")

# Função para fazer backup de arquivos
def backup_files(src_directory, dst_directory):
    try:
        if not os.path.exists(src_directory):
            logging.error(f"O diretório de origem {src_directory} não existe.")
            return
        if not os.path.exists(dst_directory):
            os.makedirs(dst_directory)
        for filename in os.listdir(src_directory):
            src_path = os.path.join(src_directory, filename)
            dst_path = os.path.join(dst_directory, filename)
            shutil.copy(src_path, dst_path)
        logging.info(f"Backup dos arquivos de {src_directory} para {dst_directory} concluído.")
    except Exception as e:
        logging.error(f"Erro ao fazer backup dos arquivos: {e}")
