import os
import sys

def get_name(filename):
	return ""

def get_voucher_number(filename):
	# &vDRMDNA2303_&
	voucher_pattern = "&vDRM"
	beg_voucher_text_index = filename.find(voucher_pattern)

	if beg_voucher_text_index == -1:
		return ""

	beg_voucher_text_index += len(voucher_pattern)
	end_voucher_text_index = filename.find("_&", beg_voucher_text_index)
	return filename[beg_voucher_text_index : end_voucher_text_index]

def get_genbank_accession_number(filename):
	# _&aKJ624355_&
	genbank_pattern = "_&a"
	beg_genbank_text_index = filename.find(genbank_pattern)

	if beg_genbank_text_index == -1:
		return ""

	beg_genbank_text_index += len(genbank_pattern)
	end_genbank_text_index = filename.find("_&", beg_genbank_text_index)
	return filename[beg_genbank_text_index : end_genbank_text_index]

def get_sequence_type(filename):
	return "DNA"

def get_sequence(filename):
	with open(filename, 'r') as f:
		return f.read().split('\n')[1]

	return ""

def save_file(filename, file_content):
	with open(filename, 'w') as f:
		f.write(file_content)

def main(argv):
	if len(argv) < 2:
		print("Filename for csv file containing GenBank Sequences must be provided!")
		return

	new_filename = argv[1]
	file_headers = ["name", "voucher_number", "genbank_accession_number", "sequence_type", "sequence"]
	file_content = ""

	for header in file_headers:
		file_content += header + "\t"

	file_content += "\n"

	for filename in os.listdir(os.getcwd()):
		if filename[0] != "&":
			continue
		
		print(filename)
		print("\t" + get_name(filename))

		file_content += get_name(filename) + "\t"
		file_content += get_voucher_number(filename) + "\t"
		file_content += get_genbank_accession_number(filename) + "\t"
		file_content += get_sequence_type(filename) + "\t"
		file_content += get_sequence(filename) + "\t"
		file_content += "\n"

	save_file(new_filename, file_content)

if __name__ == "__main__":
	main(sys.argv)