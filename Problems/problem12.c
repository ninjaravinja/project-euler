#include <stdio.h>
#include <stdbool.h>

int main(void) {

    int pos = 12375;
    int num = 0;
    for (int i = 0; i <= pos; i++) {
        num += i;
    }
    printf("%d\n", num);
    printf("76576500\n");

    int num1 = 1;
    int to_add = 1;

    while (true) {
        int count = 1;

        for (int i = 1; i <= (int)(num1/2)+1; i++) {
            if (num1%i == 0) {
                count++;
            }
        }

        if (count < 500) {
            count = 0;
        }

        if (count >= 500) {
            printf("%d, %d\n", num1, count);
            break;
        }

        to_add++;
        num1 += to_add;

    }

    return 0;
}