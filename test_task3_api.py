import http.client

conn = http.client.HTTPConnection("127.0.0.1:5000")

payload = "{\n\t\"lesson\": [ 1594663200, 1594666800 ],\n\t\"pupil\": [ 1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472 ],\n\t\"tutor\": [ 1594663290, 1594663430, 1594663443, 1594666473 ]\n}"

headers = {'Content-Type': "application/json"}

conn.request("GET", "/timing/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
