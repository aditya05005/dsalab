#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define the maximum size of the queue

struct Queue {
    int arr[MAX];
    int front;
    int rear;
};

void initQueue(struct Queue* q) {
    q->front = -1;
    q->rear = -1;
}

int isFull(struct Queue* q) {
    return (q->rear + 1) % MAX == q->front;
}

int isEmpty(struct Queue* q) {
    return q->front == -1;
}

void enqueue(struct Queue* q, int value) {
    if (isFull(q)) {
        printf("Queue Overflow! Cannot enqueue %d\n", value);
    } else {
        if (q->front == -1) {
            q->front = 0;
        }
        q->rear = (q->rear + 1) % MAX;
        q->arr[q->rear] = value;
        printf("Enqueued %d to the queue\n", value);
    }
}

int dequeue(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue Underflow! No elements to dequeue\n");
        return -1;
    } else {
        int dequeuedValue = q->arr[q->front];
        printf("Dequeued %d from the queue\n", dequeuedValue);
        if (q->front == q->rear) {
            q->front = -1;
            q->rear = -1;
        } else {
            q->front = (q->front + 1) % MAX;
        }
        return dequeuedValue;
    }
}

int front(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty! No front element\n");
        return -1;
    } else {
        return q->arr[q->front];
    }
}

int size(struct Queue* q) {
    if (isEmpty(q)) {
        return 0;
    } else {
        if (q->rear >= q->front) {
            return q->rear - q->front + 1;
        } else {
            return (MAX - q->front) + (q->rear + 1);
        }
    }
}

int main() {
    struct Queue q;
    initQueue(&q);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);

    printf("Front element is %d\n", front(&q));

    dequeue(&q);
    printf("Front element after dequeue is %d\n", front(&q));

    enqueue(&q, 40);
    enqueue(&q, 50);
    enqueue(&q, 60);

    printf("Queue size is %d\n", size(&q));

    dequeue(&q);
    dequeue(&q);

    enqueue(&q, 70);
    enqueue(&q, 80);

    printf("Queue size is %d\n", size(&q));

    return 0;
}
