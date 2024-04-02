import hashlib

# Simplified Elliptic Curve Class
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p  

   
    def add_points(self, P, Q):
    
        if P is None:
            return Q
        if Q is None:
            return P

       
        if P == Q:
            if P[1] == 0: 
                return None 
            
            slope = (3 * P[0]**2 + self.a) * pow(2 * P[1], -1, self.p)
        else:
           
            if P[0] == Q[0]:
                return None  
            
            slope = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, self.p)

        # Calculate the x and y coordinates of the sum point
        x_r = (slope**2 - P[0] - Q[0]) % self.p
        y_r = (slope * (P[0] - x_r) - P[1]) % self.p

        return (x_r, y_r)


def ecdh_shared_secret(private_key, public_point, curve):
    # Simplified; not actual elliptic curve math
    return curve.add_points(public_point, (private_key, private_key))

# "Encrypt" and "decrypt" functions (for demonstration)
def encrypt_message(message, secret):
    encrypted = ''.join(chr(ord(char) + secret % 256) for char in message)
    return encrypted

def decrypt_message(encrypted_message, secret):
    decrypted = ''.join(chr(ord(char) - secret % 256) for char in encrypted_message)
    return decrypted

# Main program
if __name__ == "__main__":
    # Example curve: y^2 = x^3 + ax + b over finite field F_p
    curve = EllipticCurve(a=2, b=3, p=97)  # Simplified curve parameters

    # Simulate user input for keys and message
    private_key = int(input("Enter your private key (integer): "))
    public_point = (4, 5)  # Example public point on the curve
    user_name = input("Enter your name to encrypt: ")

    # Generate shared secret
    shared_secret = ecdh_shared_secret(private_key, public_point, curve)
    secret_key = int(hashlib.sha256(str(shared_secret).encode()).hexdigest(), 16) % curve.p

    # Encrypt and decrypt the message
    encrypted_message = encrypt_message(user_name, secret_key)
    decrypted_message = decrypt_message(encrypted_message, secret_key)

    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")