<!---
Current Directory : /in28Minutes/git/java-to-python-in-100-steps/java-code
-->

## Complete Code Example


### /src/main/java/com/in28minutes/java/to/python/examples/set1/Book.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/BookEnhanced.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/DoWhileRepeatedQuestionRunner.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/ForLoopExercises.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/HelloWorld.java

```java
package com.in28minutes.java.to.python.examples.set1;

public class HelloWorld {
	public static void main(String[] args) {
		System.out.println("Hello World");
		char a = 'a';
	}
}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/MathBasic.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/MathBasic2.java

```java
package com.in28minutes.java.to.python.examples.set1;

public class MathBasic2 {
	
	static int sumOfTwoNumbers(int firstNumber, int secondNumber) {
		int sum = firstNumber + secondNumber;
		return sum;
	}

	public static void main(String[] args) {
		sumOfTwoNumbers(10,20);
	}
}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/MenuConditionalRunner.java

```java
package com.in28minutes.java.to.python.examples.set1;

import java.util.Scanner;

public class MenuConditionalRunner {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter Number1: ");
		int number1 = scanner.nextInt();

		System.out.print("Enter Number2: ");
		int number2 = scanner.nextInt();

		System.out.println("Choices Available are ");
		System.out.println("1 - Add");
		System.out.println("2 - Subtract");
		System.out.println("3 - Divide");
		System.out.println("4 - Multiply");

		System.out.print("Enter Choice: ");
		int choice = scanner.nextInt();

		System.out.println("Your Choices are");
		System.out.println("Number1 " + number1);
		System.out.println("Number2 " + number2);
		System.out.println("Choice " + choice);

		performOperationUsingNestedIfElse(number1, number2, choice);
	}

	private static void performOperationUsingNestedIfElse(int number1, int number2, int choice) {
		if (choice == 1) {
			System.out.println("Result " + (number1 + number2));
		} else if (choice == 2) {
			System.out.println("Result " + (number1 - number2));
		} else if (choice == 3) {
			System.out.println("Result " + (number1 / number2));
		} else if (choice == 4) {
			System.out.println("Result " + (number1 * number2));
		} else {
			System.out.println("Invalid Operation");
		}
	}
}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/MultiplicationTable.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/Person.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/Planet.java

```java
package com.in28minutes.java.to.python.examples.set1;

public class Planet {
	String name;

	public static void main(String[] args) {
		Planet earth = new Planet();
		earth.name = "Earth";

	}

}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/Player.java

```java
package com.in28minutes.java.to.python.examples.set1;
public class Player {
	private String name;
	private static int count;

	public Player(String name) {
		System.out.println("Person Constructor");
		this.name = name;
		count++;
	}
	
	public static int getCount() {
		return count;
	}
	
	public String getName() {
		return this.name;
	}
	
}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/StringBasic.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/Student.java

```java
package com.in28minutes.java.to.python.examples.set1;
public class Student extends Person {
	private String collegeName;
	private int year;

	public Student(String name, String collegeName) {
		super(name);
		this.collegeName = collegeName;
	}
	
	public String getCollegeName() {
		return collegeName;
	}

