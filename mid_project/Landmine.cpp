#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define A_row 4
#define A_col 4
#define Landmine 2
#define pass_count A_row*A_col-Landmine

//�üƥͦ��a�p��m
void  ScLandmine (char A[A_row][A_col]) {
	int i=0;
	srand(time(NULL));
	while (i<Landmine) {
		int j, k;
		j = (rand()%A_row);
		k = (rand()%A_col);
		A[j][k] = '*';
		i++;
	}
}

//��� 
void printImage(char A[A_row][A_col]) {
	for(int i=0 ; i<A_row ; i++) {
		for(int j=0 ; j<A_col ; j++) {
			printf("%c ", A[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void printEndImage(char A[A_row][A_col]) {
	for(int i=0 ; i<A_row ; i++) {
		for(int j=0 ; j<A_col ; j++) {
			if (A[i][j] == '.')
				A[i][j] = '*';
			printf("%c ", A[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

//�j�M 
void ScInImage(char A[A_row][A_col], char C[A_row][A_col],int row, int col) {
	int count = 0;
	for (int i=row-1 ; i<row+2 ; i++) {
		for (int j=col-1 ; j<col+2 ; j++) {
			if (i>=0 && j>=0 && i<A_row && j<A_col) {
				if (A[i][j] == '*') 
					count++;
			}
			
		}
	}
	C[row][col] = count+'0';
}


main() {
	//���w�a�p��m 
//	char A[A_row][A_col] = {{'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}};
//	A[0][0] = '*';
//	A[2][1] = '*';
	
	//�H���ͦ��a�p��m
	char A[A_row][A_col] = {0};
	ScLandmine(A);
	
	char C[A_row][A_col] = {{'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}};
	int count = 0;
	
	printf("�`�@�� %d �Ӧa�p\n", Landmine);
	printImage(C);
	
	while (count<pass_count) {
		int sc_row = 0, sc_col = 0;
		printf("��J�y�СG");
		scanf("%d%d", &sc_row, &sc_col);
		//���a�p 
		if (A[sc_row][sc_col] == '*'){
			printf("���a�p�աI�I�I\n");
			break;
		}
		//��J�W�X�d�� 
		else if (sc_row<0 || sc_col<0 || sc_row>=A_row || sc_col>=A_col) {
			printf("\n�Э��s��J�G\n");
		}
		//���ƿ�J 
		else  if (C[sc_row][sc_col] != '.') {
			printf("\n���ƿ�J�Э��s��J�G\n");
		}
		else {
			ScInImage(A, C, sc_row, sc_col);
			count++;
			printImage(C);
		}
	}
	if (count == pass_count){
		printf("\n���ߧA�׶}�Ҧ����a�p\n");
		printEndImage(C);
	}	
}
