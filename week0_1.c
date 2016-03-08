int function(int x, int array[], int length) 
{
	int num = 0;
	int i = 0;
	qsort(array, length, sizeof(int), mycomp);
	for(i; i <= length; i++)
	{
		x -= array[i];
		if(x < 0)
			break;
		num++;
	}
	return num;
}

int mycomp(const void * p1, const void * p2)
{
	const int * a1 = (const int *) p1;
  	const int * a2 = (const int *) p2;
  	if (*a1 < *a2)
    		return -1;
  	else if (*a1 == *a2)
    		return 0;
  	else
    		return 1;
}
