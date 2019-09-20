"""
Virtual Memory sysctl knobs [WIP]
===========================

This parser provides a representation of all files in the /proc/sys/vm/
directory. The current plan is to create a dictionary with filenames as keys and
suitable value representations


"""


# Different outputs when run with and without root, should non-root execution be valid?

import os
from insights.specs import Specs
from insights import parser, Parser, CommandParser

"""
Get sysctl vm knobs
"""
@parser(Specs.sysctl)
class ProcSysVm(CommandParser):
    def parse_content(self, content):
        # print("content: ", content)
        all_sysctls = content
        
        return all_sysctls
        


