#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * print_listint - Prints all the elements of a listint_t list.
 *
 * @h: A pointer to the head of the listint_t list.
 *
 * Return: The number of nodes in the listint_t list.
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;
	/* number of nodes */
	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}


/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 *
 * @head: A pointer to a pointer to the head node of the list.
 * @n: The integer to store in the new node.
 *
 * Return: If memory allocation fails or head is NULL, returns NULL.
 *         Otherwise, returns the address of the new element.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}


/**
 * free_listint - Frees a linked list of integers.
 *
 * @head: Pointer to the head node of the linked list.
 *
 * Return: void.
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
