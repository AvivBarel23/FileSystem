class FileNode:
    def __init__(self, name, content=None):
        self.name = name
        self.content = content

    def to_list(self):
        return [self.name]


class DirNode:
    def __init__(self):
        self.content = {}

    def add_file(self, name, content):
        self.content[name] = FileNode(name, content)

    def add_dir(self, name):
        self.content[name] = DirNode()

    def get(self, name):
        return self.content.get(name, None)

    def is_empty(self):
        return self.content is None

    def to_list(self):
        return sorted([k for k in self.content.keys()])


class FileSystem:
    def __init__(self):
        self.root = DirNode()

    def mkdir_rec(self, path, root):
        name = path[0]
        if len(path) == 1:
            root.add_dir(name)
            return
        if root.get(name) is None:
            root.add_dir(name)
        self.mkdir_rec(path[1:], root.get(name))

    def mkdir(self, path):
        path_list = path[1:].split('/')
        return self.mkdir_rec(path_list, self.root)

    def ls_rec(self, path, root):
        name = path[0]
        if len(path) == 1:
            f=root.get(name)
            l=f.to_list()
            return l
        else:
            return self.ls_rec(path[1:], root.get(name))

    def ls(self, path):
        if path == "/":
            return self.root.to_list()
        path_list = path[1:].split('/')
        return self.ls_rec(path_list, self.root)

    def create_file_rec(self, path, root, content):
        name = path[0]
        if len(path) == 1:
            root.add_file(name, content)
            return
        if root.get(name) is None:
            root.add_dir(name)
        self.create_file_rec(path[1:], root.get(name), content)

    def create_file(self, path, content):
        path_list = path[1:].split('/')
        return self.create_file_rec(path_list, self.root, content)
