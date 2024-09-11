#include "lists.h"


/**
 * check_cycle - checks if a linked list contains a cycle
 * @list : linked list to check
 * Return: 1 if the list has a cycle or 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	for (; fast != NULL && fast->next != NULL; slow = slow->next, fast = fast->next->next)
	{
		if (slow == fast)
			return (1);
	}
	return (0);
}
