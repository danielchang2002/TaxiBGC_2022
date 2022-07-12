import os
import argparse
from . import prerun
from . import pipeline
import argparse
from argparse import RawTextHelpFormatter

__author__ = "Daniel Chang, Vinod Gupta, Jaeyun Sung"
__version__ = "1.0"


def main():
    parser = argparse.ArgumentParser(
        description="DESCRIPTION:\n"
        "TaxiBGC version " + __version__ + " \n"
        "TaxiBGC (Taxonomy-guided Identification of Biosynthetic Gene Clusters) is an original"
        " computational pipeline that identifies experimentally verified BGCs" 
        " from shotgun metagenomic data and infers their known SM products.\n\n"
        "AUTHORS: \n" + __author__ + "\n\n"
        "USAGE: \n"
        "TaxiBGC is a pipeline that takes as input two raw fastq files generated "
        "from a paired end sequence, "
        "estimates microbial abundances, "
        "and using these microbial estimates, "
        "returns as output predictions of experimentally verified BGCs\n\n"
        "* Example usage:\n\n"
        "$ ls\n"
        ".\n"
        "├── forward.fastq\n"
        "└── reverse.fastq\n\n"
        "$ taxibgc -n 8 -f forward.fastq -r reverse.fastq -o output_prefix\n\n"
        "$ ls\n"
        ".\n"
        "├── forward.fastq\n"
        "├── reverse.fastq\n"
        "├── output_prefix_BGC_FINAL_RESULT.txt\n"
        "├── output_prefix_BGC_metsp.txt\n"
        "└── output_prefix_covstats_taxigc2022.txt\n\n"
        "The three output files are (i) Biosynthetic gene clusters identified,"
        " (ii) the MetaPhlAn taxonomic profiling output, and (iii) the bbmap output.",
        formatter_class=RawTextHelpFormatter,
    )
    requiredNamed = parser.add_argument_group("required named arguments")
    requiredNamed.add_argument(
        "-n", "--num_threads", required=True, help="number of threads", type=int
    )
    requiredNamed.add_argument(
        "-f", "--forward", required=True, help="forward read of metagenome (.fastq)", type=str
    )
    requiredNamed.add_argument(
        "-r", "--reverse", required=True, help="reverse read of metagenome (.fastq)", type=str
    )
    requiredNamed.add_argument(
        "-o", "--output", required=True, help="prefix for output file names", type=int
    )

    args = parser.parse_args()

    forward, reverse = args.f, args.r

    print("Inputs:", forward, reverse)
    if not os.path.exists(forward) or not os.path.exists(reverse):
        print("file(s) do not exist")
        return
    if forward.split(".")[-1] != "fastq" or reverse.split(".")[-1] != "fastq":
        print("invalid file extensions")
        return

    up_to_date = prerun.check_versions()
    if not up_to_date:
        return
    pipeline.run(args)

if __name__ == "__main__":
    main()