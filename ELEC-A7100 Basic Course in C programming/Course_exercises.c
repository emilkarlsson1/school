#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stddef.h>
#include <stdlib.h>
/*
double vectorlength(double x, double y, double z) {

	double a = pow(x, 2);
	double b = pow(y, 2);
	double c = pow(z, 2);

	double d = a + b + c;
	double e = sqrt(d);
	return e;
}

int simple_multiply(void) {

	int a, b;
	int ret;
	ret = scanf("%d %d", &a, &b);

	int d = a * b;
	printf("%d" " * " "%d" " = %d\n", a, b, d);
	return 0;
}

float simple_math(void) {

	float luku1, luku2;
	char merkki = 0;
	int ret = scanf("%f %c %f", &luku1, &merkki, &luku2);

	float f1 = luku1 * luku2;
	float f2 = luku1 / luku2;
	float f3 = luku1 - luku2;
	float f4 = luku1 + luku2;

	if (merkki == '+')
		printf("%.1f\n", f4);
	else if (merkki == '-')
		printf("%.1f\n", f3);
	else if (merkki == '*')
		printf("%.1f\n", f1);
	else if (merkki == '/')
		printf("%.1f\n", f2);
	else
		printf("ERR\n");
	return 0;
}

int array_sum(int* array, int count) {
	int i = 0;
	int a = 0;
	while (i < count) {

		a += array[i];
		i++;
	}
	return a;

}

unsigned int array_reader(int* vals, int n) {

	int a = 0;
	int i = 0;
	int ret = 0;
	for (i; i < n;) {
		ret = scanf("%d\t ", &a);

		if (ret == 1) {

			vals[i] = a;
		}
		else {

			return i;
		}

		i++;
	}
	return n;

}

unsigned int arraylen(const char* array) {
	int i = 0;
	int a = 0;
	while (array[i] != 0) {
		i++;
		a++;
	}
	//printf("%d", a);
	return a;
}

void countchars(const char* array, unsigned int* counts) {
	int i = 0;

	for (i; i < arraylen(array); i++) {
		switch (array[i]) {
		case 'a':
			counts['a'] += 1;
			break;
		case 'b':
			counts['b'] += 1;
			break;
		case 'c':
			counts['c'] += 1;
			break;
		case 'd':
			counts['d'] += 1;
			break;
		case 'e':
			counts['e'] += 1;
			break;
		case 'f':
			counts['f'] += 1;
			break;
		case 'g':
			counts['g'] += 1;
			break;
		case 'h':
			counts['h'] += 1;
			break;
		case 'i':
			counts['i'] += 1;
			break;
		case 'j':
			counts['j'] += 1;
			break;
		case 'k':
			counts['k'] += 1;
			break;
		case 'l':
			counts['l'] += 1;
			break;
		case 'm':
			counts['m'] += 1;
			break;
		case 'n':
			counts['n'] += 1;
			break;
		case 'o':
			counts['o'] += 1;
			break;
		case 'p':
			counts['p'] += 1;
			break;
		case 'q':
			counts['q'] += 1;
			break;
		case 'r':
			counts['r'] += 1;
			break;
		case 's':
			counts['s'] += 1;
			break;
		case 't':
			counts['t'] += 1;
			break;
		case 'u':
			counts['u'] += 1;
			break;
		case 'v':
			counts['v'] += 1;
			break;
		case 'w':
			counts['w'] += 1;
			break;
		case 'x':
			counts['x'] += 1;
			break;
		case 'y':
			counts['y'] += 1;
			break;
		case 'z':
			counts['z'] += 1;
			break;
		case 'A':
			counts['A'] += 1;
			break;
		case 'B':
			counts['B'] += 1;
			break;
		case 'C':
			counts['C'] += 1;
			break;
		case 'D':
			counts['D'] += 1;
			break;
		case 'E':
			counts['E'] += 1;
			break;
		case 'F':
			counts['F'] += 1;
			break;
		case 'G':
			counts['G'] += 1;
			break;
		case 'H':
			counts['H'] += 1;
			break;
		case 'I':
			counts['I'] += 1;
			break;
		case 'J':
			counts['J'] += 1;
			break;
		case 'K':
			counts['K'] += 1;
			break;
		case 'L':
			counts['L'] += 1;
			break;
		case 'M':
			counts['M'] += 1;
			break;
		case 'N':
			counts['N'] += 1;
			break;
		case 'O':
			counts['O'] += 1;
			break;
		case 'P':
			counts['P'] += 1;
			break;
		case 'Q':
			counts['Q'] += 1;
			break;
		case 'R':
			counts['R'] += 1;
			break;
		case 'S':
			counts['S'] += 1;
			break;
		case 'T':
			counts['T'] += 1;
			break;
		case 'U':
			counts['U'] += 1;
			break;
		case 'V':
			counts['V'] += 1;
			break;
		case 'W':
			counts['W'] += 1;
			break;
		case 'X':
			counts['X'] += 1;
			break;
		case 'Y':
			counts['Y'] += 1;
			break;
		case 'Z':
			counts['Z'] += 1;
			break;

		case '0':

			break;

		}

	}




}

void sort(int* start, int size) {
	int b;
	int i = 0;
	int a = 0;
	int min;

	for (i; i < size; i++) {
		min = i;

		for (a = i + 1; a < size; a++) {
			if (start[a] < start[min])
				min = a;
			//printf("a");
		}
		//printf("b");
		b = start[i];
		//printf("c");
		start[i] = start[min];
		//printf("d");
		start[min] = b;
	}
	//for (int e = 0; e < size; e++) {
		//printf("%d\n", start[e]);
	//}
}

int count_isalpha(const char* str) {

	int i = 0;
	int a = 0;
	while (str[i]) {
		if (isalpha(str[i])) {
			a++;
		}
		i++;
	}

	return a;
}

void addname(char* buffer, const char* addme, unsigned int maxsize) {


	int b = strlen(buffer);
	int c = strlen(addme);
	int yht = b + c;
	int d = maxsize - b;

	if (b < maxsize) {
		strncat(buffer, addme, d - 1);
		if (yht < maxsize) {
			strcat(buffer, ",");
		}
	}




}

int num_substr(const char* str, const char* sub) {
	int i = 0;
	//printf("%s", str);
	while ((str = strstr(str, sub)) != NULL) {
		i++;
		str += strlen(sub);

		//printf("%d\n", i);

	}

	printf("%d", i);

	return i;
}

char* my_toupper(char* dest, const char* src) {

	//printf("%s", src);
	int b = strlen(src);
	int i = 0;
	int a = 0;
	while (i < b) {
		if (src[i] == '?') {
			dest[i + a] = '!';
			i++;
		}
		else if (src[i] == '.') {
			dest[i + a] = '!';
			dest[i + a + 1] = '!';
			dest[i + a + 2] = '!';
			i++;
			a += 2;
			//printf("%d\t", i);
		}
		else if (src[i] == '\0') {
			break;

		}
		else {
			dest[i + a] = toupper(src[i]);
			i++;
			//printf("%d\n", i);
		}

		dest[i + a] = '\0';
	}


	//printf("%s", dest);
	//printf("%d", strlen(dest));
	//strchr(dest, src[i]);
	return dest;
}

void qstr_print(const char* s) {
	int i = 0;

	while (1) {
		if (s[i] != '?') {
			printf("%c", s[i]);
			i++;
		}
		else {
			break;
		}
	}


}

unsigned int qstr_length(const char* s) {
	int i = 0;

	while (1) {
		if (s[i] != '?') {

			i++;
		}
		else {
			break;
		}
	}
	//printf("%d", i);
	return i;
}

int qstr_cat(char* dst, const char* src) {

	int i = 0;
	int a = 0;

	while (dst[i] != '?') {
		i++;
	}

	while (src[a] != '?') {

		dst[i] = src[a];
		//printf("%s\n", dst);
		i++;
		a++;
	}

	dst[i] = '?';
	//printf("%d\t", i);
	return i;

}

const char* qstr_strstr(const char* str1, const char* str2) {

	int i = 0;
	int a = 0;

	while (str1[i] != '?') {
		if (str2[a] == str1[i]) {
			i++;
			a++;

			if (str2[a] == '?') {
				break;
			}
		}
		else if (str2[a] != str1[i]) {

			a = 0;
			i++;

		}
	}
	int c = i - a;

	if (str2[a] == '?') {
		//printf("%c", str1[i-a]);
		return &str1[c];
	}
	else {
		//printf("NULL");
		return NULL;
	}

}

int* create_dyn_array(unsigned int n) {

	int* lista;
	lista = (int*)malloc((n) * sizeof(int));

	unsigned int i = 0;
	while (i < n) {
		scanf("%d", &lista[i]);
		i++;
	}

	return lista;

}

int* add_dyn_array(int* arr, unsigned int num, int newval) {

	int i = num + 1;
	arr = realloc(arr, (sizeof(int) * i));

	if (arr != NULL) {
		arr[i - 1] = newval;

	}


	return arr;

}

int* join_arrays(unsigned int m_a, const int* a, unsigned int m_b, const int* b, unsigned int m_c, const int* c) {

	int sum = m_a + m_b + m_c + 3;
	unsigned int i = 0;
	unsigned int q = 0;
	unsigned int e = 0;
	int* array;
	array = (int*)malloc((sum) * sizeof(int));

	while (1) {

		if (i < m_a) {

			array[i] = a[i];
			i++;
		}
		else if (e < m_b) {

			array[i + e] = b[e];
			e++;
		}
		else if (q < m_c) {

			array[q + e + i] = c[q];
			q++;
		}
		else {
			break;
		}
	}
	return array;
}

char* delete_comments(char* input) {

	char* arr;
	int a = strlen(input);
	a += 1;
	arr = (char*)malloc(a * sizeof(char));

	char* arr2;
	arr2 = arr;

	int i = 0;
	int c = 0;

	while (input[i] != '\0') {

		if (input[i] == '/' && input[i + 1] == '*') {
			i += 2;			// hyppää  yli
			while (input[i] != '*' || input[i + 1] != '/') {
				i++;
			}
			i += 2;			// hyppää  yli
		}
		else if (input[i] == '/' && input[i + 1] == '/') {
			i += 2;
			while (input[i] != '\n') {
				i++;
			}
			i++;			// hyppää \n yli
		}
		else {
			arr[c] = input[i];
			i++;
			c++;
		}
	}
	arr[c] = '\0';


	arr = arr2;
	free(input);


	return arr;


}


struct studentqueue {
	char* name;  // Name of student (dynamically allocated)
	struct studentqueue* next;  // pointer to next student
};

int enqueue(struct studentqueue* q, const char* name) {
	struct studentqueue* uusi;
	struct studentqueue* toinen;
	uusi = malloc(sizeof(struct studentqueue));
	

	if (uusi != NULL) {
		strcpy(uusi->name, name);
		uusi->next = NULL;
		toinen = q;

		for (; toinen->next != NULL;) {
			toinen = toinen->next;
		}

		toinen->next = uusi;
		return 1;
	}
	else {
		return 0;
	}
}

int dequeue(struct studentqueue* q, char* buffer, unsigned int size) {

	struct studentqueue* b;

	if (q->next == NULL) {
		return 0;
	}
	else {
		unsigned int i = strlen(q->next->name);

		if (i < (size - 1)) {
			memmove(buffer, q->next->name, i);
		}
		else {
			memmove(buffer, q->next->name, (size - 1));
		}
		b = q->next;

		q->next = b->next;
		free(b->name);
		free(b);

		return 1;
	}

}


enum num_seats {
	BIKE = 1,
	MOTORCYCLE = 2,
	VAN = 3,
	CAR = 5,
	MINIVAN = 7
};


char** allocate_memory(int* xdim, int ydim) {
	char** taulukko;
	int i = 0;
	int j = 0;

	taulukko = calloc((ydim + 1), sizeof(char**));

	while (i < ydim) {
		taulukko[i] = malloc(xdim[i] * sizeof(char*));
		while (j < xdim[j]) {
			taulukko[i][j] = i + j;
			j++;
		}
		i++;
	}

	return taulukko;
}

void free_array(char** w, int ydim) {

	int i = 0;
	while (i < ydim) {
		free(w[i]);
		i++;
	}
	free(w);

}

	8.4.

const unsigned char luvut[8] = { 0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01};
const unsigned char luvut2[8] = { 0x7f, 0xbf, 0xdf, 0xef, 0xf7, 0xfb, 0xfd, 0xfe};

void op_bit_set(unsigned char* data, int i)
{


	int bit = i % 8;
	int alkio = i / 8;
	

	data[alkio] |= luvut[bit];

}



void op_bit_unset(unsigned char* data, int i)
{
	int bit = i % 8;
	int alkio = i / 8;
	
	data[alkio] &= luvut2[bit];
}



int op_bit_get(const unsigned char* data, int i)
{
	int bit = i % 8;
	int alkio = i / 8;
	//printf("%d \t %d\n", bit, alkio);
	//printf("%s\n", data[alkio]);

	if (data[alkio] & luvut[bit]) {
		return 1;
	}
	else {
		return 0;
	}
}



void op_print_byte(unsigned char b)
{
	int i = 7;
	int a = 0;
	while (i >= 0) {
		if (b & (luvut[a])) {
			printf("1");
			i--;
			a++;
		}
		else {
			printf("0");
			i--;
			a++;
		}
	}

}



unsigned char op_bit_get_sequence(const unsigned char* data, int i, int how_many)
{

	unsigned char luku[1] = { 0 };
	int a = 0;
	int v = 0;
	while (a <= how_many) {
		if (op_bit_get(data, (i + a)) ^ 0) {
			op_bit_set(luku, (v));
			a++;
			v++;
		
		}
		else if (op_bit_get(data, (i + a)) ^ 1) {
			a++;
			v++;
			

		}
	}
	unsigned char luku2 = luku[0];
	
	if (how_many < 8) {
		int koko = 8 - how_many;
		luku2 = luku2 >> koko;
		
	}
	return luku2;
}

	7.5.

GameArea* createGameArea(unsigned int x_size, unsigned int y_size) {

	GameArea* new = (GameArea*)malloc(sizeof(GameArea));
	new->y_size = y_size;
	new->x_size = x_size;

	unsigned int i = 0;
	unsigned int j = 0;

	new->cells = malloc((y_size + 3) * sizeof(CellStatus*));

	while (i < y_size) {
		new->cells[i] = calloc((x_size + 1), sizeof(CellStatus*));
		while (j < x_size) {

			new->cells[i][j] = DEAD;
			j++;
		}
		i++;
	}
	return new;
}


void releaseGameArea(GameArea* a) {
	unsigned int i = 0;

	while (a->y_size > i) {
		free(a->cells[i]);
		i++;

	}
	free(a->cells);
	free(a);
}


void initGameArea(GameArea* a, unsigned int n) {

	unsigned int j = 0;


	while (j < n) {
		int y = (rand() % a->y_size);
		int x = (rand() % a->x_size);
		if (a->cells[y][x] == DEAD) {
			a->cells[y][x] = ALIVE;
			j++;
			continue;
		}
		else {
			continue;
		}
	}

}

void printGameArea(const GameArea* a) {
	unsigned int j = 0;
	unsigned int i = 0;
	while (i < a->y_size) {
		while (j < a->x_size) {
			if (a->cells[i][j] == DEAD) {
				printf(".");
				j++;
			}
			else if (a->cells[i][j] == ALIVE) {
				printf("*");
				j++;
			}
		}
		i++;
		j = 0;
		printf("\n");


	}
}

unsigned int live_neighbours(const GameArea* a, unsigned int x, unsigned int y) {

	int xkoko = a->x_size;
	int ykoko = a->y_size;
	unsigned int count = 0;
	for (int b = -1; b < 2; b++) {
		int yy = y + b;
		for (int i = -1; i < 2; i++) {
			int xx = x + i;
			if (xx >= 0 && yy >= 0 && xx < xkoko && yy < ykoko) {
				if (a->cells[yy][xx] == ALIVE) {
					count++;

				}

			}
		}
	}
	if (a->cells[y][x] == ALIVE) {
		count--;
	}
	return count;
}


void gameTick(GameArea* a) {

	GameArea* new = createGameArea(a->x_size, a->y_size);

	unsigned int j = 0;
	unsigned int i = 0;

	while (i < a->y_size) {
		while (j < a->x_size) {
			if (live_neighbours(a, j, i) < 2 && a->cells[i][j] == ALIVE) {
				new->cells[i][j] = DEAD;
				j++;
			}
			else if ((live_neighbours(a, j, i) == 2 || live_neighbours(a, j, i) == 3) && a->cells[i][j] == ALIVE) {
				new->cells[i][j] = ALIVE;
				j++;
			}
			else if (live_neighbours(a, j, i) > 3 && a->cells[i][j] == ALIVE) {
				new->cells[i][j] = DEAD;
				j++;
			}
			else if (live_neighbours(a, j, i) == 3 && a->cells[i][j] == DEAD) {
				new->cells[i][j] = ALIVE;
				j++;
			}
			else {
				new->cells[i][j] = a->cells[i][j];
				j++;
			}



		}

		j = 0;
		i++;
	}

	for (unsigned int b = 0; b < a->y_size; b++) {
		for (unsigned int c = 0; c < a->x_size; c++) {
			a->cells[b][c] = new->cells[b][c];
		}
	}

	releaseGameArea(new);
}


8.5.

int getSourcePort(const unsigned char* tcp_hdr)
{
	int a = tcp_hdr[1];
	int b = tcp_hdr[0];
	int c = (b<<8) | a;
	//printf("a:%d  b:%d   c:%d\n",a,b, c );

	return c;

}

int getDestinationPort(const unsigned char* tcp_hdr)
{
	int a = tcp_hdr[3];
	int b = tcp_hdr[2];
	int c = (b << 8) | a;
	//printf("a:%d  b:%d   c:%d\n",a,b, c );

	return c;
}

void setSourcePort(unsigned char* tcp_hdr, int port)
{
	unsigned char e = 0x00;
	int a = port << 24;
	a = a >> 24;
	unsigned char  c = a | e;
	int b = port >> 8;
	b = b << 24;
	b = b >> 24;
	unsigned char d = b | e;
	tcp_hdr[0] = d;
	tcp_hdr[1] = c;

}

void setDestinationPort(unsigned char* tcp_hdr, int port)
{

	unsigned char e = 0x00;
	int a = port << 24;
	a = a >> 24;
	unsigned char  c = a | e;
	int b = port >> 8;
	b = b << 24;
	b = b >> 24;
	unsigned char d = b | e;
	tcp_hdr[2] = d;
	tcp_hdr[3] = c;
}

int getAckFlag(const unsigned char* tcp_hdr)
{
	unsigned char a = tcp_hdr[13] & 16;
	if (a == 0) {
		return 0;
	}
	else {
		return 1;
	}
}

void setAckFlag(unsigned char* tcp_hdr, int flag)
{
	if (flag > 0) {
		tcp_hdr[13] = tcp_hdr[13] | 16;
	}
	else {
		tcp_hdr[13] = tcp_hdr[13] & (~16);

	}
}

int getDataOffset(const unsigned char* tcp_hdr)
{
	unsigned char a = 0x0;
	return (tcp_hdr[12] >> 4) |( a );
}

void setDataOffset(unsigned char* tcp_hdr, int offset)
{
	unsigned char a = 0xF;
	unsigned char c = (offset << 4);
	tcp_hdr[12] &= a;
	tcp_hdr[12] = tcp_hdr[12] | c;

}


8.6.

void confidentiality_xor(uint32_t key, void* data, int len)
{
	unsigned int *a = data;
	for (int i = 0; i < len; i++) {
		a[i] = a[i] ^ key;

	}
	data = a;
}


void confidentiality_xor_shift(uint32_t key, void* data, int len)
{
	unsigned int* a = data;
	uint32_t key_uusi = key;
	uint32_t avain = key_uusi;

	for (int i = 0; i < len; i++) {
		uint32_t b;
		uint32_t c;

		a[i] = a[i] ^avain ;


		b = avain >> 31;
		c = avain <<= 1;
		avain = c | b;

	}
	data = a;
}




9.3.




int line_count(const char* filename)
{
	int count = 0;
	FILE* f = fopen(filename, "r");
	if (f == NULL) {
		return -1;
	}

	int a;
	int rivi = 0;
	while (1) {

		a = fgetc(f);
		if (feof(f)) {
			break;
		}
		if (a == '\n') {
			count++;
			rivi = 0;
		}
		else {
			rivi++;
		}
	}

	if (count == 0) {
		if ((rivi) > 0) {
			count++;

		}
	}
	else if (count != 0) {
		if (rivi > 0) {
			count++;
		}
	}

	fclose(f);
	return count;
}



int word_count(const char* filename)
{
	FILE* f = fopen(filename, "r");
	if (f == NULL) {
		return -1;
	}

	int count = 0;
	int a;

	while ((a = fgetc(f)) != EOF) {

		if (isalpha(a)) {
			while (1) {
				int b = fgetc(f);
				if (isspace(b)) {
					count++;
					break;
				}
				if (b == EOF) {
					count++;
					break;
				}

			}

		}

	}

	fclose(f);
	return count;

}

9.4.

typedef struct {
	char name[31];
	float price;
	int in_stock;
} Product;

int write_binary(const char* filename, const Product* shop)
{
	FILE* f = fopen(filename, "wb");
	if (f == NULL) {
		return 1;
	}
	int i = 0;
	while (shop[i].name[0] != '\0') {
		fwrite(&shop[i], sizeof(Product), 1, f);
		i++;
	}
	fclose(f);
	return 0;
}

Product* read_binary(const char* filename)
{
	FILE* f = fopen(filename, "rb");

	if (f == NULL) {
		return NULL;
	}
	int i = 0;
	Product* data = malloc(sizeof(Product) * 3);

	while ((fread(&data[i], sizeof(Product), 1, f)) == 1) {
		data = realloc(data, sizeof(Product) *( 3 +i));
		i++;
	}
	data[i].name[0] = '\0';
	data = realloc(data, sizeof(Product)* (i+1));
	fclose(f);
	return data;
}

int write_plaintext(const char* filename, const Product* shop)
{
	FILE* f = fopen(filename, "w");
	if (f == NULL) {
		return 1;
	}
	int i = 0;
	while (shop[i].name[0] != '\0') {
		fprintf(f, "%s %f %d\n", &shop[i].name[0], shop[i].price, shop[i].in_stock);
		i++;
	}
	fclose(f);
	return 0;
}

Product* read_plaintext(const char* filename)
{
	FILE* f = fopen(filename, "r");
	if (f == NULL) {
		return NULL;
	}
	Product* shop = malloc(sizeof(Product) * 3);
	int i = 0;

	while ((fscanf(f, "%s %f %d\n", shop[i].name, &shop[i].price, &shop[i].in_stock)) != EOF) {

		shop = realloc(shop, sizeof(Product) * (3 +i));
		i++;
	}
	shop[i].name[0] = '\0';
	shop = realloc(shop, sizeof(Product) * (i+1));
	fclose(f);
	return shop;

}

9.2.

int print_file_and_count(const char* filename)
{
	int a;
	int count = 0;
	FILE* f = fopen(filename, "r");
	if (f == NULL) {
		return -1;
	}

	while (1) {
		a = fgetc(f);
		if (feof(f)) {
			break;
		}
		printf("%c", a);
		count++;
	}
	fclose(f);
	return count;

}


char* difference(const char* file1, const char* file2)
{
	char a[1000];
	char b[1000];
	char* c;


	FILE* f1 = fopen(file1, "r");
	FILE* f2 = fopen(file2, "r");

	if (f1 == NULL) {
		return NULL;
	}
	else if (f2 == NULL) {
		return NULL;
	}

	while (1) {

		fgets(a, 1000, f1);
		fgets(b, 1000, f2);
		if (feof(f1) || feof(f2)) {
			return NULL;
		}
		if (strcmp(a, b) == 0) {
			continue;
		}
		if (strcmp(a, b) != 0) {
			c = calloc((strlen(a) + strlen(b) + 12), sizeof(char));
			strcpy(c, a);
			strcat(c, "----\n");
			strcat(c, b);


			fclose(f1);
			fclose(f2);
			return c;
		}

	}

	fclose(f1);
	fclose(f2);
	return NULL;

}
*/


