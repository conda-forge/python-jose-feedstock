from jose import jwt
msg = {'key': 'value'}
token = jwt.encode(msg, 'secret', algorithm='HS256')
decoded_msg = jwt.decode(token, 'secret', algorithms=['HS256'])
assert msg == decoded_msg
