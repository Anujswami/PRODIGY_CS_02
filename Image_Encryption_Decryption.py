import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, method='swap', key=50):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)
    
    np.random.seed(key)  # Set the seed for reproducibility
    
    if method == 'swap':
        indices = np.random.permutation(pixels.shape[0] * pixels.shape[1])
        encrypted_pixels = pixels.reshape(-1, 3)[indices].reshape(pixels.shape)
    elif method == 'math':
        encrypted_pixels = (pixels + key) % 256
    
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'), 'RGB')
    encrypted_image.save(output_path)
    messagebox.showinfo("Success", f'Image encrypted and saved to {output_path}')

def decrypt_image(image_path, output_path, method='swap', key=50):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image)
    
    np.random.seed(key)  # Set the seed for reproducibility
    
    if method == 'swap':
        indices = np.random.permutation(pixels.shape[0] * pixels.shape[1])
        reverse_indices = np.argsort(indices)
        decrypted_pixels = pixels.reshape(-1, 3)[reverse_indices].reshape(pixels.shape)
    elif method == 'math':
        decrypted_pixels = (pixels - key) % 256
    
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'), 'RGB')
    decrypted_image.save(output_path)
    messagebox.showinfo("Success", f'Image decrypted and saved to {output_path}')

def open_file_encrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        method = method_var.get()
        key = int(key_entry.get()) if method == 'math' else int(key_entry.get())
        encrypt_image(file_path, 'encrypted_image.jpg', method=method, key=key)

def open_file_decrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        method = method_var.get()
        key = int(key_entry.get()) if method == 'math' else int(key_entry.get())
        decrypt_image(file_path, 'decrypted_image.jpg', method=method, key=key)

# Set up the GUI
root = tk.Tk()
root.title("Image Encryption Tool")

method_var = tk.StringVar(value='swap')

tk.Label(root, text="Encryption Method:").pack(pady=5)
tk.Radiobutton(root, text="Swap Pixels", variable=method_var, value='swap').pack()
tk.Radiobutton(root, text="Mathematical Transformation", variable=method_var, value='math').pack()

tk.Label(root, text="Key:").pack(pady=5)
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt Image", command=open_file_encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=open_file_decrypt)
decrypt_button.pack(pady=10)

root.mainloop()
