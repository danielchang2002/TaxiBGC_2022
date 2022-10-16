import subprocess
from . import utils
import os

def repair(args):
    # handle gz case
    forward, reverse = args.forward, args.reverse
    if forward.endswith("gz"): forward = forward[:-3]
    if reverse.endswith("gz"): reverse = reverse[:-3]

    subprocess.call(
        [
            "repair.sh",
            f"in1={forward}",
            f"in2={reverse}",
            "out1=repaired1.fastq",
            "out2=repaired2.fastq",
            "outs=garbage",
        ]
    )

def run(args):
  repair(args)
  subprocess.call([
    os.path.join(utils.DEFAULT_DB_FOLDER, "TaxiBGC.sh"),
    "-n",
    str(args.num_threads),
    "-f",
    "repaired1.fastq",
    "-r",
    "repaired2.fastq",
    "-t",
    utils.DEFAULT_DB_FOLDER + "/",
    "-o",
    args.output,
    "-g",
    str(args.BGC_gene_presence_threshold),
    "-b",
    str(args.BGC_coverage_threshold)
  ])

  # cleanup
  subprocess.call([
    "rm",
    "garbage",
    "repaired1.fastq",
    "repaired2.fastq",
  ])
