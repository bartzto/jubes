#!/bin/sh

cmake ./
make

help() 
{
	echo "jubes [option]"
	printf "\t-e\tTo execute the programm after compiling\n"
	printf "\t--help\tTo show this Help page\n"
	exit
}




while test $# -gt 0
do
    case "$1" in
        -e) echo "Executing Programm:"
	    ./jubes
            ;;
        -v) echo "Version:"
            ;;
	-c)
	    rm -rf CMakeFiles/ cmake_install.cmake Makefile CMakeCache.txt bin/*
	    ;;
	--help)
	    help
	    ;;
         *) echo "Invalid Argument $1"
	    help
	    ;;
    esac
    shift
done
