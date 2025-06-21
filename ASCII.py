# m1
# def ascii_average(text):
#     javob = [ord(c) for c in text if c.isalpha()]
#     return sum(javob) / len(javob) if javob else 0
# print(ascii_average('salom'))

# m2
# def filterr(text):
#     return ''.join(i for i in text if 65 <= ord(i) <= 122)
# print(filterr('saloom'))

# m3
# def kata(text):
#     sozla = text.split()
#     return max(sozla, key=lambda soz: sum(ord(i) for i in soz))
# print(kata('salom nima xayrrrr'))

# m4
# def jufft(text):
#     juft = [c for c in text if ord(c) % 2 == 0]
#     toq = [c for c in text if ord(c) % 2 == 1]
#     return juft, toq
# print(jufft('salom nima xayrr'))


# # m5
# def siljit(text, shift):
#     result = ''
#     for i in text:
#         if i.isupper():
#             result += chr((ord(i) - 65 + shift) % 26 + 65)
#         elif i.islower():
#             result += chr((ord(i) - 97 + shift) % 26 + 97)
#         else:
#             result += i
#     return result
# print(siljit('Saloom' , 3))

# m6
# def farqi(text):
#     return [ord(text[i+1]) - ord(text[i]) for i in range(len(text) - 1)]
# print(farqi('saloom'))

# m7
# def kod(firstname, lastname):
#     hammasi = ''.join(a + b for a, b in zip(firstname, lastname))
#     ascii_qil = ''.join(str(ord(i)) for i in hammasi)
#     return ascii_qil[:8].ljust(8, '0')
# print(kod('Shaxzoda' , 'Kimdir'))