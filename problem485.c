#include <stdio.h>

int d(int j) {
    int sum = 1;
    for (int i = 1; i < (int)(j/2)+1; i++) {
        if (j%i == 0) {
            sum++;
        }
    }

    return sum;
}

int m(int n, int k) {
    int max_val = 0;
    int num;
    for (int j = n; j < n + k; j++) {
        num = d(j);
        if (num > max_val) {
            max_val = num;
        }
    }

    return max_val;
}


int s(int u, int k) {
    int sum = 0;
    // sum(m(n,k) for 1 <= n <= u-k+1
    for (int n = 1; n < u-k+2; n++) {
        sum += m(n,k);
    }

    return sum;
}

int main () {
    printf("%d\n", s(1000, 10)); // 17176
    printf("%d\n", s(100000000, 100000)); // ?????
}