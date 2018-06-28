package com.in28minutes.java.to.python.examples.set1;
public class StringBasic {	
	static void printString(String str, int times) {
	    for(int i=1; i<=times; i++) {
	         System.out.println(str);
	    }
	}
		
	public static void main(String[] args) {
		printString("I'm Having Fun", 10);
	}
}