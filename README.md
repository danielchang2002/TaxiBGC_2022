# TaxiBGC: Taxonomy-guided Identification of Biosynthetic Gene Clusters

[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/version.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/platforms.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/license.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/downloads.svg)](https://anaconda.org/danielchang2002/taxibgc)
[![Anaconda-Server Badge](https://anaconda.org/danielchang2002/taxibgc/badges/installer/conda.svg)](https://conda.anaconda.org/danielchang2002/taxibgc)


### Description
TaxiBGC is a Taxonomy-guided Approach for the Identification of 
Experimentally Verified Microbial Biosynthetic Gene Clusters 
in Shotgun Metagenomic Data.

### Installation
To avoid dependency conflicts, create an isolated conda environment and install TaxiBGC

1. Create new conda environment and install taxibgc package
```bash
conda create --name taxibgc_env \
  -c danielchang2002 \
  -c bioconda
  -c conda-forge
   taxibgc
```

2. Activate environment
```bash
conda activate taxibgc_env
```

### Usage
```bash
usage: taxibgc [-h] -n NUM_THREADS -f FORWARD -r REVERSE -o OUTPUT

DESCRIPTION:
TaxiBGC version 1.0
TaxiBGC (Taxonomy-guided Identification of Biosynthetic Gene Clusters) 
is an original computational pipeline that identifies experimentally 
verified BGCs from shotgun metagenomic data and infers 
their known SM products.

AUTHORS:
Daniel Chang, Vinod Gupta, Jaeyun Sung

USAGE:
TaxiBGC is a pipeline that takes as input two raw fastq files generated 
from a paired end sequence, estimates microbial abundances, and using 
these microbial estimates, returns as output predictions of 
experimentally verified BGCs.

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
└── output_prefix_covstats_taxigc2022.txt

The three output files are 
(i) Biosynthetic gene clusters identified
(ii) the MetaPhlAn taxonomic profiling output
(iii) the bbmap output.

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -n NUM_THREADS, --num_threads NUM_THREADS
                        number of threads
  -f FORWARD, --forward FORWARD
                        forward read of metagenome (.fastq)
  -r REVERSE, --reverse REVERSE
                        reverse read of metagenome (.fastq)
  -o OUTPUT, --output OUTPUT
                        prefix for output file names
```

### Runtime
Runtime depends on the size of the input metagenome and the system specs.

On a 2019 MacBook Pro with a 2.3 GHz 8-Core Intel Core i9 processor and 16GB of RAM, a single run of taxibgc on an input metagenome of 4 GB takes about half an hour.

Note: the initial run on any machine will take extra time because databases will need to be downloaded and installed before the actual computation.