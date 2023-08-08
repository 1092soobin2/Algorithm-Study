// (1, 골5) BOJ__10026_적록색약 50~


#include <stdio.h>

// ans: 정상 개수, 적록색약 개수

int N;
char board[100][100];

int main(void) {

	// === input ===
	scanf("%d ", &N);
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++)
			scanf(" %c  ", &board[r][c]);
	}

	printf("왜 느리고 지랄");
	// === algorithm ===
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++)
			printf("%s ", board[r]);
	}

	// === output ===

}