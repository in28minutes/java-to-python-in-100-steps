package com.in28minutes.java.to.python.examples.set1;
public class Person {
	private String name;
	private String email;
	private String phoneNumber;
		
	public Person(String name) {
		System.out.println("Person Constructor");
		this.name = name;
	}
	
	public String getName() {
		return name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}
	
	public String toString() {
        return name + "#" + email + "#" + phoneNumber;
    }
}