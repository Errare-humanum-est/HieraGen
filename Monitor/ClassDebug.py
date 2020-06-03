from colorama import init, Fore, Style
from tabulate import tabulate

# include logger functionality


class Debug:

    spacer = "\n\n\n"

    def __init__(self, debug_enabled: bool = False):

        self.dbg: bool = debug_enabled
        init()

    def pheader(self, header: str = ''):
        if self.dbg:
            print(Fore.LIGHTBLUE_EX + header + Style.RESET_ALL)

    def pdebug(self, debug: str = ''):
        if self.dbg:
            print(debug)

    def pdebugwarning(self, warning: str = ''):
        if self.dbg:
            print(Fore.YELLOW + warning + Style.RESET_ALL)

    @ staticmethod
    def psection(section_name: str = ''):
        print(Fore.CYAN + section_name + Style.RESET_ALL)

    @ staticmethod
    def pwarning(warning: str = ''):
        print(Fore.MAGENTA + warning + Style.RESET_ALL)

    @ staticmethod
    def perror(error: str = '', cond=0):
        error = Fore.RED + error + Style.RESET_ALL
        assert cond, error

    @ staticmethod
    def psuccess(successmsg: str = ''):
        print(Fore.GREEN + successmsg + Style.RESET_ALL)

    def ptable(self, header, body):
        if self.dbg:
            assert isinstance(header, list) and isinstance(body, list)

            for ind in range(0, len(header)):
                header[ind] = Fore.GREEN + header[ind]

                if ind == len(header)-1:
                    header[ind] += Style.RESET_ALL

            print(tabulate(body, headers=header))
