#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>


// Ohjelmointi projekti: Taistelija
// @Emil Karlsson 
// C-kurssi kevat 2020

typedef struct {				// Aseen tietotyyppi
	char nimi[20];
	int  damage;
} gun;

typedef struct {				// Taistelijan rakenne
	char name[25];				// Listan viimeisen olion nimi merkitty '\0'
	int  elamat;
	int  exp;
	gun  ase;					// Viittaus aseen tietotyyppiin
} Taistelija;

int muisti = 0;					// muistin realloccaamista varten mainissa kun lisataan taistelija
								// seka kun ladataan taistelijat tiedostosta
	
// Uuden taistelijan luominen
// Kokemuspisteet alkavat uudella hahmolla aina nollasta
void A(Taistelija* lista, const char* name, const int hp, char* asee, const int vahinko) {

	int i = 0;
	for (; lista[i].name[0] != '\0';) {			// taistelija listan koon selvittaminen
		i++;
	}
	
	strcpy(lista[i].ase.nimi, asee);
	strcpy(lista[i].name, name);
	lista[i].elamat = hp;
	lista[i].exp = 0;
	lista[i].ase.damage = vahinko;
	lista[i + 1].name[0] = '\0';				
	
	printf("Information has been succesfully set!\n");
}


// Kahden taistelijan valinen tappelun kuvaaminen
// Hp voi laskea 0, mutta ei sen alle
void H(Taistelija* lista, char* atck, char* targ) {

	size_t targg = 0;
	size_t atckk = 0;
	int ret = -1;
	int ret2 = -1;

	while (lista[targg].name[0] != '\0') {			// kohteen loytaminen listasta
		ret = strcmp(lista[targg].name, targ);
		if (ret == 0) {
			break;
		}
		targg++;
	}
	
	while (lista[atckk].name[0] != '\0') {			// hyokkaajan loytaminen listasta
		ret2 = strcmp(lista[atckk].name, atck);
		if (ret2 == 0) {
			break;
		}
		atckk++;
	}
	if (ret == 0 && ret2 == 0) {				// jos loopit loytaneet listasta annetut taistelijat
		int damage = lista[atckk].ase.damage;
		lista[targg].elamat -= damage;
		if (lista[targg].elamat < 0) {
			lista[targg].elamat = 0;
			
		}
		lista[atckk].exp += damage;
		printf("%s attacked %s with %s by %d damage.", lista[atckk].name, lista[targg].name, lista[atckk].ase.nimi, damage);
		printf(" %s has %d hit points remaining. %s gained %d experience points\n", lista[targg].name, lista[targg].elamat, lista[atckk].name, damage);
	}
	else {
		printf("Something went wrong finding the attacker or target!\n");
	}
}


// L (tulostus) funktion avuksi
int Compare(const void* a, const void* b)
{
	const Taistelija* eka = a;
	const Taistelija* toka = b;

	if ((eka->elamat == 0) && (toka->elamat == 0)) {
		return 0;
	}
	else if ((eka->elamat > 0) && (toka->elamat > 0)) {
		if (eka->exp == toka->exp) {
			return 0;
		}
		else if (eka->exp > toka->exp) {
			return -1;
		}
		else if (eka->exp < toka->exp) {
			return 1;
		}
	}
	else if ((eka->elamat == 0) || (toka->elamat == 0)) {
		if (eka->elamat == 0) {
			return 1;
		}
		else if (toka->elamat == 0) {
			return -1;
		}
	}
	return 0;
}

// Kokemuspisteiden mukaisesti suuremmasta pienimpaan, kuolleet lopussa. 
// Apuna Compare(const void* a, const void* b)
void L(Taistelija* lista) {

		int i = 0;
		size_t a = 0;
		for (; lista[a].name[0] != '\0';) {			// taistelija listan koon selvittaminen
			a++;
		}

		qsort(lista, a, sizeof(Taistelija), Compare);

		while (lista[i].name[0] != '\0') {
			printf("Warriors name: %s Hp: %d Exp: %d Weapon: %s Weapon dmg: %d\n", lista[i].name, lista[i].elamat, lista[i].exp, lista[i].ase.nimi, lista[i].ase.damage);
			i++;
		}
}

