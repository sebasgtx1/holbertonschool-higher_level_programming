#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into
 * a sorted singly linked list
 * @number: number to be inserted
 * @head: a double pointer to the linked list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *save, *new;

	temp = *head;
	save = *head;
	save = save->next;
	new = malloc(sizeof(listint_t));
	while (temp)
	{
		if (temp->n < number && save->n < number && save != NULL)
		{
			save = save->next;
		}
		else
		{
			new->n = number;
			new->next = save;
			temp->next = new;
			break;
		}
		temp = temp->next;
	}
	return (*head);
}
