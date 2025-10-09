#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define the maximum size of the queue

// Structure for Queue
struct Queue {
    int arr[MAX];  // Array to hold queue elements
    int front;     // Index for the front of the queue
    int rear;      // Index for the rear of the queue
};

// Function to initialize the queue
void initQueue(struct Queue* q) {
    q->front = -1;  // Set front to -1 to indicate the queue is empty
    q->rear = -1;   // Set rear to -1 to indicate the queue is empty
}

// Function to check if the queue is full
int isFull(struct Queue* q) {
    return q->rear == MAX - 1;  // Queue is full if rear reaches MAX-1
}

// Function to check if the queue is empty
int isEmpty(struct Queue* q) {
    return q->front == -1;  // Queue is empty if front is -1
}

// Function to add an element to the queue (Enqueue)
void enqueue(struct Queue* q, int value) {
    if (isFull(q)) {
        printf("Queue Overflow! Cannot enqueue %d\n", value);
    } else {
        // If the queue is empty, both front and rear should be set to 0
        if (q->front == -1) {
            q->front = 0;
        }
        q->rear++;  // Increment the rear to the next position
        q->arr[q->rear] = value;  // Add the value to the queue
        printf("Enqueued %d to the queue\n", value);
    }
}

// Function to remove an element from the queue (Dequeue)
int dequeue(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue Underflow! No elements to dequeue\n");
        return -1;  // Return -1 to indicate an error (empty queue)
    } else {
        int dequeuedValue = q->arr[q->front];  // Get the value at the front of the queue
        printf("Dequeued %d from the queue\n", dequeuedValue);
        // If there's only one element left, reset front and rear
        if (q->front == q->rear) {
            q->front = -1;
            q->rear = -1;
        } else {
            q->front++;  // Increment front to remove the front element
        }
        return dequeuedValue;  // Return the dequeued value
    }
}

// Function to get the front element of the queue without removing it
int front(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty! No front element\n");
        return -1;  // Return -1 to indicate error
    } else {
        return q->arr[q->front];  // Return the element at the front
    }
}

// Function to get the size of the queue
int size(struct Queue* q) {
    if (isEmpty(q)) {
        return 0;  // If the queue is empty, size is 0
    } else {
        return q->rear - q->front + 1;  // Size = rear - front + 1
    }
}

int main() {
    struct Queue q;  // Declare a queue variable
    initQueue(&q);  // Initialize the queue

    // Test enqueue operation
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);

    // Test the front element
    printf("Front element is %d\n", front(&q));  // Output: 10

    // Test dequeue operation
    dequeue(&q);
    printf("Front element after dequeue is %d\n", front(&q));  // Output: 20

    // Test the size of the queue
    printf("Queue size is %d\n", size(&q));  // Output: 2

    // Test enqueue when the queue is full
    enqueue(&q, 40);
    enqueue(&q, 50);
    enqueue(&q, 60);  // This will trigger queue overflow

    // Test dequeue when there are elements
    dequeue(&q);
    dequeue(&q);
    dequeue(&q);  // This will trigger queue underflow

    return 0;
}
