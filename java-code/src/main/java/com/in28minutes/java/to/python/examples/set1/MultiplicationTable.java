package com.in28minutes.java.to.python.examples.set1;
public class MultiplicationTable {
	
	static void print() {
		print(5);
	}
	
	static void print(int table) {
		print(table, 1, 10);
	}
	
	static void print(int table, int from, int to) {
		for (int i = from; i <= to; i++) {
			System.out.printf("%d X %d = %d", table, i, table * i).println();
		}
	}
	
	public static void main(String[] args) {
		print();
		print(6);
		print(7,31,40);
	}
}