#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include "gameoflife.h"



/* Exercise a: Allocates needed memory for the GameArea structure and
 * the actual game area. 'x_size' and 'y_size' indicate the horizontal and
 * vertical dimensions of the GameArea.
 * 
 * Returns: pointer to the GameArea structure allocated by this function.
 */
GameArea *createGameArea(unsigned int x_size, unsigned int y_size) {
    
    GameArea* new = (GameArea*) malloc(sizeof(GameArea));
    new->y_size = y_size;
    new->x_size = x_size;

    unsigned int i = 0;
    unsigned int j = 0;
    
    new->cells = malloc((y_size+1) * sizeof(CellStatus*));

    while (i < y_size) {
        new->cells[i] = calloc((x_size+1) , sizeof(CellStatus*));
        while (j < x_size) {
            
            new->cells[i][j] = DEAD;
            j++;
        }
        i++;
    }
    return new;
}

/* Free memory allocated for GameArea <a>.
 */
void releaseGameArea(GameArea *a) {
    unsigned int i = 0;
    
    while (a->y_size > i) {
        free(a->cells[i]);
        i++;

    }
    free(a->cells);
    free(a);
}

/* Exercise b: Initialize game GameArea by setting exactly <n> cells into
 * ALIVE CellStatus in the game GameArea <a>.
 */
void initGameArea(GameArea *a, unsigned int n) {
   
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

/* Exercise c: Output the current CellStatus of GameArea <a>.
 */
void printGameArea(const GameArea *a) {
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

/* Calculates number of live neighbours around position (x,y),
 * and returns the count.
 */
unsigned int live_neighbours(const GameArea *a, unsigned int x, unsigned int y) {
    
    int count = 0;
    
    while (count <= 8) {
        if ((x + 1) < a->x_size && a->cells[y][x + 1] == ALIVE) {
            count++;
        }
        else if (((x - 1) == 0 || (x - 1) > 0) && a->cells[y][x - 1] == ALIVE) {
            count++;
        }
        else if (((x - 1) == 0 || (x - 1) > 0) && ((y - 1) == 0 || (y - 1) > 0) && a->cells[y-1][x - 1] == ALIVE) {
            count++;
        }
        else if ((x + 1) < a->x_size && ((y - 1) == 0 || (y - 1) > 0) && a->cells[y - 1][x + 1] == ALIVE) {
            count++;
        }
        else if ( ((y - 1) == 0 || (y - 1) > 0) && a->cells[y - 1][x] == ALIVE) {
            count++;
        }
        else if ((x + 1) < a->x_size && (y + 1) < a->y_size && a->cells[y + 1][x + 1] == ALIVE) {
            count++;
        }
        else if (((x - 1) == 0 || (x - 1) > 0) && (y + 1) < a->y_size && a->cells[y + 1][x - 1] == ALIVE) {
            count++;
        }
        else if ((y + 1) < a->y_size && a->cells[y + 1][x] == ALIVE) {
            count++;
        } 
    }

    return count;
}

/* Exercise d: Advance GameArea <a> by one generation.
 */
void gameTick(GameArea *a) {
  
    GameArea* new = createGameArea(a->x_size, a->y_size);
    new->x_size = a->x_size;
    new->y_size = a->y_size;

    unsigned int j = 0;
    unsigned int i = 0;
    
    while (i < a->y_size) {
        while (j < a->x_size) {
            if (live_neighbours(a, j, i) < 2 && a->cells[i][j] == ALIVE) {
                new->cells[i][j] = DEAD;
                continue;
            }
            else if ((live_neighbours(a, j, i) == 2 || live_neighbours(a, j, i) == 3) && a->cells[i][j] == ALIVE) {
                new->cells[i][j] = ALIVE;
                continue;
            }
            else if (live_neighbours(a, j, i) > 3 && a->cells[i][j] == ALIVE) {
                new->cells[i][j] = DEAD;
                continue;
            }
            else if (live_neighbours(a, j, i) == 3 && a->cells[i][j] == DEAD) {
                new->cells[i][j] = ALIVE;
                continue;
            }
            j++;

        }
        i++;
    }

    a->cells = new->cells;
}
