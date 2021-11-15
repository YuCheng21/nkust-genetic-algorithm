#include <stdio.h>
#include <stdlib.h>

//��� A �s�b���e 
void printA (int* A) {
	printf("A�G");
	for(int i=0 ; i<4 ; i++){
		printf("%d ", A[i]);
	}
}

//��� B �s�b���e 
void printB (int* B) {
	printf(" B�G");
	for(int i=0 ; i<2 ; i++){
		printf("%d ", B[i]);
	}
}

//��� C �s�b���e 
void printC (int* C) {
	printf(" C�G");
	for(int i=0 ; i<4 ; i++){
		printf("%d ", C[i]);
	}
}

//�P�_���A 
int judgeArray (int *A, int n) {
	int count = 0;
	for(int i=0 ; i<n ; i++){
		count += A[i];
	}
	return count;
}

//�洫 
void swap (int *A, int n, int *B, int n1) {
	int a = A[n];
	A[n] = B[n1];
	B[n1] = a;
}

//��ܥ��� 
void printAll (int* A, int* B, int* C) {
	printA(A);
	printB(B);
	printC(C);
	printf("\n");
}

main() {
	int A[4] = {1, 1, 1, 1}, B[2] = {0}, C[4] = {0};
	int i, A_curr = 0, B_curr = 0;
	
	printf("Initial State\n");
	printf("Farmer�GF, Wolf�GW, Goat�GG, Vegetable�GV\n");
	printAll(A, B, C);
	printf("================================\n");
	printf("A�GF W G V  B�G     C�GF W G V\n");
	
	while(judgeArray(C, 4) != 4) {
		//farmer�W�� 
		if(A[0]!=0 && judgeArray(A, 4) != 0) {
			swap(B, B_curr, A, A_curr);
			B_curr++;
			printAll(A, B, C);
		}
		//��Ĥ@�Ӧb A �� 
		for(i=0 ; A[i]!=1 ; i++);
		A_curr = i;
		
		//���ŦX�W�w�N��U�@�� 
		if((A[1]==1&&A[2]==1)||(A[3]==1&&A[2]==1)){
			A_curr++;
			while(A[A_curr] == 0){
				A_curr++;
			}	
		}
		
		//�q A �W��
		swap(B, B_curr, A, A_curr);
		printAll(A, B, C);
		//�� C �U��
		swap(B, B_curr, C, A_curr);
		printAll(A, B, C);
		
		//�P�_C�O�_�ŦX�W�w
		if(!(C[1]==1&&C[2]==1&&C[3]==1)){
			if((C[1]==1&&C[2]==1)||(C[3]==1&&C[2]==1)) {
				while(1){
					if((C[1]==1&&C[2]==1)||(C[3]==1&&C[2]==1)){
						A_curr++;
						if (C[A_curr] != 0)
							break;
					}
					break;
				}
				printf("Change\n");
				//�q C �W��
				swap(B, B_curr, C, A_curr);
				printAll(A, B, C);
				//�� A �U��
				swap(B, B_curr, A, A_curr);
				printAll(A, B, C);
				
				//���٦b A ���U�@�� 
				for(i=A_curr+1 ; A[i]!=1 ; i++);
				A_curr = i;
				
				//�q A �W��
				swap(B, B_curr, A, A_curr);
				printAll(A, B, C);
				//�� C �U��
				swap(B, B_curr, C, A_curr);
				printAll(A, B, C);
			}
		}
		
		//�Y C �����Afarmer�U�� 
		if(judgeArray(C, 4)==3) {
			swap(B, 0, C, 0);
			printAll(A, B, C);
			printf("END\n");
		}
		else
			printf("NEXT Round\n");
	}
}
