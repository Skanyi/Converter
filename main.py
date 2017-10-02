import base64

class Converter(object):

    def convert_hex_to_text(filename):
        if filename:
            with open(filename) as hex_data:
                data = hex_data.read()
                ascii_string = ''.join([chr(int(''.join(c), 16)) for c in zip(data[0::2],data[1::2])])
                print(ascii_string)
                return ascii_string
                
    def save_state():
        print('The process was terminated by keyboard interuption')
