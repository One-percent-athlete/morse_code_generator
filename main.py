import winsound  # For Windows (replace with appropriate library for other OS)

MORSE_CODE = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    ' ': '/',  # Space is represented by a slash
}

def text_to_morse(text):
  text = text.upper()  # Convert text to uppercase for consistency
  morse_code = ''
  for char in text:
    if char in MORSE_CODE:
      morse_code += MORSE_CODE[char] + ' '  # Add space between characters
    else:
      morse_code += ' '  # Add space for unsupported characters
  return morse_code.strip()  # Remove trailing space

def play_morse_sound(symbol):
  if symbol == '.':  # Short beep
    winsound.Beep(1000, 200)  # Adjust frequency (Hz) and duration (ms) as needed
  elif symbol == '-':  # Long beep
    winsound.Beep(1000, 500)
  else:
    pass  # Do nothing for spaces

def play_morse_code(morse_code):
  for symbol in morse_code:
    play_morse_sound(symbol)
    # Add a pause between symbols (adjust as needed)
    winsound.Beep(1000, 100)  # Optional silence between symbols

text_input = input("Enter text to convert to Morse code: ")
morse_code = text_to_morse(text_input)
print("Morse Code:", morse_code)

# Play the Morse code (if sound function is implemented)
play_morse_code(morse_code)