 
def gen_keyword_phrase(message: str, keyword: str) -> str:
  """
  Generates a keyword phrase (with the same length as the provided message)
  
  Args: 
    message (str): message to encode or decode
    keyword (str): keyword to generate a keyword phrase 
    
  Returns:
    keyword_phrase (str) 
  """
  keyword_phrase = ""
  special_chars = [" ", ".", "!", "?", ",", ";", "'"]
  keyword_idx = 0 
  for idx in range(len(message)):
    char = message[idx]
    if char in special_chars:
      keyword_phrase += char
      continue
    
    keyword_phrase += keyword[keyword_idx]
    keyword_idx += 1
    
    if (keyword_idx >= len(keyword)):
      keyword_idx = 0 # reset
  return keyword_phrase


def vignere_cipher(message: str, keyword: str, encode: bool) -> str:
  """
  Deciphers or encodes a message using the Vignere cipher and a keyword. 
  
  Args:
    message (str): message to encode or message to be decoded 
    keyword (str): string used to shift the alphabet values 
    encode (bool): True to encode a message, False not to encode 
  
  Returns:
    new_char (str): the encoded message (if encode True) or decoded message (if encode False)
  """
  special_chars = [" ", ".", "!", "?", ",", ";", "'"]
  alphabet = ''.join([chr(i) for i in range(97, 123)])

  keyword_phrase = gen_keyword_phrase(message, keyword)  
  new_message = ""
  
  for i in range(len(message)):
    message_char = message[i] 
    keyword_char = keyword_phrase[i]
    if message_char in special_chars:
      new_message += message_char
      continue
    
    message_char_idx = alphabet.find(message_char)
    keyword_char_idx = alphabet.find(keyword_char)
    
    # Shift to the left by keyword_char_idx 
    shift = message_char_idx - (keyword_char_idx) if encode else message_char_idx + keyword_char_idx 
    if shift < 0:
      new_char = alphabet[25+shift+1]
    elif shift > 25:
      new_char = alphabet[shift-25-1]
    else: 
      new_char = alphabet[shift]    
    new_message += new_char
  
  return new_message 

if __name__ == "__main__":
  # Examples
  print(vignere_cipher("berry is the spy", "dog", True))
  print(vignere_cipher("yqlok cp fbb ejv", "dog", False))
  print(vignere_cipher("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!", "friends", False))


