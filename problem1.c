#include <stdio.h>

int main () {
    int sum = 0;
    int nums = 1000;

    for (int i = 0; i < nums; i++) {
        if ((i%3 == 0) || (i%5 == 0)) {
            sum += i;
        }
    }

    printf("%d", sum);

    return 0;
}