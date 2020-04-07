# read in the output from LTR Retriever, which will contain all the LTRs
# as each LTR is read in, create a new TransposableElement object, and store it in a data structure (either list or dictionary)
# the rough loop outline should be:
        # for each line that starts with >
            # that line is the header, which needs to be parsed to obtain the id, scaffoldNum, location, and superfamily
                    # from > until .        id
                    # from . until :        scaffoldNum
                    # from : until _        location
                    # from _ until end      superfamily
            # the next line is the sequence
        # create a new TransposableElement object with those parameters
        # add the new TransposableElement in a dictionary, with the key as the id and the value as the object
# the resulting data structure will contain all of the LTRs from the output of LTR Retriever

# the next step: for every TransposableElement "tElement", BLASTx tElement.sequence against the protein database
# capture the results of the BLAST in some output file
class TransposableElement:
    def __init__(self, id, scaffoldNum, location, superfamily, sequence):
        self.id = id
        self.scaffoldNum = scaffoldNum
        self.location = location
        self.superfamily = superfamily
        self.sequence = sequence
        locationPoints = location.split("..")
        self.locationStart = locationPoints[0]
        self.locationEnd = locationPoints[1]

    def __str__(self):
        return self.sequence


fname = input("Enter file name: ")
fh = open(fname)    # open the repens_scaffolds.fsa.mod.LTRlib file
trans_elem_dictionary = dict()  # create empty dictionary to store all of the transposable element objects
current_trans_elem_id = 'blank'

for line in fh:

    nline = line.rstrip()

    if nline.startswith('>'):   # if starts with >, then it is the header
        element_id = nline  # get the id
        current_trans_elem_id = element_id

        element_scaffoldNum = nline[14] # get scaffold number

        loc_nline_list1 = nline.split(':') # get the start..end location
        loc_nline = loc_nline_list1[1]
        loc_nline_list2 = loc_nline.split('_')
        element_location = loc_nline_list2[0]

        sfam_nline_list = loc_nline_list2[1].split('/') # get the superfamily
        element_superfamily = sfam_nline_list[1]

        element_sequence = 'blank'  # right now, we do not have the sequence

        transElem = TransposableElement(element_id, element_scaffoldNum, element_location, element_superfamily, element_sequence)   # create a TransposableElement object with those parameters
        trans_elem_dictionary[transElem.id] = transElem # add the object into the dictionary

    if not nline.startswith('>'):   # if the line doesn't start with >, then it is the sequence
        element_sequence = nline
        trans_elem_dictionary[current_trans_elem_id].sequence = element_sequence    # find the corresponding TransposableElement to the id and update the sequence


# PART 2 - calling BLAST

#from Bio.Blast import NCBIWWW
#sequence = """GGAGGATATATTCAAC"""
#blast_handle = NCBIWWW.qblast('blastn', 'nr', sequence)
#blast_handle.seek(0)
#blast_file = open('blast-output.xml', 'w')
#blast_file.write(blast_handle.read())
#blast_file.close()
