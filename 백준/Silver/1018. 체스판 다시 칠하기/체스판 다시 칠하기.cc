#include <iostream>
using namespace std;

char arr[51][51];
char reshiram[8][8] = {
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
};
char zekrom[8][8] = {
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
};

int ReshiramPattern(int r, int c) {
	int res = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (arr[i + r][j + c] != reshiram[i][j]) 
				res++;
		}
	}
	return res;
}
int ZekromPattern(int r, int c) {
	int res = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (arr[i + r][j + c] != zekrom[i][j])
				res++;
		}
	}
	return res;
}

int main(void)
{
	int row, column; cin >> row >> column;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < column; j++) 
			cin >> arr[i][j];
	}

	int min = 65, re, ze;
	for (int i = 0; i <= row - 8; i++) {
		for (int j = 0; j <= column - 8; j++) {
			re = ReshiramPattern(i, j);
			ze = ZekromPattern(i, j);
			if (re < ze) min = (re < min ? re : min);
			else min = (ze < min ? ze : min);
		}
	}

	cout << min;

	return 0;
}