import sqlite3
import hashlib
from datetime import datetime

# المحرك الرياضي (Zeta Logic)
SOVEREIGN_SET = {1, 7, 11, 13, 17, 19, 23, 29}

def start_node():
    # 1. إنشاء ملف قاعدة البيانات (المخزن)
    conn = sqlite3.connect('mirror_signals.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS signals 
                      (timestamp TEXT, data TEXT, mod30 INTEGER, is_prime INTEGER, vault_key TEXT)''')
    
    print("--- MIRROR-LLM: Node Khemis-Miliana-Alpha Active ---")
    
    while True:
        user_input = input("\033[1;32mInput Signal:\033[0m ")
        if user_input.lower() in ['exit', 'quit']: break
        
        # 2. الحساب الرياضي (تردد الإشارة)
        sig = sum(ord(c) for c in user_input)
        res = sig % 30
        is_prime = 1 if res in SOVEREIGN_SET else 0
        v_key = hashlib.sha256(f"{user_input}{sig}".encode()).hexdigest()[:16]
        
        # 3. الحفظ في المخزن
        cursor.execute("INSERT INTO signals VALUES (?, ?, ?, ?, ?)", 
                       (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, res, is_prime, v_key))
        conn.commit()
        
        # 4. النتيجة
        status = "PRIME POTENTIAL" if is_prime else "BALANCED ANCHOR"
        print(f">> Status: {status} | Vault ID: {v_key}\n")

    conn.close()

if __name__ == "__main__":
    start_node()import sqlite3
import hashlib
from datetime import datetime

# المحرك الرياضي (Zeta Logic)
SOVEREIGN_SET = {1, 7, 11, 13, 17, 19, 23, 29}

def start_node():
    # 1. إنشاء ملف قاعدة البيانات (المخزن)
    conn = sqlite3.connect('mirror_signals.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS signals 
                      (timestamp TEXT, data TEXT, mod30 INTEGER, is_prime INTEGER, vault_key TEXT)''')
    
    print("--- MIRROR-LLM: Node Khemis-Miliana-Alpha Active ---")
    
    while True:
        user_input = input("\033[1;32mInput Signal:\033[0m ")
        if user_input.lower() in ['exit', 'quit']: break
        
        # 2. الحساب الرياضي (تردد الإشارة)
        sig = sum(ord(c) for c in user_input)
        res = sig % 30
        is_prime = 1 if res in SOVEREIGN_SET else 0
        v_key = hashlib.sha256(f"{user_input}{sig}".encode()).hexdigest()[:16]
        
        # 3. الحفظ في المخزن
        cursor.execute("INSERT INTO signals VALUES (?, ?, ?, ?, ?)", 
                       (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, res, is_prime, v_key))
        conn.commit()
        
        # 4. النتيجة
        status = "PRIME POTENTIAL" if is_prime else "BALANCED ANCHOR"
        print(f">> Status: {status} | Vault ID: {v_key}\n")

    conn.close()

if __name__ == "__main__":
    start_node()import sqlite3
import hashlib
from datetime import datetime

# المحرك الرياضي (Zeta Logic)
SOVEREIGN_SET = {1, 7, 11, 13, 17, 19, 23, 29}

def start_node():
    # 1. إنشاء ملف قاعدة البيانات (المخزن)
    conn = sqlite3.connect('mirror_signals.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS signals 
                      (timestamp TEXT, data TEXT, mod30 INTEGER, is_prime INTEGER, vault_key TEXT)''')
    
    print("--- MIRROR-LLM: Node Khemis-Miliana-Alpha Active ---")
    
    while True:
        user_input = input("\033[1;32mInput Signal:\033[0m ")
        if user_input.lower() in ['exit', 'quit']: break
        
        # 2. الحساب الرياضي (تردد الإشارة)
        sig = sum(ord(c) for c in user_input)
        res = sig % 30
        is_prime = 1 if res in SOVEREIGN_SET else 0
        v_key = hashlib.sha256(f"{user_input}{sig}".encode()).hexdigest()[:16]
        
        # 3. الحفظ في المخزن
        cursor.execute("INSERT INTO signals VALUES (?, ?, ?, ?, ?)", 
                       (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, res, is_prime, v_key))
        conn.commit()
        
        # 4. النتيجة
        status = "PRIME POTENTIAL" if is_prime else "BALANCED ANCHOR"
        print(f">> Status: {status} | Vault ID: {v_key}\n")

    conn.close()

if __name__ == "__main__":
    start_node()import sqlite3
import hashlib
from datetime import datetime

# المحرك الرياضي (Zeta Logic)
SOVEREIGN_SET = {1, 7, 11, 13, 17, 19, 23, 29}

def start_node():
    # 1. إنشاء ملف قاعدة البيانات (المخزن)
    conn = sqlite3.connect('mirror_signals.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS signals 
                      (timestamp TEXT, data TEXT, mod30 INTEGER, is_prime INTEGER, vault_key TEXT)''')
    
    print("--- MIRROR-LLM: Node Khemis-Miliana-Alpha Active ---")
    
    while True:
        user_input = input("\033[1;32mInput Signal:\033[0m ")
        if user_input.lower() in ['exit', 'quit']: break
        
        # 2. الحساب الرياضي (تردد الإشارة)
        sig = sum(ord(c) for c in user_input)
        res = sig % 30
        is_prime = 1 if res in SOVEREIGN_SET else 0
        v_key = hashlib.sha256(f"{user_input}{sig}".encode()).hexdigest()[:16]
        
        # 3. الحفظ في المخزن
        cursor.execute("INSERT INTO signals VALUES (?, ?, ?, ?, ?)", 
                       (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, res, is_prime, v_key))
        conn.commit()
        
        # 4. النتيجة
        status = "PRIME POTENTIAL" if is_prime else "BALANCED ANCHOR"
        print(f">> Status: {status} | Vault ID: {v_key}\n")

    conn.close()

if __name__ == "__main__":
    start_node()