"""
    Programa que utiliza a biblioteca 'phonenumbers' para checar de que lugar é
    determinado número de telefone inserido pelo usuário.
"""
import phonenumbers
from phonenumbers import geocoder

phone = input("Enter the phone number in the format +551196840486: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
