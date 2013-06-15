from glob import glob
import json
import re
class Sticher(object):
    """a object that takes prestich files and adds the appropreate blocks to 
    them then outputs them to the output directory"""
    def __init__(self):
        self.files = {}
        self.blocks = {}
        self.block_path = ""
        self.file_path = ""
        self.out_path = ""
        self.matchblock = re.compile("\s*<\s*blockhtml\s*src=[\'\"].*[\'\"]\s*/>")
        self.read_config()
        self.load_blocks()
        self.load_files()
    def load_files(self):
        file_names = glob(self.file_path+"*.*")
        file_contents = []
        for f in file_names:
            file_contents.append(open(f).read())
            f =  f[len(self.file_path):]
        self.files = dict(zip(file_names, file_contents))
    def load_blocks(self):
        block_names = glob(self.block_path+"*.*")
        block_contents = []
        for n in block_names:
            block_contents.append(open(n).read())
            n =  n[len(self.block_path):]
        self.blocks = dict(zip(block_names, block_contents))
    def read_config(self):
        config = json.loads(open("stichconf.json").read())
        self.file_path = config["file_path"]
        self.block_path = config["block_path"]
        self.out_path = config["out_path"]
        pass
    def stich_file(self, file_name):
        temp_file = self.files[file_name].split("\n")
        new_file = open(self.out_path + file_name[len(self.file_path):], 'w')
        for l in temp_file:
            if self.matchblock.match(l):
                block_name = re.search("(?<=src=[\"|\'])\w+\.\w+", l).group(0)
                l = self.blocks[self.block_path + block_name]
            new_file.write(l+"\n")
    def stich_all(self):
        for f in self.files:
            self.stich_file(f)