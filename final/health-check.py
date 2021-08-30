#!/usr/bin/env python3

import emails2
import os
import psutil
import socket


sender = "automation@example.com"
receiver = ""
body = "Please check your system and resolve the issue as soon as possible."
attach = "/dev/null"

print("1")

if psutil.cpu_percent() > 80:
   print("true")
   subject = "Error - CPU usage is over 80%"
   message = emails2.generate(sender, receiver, subject, body)
   emails2.send(message)

if psutil.disk_usage('/').percent > 80:
   subject = "Error - Available disk space is less than 20%"
   message = emails2.generate(sender, receiver, subject, body)
   emails2.send(message)

if psutil.virtual_memory().free // 2**20 < 500:
   subject = "Error - Available memory is less than 500MB"
   message = emails2.generate(sender, receiver, subject, body)
   emails2.send(message)

if socket.gethostbyname('localhost') != '127.0.0.1':
   subject = "Error - localhost cannot be resolved to 127.0.0.1"
   message = emails2.generate(sender, receiver, subject, body)
   emails2.send(message)


