#include <stdio.h>

int factors(int num1) {
    int result = num1;

    for (int i = 2; i*i < num1; i++) {
        if (num1%i == 0) {
            while (num1%i == 0) {
                num1 /= i;
            }
            result -= result/i;
        }
    }

    if (num1 > 1) {
        result -= result/num1;
    }

    return result;
}

int main () {
    int num_of_primes = 0;
    int num = 0;
    double highest_ratio = 0.0;
    double ratio;
    int count;

    for (int i = 1; i <= 1000000; i++) {
        count = factors(i);
        ratio = (double)(i)/count;
        
        if (ratio > highest_ratio) {
            num_of_primes = count;
            num = i;
            highest_ratio = ratio;
        }
        
        if (i%10000 == 0) {
            printf("%d/1000000 --> %.2f%%\n", i, (double)(i)/1000000*100);
        }
    }

    printf("%d %d %.5f\n", num_of_primes, num, ratio);

    return 0;
}