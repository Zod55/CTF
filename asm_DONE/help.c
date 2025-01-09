#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

#define BUFFER_SIZE 100

int main() {
    char buffer[BUFFER_SIZE];
    ssize_t bytesRead;
    int fd;
    char x[] = "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong";
    // Open the file
    fd = open(x, O_RDONLY);
   // Read and write loop
    bytesRead = read(fd, buffer, BUFFER_SIZE);
    write(STDOUT_FILENO, buffer, bytesRead);

    return 0;
}
