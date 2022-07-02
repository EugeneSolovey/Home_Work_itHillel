# Plan
1. Homework problem analysis (briefly), terminal reopening.
2. Git (tell about ssh keys (.pub), create GitHub project, clone it, insert files, modify .gitignore, commit).
3. Variables — py-style vs c-style, how to change 2 variables, variable naming (PEP8).
    1. Variable contents
        - C-style:
            ```
            int a;

            +---------|--------+
            | address | 0x45F6 |
            +------------------+
            | type    | int    |
            +------------------+
            | value   | 100    |
            +------------------+
            | name    | a      |
            +------------------+

            sizeof(a) => 4
            ```
        - Python-style:
            ```
            a = 1252342342342342342

                         +--------------------+
                         | type      | int    |
              references +--------------------+
            a =========> | refcount  | 1      |
                         +--------------------+
                         | value     | 100    |
                         +--------------------+

            sys.getsizeof(a) => 28
            ```
4. int — bignum arithm, -256 <= x <= 256 is cached
5. float — bug, limit size (double).
6. operators. unary, binary and ternary. arithm, comparison, logical, identity, membership, bitwise (optional), operator presedence ((), **, unary -+, * / // %, + - , comparison, not and or).
