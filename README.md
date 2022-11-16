# TaxiBGC: Taxonomy-guided Identification of Biosynthetic Gene Clusters

[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/version.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/platforms.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/license.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/downloads.svg)](https://anaconda.org/danielchang2002/taxibgc)
<!-- [![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/installer/conda.svg)](https://conda.anaconda.org/danielchang2002/taxibgc) -->

### Description
TaxiBGC (Taxonomy-guided Identification of Biosynthetic Gene Clusters) is a computational pipeline for predicting experimentally characterized Biosynthetic Gene Clusters (BGCs) and their known secondary metabolites (SMs) (also called natural products) from shotgun metagenomic sequencing data. 

On a metagenome sample, TaxiBGC performs three major steps:
1. Taxonomic profiling using MetaPhlAn3 (v3.0.13 or higher) to identify BGC-harboring microbial species
2. The first-pass prediction of BGCs through querying these species (identified in the first step) in the TaxiBGC reference database 
3. in silico confirmation of the predicted BGCs (from the second step) based on read mapping (i.e., alignment) using BBMap

If you use TaxiBGC, please cite:

[TaxiBGC: a Taxonomy-guided Approach for Profiling Experimentally Characterized Microbial Biosynthetic Gene Clusters and Secondary Metabolite Production Potential in Metagenomes](https://doi.org/10.1128/msystems.00925-22)
*Gupta et al.* mSystems (2022).

### Installation
To avoid dependency conflicts, please create an isolated conda environment and install TaxiBGC. Installation via conda automatically installs TaxiBGC and its dependencies (bbmap, bowtie2, MetaPhlAn3).

1. Create new conda environment and install taxibgc package
```bash
conda create --name taxibgc_env -c danielchang2002 -c bioconda -c conda-forge taxibgc
```

2. Activate environment
```bash
conda activate taxibgc_env
```

Alternatively (not recommended), the user can clone this repository and install TaxiBGC from the source. For this option, you must manually install dependencies (see conda_recipe/meta.yaml for requirements).

1. Clone this repository
```bash
git clone https://github.com/danielchang2002/TaxiBGC_2022.git
```

2. Install python script
```bash
python setup.py install
```

### Usage

Try downloading and running TaxiBGC on an [example metagenome](https://github.com/danielchang2002/TaxiBGC_2022/tree/main/example).

```bash
Input: Two (forward/reverse) raw fastq (or fastq.gz) files generated from paired-end metagenome reads
Output: Predicted (if any) experimentally characterized BGCs and their known SMs

Usage: taxibgc [-h] -n NUM_THREADS -f FORWARD -r REVERSE -o OUTPUT [-g BGC_GENE_PRESENCE_THRESHOLD] [-b BGC_COVERAGE_THRESHOLD]
* Example usage:

$ ls
.
├── forward.fastq
└── reverse.fastq

$ taxibgc -n 8 -f forward.fastq -r reverse.fastq -o output_prefix

$ ls
.
├── forward.fastq
├── reverse.fastq
├── output_prefix_BGC_FINAL_RESULT.txt
├── output_prefix_BGC_metsp.txt
└── output_prefix_coverage_stats_taxibgc2022.txt

The three output files are: 
(i) output_prefix_BGC_FINAL_RESULT.txt: A list of the predicted biosynthetic gene clusters (i.e., MIBiG BGC IDs), SMs, BGC classes, and source species
(ii) output_prefix_BGC_metsp.txt: MetaPhlAn3 species-level taxonomic profiling output
(iii) output_prefix_coverage_stats_taxibgc2022.txt: BBMAP output

required named arguments:
  -n NUM_THREADS, --num_threads NUM_THREADS
                        number of threads
  -f FORWARD, --forward FORWARD
                        forward-read sequences of the metagenome (.fastq)
  -r REVERSE, --reverse REVERSE
                        reverse-read sequences of the metagenome (.fastq)
  -o OUTPUT, --output OUTPUT
                        prefix to designate output file names
                        
optional arguments:
  -h, --help            show this help message and exit
  -g BGC_GENE_PRESENCE_THRESHOLD, --BGC_gene_presence_threshold 
                        a user-defined BGC gene presence threshold (see description in the TaxiBGC manuscript). default is set to "5" for 5%.
  -b BGC_COVERAGE_THRESHOLD, --BGC_coverage_threshold 
                        a user-defined BGC coverage threshold (see description in the TaxiBGC manuscript). default is set to "10" for 10%.
```

### Runtime
The computation runtime depends on the size of the input metagenome and the specs of the computer system. On a 2019 MacBook Pro with a 2.3 GHz 8-Core Intel Core i9 processor and 16GB of RAM, a single run of TaxiBGC on an input metagenome of approximately 4 GB takes about half an hour. Please note that the initial run on any machine will take extra time because databases will need to be downloaded and installed prior to the actual computation.

