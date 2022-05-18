chars=['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars=['c','d','e','f','g','h','i','j','k','l','m'
,'n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# Cipher wheel with a function for finding an element in a list

# def find_in_list(query, mainlist):
#     mainlist_len=len(query)
#     range_for_loop=range(mainlist_len)
#     for i in range_for_loop:
#         element=mainlist[i]
#         if element==query:
#             return i
# query=["z","y","b","a"]
# mainlist=["a","b","c","d"]
# print(find_in_list(query,mainlist))


# encrypt_message function defined here but not called
def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the 
# encrypted message. The "plain_msg" is tranfered into "encrypted_msg" 
# using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, 
# g => i  and hence encrypted_msg = "pi"
    encrypted_msg=plain_msg
    for character in encrypted_msg:
# for character in msg
        if character in chars:
            char_index =(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
            print(encrypted_msg)
        else:
            encrypted_msg = encrypted_msg + character
            print(encrypted_msg)
plain_msg=["n","g"]
encrypt_message(plain_msg)