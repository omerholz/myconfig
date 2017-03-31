from configparser import SafeConfigParser, ConfigParser, SectionProxy
import os

class SectionWrapper(SectionProxy):
    @classmethod
    def wrap_section(cls,x):
        if isinstance(x,SectionProxy):
            x.__class__ = cls
        return x

    def __getattr__(self, name):
        return self.wrap_section(self[name])

class ConfigWrapper(SafeConfigParser):
    def __getattr__(self, name):
        return SectionWrapper.wrap_section(self[name])

    def optionxform(self, optionstr):
        return optionstr

CONFIG = ConfigWrapper(os.environ)
