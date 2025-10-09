#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SONGS 5
#define MAX_NAME 50

// Node structure for queue
struct Node {
    char songName[MAX_NAME];
    struct Node* next;
};

// Queue front and rear pointers
struct Node* front = NULL;
struct Node* rear = NULL;

// Current song pointer
char currentSong[MAX_NAME] = "None";

// Function to enqueue a song
void enqueue(char* song) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    strcpy(newNode->songName, song);
    newNode->next = NULL;

    if (rear == NULL) {
        front = rear = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }

    printf("Added \"%s\" to queue.\n", song);
}

// Function to dequeue (play next song)
void nextSong() {
    if (front == NULL) {
        printf("Queue is empty! No more songs to play.\n");
        strcpy(currentSong, "None");
        return;
    }

    struct Node* temp = front;
    strcpy(currentSong, front->songName);
    front = front->next;

    if (front == NULL) {
        rear = NULL;
    }

    free(temp);
    printf("Now playing: %s\n", currentSong);
}

// Display available songs
void displayAvailableSongs(char songs[][MAX_NAME]) {
    printf("\nAvailable Songs:\n");
    for (int i = 0; i < MAX_SONGS; i++) {
        printf("  %d. %s\n", i + 1, songs[i]);
    }
}

// Display current queue
void displayQueue() {
    struct Node* temp = front;
    printf("\nSongs in Queue:\n");
    if (temp == NULL) {
        printf("  (Queue is empty)\n");
    } else {
        while (temp != NULL) {
            printf("  - %s\n", temp->songName);
            temp = temp->next;
        }
    }
}

// Display current song
void displayCurrentSong() {
    printf("\nCurrently Playing: %s\n", currentSong);
}

// Main function
int main() {
    char songs[MAX_SONGS][MAX_NAME] = {
        "Blinding Lights",
        "Levitating",
        "Stay",
        "Heat Waves",
        "Save Your Tears"
    };

    char input[100];
    int choice;

    printf("🎵 Welcome to the Mock Music Player 🎵\n");

    while (1) {
        displayAvailableSongs(songs);
        displayCurrentSong();
        displayQueue();

        printf("\nOptions:\n");
        printf("  1. Add song to queue\n");
        printf("  2. Next song\n");
        printf("  3. Exit\n");
        printf("Enter your choice: ");
        fgets(input, sizeof(input), stdin);

        if (strncmp(input, "1", 1) == 0) {
            printf("Enter song number (1-%d): ", MAX_SONGS);
            fgets(input, sizeof(input), stdin);
            choice = atoi(input);

            if (choice >= 1 && choice <= MAX_SONGS) {
                enqueue(songs[choice - 1]);
            } else {
                printf("Invalid song number.\n");
            }

        } else if (strncmp(input, "2", 1) == 0 || strncmp(input, "next", 4) == 0) {
            nextSong();

        } else if (strncmp(input, "3", 1) == 0 || strncmp(input, "exit", 4) == 0) {
            printf("Exiting the music player. Goodbye!\n");
            break;

        } else {
            printf("Invalid input. Try again.\n");
        }
    }

    // Clean up any remaining nodes
    while (front != NULL) {
        nextSong();
    }

    return 0;
}
