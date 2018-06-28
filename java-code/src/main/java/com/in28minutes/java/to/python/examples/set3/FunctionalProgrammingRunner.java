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
