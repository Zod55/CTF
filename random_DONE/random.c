#include <stdio.h>
#include<stdlib.h>
int main(){
	unsigned int random;
	random = rand();	// random value!

	unsigned int key=0;
	scanf("%d", &key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		system("/bin/cat flag");
		return 0;
	}

        printf("%b\n",random);
	printf("Wrong, maybe you should try 2^32 cases     %b.\n",key);
	return 0;
}

