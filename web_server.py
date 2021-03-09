#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

# TASK 1
#Fill in start
HOST = '127.0.0.1'
PORT = 45678
serverSocket.bind((HOST, PORT))
serverSocket.listen()
#Fill in end

while True:
   #Establish the connection
   print('Ready to serve...')

   # TASK 2
   connectionSocket, addr = serverSocket.accept() #Fill in start  #Fill in end

   try:

      # TASK 3
      message = connectionSocket.recv(1024) #Fill in start      #Fill in end

      filename = message.split()[1]
      f = open(filename[1:])
      print('Received request for: ', filename)

      # TASK 4
      outputdata = "" #Fill in start       #Fill in end

      # TASK 5
      #Send one HTTP header line into socket
      #Fill in start
      
      #Fill in end

      #Send the content of the requested file to the client
      for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
      connectionSocket.send("\r\n".encode())
      connectionSocket.close()
   except IOError:
      print('Houston, we have a problem.')
      # TASK 6
      #Send response message for file not found
      #Fill in start
      
      #Fill in end

      # TASK 7
      #Close client socket
      #Fill in start
      
      #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
