#include <iostream>
#include "LILIST.h"

LILIST::LILIST()
{
	elem = NULL;
}

LILIST::~LILIST()
{
	// You have to implement this area, but do not do it at this time...
	//
	Node* tempPtr;

	while (elem != NULL)
	{
		if (elem->item != -1)
		{
			tempPtr = elem;
			elem = elem->next;
			delete tempPtr;
		}
		else
		{
			Node* temp = elem->sublist;
			while (temp != NULL)
			{
				tempPtr = temp;
				temp = temp->next;
				delete tempPtr;
			}
			tempPtr = elem;
			elem = elem->next;
			delete tempPtr;
		}
	}
}

int	LILIST::isLength(void)
{
	int	length;
	Node* t;

	length = 0;
	t = elem;
	while (t != NULL) {
		length++;
		t = t->next;
	}
	return length;
}

void	LILIST::InsertList(const char* clist)
{
	int	i, j;
	char	str[100];
	Node* list, * node, * t;

	list = NULL;
	i = 0;
	i++;	// skip (
	// Make a linked list
	do {
		j = 0;
		while (isdigit(clist[i]))
		{
			str[j++] = clist[i++];
		}
		str[j] = '\0';
		while (isspace(clist[i]))
			++i;
		int temp = 0;
		for (int k = 0; k < j; k++)
		{
			temp = temp * 10 + int(str[k]) - 48;
		}
		node = new Node;
		node->item = temp;
		node->sublist = NULL;
		node->next = NULL;
		if (list == NULL)
			list = node;
		else
		{
			Node* loc = list;
			while(loc->next != NULL)
				loc = loc->next;
			loc->next = node;
		}



	} while (clist[i] != ')');

	Node* temp = elem;
	t = new Node;
	t->item = -1;
	t->sublist = list;
	while (temp->next != NULL)
		temp = temp->next;
	t->next = temp->next;
	temp->next = t;

}

void	LILIST::InsertItem(int v)
{
	// Implement Here
	Node* insert = new Node;
	insert->item = v;
	insert->next = NULL;
	insert->sublist = NULL;

	if (isLength() == 0)
	{
		insert->sublist = NULL;
		elem = insert;
	}
	else
	{
		Node* temp = elem;
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = insert;
		insert->sublist = NULL;
	}

}

void	LILIST::DeleteItem(int v)
{
	// Implement Here
	//
	Node* location = elem;
	Node* tempLocation;

	// Locate node to be deleted.
	if (v == elem->item)
	{
		tempLocation = location;
		elem = elem->next;		// Delete first node.
	}
	else
	{
		while (!(v == (location->next)->item))
			location = location->next;

		// Delete node at location->next
		tempLocation = location->next;
		location->next = (location->next)->next;
	}
	delete tempLocation;
}

int	LILIST::Sum1()
{
	// Implement Here
	//
	Node* temp = elem;
	int sum = 0;
	for (int i = 0; i < isLength(); i++)
	{
		if (temp->item != -1)
			sum += temp->item;
		temp = temp->next;
	}
	return sum;
}

int	LILIST::Sum2()
{
	// Implement Here
	//
	Node* temp = elem;
	int sum = 0;
	for (int i = 0; i < isLength(); i++)
	{
		if (temp->item != -1)
			sum += temp->item;
		else
		{
			Node* temp2 = temp->sublist;
			while (temp2->next != NULL)
			{
				sum += temp2->item;
				temp2 = temp2->next;
			}
			sum += temp2->item;
		}
		temp = temp->next;
	}
	return sum;
}

void LILIST::PrintRec(Node* t)
{
	while (t != NULL) {
		if (t->sublist != NULL) {
			std::cout << "(";
			PrintRec(t->sublist);
			std::cout << ") ";
		}
		else
			std::cout << t->item << " ";
		t = t->next;
	}
	std::cout << "\b";
}

void	LILIST::Print()
{
	std::cout << "Content: (";
	PrintRec(elem);
	std::cout << ")\n";
}
