#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
#include <stdio.h>

/**
 * struct list_pointer - singly linked list
 * @address: address holder pointer
 * @next: points to the next node
 * Description: linked list node strcture
 */
typedef struct list_pointer
{
	void *address;
	struct list_pointer *next;
} list_p;

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
