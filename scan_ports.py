import socket


CIBLE = "192.168.56.101"  


PORTS_A_TESTER = [21, 22, 80, 139, 443, 8080]

print(f"--- Début du scan réseau sur la machine cible : {CIBLE} ---")

for port in PORTS_A_TESTER:
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) 
    
   
    resultat = s.connect_ex((CIBLE, port))
    
  
    if resultat == 0:
        print(f"[+] Port {port} : OUVERT -> Vulnérabilité détectée")
    else:
        print(f"[-] Port {port} : Fermé")
        
    s.close()

print("--- Scan réseau terminé ---")