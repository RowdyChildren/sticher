from glob import glob
import json
import re
class Sticher(object):
    """a object that takes prestich files and adds the appropreate blocks to
    them then outputs them to the output directory"""
    def __init__(self):
        self.block_path = ""
        self.file_path = ""
        self.out_path = ""
        self.matchblock = re.compile("\s*<\s*blockhtml\s*src=[\'\"].*[\'\"]\s*/>")
        self.read_config()
        self.files = self.load(self.file_path)
        self.blocks = self.load(self.block_path)
    """find all files in a dir and loops thru them
    geting all the file names and contents, then ziping
    them to a dict """
    def load(self, dir):
        names = glob(dir+"*.*")
        contents = []
        for n in names:
            contents.append(open(n).read())
            n =  n[len(dir):]
            print(n)
        print('load complete')
        print('names: ' + repr(names))
        return dict(zip(names, contents))
    def read_config(self):
        config = json.loads(open("stichconf.json").read())
        self.file_path = config["file_path"]
        self.block_path = config["block_path"]
        self.out_path = config["out_path"]
        print('out path: ' + self.out_path + '\n')
        print('file path: ' + self.file_path + '\n')
        print('block path: ' + self.block_path + '\n')
        print('read config complete')
        pass
    def stich_file(self, file_name):
        print('searching file:' + file_name)
        temp_file = self.files[file_name].split("\n")
        new_file = open(self.out_path + file_name[len(self.file_path):], 'w')
        for l in temp_file:
            if self.matchblock.match(l):
                print('found match')
                block_name = re.search("(?<=src=[\"|\'])\w+\.\w+", l).group(0)
                l = self.blocks[self.block_path + block_name]
            new_file.write(l+"\n")
        new_file.close()
    def stich_all(self):
        for f in self.files:
            self.stich_file(f)