	public void setCollegeName(String collegeName) {
		this.collegeName = collegeName;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set1/SwitchExercisesRunner.java

```java
package com.in28minutes.java.to.python.examples.set1;
public class SwitchExercisesRunner {

	public static void main(String[] args) {
		System.out.println(determineNameOfDay(5));
	}

	public static String determineNameOfDay(int dayNumber) {
		switch (dayNumber) {
		case 0:
			return "Sunday";
		case 1:
			return "Monday";
		case 2:
			return "Tuesday";
		case 3:
			return "Wednesday";
		case 4:
			return "Thursday";
		case 5:
			return "Friday";
		case 6:
			return "Saturday";
		}

		return "Invalid_day";
	}
}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/AbstractRecipe.java

```java
package com.in28minutes.java.to.python.examples.set2;

public abstract class AbstractRecipe {
	
	public void execute() {
		getReady();
		doTheDish();
		cleanup();
	}
	
	abstract void getReady();
	abstract void doTheDish();
	abstract void cleanup();
}

```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/ChessGame.java

```java
package com.in28minutes.java.to.python.examples.set2;
public class ChessGame implements GamingConsole{

	@Override
	public void up() {
		System.out.println("Move piece up");
	}

	@Override
	public void down() {
		System.out.println("Move piece down");
	}

	@Override
	public void left() {
		System.out.println("Move piece left");
	}

	@Override
	public void right() {
		System.out.println("Move piece right");
	}
	
}


```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/GameRunner.java

```java
package com.in28minutes.java.to.python.examples.set2;
public class GameRunner {

	public static void main(String[] args) {
		GamingConsole[] games = {new MarioGame(), new ChessGame()};
		
		for(GamingConsole game:games) {
			game.up();
			game.down();
			game.left();
			game.right();
		}

	}

}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/GamingConsole.java

```java
package com.in28minutes.java.to.python.examples.set2;

public interface GamingConsole {
	public void up();
	public void down();
	public void left();
	public void right();
}

```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/MarioGame.java

```java
package com.in28minutes.java.to.python.examples.set2;
public class MarioGame implements GamingConsole{

	@Override
	public void up() {
		System.out.println("Jump");
	}

	@Override
	public void down() {
		System.out.println("Goes into a hole");
	}

	@Override
	public void left() {
	}

	@Override
	public void right() {
		System.out.println("Go Forward");
	}
	
}

```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/Recipe1.java

```java
package com.in28minutes.java.to.python.examples.set2;
public class Recipe1 extends AbstractRecipe{

	@Override
	void getReady() {
		System.out.println("Get the raw materials");
		System.out.println("Get the utensils");
	}

	@Override
	void doTheDish() {
		System.out.println("do the dish");
	}

	@Override
	void cleanup() {
		System.out.println("Cleanup the utensils");		
	}

}

```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/RecipeRunner.java

```java
package com.in28minutes.java.to.python.examples.set2;
public class RecipeRunner {

	public static void main(String[] args) {
		Recipe1 recipe = new Recipe1();
		recipe.execute();

		RecipeWithMicrowave recipeWithMicrowave = new RecipeWithMicrowave();
		recipeWithMicrowave.execute();

	}

}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set2/RecipeWithMicrowave.java

```java
package com.in28minutes.java.to.python.examples.set2;
public class RecipeWithMicrowave extends AbstractRecipe{

	@Override
	void getReady() {
		System.out.println("Get the raw materials");
		System.out.println("Switch on the microwave");
	}

	@Override
	void doTheDish() {
		System.out.println("get stuff ready");
		System.out.println("Put it in the microwave");
	}

	@Override
	void cleanup() {
		System.out.println("Cleanup the utensils");
		System.out.println("Switch off the microwave");
	}

}

```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set3/ExceptionHandlingRunner.java

```java
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
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set3/FunctionalProgrammingRunner.java

```java
package com.in28minutes.java.to.python.examples.set3;

import java.util.List;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.stream.Collectors;

public class FunctionalProgrammingRunner {

	public static void main(String[] args) {

		Function<Integer, Integer> 
			multiplyByTwo = x -> x * 2;

		System.out.println(multiplyByTwo.apply(2));

		BiFunction<Integer, Integer, Integer> 
			productOfTwoNumbers = (x, y) -> x * y;

		System.out.println(
				productOfTwoNumbers.apply(2, 7));

		List<Integer> numbers = List.of(1, 4, 7, 9);
		
		System.out.println(numbers.stream()
				.filter(x -> x % 2 == 1)
				.collect(Collectors.toList()));
		
		System.out.println(numbers.stream()
				.map(x -> x * 2)
				.collect(Collectors.toList()));
		
		System.out.println(numbers.stream()
				.reduce((x, y) -> x * y).get());
		
		System.out.println(numbers.stream()
				.reduce((x, y) -> x + y).get());
		
		System.out.println(numbers.stream()
				.reduce((x, y) -> Math.max(x, y)).get());

		List<String> words = List.of("Apple", "Ant", "Bat");
		
		System.out.println(words.stream()
				.map(x -> x.toUpperCase())
				.collect(Collectors.toList()));
		
		System.out.println(words.stream()
				.map(x -> x.length())
				.collect(Collectors.toList()));

	}

}
```
---

### /src/main/java/com/in28minutes/java/to/python/examples/set3/ThrowingExceptionRunner.java

```java

package com.in28minutes.java.to.python.examples.set3;

class Amount {
	private String currency;
	private int amount;

	public Amount(String currency, int amount) {
		super();
		this.currency = currency;
		this.amount = amount;
	}

	public void add(Amount that) throws CurrenciesDoNotMatchException {

		if (!this.currency.equals(that.currency)) {
			// throw new Exception("Currencies Don't Match " + this.currency + " & "
			// +that.currency );
			throw new CurrenciesDoNotMatchException("Currencies Don't Match " + this.currency + " & " + that.currency);
		}

		this.amount = this.amount + that.amount;
	}

	public String toString() {
		return amount + " " + currency;
	}
}

class CurrenciesDoNotMatchException extends Exception {
	public CurrenciesDoNotMatchException(String msg) {
		super(msg);
	}
}

public class ThrowingExceptionRunner {

	public static void main(String[] args) throws CurrenciesDoNotMatchException {
		Amount amount1 = new Amount("USD", 10);
		Amount amount2 = new Amount("EUR", 20);
		amount1.add(amount2);
		System.out.println(amount1);
	}

}
```
---
