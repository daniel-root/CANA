import java.util.*;
class program{

	public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		int n,maior=0;
		System.out.print("Entre com o tamanho do Vetor: ");
		n = ler.nextInt();
		int v[] = new int[n];
		String nomes[] = new String[n];
		for (int i = 0; i < n; i++) {
			System.out.printf("Entre com a palavra No %d: ", i);
			nomes[i] = ler.next();
			v[i] = nomes[i].length();
		} 
        for (int i = 1; i < n; ++i) { 
			int key = v[i];
			String aux = nomes[i];
            int j = i - 1;
            while (j >= 0 && v[j] > key) { 
				v[j + 1] = v[j];
				nomes[j+1] = nomes[j];
                j = j - 1; 
            } 
			v[j + 1] = key;
			nomes[j+1] = aux;
		}

		System.out.println(Arrays.toString(nomes));
	}
}
