class TrieNode:
    _children = {}
    _end_of_word = False

    def __init__(self):
        self._children = {}
        self._end_of_word = False


class Trie:
    _root = []

    def __init__(self, directed: bool = False):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        current = self._root

        for c in word:
            if c not in current._children:
                current._children[c] = TrieNode()

            current = current._children[c]
        current._end_of_word = True

    def search(self, word: str) -> bool:
        current = self._root

        for c in word:
            if c not in current._children:
                return False

            current = current._children[c]
        return current._end_of_word

    def starts_width(self, prefix: str) -> bool:
        current = self._root
        for c in prefix:
            if c not in current._children:
                return False
            current = current._children[c]
        return True


def add_words_from_file_to_trie(file_name, trie):
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip().strip('.,?!"\'').lower()
                if word:
                    trie.insert(word)


trie = Trie()
add_words_from_file_to_trie('Tareas\Tarea6\story.txt', trie)

# Search words
print("Search words")
print("Search because: ", trie.search("because"))
print("Search gone: ", trie.search("gone"))
print("Search adamantly: ", trie.search("adamantly"))
print("Search me: ", trie.search("me"))
print("Search mug: ", trie.search("mug"))
print("Search knowing: ", trie.search("knowing"))
print("Search frowned: ", trie.search("frowned"))
print("Search reversible: ", trie.search("reversible"))
print("Search swiftly: ", trie.search("swiftly"))
print("Search grapes: ", trie.search("grapes"))
print("Search scowled: ", trie.search("scowled"))
print("Search doctor: ", trie.search("doctor"))
print("Search rapid: ", trie.search("rapid"))
print("Search dimension: ", trie.search("dimension"))
print("Search library: ", trie.search("library"))
print("Search termometer: ", trie.search("termometer"))
print("Search jungle: ", trie.search("jungle"))
print("Search magic: ", trie.search("magic"))
print("Search stir: ", trie.search("stir"))
print("Search share: ", trie.search("share"))
print("Search chart: ", trie.search("chart"))

# Search prefixes
print("\nSearch prefixes")
print("Search go: ", trie.starts_width("go"))
print("Search ada: ", trie.starts_width("ada"))
print("Search me: ", trie.starts_width("me"))
print("Search mug: ", trie.starts_width("mug"))
print("Search know: ", trie.starts_width("know"))
print("Search frow: ", trie.starts_width("frow"))
print("Search swift: ", trie.starts_width("swift"))
print("Search gra: ", trie.starts_width("gra"))
print("Search scow: ", trie.starts_width("scow"))
print("Search doc: ", trie.starts_width("doc"))
print("Search sw: ", trie.starts_width("sw"))
print("Search rap: ", trie.starts_width("rap"))
print("Search dim: ", trie.starts_width("dim"))
print("Search lib: ", trie.starts_width("lib"))
print("Search term: ", trie.starts_width("term"))
print("Search jung: ", trie.starts_width("jung"))
print("Search mag: ", trie.starts_width("mag"))
print("Search stir: ", trie.starts_width("stir"))
print("Search sha: ", trie.starts_width("sha"))
print("Search char: ", trie.starts_width("char"))