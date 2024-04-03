# build a program to convert from the bianry file that is produced by the vbcc to a hex rom file that can be read by logisim.
import sys

MAXPROGRAMLENGTH = 200

def logisim():
    filename = "out.rom"
    append_copy = open(filename, "rb")
    original_text = str(append_copy.read())
    append_copy.close()

    original_text = original_text[1:]
    original_text = original_text.replace("'", "")
    original_text = original_text.replace('\\x', " ")
    original_text = original_text[1:]

    original_text_sections = original_text.split(" ")
    for i in range(200):
        if len(original_text_sections[i]) > 2:
            original_text_sections[i] = original_text_sections[i][:2]
    original_text = " ".join(original_text_sections)

    append_copy = open(filename, "w")
    append_copy.write("v2.0 raw\n")
    append_copy.write(original_text)
    append_copy.close()

def phys():
    print("Still working!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        phys()
    else:
        if sys.argv[1] == "-phys":
            phys()
        elif sys.argv[1] == "-logisim":
            print("Logisim convertion!")
            logisim()
    