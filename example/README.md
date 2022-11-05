# Example usage of TaxiBGC

TaxiBGC is a computational pipeline that takes as inputs two raw fastq (or fastq.gz) files generated 
from paired-end metagenome reads; performs taxonomic profiling to identify BGC-harboring microbial species; and returns as outputs the predictions of 
experimentally characterized biosynthetic gene clusters (BGCs), their known secondary metabolites (SMs), and their source BGC-harboring species.

Below is a mini-tutorial on how to download a metagenome sample (run accession SRR6915153) from the Sequence Read Archive (SRA) and use TaxiBGC on the downloaded .fastq files.

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

## Run TaxiBGC on the extracted paired-end metagenome reads
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
└── SRR6915153_coverage_stats_taxibgc2022.txt
```

## Verify that your output files are identical to those shown below
Note: Slight differences in the output may occur due to updates to the marker databases or differences in versions of dependencies.

```bash
head *.txt
```

Output:
```bash
==> SRR6915153_BGC_FINAL_RESULT.txt <==
BGC0000522	lacticin Z	RiPP (Lanthipeptide)	Lactococcus lactis
BGC0000523	lactocin S	RiPP (Lanthipeptide)	Lactobacillus sakei
BGC0000530	mutacin B-Ny266	RiPP (Lanthipeptide)	Streptococcus mutans N66
BGC0000535	nisin A	RiPP (Lanthipeptide)	Lactococcus lactis subsp. lactis
BGC0000538	nisin Z	RiPP (Lanthipeptide)	Lactococcus lactis
BGC0000552	SmbA, SmbB	RiPP (Lanthipeptide)	Streptococcus mutans
BGC0000764	exopolysaccharide	Saccharide	Lactococcus lactis
BGC0002287	leuvalin, mutanocyclin, tyrvalin	NRP	Streptococcus mutans
BGC0002583	tryglysin B	RiPP	Streptococcus mutans UA159

==> SRR6915153_BGC_metsp.txt <==
s__Eubacterium_eligens_CAG_72
s__Faecalibacterium_sp_CAG_82
s__Bacteroides_vulgatus_CAG_6
s__Bacteroides_plebeius_CAG_211
s__Eubacterium_sp_CAG_251
s__Clostridium_sp_CAG_492
s__Prevotella_sp_CAG_487
s__Alistipes_putredinis_CAG_67
s__Prevotella_sp_CAG_604
s__Eubacterium_sp_CAG_76

==> SRR6915153_covstats_taxibgc2022.txt <==
#ID	Avg_fold	Length	Ref_GC	Covered_percent	Covered_bases	Plus_reads	Minus_readsRead_GC	Median_fold	Std_Dev
BGC0000001_orfP_1	0.0000	1083	0.7138	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_NULL_2	0.0000	627	0.6794	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyR_3	0.0000	747	0.6961	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyX_4	0.0000	1191	0.6986	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyH_5	0.0000	2670	0.7502	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyI_6	0.0000	759	0.7101	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyK_7	0.0000	1860	0.7161	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyA1_8	0.0000	1026	0.7212	0.0000	0	0	0	0.0000	0	0.00
BGC0000001_abyA2_9	0.0000	1869	0.7309	0.0000	0	0	0	0.0000	0	0.00
```
