def caesar_cipher(message: str, offset: int, encode: bool) -> str:
  special_chars = [" ", ".", "!", "?", ",", ";", "'"]
  alphabet = ''.join([chr(i) for i in range(97, 123)])
  new_message = ""
  for char in message:
    if char in special_chars:
      new_message += char
      continue 
    
    shift = alphabet.find(char) - offset if encode else alphabet.find(char) + offset 
    
    if shift < 0:
      new_char = alphabet[25 + shift + 1]
    elif shift > 25:
      new_char = alphabet[shift - 25 - 1]
    else:
      new_char = alphabet[shift]
    
    new_message += new_char 
    
  return new_message

if __name__ == "__main__":
  # Examples 
  print(caesar_cipher("the offset for the second message is fourteen.", 10, True))
  print(caesar_cipher("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10, False))
  print(caesar_cipher("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14, False))
