import random
import sys

try:
  ports={(20,21):"FTP",22:"SSH",23:"TELNET",53:"DNS",110:"POP3",123:"NTP",
  143:"IMAP",80:"HTTP",443:"HTTP",389:"LDAP",179:"BGP",69:"TFTP",(67,68):"DHCP",
  (137,138,139):"netBIOS",(161,162):"SNMP",636:"LDAPS",(989,990):"SSL/TLS/FTPw"}

  ports_list=list(ports.items())
  port=random.choice(ports_list)
  print("Bu hangi port? ",port)
 
  def quiz():
   while True:
    answer=input()
    if not(answer == port):
       print("Yanlış cevap Tekrar dene")
       continue
    
    else:
      print("Doğru cevap")
      break
   
  quiz()


except ValueError:
    print("Lütfen tam sayı girdiğinizden emin olunuz")
    quiz()

finally:
    again=input("Tekrardan soralım mı? Y/N \n")

    if again == "Y":
        quiz()
    else:
        print("Programdan çıkıldı.")
        sys.exit()