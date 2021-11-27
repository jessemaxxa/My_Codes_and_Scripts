
from hashlib import sha256

def dictionary_attack(dictionary_word, target_hash):
    pass_bytes = dictionary_word.encode('utf-8')
    pass_hash = sha256(pass_bytes)
    digest = pass_hash.hexdigest()
    if digest == target_hash:
        return True
        
        path = input("Enter Wordlist Path")
        hash = input("Enter Hash to crack: ")
        dictionary = open(path, 'r')
        for word in dictionary:
            if dictionary_attack(word, hash["password_hash"][0]) == True:
                print("Matched Password: ", word)
                break
            else:
                continue
            
