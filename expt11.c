#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Number of vertices

// Queue structure for BFS
struct Queue {
    int items[MAX];
    int front, rear;
};

void initQueue(struct Queue* q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(struct Queue* q) {
    return q->front == -1;
}

void enqueue(struct Queue* q, int value) {
    if (q->rear == MAX - 1) {
        printf("Queue is full!\n");
        return;
    }
    if (q->front == -1) q->front = 0;
    q->rear++;
    q->items[q->rear] = value;
}

int dequeue(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty!\n");
        return -1;
    }
    int item = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
        q->front = q->rear = -1;
    }
    return item;
}

// BFS function
void BFS(int graph[MAX][MAX], int start) {
    int visited[MAX] = {0};
    struct Queue q;
    initQueue(&q);

    visited[start] = 1;
    enqueue(&q, start);

    printf("BFS Traversal: ");

    while (!isEmpty(&q)) {
        int current = dequeue(&q);
        printf("%d ", current);

        for (int i = 0; i < MAX; i++) {
            if (graph[current][i] == 1 && !visited[i]) {
                visited[i] = 1;
                enqueue(&q, i);
            }
        }
    }
    printf("\n");
}

// DFS function (recursive)
void DFSUtil(int graph[MAX][MAX], int vertex, int visited[]) {
    visited[vertex] = 1;
    printf("%d ", vertex);

    for (int i = 0; i < MAX; i++) {
        if (graph[vertex][i] == 1 && !visited[i]) {
            DFSUtil(graph, i, visited);
        }
    }
}

void DFS(int graph[MAX][MAX], int start) {
    int visited[MAX] = {0};
    printf("DFS Traversal: ");
    DFSUtil(graph, start, visited);
    printf("\n");
}

// Main function
int main() {
    // Directed graph adjacency matrix
    int graph[MAX][MAX] = {
        {0, 1, 1, 0, 0},
        {0, 0, 0, 1, 0},
        {0, 0, 0, 1, 1},
        {0, 0, 0, 0, 1},
        {0, 0, 0, 0, 0}
    };

    int startVertex = 0;

    BFS(graph, startVertex);
    DFS(graph, startVertex);

    return 0;
}
