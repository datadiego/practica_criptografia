import hashlib
import random
import string

def generate_random_string(length=64):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def find_sha1_collision():
    seen_hashes = {}
    n = 0
    while True:
        # Generate a random string
        random_string = generate_random_string()
        
        # Calculate its SHA1 hash
        sha1_hash = hashlib.sha1(random_string.encode('utf-8')).hexdigest()
        print("Intento", n)
        # Check if this hash has been seen before
        if sha1_hash in seen_hashes:
            # Found a collision
            print(f"Collision found!\nString 1: {seen_hashes[sha1_hash]}\nString 2: {random_string}\nSHA1: {sha1_hash}")
            break
        else:
            # Store the hash and the corresponding string
            n += 1
            seen_hashes[sha1_hash] = random_string

if __name__ == "__main__":
    find_sha1_collision()
