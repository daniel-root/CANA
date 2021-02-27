#include <iostream>
#include <cstring>
using namespace std;

class Funcionario{
private:
	string Nome;
	float Salario;
public:
	Funcionario(){
	}
	void setNome(string _Nome){
		Nome = _Nome;
	}
	void setSalario(float _Salario){
		Salario = _Salario;
	}
	string getNome(){
		return Nome;
	}
	float getSalario(){
		return Salario;
	}
};
int main(){
	Funcionario funcionario[5];
	string nome;
	float salario;
	for (int i=0;i<5;i++){
		cout<<"Digite com o nome do funcionario: ";
		cin>>nome;
		funcionario[i].setNome(nome);
		cout<<"Entre com o sálario: ";
		cin>>salario;
		funcionario[i].setSalario(salario);
	}
	cout<<endl<<"Ordenado por Nome!"<<endl;  
	for( int i = 1; i < 5; i++){
         for ( int j = 0; j < 4; j++){
         	float aux2 = funcionario[j].getSalario();
			string aux3 = funcionario[j].getNome(); 
			char c1[30];  strcpy(c1, funcionario[j].getNome().c_str() );  
			char c2[30];  strcpy(c2, funcionario[j+1].getNome().c_str() );          
            if(strcmp(c1,c2) > 0){
                aux3=funcionario[j].getNome();
                funcionario[j].setNome(funcionario[j+1].getNome());
                funcionario[j+1].setNome(aux3);
                aux2=funcionario[j].getSalario();
                funcionario[j].setSalario(funcionario[j+1].getSalario());
                funcionario[j+1].setSalario(aux2);
         	}                               
        }      
    }
    for (int i=0;i<5;i++){
		cout<<funcionario[i].getNome()<<endl;
		cout<<funcionario[i].getSalario()<<endl;
	}

	cout<<endl<<"Ordenado por Salário!"<<endl;
	/*Insertion Sort*/
	for (int i = 1; i < 5; i++) {
		float escolhido = funcionario[i].getSalario();
		string aux = funcionario[i].getNome();
		int j = i - 1;
		while ((j >= 0) && (funcionario[j].getSalario() > escolhido)) {
			funcionario[j+1].setSalario(funcionario[j].getSalario());
			funcionario[j+1].setNome(funcionario[j].getNome());
			j--;
		}
		funcionario[j + 1].setSalario(escolhido);
		funcionario[j + 1].setNome(aux);
	}
	for (int i=0;i<5;i++){
		cout<<funcionario[i].getNome()<<endl;
		cout<<funcionario[i].getSalario()<<endl;
	}

return 0;
}