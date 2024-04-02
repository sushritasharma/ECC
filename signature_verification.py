from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

class ECCSignatureSystem:
    def _init_(self):
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self):
        """Generate ECC key pair."""
        self.private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        self.public_key = self.private_key.public_key()
        print("Key pair generated successfully.")

    def sign_message(self, message):
        """Sign a message using the private key."""
        if self.private_key is None:
            print("Error: No private key available.")
            return None

        signature = self.private_key.sign(
            message,
            ec.ECDSA(hashes.SHA256())
        )
        print("Message signed successfully.")
        return signature

    def verify_signature(self, message, signature):
        """Verify the signature using the public key."""
        if self.public_key is None:
            print("Error: No public key available.")
            return False

        try:
            self.public_key.verify(
                signature,
                message,
                ec.ECDSA(hashes.SHA256())
            )
            print("Signature is valid.")
            return True
        except InvalidSignature:
            print("Invalid signature.")
            return False

if __name__ == "__main__":
    signature_system = ECCSignatureSystem()

    while True:
        print("\n1. Generate Key Pair")
        print("2. Sign Message")
        print("3. Verify Signature")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            signature_system.generate_key_pair()

        elif choice == "2":
            if signature_system.private_key is None:
                print("Error: No private key available. Please generate a key pair first.")
                continue

            message = input("Enter the message to sign: ").encode()
            signature = signature_system.sign_message(message)
            if signature:
                print("Signature:", signature.hex())

        elif choice == "3":
            if signature_system.public_key is None:
                print("Error: No public key available. Please generate a key pair first.")
                continue

            message = input("Enter the message: ").encode()
            signature = bytes.fromhex(input("Enter the signature (in hexadecimal format): ").strip())
            signature_system.verify_signature(message, signature)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")