import ssl
import socket
from datetime import datetime


# SSL Checker
def check_ssl(domain):

    try:
        context = ssl.create_default_context()

        # get IP
        ip = socket.gethostbyname(domain)

        print(f"\nScanning {domain} ({ip})...")
        print("\nChecking SSL certificate...")

        # secure connection
        with socket.create_connection((domain, 443)) as sock:

            with context.wrap_socket(sock, server_hostname=domain) as ssock:

                cert = ssock.getpeercert()

        # expiry date
        expiry_date = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        days_left = (expiry_date - datetime.now()).days

        # output
        print(f"\nDomain: {domain}")

        for field in cert["issuer"]:

            key, value = field[0]
            print(f"{key}: {value}")

        print(f"Valid From : {cert['notBefore']}")
        print(f"Expiry Date: {cert['notAfter']}")
        print(f"Days Left  : {days_left}")

        # status
        if days_left > 0:

            if days_left <= 30:
                print("Certificate Status: EXPIRING SOON")
            else:
                print("Certificate Status: VALID")

        else:
            print("Certificate Status: EXPIRED")

    except socket.gaierror:
        print("Unable to resolve domain.")

    except ssl.SSLError:
        print("SSL certificate error.")

    except Exception as e:
        print(f"Error: {e}")


# Main Loop
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

    check_ssl(domain)