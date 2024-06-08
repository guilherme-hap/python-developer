"""
    Programa que utiliza a biblioteca 'ctypes' para implementar um ocultador de arquivos
    ou diretórios.
"""
import ctypes

file = input("Enter the name of the file to be hidden (e.g. file.txt): ")

hide = 0x02

result = ctypes.windll.kernel32.SetFileAttributesW(file, hide)

if result:
    print("File hidden.")
else:
    print("File has not been hidden.")
