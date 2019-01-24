import requests

code_origin = 2226304
code_end = 2228220

url = ''

r = requests.get(url, stream=True)
chunk_size = 6000
with open('output/{{code}}', 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
