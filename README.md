# shi
a Simple Hackable Interpreter

## Goal
The goal of this project is to implement the same simple, hackable interpreter core in multiple host languages. For educational purposes, and to allow comparing performance and optimal implementation strategies.

## Motivation
I can't remember a time when I didn't feel the urge to design and implement my own programming languages, to gain a deeper understanding and enable building my own tools.

I started out with template engines and formula evaluators, but as I gained more experience the goal posts moved further and further towards general purpose languages.

Most tutorials unfortunately start with parsing, which I consider to be the least interesting aspect. It wasn't until I discovered Forth that I managed to implement something I would consider using myself before running ut of motivation.

I then went through a long period of messing around with those ideas, adding more and more elaborate features on top until I ended up with something more resembling Lisp.

Along the way I kept switching host languages, moving ideas from language to language in an attempt to cut them down to their core and find optimal implementation strategies.

This project in many ways represents the culmination of that work, and is offered with the hope of helping other developers get started designing and implementing their own languges.

## License
The content is openly licensed via [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Support
I've decided to use an open license to benefit as many as possible, because I believe knowledge should be shared freely.

But I also believe in compensation for creators; and the less economic pressure I have to deal with, the more time and energy I can put into the project.

Please take a moment to consider chipping in if you like the idea. Nothing is free in this world, your contribution could make a big difference.

The repository is set up for sponsoring via Stripe and Liberapay, alternatively you may use BTC (bitcoin:18k7kMcvPSSSzQtJ6hY5xxCt5U5p45rbuh) or ETH (0x776001F33F6Fc07ce9FF70187D5c034DCb429811). 

## Implementations

- [C](https://github.com/codr7/shi-c)
- [Java](https://github.com/codr7/shi-java)

## Performance

Python3 is used as a performance baseline.
```
fact 532530451
fib1 303582953
fib2 441846114
```

C
```
fact 1357571091
fib1 1370970198
fib2 1486216493
```

Java
```
fact 1064277762
fib1 1011048014
fib2 922161095
```

## Language
The language implemented out of the box is a strictly prefix, dynamically typed scripting language. The syntax is designed to be easy to replace/extend without touching other parts of the implementation.

```
method fib (n Int)
  if < n 2
    n
  else
    + fib - n 1
      fib - n 2
```

Macros and methods have a fixed number of arguments, parens may be used to group expressions.

```
say (1 2 3)
```
`1 2 3`

## Types
The following types are provided:

### Any
The root of all types.

### Binding
The type of bindings (values in registers).

### Bool
The boolean type has two values, `T` and `F`.

### Int
Signed 64-bit integers.

### Macro
The type of macros like `method` and `if`.

### Method
The type of methods like `+` and `-`, as well as user defined methods like `fib`.

## Macros
The following macros are provided, adding more is trivial.

### benchmark [rounds body]
Repeat `body` `rounds` times and push elapsed time on stack.

### check [expected actual]
Evaluate `actual` and compare to `expected`, throw an exception if they're not equal.
### if [cond expr1] else [expr2]
Evaluate `expr1` if `cond` is truthy, else `expr2` (if provided).

### method [name arguments body]
Define a new method with specified `name`, `arguments` and `body`. Arguments may optionally be suffixed with a type, which is checked when the method is called; defaults to `Any` if not provided.

### return [value]
Emit arguments and goto start of method if `value` is a SHI-method, otherwise emit `value` and exit the current call.

## Methods
The following methods are provided, adding more is trivial.

### + [x y]
Add `x` to `y` and push the result on stack.

### - [x y]
Subtract `x` from `y` and push the result on stack.

### * [x y]
Multiply `x` by `y` and push the result on stack.

### = [x y]
Push `T` on stack if `x` equals `y`, otherwise `F`.

### < [x y]
Push `T` on stack if `x` is less than `y`, otherwise `F`.

### > [x y]
Push `T` on stack if `x` is greater than `y`, otherwise `F`.

### say [what]
Print `what` followed by newline to standard output.

## VM
The VM is primarily stack based, using registers for bindings.

### Operations
Note that all implementations allow easily adding new operations from user code.

#### benchmark [rounds end_pc]
Evaluate `rounds` times from the next operation to `end_pc` and push elapsed time on stack.

#### call_method [target_method location]
Call `target_method`. Host methods are called directly while script methods push an entry on the call stack and jump to the start of the method.

#### check_value [expected location]
Pop value from stack and compare to `expected`, throw an exception if they're not equal.

#### branch [end_pc]
Pop value from stack and continue evaluating if it's truthy, otherwise jump to the end of the branch.

#### get_registers [source count]
Get value from `source` register(s) and push on stack.

#### goto [target_pc]
Jump to `target_pc`.

#### push_value [value]
Push `value` on stack.

#### return []
Pop entry from call stack and jump to its return pc.

#### set_registers [target count]
Pop `count` values from stack and put in `target` register(s).

## Forms
Forms are the bits and pieces that syntax consists of, shi supports the following kinds of forms:

### Identifiers
Anything that's not a literal or list, for example `foo`.

### Literals
Constant values, for example `42`.

### Scopes
Sequences of forms, for example `(foo 42)`

## Readers
Readers consume source code and prduce sequences of forms by breaking syntactic constructs down recursively. The following readers are supported:

### Whitespace
Consumes sequences of whitespace.

### Identifier
Consumes sequences of characters that are not whitespace, literals nor lists.

### Int
Consumes integers.

### Scope
Consumes sequences of forms.