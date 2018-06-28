package com.in28minutes.java.to.python.examples.set1;

public class Book {
	
	private int noOfCopies;
	private String name;

	public Book(String name, int noOfCopies) {
		this.name = name;
		this.noOfCopies = noOfCopies;
	}

	public void increaseNoOfCopies(int howMuch) {
		this.noOfCopies = this.noOfCopies + howMuch;
	}

	public void decreaseNoOfCopies(int howMuch) {
		this.noOfCopies = this.noOfCopies - howMuch;
	}
	
	public String toString() {
		return "Book["+name+","+noOfCopies+"]";
	}
}
