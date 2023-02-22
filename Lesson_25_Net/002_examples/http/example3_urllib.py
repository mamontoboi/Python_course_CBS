from urllib import request

# отримуємо вміст сторінки по domain- як порт буде використаний 80
# # Для вказівки іншого порту використовуємо запис виду: http://example:81.com
response = request.urlopen('http://example.com')

# друкуємо інформацію про http-відповідь
print(response.status)  # 200
print(response.getcode())  # 200
print(response.msg)  # OK
print(response.reason)  # OK
# отримуємо заголовки у вигляді внутрішнього об'єкта
print(response.headers)  # Accept-Ranges: bytes (line by line)
# отримуємо словник усіх заголовків
print(response.getheaders())  # [('Accept-Ranges', 'bytes'), ('Age', '591306'), ('Cache-Control', 'max-age=604800'),...]
# отримання заголовку
print(response.headers.get('Content-Type'))  # text/html; charset=UTF-8
print(response.getheader('Content-Type'))  # text/html; charset=UTF-8

print(response.headers.get('Expires'))  # Tue, 29 Nov 2022 23:16:06 GMT
print(response.getheader('Expires'))  # Tue, 29 Nov 2022 23:16:06 GMT
