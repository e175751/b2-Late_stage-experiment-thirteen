#include <stdio.h>
#define MAX 100
float r = 3.80;
float x_list[MAX];
float y_list[MAX];

int main(void){
  FILE *file;
	file = fopen("c_returnmap.txt","w");
  float init = 0.7;
  for(int i=0; i<MAX; i++){
    if (i%2==0){
      x_list[i]=init;
      init = r * (1 - init) * init;
      y_list[i]=init;
    }else{
      x_list[i]=y_list[i-1];
      y_list[i]=y_list[i-1];
    }
  }
  for(int j=0; j<MAX; j++){
    fprintf(file,"%.3f",x_list[j]);
    fprintf(file,",");
    fprintf(file,"%.3f",y_list[j]);
		fprintf(file,"\n");
  }
  fclose(file);
  printf("終了しました");
	return 0;
}