// Tallentaa pelin hahmot (mukaanlukien kuolleet) tiedostoon,
// joka on nimeltaan -filename-
void W(const Taistelija* lista, char* filename) {
	FILE* f = fopen(filename, "w");
	if (f == NULL) {
		printf("File couldn't be opened!\n");
	}
	int i = 0;
	if (f != NULL) {
		while (lista[i].name[0] != '\0') {
			fprintf(f, "%s %d %d %s %d\n", lista[i].name, lista[i].elamat, lista[i].exp, lista[i].ase.nimi, lista[i].ase.damage);
			i++;
		}
		fclose(f);
		printf("Saving to file succeeded!\n");
	}
}

// Lataa pelin hahmot tiedostosta jonka nimi on -filename-,
// korvaten aiemmin muistissa olleen tilanteen.
// Palauttaa tiedostosta ladatun listan
Taistelija* O(Taistelija* lista, const char* filename) {
	FILE* f = fopen(filename, "r");
	if (f == NULL) {
		printf("File couldn't be opened!\n");
		
	}

	int i = 0;
	if (f != NULL) {
		muisti = 0;
		while ((fscanf(f, "%s %d %d %s %d", lista[i].name, &lista[i].elamat, &lista[i].exp, lista[i].ase.nimi, &lista[i].ase.damage)) != EOF) {
			lista = realloc(lista, sizeof(Taistelija) * (i + 2));
			i++;
			muisti++;
		}
		lista = realloc(lista, sizeof(Taistelija) * (i + 2));
		lista[i].name[0] = '\0';
		printf("Succesfully loaded list of warriors from file!\n");
		fclose(f);
		
	}
	return lista;
}

// Poistuu ohjelmasta ja vapauttaa kaiken kaytetyn muistin.
void Q(Taistelija* lista) {
	if (lista != NULL) {
		free(lista);
		printf("Succesfully released memory!\n");
	}
	else {
		printf("Something went wrong when releasing memory\n");
	}
}


int main() {
	Taistelija* warriors;								
	warriors = calloc(1, sizeof(Taistelija));
	memset(warriors, 0, sizeof(Taistelija));
	char kirjain[1];
	char input[80];
	
	

	while (fgets(input, sizeof(input), stdin) != NULL) {

		switch (input[0]) {
		case ('A'): {
			int hp, damage;
			char nimi[25];
			char gunn[25];

			nimi[0] = '+';		// '+', tarkistetaan sen avulla oliko syote vaaditun muotoinen
			gunn[0] = '+';
			hp = -1;
			damage = -1;

			sscanf(input, "%c %s %d %s %d", kirjain, nimi, &hp, gunn, &damage);
			
			if (nimi[0] != '+' && gunn[0] != '+') {
				if (hp != -1 && damage != -1) {
					muisti++;
					warriors = realloc(warriors, (muisti + 1) * sizeof(Taistelija));
					A(warriors, nimi, hp, gunn, damage);
				}
				else {
					printf("Incorrect parameters\n");
				}
			}
			else {
				printf("Incorrect parameters\n");
			}
			break;
		}
		case ('H'): {
			char nimi1[39];
			char nimi2[39];
			nimi1[0] = '+';
			nimi2[0] = '+';
			sscanf(input, "%c %s %s", kirjain, nimi1, nimi2);
			if (nimi1[0] != '+' && nimi2[0] != '+') {
				H(warriors, nimi1, nimi2);
			}
			else {
				printf("Incorrect parameters\n");
			}
			break;
		}
		case ('L'): {
			L(warriors);
			break;
		}
		case ('W'): {
			char file[78];
			file[0] = '+';
			sscanf(input, "%c %s", kirjain, file);
			if (file[0] != '+') {
				W(warriors, file);
			}
			else {
				printf("Incorrect parameters\n");
			}
			break;
		}
		case ('O'): {
			char file[78];
			file[0] = '+';
			sscanf(input, "%c %s", kirjain, file);
			if (file[0] != '+') {
				warriors = O(warriors, file);
			}
			else {
				printf("Incorrect parameters\n");
			}
			break;
		}
		case ('Q'): {
			Q(warriors);
			printf("Program stopped!\n");
			return 0;
			break;
		}
		default: {
			printf("Incorrect parameters\n");
		}
		}
	}
}
