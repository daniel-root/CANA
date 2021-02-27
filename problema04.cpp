#include <iostream>
#include <cstring>
using namespace std;

class Aluno{
private:
	string Nome;
	float Nota1;
	float Nota2;
	float Media;
public:
	Aluno(){
	}
	void setNome(string _Nome){
		Nome = _Nome;
	}
	void setNota1(float _Nota1){
		Nota1 = _Nota1;
	}
	void setNota2(float _Nota2){
		Nota2 = _Nota2;
	}
	void setNota(float _Nota1,float _Nota2){
		Nota1 = _Nota1;
		Nota2 = _Nota2;
		setMedia();
	}
	void setMedia(){
		Media = (Nota1*2+Nota2*3)/5;
	}
	string getNome(){
		return Nome;
	}
	float getNota1(){
		return Nota1;
	}
	float getNota2(){
		return Nota2;
	}
	float getMedia(){
		return Media;
	}
};
int main(){
	Aluno aluno[8];
	string nome;
	float salario,nota1,nota2,media;
	for (int i=0;i<8;i++){
	    cout<<"Digite o nome do aluno: ";
		cin>>nome;
		aluno[i].setNome(nome);
		cout<<"Digite as Notas: "<<endl;
		cout<<"N1: ";
		cin>>nota1;
		cout<<"N2: ";
		cin>>nota2;
		aluno[i].setNota(nota1,nota2);
	}
	cout<<endl<<"Insertion Sort - Ordenado por Media!"<<endl;
	int i, j;
	float key;
	Aluno aux;  
    for (i = 1; i < 8; i++) 
    {  
        key = aluno[i].getMedia();
        aux = aluno[i];  
        j = i - 1;  
  		while (j >= 0 && aluno[j].getMedia() > key) 
        {  
            aluno[j + 1] = aluno[j];  
            j = j - 1;  
        }  
        aluno[j + 1] = aux;  
    }
    for (int i = 0;i<8;i++){
    	cout<<aluno[i].getNome()<<endl;
    	cout<<aluno[i].getMedia()<<endl;
    }
	cout<<endl<<"Shell Sort - Ordenado por Nota 1!"<<endl;
	for (int gap = 8/2; gap > 0; gap /= 2) 
    { 
        for (int i = gap; i < 8; i += 1) 
        {
        	float temp = aluno[i].getNota1();
        	Aluno aux = aluno[i];
  	    	             
            for (j = i; j >= gap && aluno[j - gap].getNota1() > temp; j -= gap) {
                aluno[j] = aluno[j - gap]; 
            }
              
            aluno[j] = aux; 
        } 
    } 
    for (int i = 0;i<8;i++){
    	cout<<aluno[i].getNome()<<endl;
    	cout<<aluno[i].getNota1()<<endl;
    }
	
	cout<<endl<<"Bubble Sort - Ordenado por Nome (Alunos Reprovados)!"<<endl;
	for( int i = 1; i < 8; i++){
         for ( int j = 0; j < 7; j++){
         	Aluno aux = aluno[j]; 
			char c1[30];  strcpy(c1, aluno[j].getNome().c_str() );  
			char c2[30];  strcpy(c2, aluno[j+1].getNome().c_str() );          
            if(strcmp(c1,c2) > 0){
                aux=aluno[j];
                aluno[j]=aluno[j+1];
                aluno[j+1]=aux;
         	}                               
        }      
    }
    for (int i = 0;i<8;i++){
    	if (aluno[i].getMedia()<7){
    	cout<<aluno[i].getNome()<<endl;
    	cout<<aluno[i].getMedia()<<endl;
    }
    }

return 0;
}
