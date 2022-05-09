#include "lists.h"
#include <stdio.h>
/**
 * second_half - extract the second half of a list
 * @aux2: list
 * @len: list lenght
 * Return: no return
 */
void second_half(listint_t **aux2, int len)
{
	listint_t *prev;
	listint_t *current;
	listint_t *next;
	int i = 0;

	prev = NULL;
	for (; i < len / 2; i++)
		*aux2 = (*aux2)->next;
	current = *aux2;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*aux2 = prev;
}
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
	int len = 0;

	if (!*head)
		return (1);
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	aux1 = *head;
	aux2 = *head;
	second_half(&aux2, len);
	while (aux2)
	{
		if (aux1->n != aux2->n)
			return (0);
		aux1 = aux1->next;
		aux2 = aux2->next;
	}
	return (1);
}
