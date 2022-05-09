#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked
 * list is a palindrome
 * @head: pointer to the list
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *aux1, *aux2;
	int len = 0, i = 0, stop = 0;

	if (!*head)
		return (1);
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	if (len % 2 != 0)
		return (0);
	aux1 = *head;
	aux2 = *head;
	stop = len / 2;
	while (stop != len)
	{
		aux2 = *head;
		for (i = 0; i < len - 1; i++)
		{
			aux2 = aux2->next;
		}
		if (aux1->n != aux2->n)
			return (0);
		aux1 = aux1->next;
		len--;
	}
	return (1);
}
