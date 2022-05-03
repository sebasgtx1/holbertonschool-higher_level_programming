#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into
 * a sorted singly linked list
 * @number: number to be inserted
 * @head: a double pointer to the linked list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *save;

	temp = *head;
	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (temp)
	{
		if (temp->n > number)
			break;
		save = temp;
		temp = temp->next;
	}

	if (!*head)
		*head = new;
	else
	{
		new->next = temp;
		if (temp == *head)
			*head = new;
		else
			save->next = new;
	}

	return (new);
}
