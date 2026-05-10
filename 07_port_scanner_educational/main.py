import socket


def scan_ports(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\nScanning {domain} ({ip})...\n")

        ports = [75, 76, 77, 78, 79, 80, 81, 443, 22, 3306]

        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            try:
                s.connect((ip, port))
                print(f"[OPEN] Port {port}")
            except:
                print(f"[CLOSED] Port {port}")
            finally:
                s.close()

    except socket.gaierror:
        print("Unable to resolve domain.")


# MAIN LOOP
while True:
    url = input("\nEnter URL (or 'q'): ").strip()

    if url.lower() == "q":
        print("Exiting...")
        break

    if not url:
        continue

    if not url.startswith("http"):
        url = "https://" + url

    domain = url.replace("https://", "").replace("http://", "").split("/")[0]


    scan_ports(domain)
    print("Scan Complete!")
