# BSCPE 1-4
# PABUNA, KARTINA B. 
# ASSIGNMENT 2
# ITEM NO. 2

# Pseudocode
# Ask the user for an encrypted text ten save it
print("\033[93m=" * 80, "\n")
encrypted_str = input("\033[92mEnter a string to decrypt: \033[97m")
decrypted_str = ""

# Check every character
for i in range(len(encrypted_str)):

# Convert '*' to 'a'
    if encrypted_str[i] == "*":
        decrypted_str += "a"

# Convert '&' to 'e'
    elif encrypted_str[i] == "&":
        decrypted_str += "e"

# Convert '#' to 'i'
    elif encrypted_str[i] == "#":
        decrypted_str += "i"

# Convert '+' to 'o'
    elif encrypted_str[i] == "+":
        decrypted_str += "o"

# Convert '!' to 'u'
    elif encrypted_str[i] == "!":
        decrypted_str += "u"
    else:
        decrypted_str += encrypted_str[i]

# Print the output
print("\n", "\033[93m=" * 80, "\n")
print("\033[1m\033[95mThe Plain Text:\x1B[3m\033[97m", decrypted_str)
print("\n", "\033[93m=" * 80, "\n")


# ITEM NO. 3
# Pseudocode
# Take user's inputs for message and key. Convert them into uppercase letter. 
# The input message or key should not have spaces
input_str = ""
while input_str != 1:
    message = input("\033[92mEnter your Message: \033[97m").upper()
    key = input("\033[96mEnter your Key: \033[97m").upper()
    if " " in message or " " in key:
        print("\033[91mERROR. There should be no spaces on both inputs. Try again.\n")
        continue
    else:
        break

print("\n", "\033[93m=" * 80, "\n")
print("\033[92mMessage:\033[97m", message)
print("\033[96mKey:\033[97m", key, "\n")

# Create a dictionary to map each alphabet to a number
str_to_int = {}
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    str_to_int[letter] = i

# Create a dictionary to map each number to an alphabet
int_to_str = {}
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    int_to_str[i] = letter

# Match the length of the key to the length of the message by repeating it
if len(message) > len(key):
    key *= (len(message) // len(key)) + 1
    key = key[:len(message)]

# Convert each character in message to its corresponding number and append to a list
converted_message = []
for char in message:
    if char in str_to_int:
        converted_message.append(str_to_int[char])

# Convert each character in key to its corresponding number and append to a list
converted_key = []
for char in key:
    if char in str_to_int:
        converted_key.append(str_to_int[char])

# Add each value in the converted message and key and append to a list
added_values = []
for i in range(len(converted_message)):
    added_values.append(converted_message[i] + converted_key[i])

# If the sum of the values exceed 25, reduce it to its modular value and append to a list
mod_values = []
for i in range(len(added_values)):
    if added_values[i] % 26 != 0:
        mod_values.append(added_values[i] % 26)
    elif added_values[i] % 26 == 0:
        mod_values.append(0)
    else:
        mod_values.append(added_values[i])

# Convert each value in modular values to its corresponding alphabet and append to a list
ciphertext = []
for char in mod_values:
    if char in int_to_str:
        ciphertext.append(int_to_str[char])

# Print the key stream and the converted message and key
print("\033[93m=" * 80, "\n")
print("\033[94mKey Stream:\033[97m", key)
print("\033[92mConverted Message:\033[97m", " ".join(str(x) for x in converted_message))
print("\033[96mConverted Key:\033[97m", " ".join(str(x) for x in converted_key))

# Print the added and modular values and the final ciphertext
print("\n", "\033[93m=" * 80, "\n")
print("\033[94mAdd:\033[97m", " ".join(str(x) for x in added_values))
print("\033[94mMod:\033[97m", " ".join(str(x) for x in mod_values))
print("\n", "\033[93m=" * 80, "\n")
print("\033[95mCiphertext:\033[97m", " ".join(ciphertext))
print("\n", "\033[93m=" * 80, "\n")