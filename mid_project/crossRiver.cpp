#include <stdio.h>
#include <stdlib.h>

//顯示 A 存在內容 
void printA (int* A) {
	printf("A：");
	for(int i=0 ; i<4 ; i++){
		printf("%d ", A[i]);
	}
}

//顯示 B 存在內容 
void printB (int* B) {
	printf(" B：");
	for(int i=0 ; i<2 ; i++){
		printf("%d ", B[i]);
	}
}

//顯示 C 存在內容 
void printC (int* C) {
	printf(" C：");
	for(int i=0 ; i<4 ; i++){
		printf("%d ", C[i]);
	}
}

//判斷狀態 
int judgeArray (int *A, int n) {
	int count = 0;
	for(int i=0 ; i<n ; i++){
		count += A[i];
	}
	return count;
}

//交換 
void swap (int *A, int n, int *B, int n1) {
	int a = A[n];
	A[n] = B[n1];
	B[n1] = a;
}

//顯示全部 
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
	printf("Farmer：F, Wolf：W, Goat：G, Vegetable：V\n");
	printAll(A, B, C);
	printf("================================\n");
	printf("A：F W G V  B：     C：F W G V\n");
	
	while(judgeArray(C, 4) != 4) {
		//farmer上船 
		if(A[0]!=0 && judgeArray(A, 4) != 0) {
			swap(B, B_curr, A, A_curr);
			B_curr++;
			printAll(A, B, C);
		}
		//找第一個在 A 的 
		for(i=0 ; A[i]!=1 ; i++);
		A_curr = i;
		
		//不符合規定就找下一個 
		if((A[1]==1&&A[2]==1)||(A[3]==1&&A[2]==1)){
			A_curr++;
			while(A[A_curr] == 0){
				A_curr++;
			}	
		}
		
		//從 A 上船
		swap(B, B_curr, A, A_curr);
		printAll(A, B, C);
		//到 C 下船
		swap(B, B_curr, C, A_curr);
		printAll(A, B, C);
		
		//判斷C是否符合規定
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
				//從 C 上船
				swap(B, B_curr, C, A_curr);
				printAll(A, B, C);
				//到 A 下船
				swap(B, B_curr, A, A_curr);
				printAll(A, B, C);
				
				//找還在 A 的下一個 
				for(i=A_curr+1 ; A[i]!=1 ; i++);
				A_curr = i;
				
				//從 A 上船
				swap(B, B_curr, A, A_curr);
				printAll(A, B, C);
				//到 C 下船
				swap(B, B_curr, C, A_curr);
				printAll(A, B, C);
			}
		}
		
		//若 C 為滿，farmer下船 
		if(judgeArray(C, 4)==3) {
			swap(B, 0, C, 0);
			printAll(A, B, C);
			printf("END\n");
		}
		else
			printf("NEXT Round\n");
	}
}
