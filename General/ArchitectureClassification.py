class ArchitectureClassification:

    cache = "Cache"
    dir = "Dir"
    mem = "Memory"

    def __init__(self, parser, arch_name: str):
        self.arch_type = self._test_arch(parser, arch_name)
        pass

    def _test_arch(self, parser, arch_name: str):
        if arch_name in parser.cacheNode:
            return self.cache
        elif arch_name in parser.dirNode:
            return self.dir
        elif arch_name in parser.memNode:
            return self.mem
        elif arch_name == self.cache or arch_name == self.dir or arch_name == self.mem:
            return arch_name
        else:
            assert 0, "Unknown architecture classification"

    def test_cache(self) -> bool:
        if self.arch_type == self.cache:
            return True
        return False

    def test_dir(self) -> bool:
        if self.arch_type == self.dir:
            return True
        return False

    def test_mem(self) -> bool:
        if self.arch_type == self.mem:
            return True
        return False
