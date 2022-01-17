#!/usr/bin/env python
import sys
import re


def valid_password_counter(filepath):
    """Counts valid passwords in the given file."""
    pattern = re.compile(r'\s*(.)\s+(\d+)-(\d+):\s+(.*)') # \s* and \s+ were added for space character resilence
    count = 0
    with open(filepath, 'r') as file:
        for line in file:
            matchobj = re.match(pattern, line)
            if matchobj:
                char, min_cnt, max_cnt, password = matchobj.groups()
                count += int(min_cnt) <= password.count(char) <= int(max_cnt)
    return count


if __name__ == '__main__':
    # Get the file path
    args = sys.argv
    filepath = args[1] if len(args) == 2 else raw_input('Enter path to your text file: ')

    cnt = valid_password_counter(filepath)

    # Pretty print
    verb, ending = ('is', '') if cnt == 1 else ('are', 's')
    print('There {} {} valid password{} in the file.'.format(verb, cnt, ending))
