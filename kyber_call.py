import oqs

# Create a Key Encapsulation Mechanism (KEM) object
# "Kyber512", "Kyber768", or "Kyber1024" (or the new "ML-KEM-*" names)
kem = oqs.KeyEncapsulation("Kyber768")

# Generate public and secret keys
public_key = kem.generate_keypair()
secret_key = kem.export_secret_key()

print(f"Mechanism: {kem.details['name']}")
print(f"Public Key (bytes): {public_key[:20]}...")
