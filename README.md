# whitespace-enc

```console
$ cat input.txt
Hello, World!
TESTING!

$ python3 main.py
Hello, World!
TESTING!

$ cat output.txt | xxd
00000000: 2009 0920 0909 090a 2020 0909 2009 200a   .. ....  .. . .
00000010: 2020 0920 2009 090a 2020 0920 2009 090a    .  ...  .  ...
00000020: 2020 0920 2020 200a 2009 2020 0909 0a20    .    . .  ...
00000030: 0909 0909 090a 2009 2009 2020 200a 2020  ...... . .   .
00000040: 0920 2020 200a 2020 2009 0920 090a 2020  .    .   .. ..
00000050: 0920 2009 090a 2020 0909 2009 090a 2009  .  ...  .. ... .
00000060: 0909 0920 0a20 0920 090a 2009 2009 2009  ... . . .. . . .
00000070: 090a 2009 0909 2009 200a 2009 2009 0920  .. ... . . . ..
00000080: 200a 2009 2009 2009 090a 2009 0920 0909   . . . ... .. ..
00000090: 200a 2009 0920 2020 090a 2009 0909 2020   . ..   .. ...
000000a0: 200a 2009 0909 0920 0a20 0920 090a        . .... . . ..
``