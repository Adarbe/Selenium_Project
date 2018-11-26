from selenium import webdriver
import time
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys("C:\Users\adarb\Pictures\IMG_20150512_130821-COLLAGE.jpg")
shell.Sendkeys("~")


print ("Hello")
print ("HAHAHAH")