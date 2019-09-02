package pretest1;

public class pretest1 {

	public static void main(String[] args) {
		//Print first 100 prime numbers
		/*int i,j,n=0;
		for (i=2;;i++){
			for (j=2;j<=i;j++){
				if (i%j==0) {
					break;
				}
			}
			if(i==j) {
					n++;
					System.out.println(i);
			}
			if (n==100) {
				break;
			}
		}*/
		int i,j,count =0;
		for(i = 0;;i++) {
			for(j = 2; j<= i; j++) {
				if(i%j == 0) {
					break;
				}
			}
			if(i == j) {
				count++;
				System.out.println(i);
			}
			if(count == 100) {
				break;
			}
		}
	}

}

