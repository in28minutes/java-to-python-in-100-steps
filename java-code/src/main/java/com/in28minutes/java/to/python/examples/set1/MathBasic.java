package com.in28minutes.java.to.python.examples.set1;
public class MathBasic {
	
	static void printSquaresOfNumbersUpto(int n) {
	    for(int i=1; i<=n; i++) {
	         System.out.println(i*i);
	    }
	}
		
	public static void main(String[] args) {
		printSquaresOfNumbersUpto(10);
		//printSquaresOfEvenNumbersUpto(10);
		//printNumbersInReverse(10);
	}
}