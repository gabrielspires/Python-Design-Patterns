# Python Design Patterns

This project provides **easy-to-understand code examples** of the most important design patterns in Python. The goal is to help developers grasp the core principles behind each pattern through clear, concise, and practical demonstrations.

## Table of Contents

- [Introduction](#introduction)
- [Foundation Design Principles](#foundation-design-principles)
  - [Encapsulate What Varies](#encapsulate-what-varies)
  - [Composition Over Inheritance](#composition-over-inheritance)
  - [Apply Loose Coupling](#apply-loose-coupling)
  - [Program to Interfaces](#program-to-interfaces)
- [SOLID](#solid)
  - [Single Responsibility Principle](#single-responsibility-principle)
  - [Open-Closed Principle](#open-closed-principle)
  - [Liskov Substitution Principle](#liskov-substitution-principle)
- [Creational Patterns](#creational-patterns)
- [Structural Patterns](#structural-patterns)
- [Behavioral Patterns](#behavioral-patterns)
- [Architectural Design Patterns](#architectural-design-patterns)
- [Concurrency and Asynchronous Patterns](#concurrency-and-asynchronous-patterns)
- [License](#license)

## Introduction

Design patterns are proven solutions to common problems in software design. This repository aims to make learning these patterns accessible by providing simple Python examples and explanations.

## Foundation Design Principles

The foundation of good software design starts with understanding key principles. This section contains examples that illustrate these concepts:

### Encapsulate What Varies

Isolate parts of your code that are likely to change and encapsulate them. Techniques include polymorphism and property-based getters/setters.

See: [`encapsulate_what_varies.py`](Foundation-Design-Principles/encapsulate_what_varies.py)

### Composition Over Inheritance

Favor composing objects from simpler parts rather than inheriting functionality from base classes.

See: [`composition_over_inheritance.py`](Foundation-Design-Principles/composition_over_inheritance.py)

### Apply Loose Coupling

Minimize dependencies between components using abstraction and dependency injection.

See: [`apply_loose_coupling.py`](Foundation-Design-Principles/apply_loose_coupling.py)

### Program to Interfaces

Use abstract base classes and protocols to define contracts for your classes, enabling flexible and robust code.

See: [`program_to_interfaces.py`](Foundation-Design-Principles/program_to_interfaces.py)

## SOLID

### Single Responsibility Principle

A class should have only one reason to change, meaning it should be responsible for a single part of the program's functionality. This makes code easier to maintain and extend. For example, instead of one class handling both car actions and race results, split responsibilities into separate classes.

See: [`single_responsibility.py`](SOLID-Principles/single_responsibility.py)

### Open-Closed Principle

Once a software entity is defined and implemented, it should not be changed to add new functionality. Instead, the entity should be extended through inheritance or interfaces to accommodate new requirements and behaviors.

See: [`open_closed.py`](SOLID-Principles/open_closed.py)

### Liskov Substitution Principle

According to the LSP, if a program uses objects of a superclass, then the substitution of these objects with objects of a subclass should not change the correctness and expected behavior of the program.

See: [`liskov_substitution.py`](SOLID-Principles/liskov_substitution.py)


## Creational Patterns

*Coming soon...*

## Structural Patterns

*Coming soon...*

## Behavioral Patterns

*Coming soon...*

## Architectural Design Patterns

*Coming soon...*

## Concurrency and Asynchronous Patterns

*Coming soon...*

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE)