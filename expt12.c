#include <stdio.h>
#include <string.h>

#define MAX 10
#define LEN 20

// Binary search function for strings
int binarySearch(char arr[][LEN], int size, char target[]) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        int cmp = strcmp(arr[mid], target);

        if (cmp == 0) {
            return mid; // Found target
        } else if (cmp < 0) {
            low = mid + 1; // Target is after mid
        } else {
            high = mid - 1; // Target is before mid
        }
    }
    return -1; // Not found
}

int main() {
    // Sorted list of names (like a phonebook)
    char phonebook[MAX][LEN] = {
        "Aditya",
        "Arkam",
        "Madhavan",
        "Sahil",
        "Harsh",
        "Jaideep",
        "MRINAL",
        "Rittam",
        "Ayush",
        "Aryaman"
    };

    char name[LEN];
    printf("Enter name to search: ");
    fgets(name, LEN, stdin);
    name[strcspn(name, "\n")] = 0; // Remove trailing newline

    int index = binarySearch(phonebook, MAX, name);

    if (index != -1) {
        printf("%s found at position %d in the phonebook.\n", name, index + 1);
    } else {
        printf("%s not found in the phonebook.\n", name);
    }

    return 0;
}
