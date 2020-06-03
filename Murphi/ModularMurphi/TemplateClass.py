import inspect
import os
import re


class TemplateHandler:

    # Constant definitions
    tab = "  "
    nl = "\n"
    sem = ";"
    end = sem + nl

    def __init__(self, template_dir: str):
        self.templatepath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + \
                            "/../" + template_dir

    ####################################################################################################################
    # REPLACE DYNAMIC
    ####################################################################################################################
    def _openTemplate(self, filename):
        return re.sub(r'^\#.*\n?', '', open(self.templatepath + "/" + filename, "r").read(), flags=re.MULTILINE)

    def _stringReplKeys(self, refstring, replacekeys):
        inputstr = refstring
        for ind in range(0, len(replacekeys)):
            inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])
        return inputstr

    def _stringRepl(self, string, ind, keyword):
        return re.sub(r"\$" + str(ind) + "\$", keyword, string)

    def _addtabs(self, string, count):
        tabstring = ""
        for ind in range(0, count):
            tabstring += self.tab

        outstr = ""
        for line in string.splitlines():
            outstr += tabstring + line + self.nl

        return outstr

    @staticmethod
    def _testInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def _testOperator(string):
        if string.isalpha():
            return True
        return False
