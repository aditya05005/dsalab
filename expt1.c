#include <stdio.h>
#include <stdlib.h>  // For dynamic memory allocation

#define MAX 5  // Define the maximum size of the stack

// Define the stack structure
struct Stack {
    int arr[MAX];  // Array to hold the stack elements
    int top;       // Index to track the top element
};

// Function to initialize the stack
void initStack(struct Stack* stack) {
    stack->top = -1;  // Stack is initially empty, so top is set to -1
}

// Function to check if the stack is full
int isFull(struct Stack* stack) {
    return stack->top == MAX - 1;  // If top reaches MAX-1, stack is full
}

// Function to check if the stack is empty
int isEmpty(struct Stack* stack) {
    return stack->top == -1;  // If top is -1, stack is empty
}

// Function to push an element onto the stack
void push(struct Stack* stack, int value) {
    if (isFull(stack)) {
        printf("Stack Overflow! Cannot push %d\n", value);
    } else {
        stack->arr[++(stack->top)] = value;  // Increment top and insert the value
        printf("Pushed %d onto the stack\n", value);
    }
}

// Function to pop an element from the stack
int pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow! No elements to pop\n");
        return -1;  // Return -1 to indicate error (stack is empty)
    } else {
        int poppedValue = stack->arr[stack->top--];  // Return the top element and decrement top
        printf("Popped %d from the stack\n", poppedValue);
        return poppedValue;
    }
}

// Function to peek at the top element of the stack without removing it
int peek(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty! No element to peek\n");
        return -1;  // Return -1 to indicate error
    } else {
        return stack->arr[stack->top];  // Return the top element
    }
}

// Function to get the size of the stack
int size(struct Stack* stack) {
    return stack->top + 1;  // Top + 1 gives the number of elements in the stack
}

int main() {
    struct Stack stack;  // Declare a stack variable
    initStack(&stack);  // Initialize the stack

    // Test pushing elements onto the stack
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);

    // Test peeking the top element
    printf("Top element is %d\n", peek(&stack));  // Output: 30

    // Test popping elements from the stack
    pop(&stack);
    printf("Top element after pop is %d\n", peek(&stack));  // Output: 20

    // Test the size of the stack
    printf("Stack size is %d\n", size(&stack));  // Output: 2

    // Test pushing to a full stack
    push(&stack, 40);
    push(&stack, 50);
    push(&stack, 60);  // This will trigger stack overflow

    return 0;
}
