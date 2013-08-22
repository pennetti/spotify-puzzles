import java.util.Scanner;

public static void main(String[] args) {

	String inputLine = "";
	String inputBinaryString = "";
	String outputBnaryString = "";
	int inputNumber = 0;
	int outputNumber = 0;
	BufferedReader stdin = 
						new BufferedReader(new InputStreamReader(System.in));
	System.out.flush();

	inputLine = stdin.readLine();
	try {
		inputNumber = Integer.parseInt(inputLine);
	} catch(NumberFormatException e) {
		System.exit(1);
	}

	if (inputNumber < 1 || inputNumber > 1000000000)
		System.exit(1);

	inputBinaryString = Integer.toBinaryString(inputNumber);
	outputBnaryString = new StringBuffer(inputBinaryString).reverse().toString();

	outputNumber = Integer.parseInt(outputBnaryString, 2);

	System.out.println(inputBinaryString);
	System.out.println(outputBnaryString);

	// for ()
	// {

	// }

	System.exit(0);
}