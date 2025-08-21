#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>  // for isalpha (to check operands)

// ----- Stack implementation -----
#define MAX 100

typedef struct {
    char items[MAX];
    int top;
} Stack;

void initStack(Stack *s) {
    s->top = -1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

int isFull(Stack *s) {
    return s->top == MAX - 1;
}

void push(Stack *s, char c) {
    if (!isFull(s)) {
        s->items[++s->top] = c;
    }
}

char pop(Stack *s) {
    if (!isEmpty(s)) {
        return s->items[s->top--];
    }
    return '\0'; // return null char if empty
}

char peek(Stack *s) {
    if (!isEmpty(s)) {
        return s->items[s->top];
    }
    return '\0';
}

// ----- Helper functions -----
int precedence(char op) {
    switch (op) {
        case '+':
        case '-': return 1;
        case '*':
        case '/': return 2;
        default:  return 0;
    }
}

// ----- Infix to Postfix -----
void infixToPostfix(char infix[], char postfix[]) {
    Stack s;
    initStack(&s);
    int i = 0, k = 0;

    while (infix[i] != '\0') {
        char token = infix[i];

        // If operand, add to postfix
        if (isalpha(token)) {
            postfix[k++] = token;
        }
        // If '(', push to stack
        else if (token == '(') {
            push(&s, token);
        }
        // If ')', pop until '('
        else if (token == ')') {
            while (!isEmpty(&s) && peek(&s) != '(') {
                postfix[k++] = pop(&s);
            }
            pop(&s); // discard '('
        }
        // If operator
        else {
            while (!isEmpty(&s) && precedence(peek(&s)) >= precedence(token)) {
                postfix[k++] = pop(&s);
            }
            push(&s, token);
        }
        i++;
    }

    // Pop remaining operators
    while (!isEmpty(&s)) {
        postfix[k++] = pop(&s);
    }
    postfix[k] = '\0'; // null terminate
}

int main() {
    char infix[MAX], postfix[MAX];

    printf("Enter an infix expression (use single letters like A+B*C without space): \n");
    scanf("%s", infix);

    infixToPostfix(infix, postfix);

    printf("Postfix expression: %s\n", postfix);

    return 0;
}
