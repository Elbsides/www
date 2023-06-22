---
layout: page
permalink: /2021/programm/workshop-fuzzing/
---

# Trainer

Hardik Shah

# Schedule

- Begins: 9:00
- Run time: 3 hours

# Abstract

In this workshop, we will discuss what is fuzzing how does fuzzer works, what are different types of fuzzers and how to use them to fuzz various open source softwares on linux. First we will have basic introduction to different types of vulnerabilities like integer overflow/underflow, stack/heap overflow/out of bound read/write which are very common in software, we will also see some example of real world vulnerabilities to get an understanding of these vulnerability types.

Later on during the training we will first start with fuzzing a simple C program which contains these vulnerabilities. After that we will see how we fuzz real world open source software using fuzzers like AFL, honggfuzz and libfuzzer.

This talk will also provide details on how does AFL works, what are the different mutation strategies it uses. basics of compile time instrumentation, how to collect corpus for fuzzing and how to minimize it, crash triage and finding root cause.

Detailed Outline:

1.  Different types of vulnerabilities - quick overview of Buffer overflow, heap overflow, integer overflow, use after free, out of bound read/Write.
2.  Manually identifying the vulnerabilities in C code.
3.  What is fuzzing and different types of fuzzer - dumb fuzzer, mutation fuzzer, coverage guided fuzzer.
4.  Fuzzing Process
5.  corpus collection
6.  corpus minimization
7.  Fuzzing Sample C program using AFL, libfuzzer and Honggfuzz, libfuzzer
8.  Analyzing and triaging crashes
9.  How to fuzz real world softwares using AFL,honggfuzz
10. How to fuzz tcpdump/libtiff using AFL/Honggfuzz.
11. Reporting crashes and bug bounties
12. QnA
13. Conclusion

# Bio

Hardik Shah

- [@hardik05](https://twitter.com/hardik05)
- Hardik Shah is an experienced security researcher and technology evangelist. He is currently working with McAfee as a vulnerability researcher. Hardik has found many vulnerabilities in windows and other open source software. He was also MSRC most valuable researcher for year 2019 and Top contributing researcher for Q1 2020. Hardik enjoys analyzing latest threats and figuring out ways to protect customers from them. You can follow him on twitter [@hardik05](https://twitter.com/hardik05) and read some of his blogs here: https://www.mcafee.com/blogs/author/hardik-shah
