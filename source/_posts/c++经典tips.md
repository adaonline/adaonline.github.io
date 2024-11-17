---
title: c++经典tips
date: 2024-11-18 03:43:44
tags: c++
categories:
  - c++
---

### 常量指针、指针常量、常量指针常量

在 C++ 中，常量指针（`const pointer`）、指针常量（`constant pointer`）和常量指针常量（`constant pointer to constant`）是三种不同的概念。它们涉及指针和常量修饰符的组合方式

#### 1. 常量指针（`const pointer`）

常量指针是指指针本身是常量的，意味着指针的值（即存储的地址）不可更改，但指针指向的数据是可以修改的。

```c++
int a = 10;
int b = 20;
int *const ptr = &a;  // ptr 是常量指针

ptr = &b;  // 错误：ptr 是常量指针，不能更改指向的地址
*ptr = 30;  // 正确：可以修改 ptr 指向的内容
```

- `*const ptr` 说明 `ptr` 是常量指针（即指针值不可修改）。

- 但是 `*ptr` 允许修改指针所指向的对象。

#### 2. 指针常量（`constant pointer`）

指针常量是指指针指向的内容是常量的，意味着指针指向的数据不可更改，但指针本身可以重新指向不同的地址。

```c++
int a = 10;
int b = 20;
const int *ptr = &a;  // ptr 是指针常量

ptr = &b;  // 正确：ptr 可以指向不同的地址
*ptr = 30;  // 错误：ptr 指向的内容是常量，不能修改
```

- `const int *ptr` 说明 `ptr` 是指向常量的指针。

- `ptr` 可以改变它指向的地址，但是不能修改它指向的内容。

#### 3. 常量指针常量（`constant pointer to constant`）

常量指针常量是指指针本身和指针指向的内容都不能更改，既不能改变指针的值，也不能修改指针所指向的内容。

```c++
int a = 10;
int b = 20;
const int *const ptr = &a;  // ptr 是常量指针常量

ptr = &b;  // 错误：ptr 是常量指针，不能更改指向的地址
*ptr = 30;  // 错误：ptr 指向的内容是常量，不能修改
```

- `const int *const ptr` 说明 `ptr` 是指向常量的常量指针。

- 既不能改变 `ptr` 指向的地址，也不能修改它指向的内容。

#### 总结

1. **常量指针**（`int *const ptr`）：指针的地址不可修改，但指向的数据可以修改。

2. **指针常量**（`const int *ptr` 或 `int const *ptr`）：指针可以修改指向的地址，但指向的数据不可修改。

3. **常量指针常量**（`const int *const ptr`）：指针的地址和指向的数据都不可修改。
