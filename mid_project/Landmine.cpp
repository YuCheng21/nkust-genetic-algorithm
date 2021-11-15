#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define A_row 4
#define A_col 4
#define Landmine 2
#define pass_count A_row*A_col-Landmine

//亂數生成地雷位置
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

//顯示 
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

//搜尋 
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
	//指定地雷位置 
//	char A[A_row][A_col] = {{'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}};
//	A[0][0] = '*';
//	A[2][1] = '*';
	
	//隨機生成地雷位置
	char A[A_row][A_col] = {0};
	ScLandmine(A);
	
	char C[A_row][A_col] = {{'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}, {'.','.','.','.'}};
	int count = 0;
	
	printf("總共有 %d 個地雷\n", Landmine);
	printImage(C);
	
	while (count<pass_count) {
		int sc_row = 0, sc_col = 0;
		printf("輸入座標：");
		scanf("%d%d", &sc_row, &sc_col);
		//踩到地雷 
		if (A[sc_row][sc_col] == '*'){
			printf("踩到地雷啦！！！\n");
			break;
		}
		//輸入超出範圍 
		else if (sc_row<0 || sc_col<0 || sc_row>=A_row || sc_col>=A_col) {
			printf("\n請重新輸入：\n");
		}
		//重複輸入 
		else  if (C[sc_row][sc_col] != '.') {
			printf("\n重複輸入請重新輸入：\n");
		}
		else {
			ScInImage(A, C, sc_row, sc_col);
			count++;
			printImage(C);
		}
	}
	if (count == pass_count){
		printf("\n恭喜你避開所有的地雷\n");
		printEndImage(C);
	}	
}
