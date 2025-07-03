from PIL import Image
import os 

def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded_img = img.copy()
    width, height = img.size
    
    # Add a special end symbol to mark the end of the message
    message += '\0'
    
    # Convert the message to a binary string
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                pixel = list(encoded_img.getpixel((x, y)))
                
                # Change the Red channel least significant bit to message bit
                pixel[0] = (pixel[0] & ~1) | int(binary_message[data_index])
                
                encoded_img.putpixel((x, y), tuple(pixel))
                data_index += 1
            else:
                # Finished encoding all bits
                break
                
    encoded_img.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ''
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            binary_message += str(pixel[0] & 1)
            
            # Check if the last 8 bits are the null character (end of message)
            if binary_message[-8:] == '00000000':
                # Stop reading bits
                break
                
    # Convert binary to characters
    message = ''
    for i in range(0, len(binary_message)-8, 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        
    return message

if __name__ == "__main__":
    # Example usage
    cover_image_path = "cover.png"  # Put your image path here
    output_image_path = "encoded_image.png"
    secret_message = "can you see me fuck"
    
    encode_image(cover_image_path, secret_message, output_image_path)
    hidden_message = decode_image(output_image_path)
    print("Decoded message:", hidden_message)
