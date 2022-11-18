# -*- coding: utf-8 -*-

import collections

def build_index(source):
    """ Build index in markdown from given markdown source """
    index = ''
    title_nums = collections.deque([0])
    for row in source.split("\n"):
        stripped_row = row.strip()
        tokens = stripped_row.split(" ")
        if len(tokens) and len(tokens[0]) and \
                all(map(lambda c: c == '#', tokens[0])):
            curr_head_depth = len(tokens[0])
            if curr_head_depth == len(title_nums):
                title_nums.append(title_nums.pop()+1)
            elif curr_head_depth > len(title_nums):
                while curr_head_depth > len(title_nums):
                    title_nums.append(1)
            else:
                while curr_head_depth <= len(title_nums):
                    new_title_num = title_nums.pop()+1
                title_nums.append(new_title_num)
            index += " "*4*(len(title_nums)-1)
            index += str(title_nums[-1])
            index += ". ["
            index += stripped_row[len(title_nums):].strip()
            index += "](#"
            index += "-".join(map(lambda s: s.strip().lower(),tokens[1:]))
            index += ")\n"
    return index
