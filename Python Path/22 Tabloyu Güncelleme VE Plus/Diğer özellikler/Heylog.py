import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Günün tarihini al
today = datetime.today().strftime('%Y-%m-%d')

# Kayıt dosyasının adı
filename = f'{today}_record.txt'

# Dosya yoksa oluştur
if not os.path.exists(filename):
    open(filename, 'w').close()

# Yazılanları dosyaya ekle
while True:
    user_input = input('Bir şeyler yazın: ')
    with open(filename, 'a') as f:
        f.write(user_input + '\n')
    if user_input.lower() == 'exit':
        break

# Günlük rapor oluştur
with open(filename, 'r') as f:
    contents = f.read()
    # Eğer dosya boşsa, rapor oluşturma
    if not contents:
        print('Kaydedilen hiçbir şey yok.')
    else:
        # Raporu oluştur
        report = f'{today} günlük raporu:\n\n{contents}'
        print(report)

        # Mail gönderme
        sender_email = 'your_email@example.com'
        receiver_email = 'recipient_email@example.com'
        password = 'your_password'

        msg = MIMEText(report)
        msg['Subject'] = f'{today} günlük raporu'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f'Rapor {receiver_email} adresine gönderildi.')
        except:
            print('Rapor gönderilemedi.')
        finally:
            server.quit()