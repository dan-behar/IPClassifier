import ipaddress

def validar_ip(ip):
    try:
        direccion_ip = ipaddress.ip_address(ip)
    except ValueError:
        return False
    return True

def es_privada(ip):
    direccion_ip = ipaddress.ip_address(ip)
    if direccion_ip.is_private:
        return True
    else:
        return False

def tipo_ip(ip):
    direccion_ip = ipaddress.ip_address(ip)
    if direccion_ip.is_multicast:
        return "D"
    else:
        octetos = ip.split(".")
        primer_octeto = int(octetos[0])
        if primer_octeto >= 1 and primer_octeto <= 126:
            return "A"
        elif primer_octeto >= 128 and primer_octeto <= 191:
            return "B"
        elif primer_octeto >= 192 and primer_octeto <= 223:
            return "C"
        else:
            return "Desconocido"

ip = input("Ingresa una dirección IP: ")
if validar_ip(ip):
    if es_privada(ip):
        print(f"La dirección IP {ip} es privada y de tipo {tipo_ip(ip)}")
    else:
        print(f"La dirección IP {ip} es pública y de tipo {tipo_ip(ip)}")
else:
    print("La dirección IP ingresada no es válida.")
