// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define KEY_SIZE_BYTES 32 // 256 bits

void generate_key(unsigned char *key, size_t key_size) {
    int urandom = open("/dev/urandom", O_RDONLY);
    if (urandom == -1) {
        fprintf(stderr, "Error opening /dev/urandom\n");
        exit(1);
    }

    ssize_t bytes_read = read(urandom, key, key_size);
    if (bytes_read < 0) {
        fprintf(stderr, "Error reading from /dev/urandom\n");
        exit(1);
    }

    close(urandom);
}

int main() {
    unsigned char key[KEY_SIZE_BYTES];

    generate_key(key, sizeof(key));

    printf("Generated Key: ");
    for (int i = 0; i < sizeof(key); ++i) {
        printf("%02x", key[i]);
    }
    printf("\n");

    return 0;
}