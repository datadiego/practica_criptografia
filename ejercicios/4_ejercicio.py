import base64
import jwt

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"

header, payload, signature = token.split(".")
header = base64.b64decode(header + "==").decode()
payload = base64.b64decode(payload + "==").decode()
signature = base64.b64decode(signature + "==")

print("Header: ", header)
print("Payload: ", payload)
print("Signature: ", signature)

hacker_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHR"

header, payload, signature = hacker_token.split(".")
header = base64.b64decode(header + "==").decode()
payload = base64.b64decode(payload + "==").decode()
signature = base64.b64decode(signature + "==")
print("----")
print("Header: ", header)
print("Payload: ", payload, "<-- esta intentando hacerse pasar por un administrador")
print("Signature: ", signature)