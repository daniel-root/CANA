import java.util.Scanner;

class Pessoa{
	private int Matricula;
	private String Nome;
	private double Nota;

	
	public Pessoa(){
	}
	public Pessoa(int Matricula,String Nome,double Nota){
		this.Matricula=Matricula;
		this.Nome=Nome;
		this.Nota=Nota;
	}
	public void setMatricula(int Matricula) {
		this.Matricula = Matricula;
	}
	public void setNome(String Nome){
		this.Nome=Nome;
	}
	public void setNota(double Nota){
		this.Nota=Nota;
	}
	public int getMatricula() {
		return Matricula;
	}
	public String getNome(){
		return Nome;
	}
	public double getNota(){
		return Nota;
	}

}
class Programa{
    public static void main(String[] args) {
    	int n;
    	Scanner ler = new Scanner(System.in);
        System.out.print("Entre com o tamanho: ");
        n = ler.nextInt();
        Pessoa x[] = new Pessoa[n];
        String Nome; int Matricula; double Nota;
        for (int i=0; i<n; i++) {
        	x[i] = new Pessoa();
        }
    	for (int i=0; i<n; i++) {
    		System.out.print("Entre o numero de Matricula: ");
    		Matricula = ler.nextInt();
    		x[i].setMatricula(Matricula);
    		ler.nextLine();
    		System.out.print("Entre o numero de Nome: ");
    		Nome = ler.nextLine();
    		x[i].setNome(Nome);
    		System.out.print("Entre com a Nota: ");
    		Nota = ler.nextDouble();
    		x[i].setNota(Nota);
		}
		System.out.println();
		for (int i=0; i<n; i++) {
    		System.out.println("Nº Matricula: "+x[i].getMatricula());
    		System.out.println("Nome: "+x[i].getNome());
    		System.out.println("Nota: "+x[i].getNota());
    		System.out.println();
		}
		System.out.println("Digite 1 - Matricula");
		System.out.println("Digite 2 - Nome");
		System.out.println("Digite 3 - Nota");
		System.out.print("Como deseja ordenar? ");
		int escolha = ler.nextInt();
		int aux=0;
		String aux1;
		double aux2;
		 switch (escolha) {
			case 1:
		for(int i = 0; i<n; i++){
		        for(int j = 0; j<n-1; j++){
		            if(x[j].getMatricula() > x[j + 1].getMatricula()){
                		aux = x[j].getMatricula();
                		aux1 = x[j].getNome();
                		aux2 = x[j].getNota();
                		x[j].setMatricula(x[j+1].getMatricula()); 
                		x[j].setNome(x[j+1].getNome());
                		x[j].setNota(x[j+1].getNota());
		                x[j+1].setMatricula(aux);
                		x[j+1].setNome(aux1);
        		        x[j+1].setNota(aux2);
		            	}
        			}
    			}
				break;
			case 2:
		    	for(int i = 0; i<n; i++){
		        for(int j = 0; j<n-1; j++){
		            if (x[j].getNome().compareTo(x[j + 1].getNome())>0){
                		aux = x[j].getMatricula();
                		aux1 = x[j].getNome();
                		aux2 = x[j].getNota();
                		x[j].setMatricula(x[j+1].getMatricula()); 
                		x[j].setNome(x[j+1].getNome());
                		x[j].setNota(x[j+1].getNota());
		                x[j+1].setMatricula(aux);
                		x[j+1].setNome(aux1);
        		        x[j+1].setNota(aux2);
		            	}
        			}
    			}
    			
				break;
			case 3:
				for(int i = 0; i<n; i++){
		        for(int j = 0; j<n-1; j++){
		            if(x[j].getNota() > x[j + 1].getNota()){
                		aux = x[j].getMatricula();
                		aux1 = x[j].getNome();
                		aux2 = x[j].getNota();
                		x[j].setMatricula(x[j+1].getMatricula()); 
                		x[j].setNome(x[j+1].getNome());
                		x[j].setNota(x[j+1].getNota());
		                x[j+1].setMatricula(aux);
                		x[j+1].setNome(aux1);
        		        x[j+1].setNota(aux2);
		            	}
        			}
    			}
				break;
		}
    	System.out.println();
    	for (int i=0; i<n; i++) {
    		System.out.println("Nº Matricula: "+x[i].getMatricula());
    		System.out.println("Nome: "+x[i].getNome());
    		System.out.println("Nota: "+x[i].getNota());
    		System.out.println();
		}
	}
}
