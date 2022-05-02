#include "lists.h"
/**
 * free_listp - frees a listint_t list and set the head to NULL
 * @head: pinter to the list to be free it
 * Return: no return
 */
void free_listp(list_p **head)
{
	list_p *headp;

	if (head)
	{
	while ((headp = *head))
	{
		*head = (*head)->next;
		free(headp);
	}
	*head = NULL;
	}
}
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	list_p *a_u = NULL, *a_h = NULL, *a_c = NULL;
	/**
	 * a_u:address updater
	 * a_h: address holder
	 * a_c: address checker
	 */
	while (list)
	{
		a_h = malloc(sizeof(list_p));

		if (!a_h)
		{
			free_listp(&a_h);
			return (0);
		}

		a_h->address = (void *)list;
		a_h->next = a_u;
		a_u = a_h;
		a_c = a_u;

	/**
	 * While for check if a loop exist at this point
	 */
		while (a_c->next)
		{
			a_c = a_c->next;

			if (list == a_c->address)
			{
				free_listp(&a_u);
				return (1);
			}
		}
		list = list->next;
	}
	free_listp(&a_u);
	return (0);
}
