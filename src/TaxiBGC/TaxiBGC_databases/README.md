# TaxiBGC databases

This directory contains databases and shell scripts for running TaxiBGC. 

For predicting BGCs in a metagenome, the TaxiBGC pipeline relies on the TaxiBGC reference database that includes the following files:
1.	BGC_MiBIG_01_13_2022_final.fasta: A FASTA file containing nucleotide sequences of all BGC genes retrieved from the MIBiG database (as of January 2022). This file is required to identify BGC genes through read mapping using BBMap.

2.	BGC_SMs_MiBIG_database.txt: Information about the experimentally characterized BGCs and their known SMs and their respective source organisms obtained from the MIBiG database. The TaxiBGC pipeline uses this file to provide SMs, BGC classes, and source organisms for predicted BGCs.

3.	TaxiBGC_MiBIG_metaphlan_database.txt: A list of BGCs with their source species, which are optained using MetaPhlAn3. This file is required for TaxiBGC to provide the first-pass prediction of BGCs.

4.	TaxiBGC.sh: The shell script of the TaxiBGC pipeline.

5.	BGC_gene_count.awk: The shell script on which the TaxiBGC pipeline relies for calculating the number of BGC genes present in a metagenome.
