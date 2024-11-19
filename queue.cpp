#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef int Item;
typedef struct queue_type* Queue;

Queue create();
bool is_empty(Queue q);
void terminate(const char* message);
void enqueue(Queue q, Item i);
Item dequeue(Queue q);
void print_queue(Queue q);
void destroy(Queue q);
Item peek(Queue q);

int get_size(Queue q);

struct node {
	Item data;
	struct node* next;
};

struct queue_type {
	struct node* front;
	struct node* rear;
	Item size;
};

Queue create() {
	Queue q = (Queue)malloc(sizeof(struct queue_type));

	if (q == NULL) {
		terminate("Error: queue could not be created. 1");
	}

	q->front = NULL;
	q->rear = NULL;
	q->size = 0;

	return q;
}

void terminate(const char* message) {
	printf("%s", message);
	exit(EXIT_FAILURE);
}

bool is_empty(Queue q) {
	return q->front == NULL;
}

void enqueue(Queue q, Item i) {
	struct node* new_node = (node*)malloc(sizeof(struct node));

	if (new_node == NULL) {
		terminate("Error: enable to allocate memory. 2");
	}

	new_node->data = i;
	new_node->next = NULL;

	if(q->front == NULL) {
		q->front = new_node;
		q->rear = new_node;
	}
	else {
		q->rear->next = new_node;
		q->rear = new_node;
	}
	q->size++;
}

Item dequeue(Queue q) {
	struct node* old_node;
	Item i;

	if (is_empty(q)) {
		terminate("Error: queue is empty.3");
	}

	old_node = q->front;
	i = old_node->data;
	q->front = old_node->next;

	free(old_node);
	q->size--;

	return i;
}

int get_size(Queue q) {
	return q->size;
}

void print_queue(Queue q) {
	struct node* tmp = q->front;

	for (int i = 0; i < q->size; i++) {
		printf("%d", tmp->data);
		tmp = tmp->next;
	}
	printf("\n");
}

void destroy(Queue q) {
	while (!is_empty(q)) {
		dequeue(q);
	}
	q->size = 0;
	free(q);

	printf("All queue have been destroyed\n");
}

int main() {
	Queue q = create();
	enqueue(q, 1);
	enqueue(q, 2);
	enqueue(q, 3);
	printf("queue : ");
	print_queue(q);

	printf("dequeue: %d\n", dequeue(q));
	printf("queue: ");
	print_queue(q);

	destroy(q);

	return 0;
}
