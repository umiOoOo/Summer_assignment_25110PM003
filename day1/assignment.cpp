
// Q1: Program to calculate sum of first n natural numbers
 
#include <iostream>
using namespace std;
 
int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    int sum = n * (n + 1) / 2;
    cout << "Sum of first " << n << " natural numbers = " << sum << endl;
    return 0;
}
 
 
// -------------------------------------------------------
 
 
// Q2: Program to print multiplication table of a given number
 
#include <iostream>
using namespace std;
 
int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Multiplication table of " << num << ":" << endl;
    for (int i = 1; i <= 10; i++) {
        cout << num << " x " << i << " = " << num * i << endl;
    }
    return 0;
}
 
 
// -------------------------------------------------------
 
 
// Q3: Program to find factorial of a number
 
#include <iostream>
using namespace std;
 
int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    long long factorial = 1;
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    cout << "Factorial of " << n << " = " << factorial << endl;
    return 0;
}
 
 
// -------------------------------------------------------
 
 
// Q4: Program to count digits in a number
 
#include <iostream>
using namespace std;
 
int main() {
    long long num;
    cout << "Enter a number: ";
    cin >> num;
    int count = 0;
    if (num == 0) {
        count = 1;
    } else {
        if (num < 0) num = -num;
        while (num != 0) {
            num /= 10;
            count++;
        }
    }
    cout << "Number of digits = " << count << endl;
    return 0;
}
 