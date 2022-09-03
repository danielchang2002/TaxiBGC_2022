# Example TaxiBGC usage

TaxiBGC is a pipeline that takes as input two raw fastq (or fastq.gz) files generated 
from a paired end sequence, estimates microbial abundances, and using 
these microbial estimates, returns as output predictions of 
experimentally verified BGCs.

Below is a mini-tutorial on how to download SRA data from the run accession SRR6915153 and use TaxiBGC on the downloaded .fastq files.

## Download and uncompress fastq files using [sra-tools](https://github.com/ncbi/sra-tools/wiki/)

```bash
prefetch SRR6915153
cd SRR6915153
fasterq-dump --split-spot SRR6915153.sra --skip-technical --split-files
```

Output:
```bash
.
├── SRR6915153.sra
├── SRR6915153_1.fastq
└── SRR6915153_2.fastq
```

## Run taxibgc on the extracted metagenome
```bash
taxibgc -n 8 -f SRR6915153_1.fastq -r SRR6915153_2.fastq -o SRR6915153
```

Output:
```bash
.
├── SRR6915153.sra
├── SRR6915153_1.fastq
├── SRR6915153_2.fastq
├── SRR6915153_BGC_FINAL_RESULT.txt
├── SRR6915153_BGC_metsp.txt
└── SRR6915153_covstats_taxigc2022.txt
```

## Verify that the produced output files are identical to those in this directory
Note: slight differences in output may be present due to updated marker databases 

```bash
head *.txt
```

Output:
```bash
==> SRR6915153_BGC_FINAL_RESULT.txt <==
BGC0000552      SmbA, SmbB      Lanthipeptide   Streptococcus mutans
BGC0000530      mutacin B-Ny266 Lanthipeptide   Streptococcus mutans N66
BGC0000522      lacticin Z      Lanthipeptide   Lactococcus lactis
BGC0000538      nisin Z Lanthipeptide   Lactococcus lactis
BGC0000764      exopolysaccharide       Saccharide      Lactococcus lactis
BGC0000535      nisin A Lanthipeptide   Lactococcus lactis subsp. lactis
BGC0000523      lactocin S      Lanthipeptide   Lactobacillus sakei
BGC0000619      gassericin T    RiPP    Lactobacillus gasseri
BGC0001388      gassericin E    RiPP    Lactobacillus gasseri
BGC0001601      gassericin-S    RiPP    Lactobacillus gasseri

==> SRR6915153_BGC_metsp.txt <==
s__Eubacterium_eligens_CAG_72
s__Alistipes_sp
s__Bacteroides_sp_3_1_40A
s__Ruminococcus_bicirculans     2|1239|186801|186802|541000|1263|1160721        3.4851072768608917
s__Bacteroides_plebeius_CAG_211
s__Eubacterium_sp_CAG_251       2|1239|186801|186802|186806|1730|1262886        2.040197340977951
s__Alistipes_putredinis_CAG_67
s__Lachnospira_pectinoschiza    2|1239|186801|186802|186803|28050|28052 1.338940392288483
s__Ruminococcus_torques 2|1239|186801|186802|186803|572511|33039        1.22351251200625
s__Dorea_longicatena    2|1239|186801|186802|186803|189330|88431        1.177466320099923

==> SRR6915153_covstats_taxigc2022.txt <==
#ID     Avg_fold        Length  Ref_GC  Covered_percent Covered_bases   Plus_reads      Minus_reads     Read_GC Median_fold  Std_Dev
BGC0000001_orfP_1       0.0000  1083    0.7138  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_NULL_2       0.0000  627     0.6794  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyR_3       0.0000  747     0.6961  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyX_4       0.0000  1191    0.6986  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyH_5       0.0000  2670    0.7502  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyI_6       0.0000  759     0.7101  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyK_7       0.0000  1860    0.7161  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyA1_8      0.0000  1026    0.7212  0.0000  0       0       0       0.0000  0       0.00
BGC0000001_abyA2_9      0.0000  1869    0.7309  0.0000  0       0       0       0.0000  0       0.00
```
