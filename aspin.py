#Aspin: Filipino-centric Passphrase Generator
#GitHub @unclesocks: https://github.com/UncleSocks
#
#MIT License
#
#Copyright (c) 2024 Tyrone Kevin Ilisan
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.




import argparse
import random
import string


class ArgumentParser:
    
    def __init__(self):
        
        self.parser = argparse.ArgumentParser(prog="ASPIN", description="ASPIN is a Filipino-centric passphrase generator.")
        self._add_arguments()

    
    def _add_arguments(self):
        
        self.parser.add_argument(
            "-l", "--WORDLENGTH",
            type=int,
            default=5,
            dest="word_length",
            help="Specify an integer for the number of words in your passphrase. Default value is 5",
        )

        self.parser.add_argument(
            "-n", "--GENERATENUMBER",
            type=int,
            default=1,
            dest="generate_number",
            help="Specify the number of passphrases to be generated. Default value is 1."
        )

        self.parser.add_argument(
            "-s", "--SEPARATOR",
            type=str,
            default="",
            dest="separator",
            help="Specify a separator character between each word in your passphrase. Default is a no space."
        )

        self.parser.add_argument(
            "-sC", "--SEPARATORCOUNT",
            type=int,
            default=1,
            dest="separator_count",
            help="Specify the number of separators between each word. Default value is 1."
        )

        self.parser.add_argument(
            "-N", "--NUMBERS",
            action="store_true",
            dest="numbers",
            help="Append numbers at the end of each word in your passphrase. Default value is False."
        )

        self.parser.add_argument(
            "-S", "--SPECIALCHARS",
            action="store_true",
            dest="special_characters",
            help="Append special characters at the end of each word in your passphrase. Default value is False."
        )

        self.parser.add_argument(
            "-c", '--WORDCASE',
            type=str,
            default="lowercase",
            dest="word_case",
            help=(
                "Specify a word case for your passphrase. Default value is lowercase. "
                "Options are: lowercase, uppercase, capitalize, randomize, alternate."
            )
        )

        self.parser.add_argument(
            "-x", "--SUBSTITUTION",
            type=str,
            default=None,
            dest="substitution",
            help=(
                "Specify a character substitution using the equals (=) symbol between your old and new character (e.g., l=!). "
                "Default value is None."
            )
        )

        self.parser.add_argument(
            "-w", '--WORDLIST',
            type=str,
            default="./wordlist/tagalog.txt",
            dest="wordlist",
            help="Specify the wordlist file location. Default is the tagalog.txt file."
        )

        self.parser.add_argument(
            "-wC", "--WORDLISTCOMBINE",
            type=str,
            default=None,
            dest="wordlist_combine",
            help="Specify a second language wordlist to be combined. Default value is None."
        )
        
        self.parser.add_argument(
            "-i", "--INTERACTIVE",
            action="store_true",
            dest="interactive",
            help="The program will ask for user inputs to generate the passphrase. Default value is False."
        )


    def parse_arguments(self):
        return self.parser.parse_args()
    
    
    def argument_output(self):

        return {
            'word_length': self.parser.parse_args().word_length,
            'generate_number': self.parser.parse_args().generate_number,
            'separator': self.parser.parse_args().separator,
            'separator_count': self.parser.parse_args().separator_count,
            'numbers': self.parser.parse_args().numbers,
            'special_characters': self.parser.parse_args().special_characters,
            'substitution': self.parser.parse_args().substitution,
            'word_case': self.parser.parse_args().word_case,
            'wordlist': self.parser.parse_args().wordlist,
            'wordlist_combine': self.parser.parse_args().wordlist_combine
        }    


class NumbersAndSpecialChars:

    def __init__(self, wordlist, word_length):
        self.wordlist = wordlist
        self.word_length = word_length


    def add_special_chars(self):
        special_chars = ''.join(random.choice(string.punctuation) for _ in range(self.word_length))
        wordlist_with_special_chars = [f"{word}{special_char}" for word, special_char in zip(self.wordlist, special_chars)]
        return wordlist_with_special_chars
    

    def add_numbers(self):
        numbers = ''.join(random.choice(string.digits) for _ in range(self.word_length))
        wordlist_with_numbers = [f"{word}{number}" for word, number in zip(self.wordlist, numbers)]
        return wordlist_with_numbers
    

    def special_chars_nums_process(self, numbers_args, special_chars_args):
        
        if special_chars_args == True:
            self.wordlist = self.add_special_chars()
        
        if numbers_args == True:
            self.wordlist = self.add_numbers()

        return self.wordlist



