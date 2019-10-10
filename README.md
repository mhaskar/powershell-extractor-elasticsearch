# powershell-extractor-elasticsearch
Python script to extract powershell scrips from elasticsearch based on windows event "4104".

The windows event "4104" logs all the executed powershell scripts so you can audit them later, by forwarding all these events to elasticsarch using winlogbeat we can search for them easily and then dump the "ScriptBlockText" which is the powershell code that has been executed.

The script will save the results in a txt files so you can use them later.
