import os
import sys
from . import utils
import argparse
from . import prerun
from . import pipeline
import argparse
import subprocess
from argparse import RawTextHelpFormatter

__author__ = "Daniel Chang, Vinod Gupta, Jaeyun Sung"
__version__ = "1.0"

def main():
    parser = argparse.ArgumentParser(
        description="\n" + utils.logo() + 
        "\n\nDESCRIPTION:\n"
        "TaxiBGC version " + __version__ + " \n"
        "TaxiBGC (Taxonomy-guided Identification of Biosynthetic Gene Clusters) is an original"
        " computational pipeline that predicts experimentally characterized BGCs" 
        " and their known SM products from shotgun metagenomic data.\n\n"
        "AUTHORS: \n" + __author__ + "\n\n"
        "USAGE: \n"
        "TaxiBGC is a pipeline that takes as input two raw fastq (or fastq.gz) files generated "
        "from a paired-end metagenome, "
        "estimates microbial abundances, "
        "and using these microbial estimates, "
        "returns as outputs the predictions of experimentally characterized BGCs\n\n"
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
        "└── output_prefix_covstats_taxibgc2022.txt\n\n"
        "The three output files are: \n"
        "(i) output_prefix_BGC_FINAL_RESULT.txt: A list of the predicted biosynthetic gene clusters\n"
        "(ii) output_prefix_BGC_metsp.txt: MetaPhlAn3 taxonomic profiling output\n"
        "(iii) output_prefix_covstats_taxibgc2022.txt: BBMAP output",
        formatter_class=RawTextHelpFormatter,
    )
    requiredNamed = parser.add_argument_group("required named arguments")
    requiredNamed.add_argument(
        "-n", "--num_threads", required=True, help="number of threads", type=int
    )
    requiredNamed.add_argument(
        "-f", "--forward", required=True, help="forward-read of metagenome (.fastq)", type=str
    )
    requiredNamed.add_argument(
        "-r", "--reverse", required=True, help="reverse-read of metagenome (.fastq)", type=str
    )
    requiredNamed.add_argument(
        "-o", "--output", required=True, help="prefix to designate output file names", type=str
    )
    parser.add_argument(
        "-g", "--BGC_gene_presence_threshold", required=False, default=5, 
        help="BGC gene presence threshold for predicting BGCs from the metagenomes", 
        type=int
    )
    parser.add_argument(
        "-b", "--BGC_coverage_threshold", required=False, default=10, 
        help="BGC coverage threshold for predicting BGCs from the metagenomes", 
        type=int
    )

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()
    forward, reverse = args.forward, args.reverse
    if not os.path.exists(forward) or not os.path.exists(reverse):
        print("input file(s) do not exist")
        return

    print(utils.logo())
    print()
    
    up_to_date = prerun.check_dependencies()
    if not up_to_date:
        return
        
    # check forward file
    if forward.endswith("fastq.gz"):
        # unzip command
        print("unzipping", forward)
        subprocess.call(["gunzip", forward])
        forward = forward[:-3]
    if forward.split(".")[-1] != "fastq":
        print("invalid input file extensions")
        return
    
    # check reverse file
    if reverse.endswith("fastq.gz"):
        # unzip command
        print("unzipping", reverse)
        subprocess.call(["gunzip", reverse])
        reverse = reverse[:-3]
    if reverse.split(".")[-1] != "fastq":
        print("invalid input file extensions")
        return

    pipeline.run(args)

if __name__ == "__main__":
    main()
