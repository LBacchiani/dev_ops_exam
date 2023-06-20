# dev_ops_exam

The program could be installed using the docker container technology (https://www.docker.com/) available for the majority of the operating systems.

## Docker Installation

The Docker image is availabe in Docker Hub. To install it please run the following commands.

```
sudo docker pull lorenzobacchinai/dev_ops_exam
sudo docker run --entrypoint="/bin/bash" -i --rm -t lorenzobacchiani/dev_ops_exam
```

## Execution Instruction

To run the program, please run the following commands. 

```
python main.py
```

If you decide to use the ```-f``` flag, then the program will use the fibonacci function, otherwise, if you use the ```-p``` flag, the program will use the prime_numbers function
