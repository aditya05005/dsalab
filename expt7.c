#include <stdio.h>
#include <stdlib.h>

// Define the node structure
struct Node {
    int data;
    struct Node* next;
};

// Head pointer
struct Node* head = NULL;

// Insert a node at the end
void insertAtEnd(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;

    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
    }
    printf("%d inserted at end.\n", value);
}

// Insert a node at the beginning
void insertAtBeginning(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;

    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
        head = newNode;
    }
    printf("%d inserted at beginning.\n", value);
}

// Delete a node from the beginning
void deleteFromBeginning() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    if (head->next == head) {
        free(head);
        head = NULL;
    } else {
        struct Node* temp = head;
        struct Node* last = head;

        while (last->next != head) {
            last = last->next;
        }

        head = head->next;
        last->next = head;
        free(temp);
    }
    printf("Node deleted from beginning.\n");
}

// Delete a node from the end
void deleteFromEnd() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    if (head->next == head) {
        free(head);
        head = NULL;
    } else {
        struct Node* temp = head;
        struct Node* prev = NULL;

        while (temp->next != head) {
            prev = temp;
            temp = temp->next;
        }

        prev->next = head;
        free(temp);
    }
    printf("Node deleted from end.\n");
}

// Display the list
void display() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct Node* temp = head;
    printf("Circular Linked List: ");

    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);

    printf("(back to head)\n");
}

// Main function to test
int main() {
    insertAtEnd(10);
    insertAtEnd(20);
    insertAtBeginning(5);
    display();

    deleteFromBeginning();
    display();

    deleteFromEnd();
    display();

    return 0;
}
