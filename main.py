
import ipaddress

print("======================================")
print("       IP ADDRESS SUBNET CALCULATOR")
print("======================================")

# Meminta input dari pengguna
ip = input("Masukkan IP Address : ")
prefix = input("Masukkan Prefix     : ")

try:
    # Menghitung informasi jaringan
    network = ipaddress.ip_network(
        ip + "/" + prefix,
        strict=False
    )

    if network.version != 4:
        raise ValueError("Program hanya mendukung IPv4")

    # Menampilkan hasil perhitungan
    print("\n========== HASIL PERHITUNGAN ==========")

    print("IP Address        :", ip)
    print("Prefix            :", network.prefixlen)
    print("Subnet Mask       :", network.netmask)
    print("Network Address   :", network.network_address)
    print("Broadcast Address :", network.broadcast_address)

    # Menghitung jumlah host yang dapat digunakan
    if network.prefixlen <= 30:
        total_host = network.num_addresses - 2
        first_host = network.network_address + 1
        last_host = network.broadcast_address - 1

    elif network.prefixlen == 31:
        total_host = 2
        first_host = network.network_address
        last_host = network.broadcast_address

    else:
        total_host = 1
        first_host = network.network_address
        last_host = network.network_address

    print("First Usable IP   :", first_host)
    print("Last Usable IP    :", last_host)
    print("Jumlah Host       :", total_host)

    print("======================================")

except ValueError:
    print("\nInput IP Address atau Prefix tidak valid!")


