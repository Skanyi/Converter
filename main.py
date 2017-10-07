import base64

class Converter(object):

    def convert_hex_to_text(filename):
        if filename:
            with open(filename) as hex_data:
                data = hex_data.read()
                ascii_string = ''.join([chr(int(''.join(c), 16)) for c in zip(data[0::2],data[1::2])])
                print(ascii_string)
                return ascii_string

    def decode_base64(encoded_string):
        decoded_string = base64.b64decode(encoded_string)
        print(decoded_string)

    def encode_txt_to_base64(filename):
        if filename:
            with open(filename) as clear_text:
                text = clear_text.read()
                coded_text = base64.b64encode(bytes(text.encode()))
                print(coded_text)
        
    def save_state():
        print('The process was terminated by keyboard interuption')
