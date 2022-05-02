#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *list_faster;

	list_faster = list;
	while (list && list_faster && list_faster->next)
	{
		list = list->next;
		list_faster = list_faster->next->next;

		if (list == list_faster)
			return (1);
	}

	return (0);
}
