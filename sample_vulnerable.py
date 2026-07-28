import os
from pycryptodome.cipher import AES
from pqc import ml_kem

def initialize_auth_session():
    # Generate a random seed for the ML-KEM
    seed = os.urandom(32)

    # Initialize the ML-KEM
    kem = ml_kem.ML_KEM()

    # Generate a public-private key pair using ML-KEM
    pubkey, privkey = kem.generate_keypair(seed)

    # Generate a shared secret key
    shared_secret = kem.generate_shared_secret(pubkey, privkey)

    # Derive a symmetric key from the shared secret
    symmetric_key = kem.derive_symmetric_key(shared_secret)

    # Use the symmetric key for encryption
    print("Session encrypted with quantum-safe ML-KEM.")

    return symmetric_key

def main():
    symmetric_key = initialize_auth_session()
    # Use the symmetric key for encryption and decryption
    # For example, using AES
    cipher = AES.new(symmetric_key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(b"Hello, World!")
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Nonce: {nonce.hex()}")
    print(f"Tag: {tag.hex()}")

if __name__ == "__main__":
    main()