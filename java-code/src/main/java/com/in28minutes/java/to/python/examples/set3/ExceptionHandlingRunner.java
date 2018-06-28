package com.in28minutes.java.to.python.examples.set3;

public class ExceptionHandlingRunner {

	public static void main(String[] args) {
		try {
			// String str = null;
			// str.length();
			int i = 0;
			int number = 10 / i;
			System.out.println("Method2 Ended");
		} catch (NullPointerException ex) {
			System.out.println("Matched NullPointerException");
			ex.printStackTrace();
		} catch (ArithmeticException ex) {
			System.out.println("Matched ArithmeticException");
			ex.printStackTrace();
		} catch (Exception ex) {
			System.out.println("Matched Exception");
			ex.printStackTrace();
		}
		System.out.println("Method1 Ended");
		System.out.println("Main Ended");
	}
}
