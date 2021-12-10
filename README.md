# Convert_tsv_to_embl
This script is designed to convert a tsv file of known repetitive and prophage reigions to be excluded from alignments and convert these into an embl format compatible with remove_blocks_from_aln.py (available at: https://github.com/sanger-pathogens/remove_blocks_from_aln)


## Usage
```python2 convert_csv_embl.py --excluded_regions CT18_repeats_phages_excluded_regions.tsv --output_prefix converted_file```
