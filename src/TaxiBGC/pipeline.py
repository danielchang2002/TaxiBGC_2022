import subprocess
from . import utils
import os

def repair(args):
    subprocess.call(
        [
            "repair.sh",
            f"in1={args.forward}",
            f"in2={args.reverse}",
            "out1=repaired1.fastq",
            "out2=repaired2.fastq",
            "outs=garbage",
        ]
    )

def run(args):
  print(utils.logo())
  repair(args)
  subprocess.call([
    os.path.join(utils.DEFAULT_DB_FOLDER, "TaxiBGC_02_17_2022.sh"),
    "-n",
    str(args.num_threads),
    "-f",
    "repaired1.fastq",
    "-r",
    "repaired2.fastq",
    "-t",
    utils.DEFAULT_DB_FOLDER + "/",
    "-o",
    args.output
  ])

  # cleanup
  subprocess.call([
    "rm",
    "garbage",
    "repaired1.fastq",
    "repaired2.fastq",
  ])
