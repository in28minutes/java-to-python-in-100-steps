package com.in28minutes.java.to.python.examples.set1;

public class ForLoopExercises {

	public static boolean isPrime(int number) {
		// 2 to number-1
		// How can check if a number is divisible by 2?

		if (number < 2) {
			return false;
		}

		for (int i = 2; i <= number - 1; i++) {
			if (number % i == 0) {
				return false;
			}
		}

		return true;
	}

	public static int sumUptoN(int number) {
		int sum = 0;

		for (int i = 1; i <= number; i++) {
			sum = sum + i;
		}

		return sum;
	}

	public static int sumOfDivisors(int number) {
		// 6 except 1 , 6 => 2,3
		// 2 + 3

		int sum = 0;

		for (int i = 2; i <= number - 1; i++) {
			if (number % i == 0) {
				sum = sum + i;
			}
		}

		return sum;
	}

	public static void printNumberTriangle(int number) {
		// 1
		// 1 2
		// 1 2 3
		// 1 2 3 4
		// 1 2 3 4 5

		for (int i = 1; i <= number; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.print(j + " ");
			}
			System.out.println();
		}

	}

}
