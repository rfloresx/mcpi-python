CC = g++
FILES = hestec-interface.cpp
OUTPUT = interface

build:
	$(CC) $(FILES) -o $(OUTPUT)