def separator_multiplier(separator, multiplier):

    if isinstance(multiplier, int):
        multiplied = f"{separator*multiplier}"
        return multiplied
    else:
        ValueError("ERR02: Separator multiplier must be an integer.") 


def substitution_parser(substitution):

    if substitution:
        parsed_substitution = substitution.split("=")
        current_char = parsed_substitution[0]
        new_char = parsed_substitution[1]
        return current_char, new_char
    
    else:
        return


def parameter_parser(parameter_dict):
    
    word_length = parameter_dict['word_length']
    generate_number = parameter_dict['generate_number']
    separator = parameter_dict['separator']
    separator_count = parameter_dict['separator_count']
    numbers = parameter_dict['numbers']
    special_characters = parameter_dict['special_characters']
    substitution = parameter_dict['substitution']
    word_case = parameter_dict['word_case']
    wordlist = parameter_dict['wordlist']
    wordlist_combine = parameter_dict['wordlist_combine']

    return word_length, generate_number, separator, separator_count, numbers, \
        special_characters, substitution, word_case, wordlist, wordlist_combine


class InteractiveGeneration():

    def __init__(self):
        
        self.word_length = 5
        self.generate_number = 1
        self.separator = ""
        self.separator_count = 1
        self.numbers = False
        self.special_characters = False
        self.substitution = None
        self.word_case = "lowercase"
        self.wordlist = "./wordlist/tagalog.txt"
        self.wordlist_combine = None

        self._collect_user_inputs()

            
    def verify_int_input(self, prompt, default):
        user_input = input(prompt)
        return int(user_input) if user_input.isdigit() else default
    
    def verify_bool_input(self, prompt):
        user_input = input(prompt)
        return user_input in ('yes', 'y', 'true', 't', '1')
    

    def _collect_user_inputs(self):
        
        self.word_length = self.verify_int_input(f"\tEnter passphrase word count (default {self.word_length}): ", self.word_length)
        self.generate_number = self.verify_int_input(f"\tNumber of passphrase to generate (default {self.generate_number}): ", self.generate_number)
        self.separator = input(f"\tSeparator character (default space (default is no space)): ").strip() or self.separator
        self.separator_count = self.verify_int_input(f"\tEnter separator count (default {self.separator_count}): ", self.separator_count)
        self.numbers = self.verify_bool_input(f"\tInclude numbers (default {self.numbers}): ")
        self.special_characters = self.verify_bool_input(f"\tInclude special characters (default {self.special_characters}): ")
        self.substitution = input(f"\tSpecify character substitution (default {self.substitution}): ") or self.substitution
        self.word_case = input (f"\tWord case (default {self.word_case}): ") or self.word_case
        self.wordlist = input(f"\tWordlist file path (defult {self.wordlist}): ") or self.wordlist
        self.wordlist_combine = input(f"\tCombine another wordlist (default {self.wordlist_combine}): ") or self.wordlist_combine

    
    def output(self):
        
        return {
            'word_length': self.word_length,
            'generate_number': self.generate_number, 
            'separator': self.separator,
            'separator_count': self.separator_count,
            'numbers': self.numbers,
            'special_characters': self.special_characters,
            'substitution': self.substitution,
            'word_case': self.word_case,
            'wordlist': self.wordlist,
            'wordlist_combine': self.wordlist_combine
        }


class WordlistProcess:

    def __init__(self, filepaths):
        self.filepaths = filepaths

    def count_lines(self):
        
        filepath_dict = {}
        for filepath in self.filepaths:
        
            with open(filepath, 'rb') as file:
                lines_sum = sum(1 for _ in file) 
                #The underscore (_) is a common variable placeholder for variable values not being used.
                filepath_dict.update({filepath:lines_sum})

        return filepath_dict
    
    def get_word(self, line_number, chosen_filepath):
        
        with open(chosen_filepath, 'r') as file:
            for current_line, line in enumerate(file, start=1):
                if current_line == line_number:
                    return line.strip()
                
    def process_wordlist(self, word_length):
        
        filepath_lines_sum = self.count_lines()
        wordlist = []

        while len(wordlist) < word_length:
            
            randomized_filepath_index = random.randint(0,len(self.filepaths) - 1)
            chosen_filepath = self.filepaths[randomized_filepath_index]
        
            line_number = random.randint(1, filepath_lines_sum[chosen_filepath])
            current_word = self.get_word(line_number, chosen_filepath)

            if current_word and current_word not in wordlist:
                wordlist.append(current_word)

        return wordlist
    

