
import os

input_file = "/Users/.../dmel_all_genes_r6.18_try.fasta"
output_dir = "/Users/../multifasta_to_fasta/data"

with open(input_file) as f:
    content = f.readlines()
content = [x.strip() for x in content]
#print(content)

full_text = "".join(content);

#print(full_text)
count = 0
for fasta in full_text.split(">"):
	count += 1
	fasta = fasta.replace(" ", "")
	sequence = ">" + fasta.split(";")[-1]
	#sequence = sequence[:-1]
	loc_param = ""
	id_param = ""
	#print(fasta)
	#print(sequence)
	#if count is 2:
	#	pass
	#	#sys.exit(0)
	for param in fasta.split(";"):
		if param.startswith("ID="):
			id_param = param.split("=")[-1]
		if param.startswith("loc="):
			loc_param = param.split("=")[-1]
			loc_param = loc_param.split(":")[0]		
	fasta_file_name = str(loc_param) + "_" + str(id_param)
	#print("file=" + str(fasta_file_name))

	with open(fasta_file_name, "w") as text_file:
    		text_file.write(sequence)
		
		
	