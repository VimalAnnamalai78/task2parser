#Why pandas?
```
Pandas is quite advisable than CSV for manipulating and doing operations on the data
In case we don't have much operations to do then we can rely on CSV itself which is in the standard library
without installing many dependencies third-party packages unlike pandas.
```

# why i used read_csv instead read_excel in solution2?
```
Actually given forParsing_task.xls file is corrupted, i tried open with "read_excel" method but it was start asking 
a lot of dependencies to add xlrd engine, openpyxl engine but nothing worked.

when i re-saved the given file as .xls again & tried reading the newly saved file that worked.
But i thought dealing with the corrupted file is a given challenge, then i did try with "read_csv" function. 
```

# How read_csv worked on .xls file?
```commandline
Eventhough file saved extension is ".xls" but content saved in that file was ".csv" representation.
```
