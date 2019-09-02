# Snnifer captura de trama de red

## Modo de uso:

- Como administrador desde consola
- Activar venv y ejecutar script o instalar libreria scapy  
- usage: snnifer.py [-h] -r NET [-p [PROTOCOLS [PROTOCOLS ...]]] [-s SOURCE]
                  [-d DESTINATION] [-n NUMBER]

### optional arguments:
- -h, --help            show this help message and exit
- -r NET, --net NET     net name to analize
- -p [PROTOCOLS [PROTOCOLS ...]], --protocols [PROTOCOLS [PROTOCOLS ...]]
                        filter by protocols
- -s SOURCE, --source SOURCE
                        ip source
- -d DESTINATION, --destination DESTINATION
                        ip destination
  -n NUMBER, --number NUMBER
                        number frames

- Ejemplo:

`sudo python3.7 snnifer.py -r wlp3s0 -d 192.168.0.17 -n 2 -p tcpsudo python3.7 snnifer.py -r wlp3s0 -d 192.168.0.17 -n 2 -p tcp`

<p>analisis de trama con destino 192.168.0.17, numero de tramas 2, filtrado por protocolo tcp, tarjeta de red wlp3s0</p>
