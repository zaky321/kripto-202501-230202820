import random

# parameter publik
p = 23
g = 5

# private key
a = random.randint(1, p-1)  # Alice
b = random.randint(1, p-1)  # Bob
e = random.randint(1, p-1)  # Eve (satu kunci saja untuk sederhana)

# public key asli
A = pow(g, a, p)
B = pow(g, b, p)

# Eve membuat public key palsu
E = pow(g, e, p)

# --- Eve menyerang ---
# Alice mengirim A → diterima Eve → Eve kirim E ke Bob
# Bob mengirim B → diterima Eve → Eve kirim E ke Alice
public_to_Alice = E
public_to_Bob    = E

# --- Kunci yang dihitung ---
# Alice menghitung kunci (dengan E)
key_Alice = pow(public_to_Alice, a, p)

# Bob menghitung kunci (dengan E)
key_Bob = pow(public_to_Bob, b, p)

# Eve menghitung dua kunci:
key_Eve_with_Alice = pow(A, e, p)
key_Eve_with_Bob   = pow(B, e, p)

print("Kunci Alice:", key_Alice)
print("Kunci Bob  :", key_Bob)
print("Kunci Eve (Alice):", key_Eve_with_Alice)
print("Kunci Eve (Bob):  ", key_Eve_with_Bob)

print("\nAlice == Bob? :", key_Alice == key_Bob)
print("Alice == Eve(A)? :", key_Alice == key_Eve_with_Alice)
print("Bob == Eve(B)?   :", key_Bob == key_Eve_with_Bob)
