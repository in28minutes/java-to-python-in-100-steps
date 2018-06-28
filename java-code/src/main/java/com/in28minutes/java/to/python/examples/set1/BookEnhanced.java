package com.in28minutes.java.to.python.examples.set1;

public class BookEnhanced {

	private int copies;

	private String name;

	public BookEnhanced(String name, int copies) {
		this.name = name;
		this.copies = copies;
	}

	public int getCopies() {
		return copies;
	}

	public void setCopies(int copies) {
		if(copies>=0)
			this.copies = copies;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

}