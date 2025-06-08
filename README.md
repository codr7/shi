# shi
a Simple Hackable Interpreter

## Goal
The goal of this project is to implement the same simple, hackable interpreter core in multiple host languages. For educational purposes, and to allow comparing the performance and features of different host languages.

## Motivation
I can't remember a time when I didn't feel the urge to design and implement my own programming languages, to gain a deeper understanding and make it possible to build my own tools.

I started out with relatively primitive template languages and formula evaluators, but as I gained more experience the goal posts moved further and further towards general purpose languages.

Most tutorials unfortunately start with parsing, which I consider to be the least interesting aspect. It wasn't until I discovered Forth that I managed to implement something I would consider using myself before running ut of motivation.

I then went through a long period of messing around with those ideas, adding more and more elaborate features on top until I ended up with something more resembling Lisp.

Along the way I kept switching host languages, moving ideas from language to language in an attempt to cut them down to their core and find optimal implementation strategies.

This project in many ways represents the culmination of that work, and is offered with the hope of helping other developers get started designing and implementing their own languges.

## License
The content of this tutorial is openly licensed via [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Support
I've decided to use an open license to benefit as many as possible, because I believe knowledge should be shared freely.

But I also believe in compensation for creators; and the less economic pressure I have to deal with, the more time and energy I can put into the project.

Please take a moment to consider chipping in if you like the idea. Nothing is free in this world, your contribution could make a big difference.

The repository is set up for sponsoring via Stripe and Liberapay, alternatively you may use BTC (bitcoin:18k7kMcvPSSSzQtJ6hY5xxCt5U5p45rbuh) or ETH (0x776001F33F6Fc07ce9FF70187D5c034DCb429811). 

## Implementations

- [Go](https://github.com/codr7/shi-go)
- [Java](https://github.com/codr7/shi-java)

## Language
The language implemented is a strictly prefix, dynamically typed scripting language capable of recursively generating the Fibinacci sequence. The syntax is intentionally kept as simple as possible.

```
method fib (n Int)
  if < n 2
    n
  else
    + fib - n 1
      fib - n 2
```

## Types
The following types are provided.

### Binding
The type of registers.

### Bool
The boolean type has two values, `T` and `F`.

### Int
Signed 32-bit integers.

### Macro
The type of macros like `method` and `if`.

### Method
The type of methods like `+` and `-`, as well as user defined methods like `fib`.

### Time
Durations of time.

## VM Operations
The VM is primarily stack based, using registers for bindings; and provides the following operations. Note that all implementations allow adding new operations from user code.

### Benchmark [rounds, end pc]
Evaluate until `end pc` `rounds` times and push elapsed time on stack.

### Call [location, target method]
Call target method.

### Branch [end pc]
Pop value from stack and continue evaluating if it's truthy, otherwise jump to the end of the branch.

### Get [source register]
Get value from register and push on stack.

### Goto [target pc]
Jump to target pc.

### Push [value]
Push value on stack.

### Put [target register, count]
Pop values from stack and put in registers.

### Return []
Pop call and jump to return pc.