#include <stdio.h>

int Test(int a, int b, int c) {
    int t = 7;
    switch (a % 4) {
        case 0:
            if (c % 2) t = 6;
            // break;
            // Fall through
        case 1:
            if (b > 9) t = 1;
            else {
                if (c % 2) t = 2;
                else t = 3;
            }
            break;
        case 2:
            if ((b < 0) || (b > 10)) t = 0;
            else if (c >= 3) t = 4;
            else t = 5;
            break;
    }
    return t;
}

int main() {
    int a = 1;
    int b = 0;
    int c = 3;

    int result = Test(a, b, c);
    printf("The result of Test(%d, %d, %d) is: %d\n", a, b, c, result);

    return 0;
}
