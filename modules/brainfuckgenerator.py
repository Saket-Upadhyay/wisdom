class BFGenerator(object):
    def text_to_brainfuck(self, data):

        glyphs = len(set([c for c in data]))
        number_of_bins = max(max([ord(c) for c in data]) // glyphs, 1)

        bins = [(i + 1) * number_of_bins for i in range(glyphs)]
        code = "+" * number_of_bins + "["
        code += "".join([">" + ("+" * (i + 1)) for i in range(1, glyphs)])
        code += "<" * (glyphs - 1) + "-]"
        code += "+" * number_of_bins
        current_bin = 0
        for char in data:
            new_bin = [abs(ord(char) - b)
                       for b in bins].index(min([abs(ord(char) - b)
                                                 for b in bins]))
            appending_character = ""
            if new_bin - current_bin > 0:
                appending_character = ">"
            else:
                appending_character = "<"
            code += appending_character * abs(new_bin - current_bin)
            if ord(char) - bins[new_bin] > 0:
                appending_character = "+"
            else:
                appending_character = "-"
            code += (appending_character * abs(ord(char) - bins[new_bin])) + "."
            current_bin = new_bin
            bins[new_bin] = ord(char)
        return code


if __name__ == "__main__":
    bfg = BFGenerator()
    print(bfg.text_to_brainfuck(input("Set text>")))
