package com.in28minutes.java.to.python.examples.set1;

import java.util.Scanner;

public class DoWhileRepeatedQuestionRunner {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int number;

		do {
			System.out.print("Enter a number: ");
			number = scanner.nextInt();
			System.out.println("Cube is " + (number * number * number));
		} while (number >= 0);
		
		System.out.print("Thank You! Have Fun!");
		scanner.close();
	}

}