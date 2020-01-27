cmake_minimum_required(VERSION 3.10)

#Project name:
project(jubes VERSION 0.1)

#Add Library
add_subdirectory("lib")



#Set C Compiler Version:

set(CMAKE_C_COMPILER /usr/bin/gcc)

set(EXECUTABLE_OUTPUT_PATH "bin")
add_executable(jubes src/main.c)