class WordCase:

    def __init__(self, wordlist, word_case):
        self.wordlist = wordlist
        self.word_case = word_case
    
    def lowercase(self):
        lowercase_wordlist = [word.lower() for word in self.wordlist]
        return lowercase_wordlist
    
    def uppercase(self):
        uppercase_wordlist = [word.upper() for word in self.wordlist]
        return uppercase_wordlist
    
    def capitalize(self):
        capitalize_wordlist = [word.capitalize() for word in self.wordlist]
        return capitalize_wordlist
    
    def randomize(self):
        randomize_wordlist = []
        for word in self.wordlist:
            randomize_word = ''.join(random.choice([char.upper(), char]) for char in word)
            randomize_wordlist.append(randomize_word)
        return randomize_wordlist
    
    def alternate(self):
        alternate_wordlist = []
        for word in self.wordlist:
            alternate_word = ''.join(char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(word))
            alternate_wordlist.append(alternate_word)
        return alternate_wordlist

    def process(self):
        word_case_method = {
            'lowercase':self.lowercase,
            'uppercase':self.uppercase,
            'capitalize':self.capitalize,
            'randomize':self.randomize,
            'alternate':self.alternate
        }

        if self.word_case in word_case_method:
            return word_case_method[self.word_case]()
        else:
            ValueError(f"ERR01: Unsupported word case method: {self.word_case}")


def banner():

    aspin_banner = """
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
             ████                                               ██                                 
          █    ███                                            ███                                  
          ████  ██              ███                                                                
      █     ███████████          ██       ███       ██                            █████████        
      ████ █████  ███    ███     ██      ███         ███          ████████      █████ ████████     
        ████         █████████   ███    ██████       ████       ████    ██    ███      ███  ███    
       ███         ████     ███  ███  ███    ███    ███       █████     ███  ███       ███   ███   
      ███        ████       ██    ██ ███   ████     ███    ████  ██     ██  ███        ███    ███  
      ███      ████        ██     █████     ███      ███████      █         ███         ██    ███  
       ███  █████                 ████       ███                             ██       ████    ███  
        ██████                       ██   ███████                                     █            
                                   ██████                                          ███████         
                                     ██                                              ██                                                                                   
                                                                                                                       
                                ASPIN: Filipino-centric Passphrase Generator     


\t[+] Generates randomized passphrases
\t[+] Use the `-h` option for help

\t@unclesocks
\thttps://github.com/UncleSocks/aspin-filipino-centric-passphrase-generator
\t-------------------------------------------------------------------------------------------------                                                                                              
    """
    return print(aspin_banner)


def aspin():
    
    banner()

    argument_parser = ArgumentParser()
    argument = argument_parser.parse_arguments()
    init_generate_count = 0

    if argument.interactive:
        user_input_parameters = InteractiveGeneration()
        parameter_output = user_input_parameters.output()

    else:
        parameter_output = argument_parser.argument_output()
        
    word_length, generate_number, separator, separator_count, numbers, special_characters, \
        substitution, word_case, wordlist, wordlist_combine = parameter_parser(parameter_output)
    
    wordlist_list = []
    wordlist_list.append(wordlist)

    if wordlist_combine and wordlist_combine is not None:
        wordlist_list.append(wordlist_combine)
    
    print("\n\tPassphrase Generated:\n\t")
    while init_generate_count < generate_number:
        process_wordlist = WordlistProcess(wordlist_list)

        wordlist = process_wordlist.process_wordlist(word_length)

        multiplied_separator = separator_multiplier(separator, separator_count)
        nums_and_special_chars = NumbersAndSpecialChars(wordlist, word_length)
        wordlist = nums_and_special_chars.special_chars_nums_process(numbers, special_characters)
        
        wordlist = WordCase(wordlist, word_case).process()
        
        passphrase_raw = f'{multiplied_separator}'.join(wordlist)

        if substitution and substitution is not None:
            current_char, new_char = substitution_parser(substitution)
            passphrase_raw = passphrase_raw.replace(current_char, new_char)

        print(f"\t{passphrase_raw}")
        init_generate_count += 1
    print("\n")


if __name__ == "__main__":
    aspin()
