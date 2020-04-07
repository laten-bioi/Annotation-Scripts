fname = input("Enter file name: ")
fh = open(fname)    # open the repens_scaffolds.fsa.mod.LTRlib file
for line in fh:
    nline = line.rstrip()
    if not nline.startswith('>'):
        print(nline)
