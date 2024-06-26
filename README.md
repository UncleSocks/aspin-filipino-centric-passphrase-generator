![aspin_01](https://github.com/UncleSocks/aspin-filipino-centric-passphrase-generator/assets/79778613/7bccf670-a404-41fc-8ab3-489d7da828f7)

# Aspin: Filipino-centric Passphrase Generator

**Aspin** _[ˈʔas.pɪn]_, short for Asong Pinoy, is a term used for mixed-breed street dogs.

Why create another passphrase generator? 

I wanted to create a passphrase generator that focuses on Philippine dialects as its wordlists -- "mixing" words, separators, case, and others to generate a more secure passphrase. This passphrase generator has the generic features of specifying the word count, word case, and separator. In addition, it also supports character substitution, separator multiplier, and inclusion of randomized numbers and/or special characters.
Furthermore, this allowed me to practice my Python skills and at the same time contribute to the information security knowledge body.

I also included a folder of my photographs to raise awareness to aspins.
```
aspin.py -l 5 -s * -sC 3 -N -S -c randomize -x a=@

Passphrase Generated:
@LPAS.2***P@glAL@IB/0***ItuWAD=8***sALIGWIl(5***SuGid,2
```
The above example looks very complicated, but this would be ideal if you need extra security. Specifying lesser arguments can result in a more memorable passphrase:
```
aspin.py -l 5 -s - -sC 3 -N -c capitalize

Passphrase Generated:
Mahigit9---Nakakabit6---Maulol1---Tukuyin9---Kalinga5
```

## Usage and Available Arguments
You can run the `-h` option to display the list of available command-line arguments. 
```
ASPIN [-h] [-l WORD_LENGTH] [-n GENERATE_NUMBER] [-s SEPARATOR] [-sC SEPARATOR_COUNT] [-N] [-S] [-c WORD_CASE] [-x SUBSTITUTION] [-w WORDLIST] [-wC WORDLIST_COMBINE] [-i]
```
### Available Arguments
Below you will find the list of available options. Each of these options/arguments has their own default value, which will be used when unspecified. Alternatively, you can run interactive mode by specifying the `-i` option. Aspin will then display prompts for you to answer.
- `-l` or `--WORDLENGTH` : Specify an integer for the number of words in your passphrase. Default value is 5.
- `n` or `--GENERATENUMBER` : Specify an interger for the number of passphrases to generate. Default value is 1.
- `-s` or `--SEPARATOR` : Specify a separator character between each word in your passphrase. Default is a space.
- `-sC` or `--SEPARATORCOUNT` : Specify the number of separators between each word. Default value is 1.
- `-N` or `--NUMBERS` :  Append numbers at the end of each word in your passphrase. Default value is False.
- `-S` or `--SPECIALCHARS` :  Append special characters at the end of each word in your passphrase. Default value is False.
- `-x` or `--SUBSTITUTION` :  Specify a character substitution using the '>' symbol between your old and new character (e.g., l>!). Default value is None.
- `-w` or `--WORDLIST` : Specify the wordlist file location. Default is the tagalog.txt file.
- `-wC` or `--WORDLISTCOMBINE` : Specify another wordlist file location to combine with the current chosen wordlist. Default is None.
- `-i` or `--INTERACTIVE` : The program will ask for user inputs to generate the passphrase. Default value is False.

### Word Case Options
- lowercase: All characters are in lowercase
- uppercase: All characters are in uppercase
- capitalize: Begining character of each word is in uppercase
- randomize: Random uppercase and lowercase on each word

### Numbers and Special Characters
When specifying the `-N` or `--NUMBERS` argument, it will append a random number on each word. Similarly, when specifying `-S` or `-SPECIALCHARS`, it will also append a special character on each word.

## Roadmap
I will be adding other Philippine dialect wordlists. At the time of writing, I considered this project as a practice for OOP (Classes) and Python in general but we will see where this would go.
