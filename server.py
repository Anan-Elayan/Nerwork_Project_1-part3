from socket import *


serverPort = 9966
serverSocket = socket(AF_INET, SOCK_STREAM)#will use the internet 'protocol' version 4
serverSocket.bind(("", serverPort))
serverSocket.listen(2)#who many connections.
print("The server is ready to receive")


while True:
    # connect to the server
    # connectionSocket = new Socket between client and server
    connectionSocket, address = serverSocket.accept() #return address of client && new socket
    sentence = connectionSocket.recv(1024).decode()# containing the HTTP Request


    # get the request from client and make a processing in text to get the html/css files or jpg/png/icon images to send it to user
    sent = sentence[sentence.find("Get /") + len("GET /") + 1:sentence.find(" HTTP")].strip()
    # print(address)
    print(address)
    print(sentence)
    ip = address[0]
    port = address[1]
    print(" ip " + ip)
    print(" port " + str(port))

    wrong = f"""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Error 404</title>
    <!-- styling file -->
    <link rel="stylesheet" href="wrongStyle.css" />
  </head>
  <body>
    <section class="container">
      <h1 class="text-error">The file is not found</h1>
      <h3 class="info">Motasem Ali: 1210341</h3>
      <h3 class="info">Anan Elayan: 1211529</h3>
      <h3 class="info">IP: {ip}</h3>
      <h3 class="info">Port: {port}</h3>
    </section>
  </body>
</html>


        """

    # check the type of file or image to send it to user as this type by method .endswith()
    if (sent == "" or sent == 'index.html' or sent == "main_en.html"
            or sent == "en" or sent == "/" or sent == "main"):
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())#the server sends an HTTP response with a 'status line'
        connectionSocket.send("Content-Type: text/html \r\n\r\n".encode())
        file = open("main_en.html", "rb", 1024)
        connectionSocket.send(file.read())
    elif sent == 'cr':
        connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\n")
        connectionSocket.send(b"Location: https://www.cornell.edu\r\n")
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    elif sent == 'so':
        connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\n")
        connectionSocket.send(b"Location: https://stackoverflow.com \r\n")
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    elif sent == 'rt':
        connectionSocket.send(b"HTTP/1.1 307 Temporary Redirect\r\n")
        connectionSocket.send(b"Location: https://ritaj.birzeit.edu/register \r\n")
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    elif sent.endswith("ar"): # open file html as a arabic
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n\r\n".encode())
        file = open("main_ar.html", "rb", 1024)
        connectionSocket.send(file.read())

    elif sent.endswith(".html"):
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n\r\n".encode())
        file = open(sent, "rb", 1024)
        connectionSocket.send(file.read())

    elif sent.endswith(".css"):
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n\r\n".encode())
        file = open(sent, "rb", 1024)
        connectionSocket.send(file.read())

    elif sent.endswith(".js"):
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/js \r\n\r\n".encode())
        file = open(sent, "rb", 1024)
        connectionSocket.send(file.read())

    elif sent.endswith(".jpg"):
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: images/jpg \r\n\r\n".encode())
        file = open(sent, "rb", 1024)
        connectionSocket.send(file.read())

    elif sent.endswith(".png"):
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: images/png \r\n\r\n".encode())
        file = open(sent, "rb", 1024)
        connectionSocket.send(file.read())

    else:
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send(b"\r\n")
        connectionSocket.send(wrong.encode())
        connectionSocket.close()

    connectionSocket.close()
