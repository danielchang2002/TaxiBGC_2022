#!/bin/bash 
set -e
 
display_usage() { 
#	echo "This script must be run with super-user privileges." 
	echo -e "\nUsage: $0 [arguments] \n\n-f: path to forward reads\n-r: path to reverse reads\n-t: path to TaxiBGC script folder\n-o: path to output folder with prefix of output file names\n-n: number of threads\n\nPre-requisites:\n\tBBMAP\n\tMetaPhlAn3\n\tBowtie2\nNOTE: All three softwares should be added to the system path" 
	} 
# if less than two arguments supplied, display usage 
	if [  $# -le 1 ] 
	then 
		display_usage
		exit 1
	fi 
 
# check whether user had supplied -h or --help . If yes display usage 
	if [[ ( $# == "--help") ||  $# == "-h" ]] 
	then 
		display_usage
		exit 0
	fi


while getopts f:r:t:o:n:g:b: option 
do
 case "${option}"
 in
 f) i1=${OPTARG};;
 r) i2=${OPTARG};;
 t) t=${OPTARG};;
 o) o=${OPTARG};;
 n) n=${OPTARG};;
 g) g=${OPTARG};;
 b) b=${OPTARG};;

 esac
done

bbmap.sh in1=${i1} in2=${i2} ref=${t}BGC_MiBIG_final.fasta out=${o}.sam covstats=${o}_covstats_taxibgc2022.txt nodisk
rm ${o}.sam
awk -F"\t" -v OFS="\t" '{gsub(/_.+/,"",$1)}1' ${o}_covstats_taxibgc2022.txt >${o}_BGC_name_clean.txt
awk -F"\t" -v OFS="\t" '{print $1,$5}' ${o}_BGC_name_clean.txt >${o}_BGC_gene_coverage.txt
rm ${o}_BGC_name_clean.txt
sed '1d' ${o}_BGC_gene_coverage.txt >${o}_BGC_gene_coverage_1.txt
rm ${o}_BGC_gene_coverage.txt
awk -F"\t" -v OFS="\t" '{print $0,1}' ${o}_BGC_gene_coverage_1.txt >${o}_BGC_gene_column.txt
rm ${o}_BGC_gene_coverage_1.txt
awk -F'\t' -v OFS="\t" '{ if($2>='${g}') $4=1; else $4=0;print $0; }' ${o}_BGC_gene_column.txt >${o}_BGC_gene_presence.txt
rm ${o}_BGC_gene_column.txt
awk -f ${t}BGC_gene_count.awk ${o}_BGC_gene_presence.txt >${o}_BGC_gene_presence_count.txt
rm ${o}_BGC_gene_presence.txt
awk -F'\t' -v OFS="\t" '{print $1,$4*100/$3 }' OFMT='%.3g' ${o}_BGC_gene_presence_count.txt >${o}_BGC_gene_presence_percent.txt
rm ${o}_BGC_gene_presence_count.txt
awk -F'\t' -v OFS="\t" '{ if($2>='${b}') print $0}' ${o}_BGC_gene_presence_percent.txt >${o}_BGC_gene_presence_pred_raw.txt
rm ${o}_BGC_gene_presence_percent.txt
metaphlan ${i1},${i2} --bowtie2out ${o}_BGC.bowtie2.bz2 --nproc ${n} --input_type fastq -o ${o}_BGC_metaphlan3.txt --add_viruses --unknown_estimation
rm ${o}_BGC.bowtie2.bz2
sed -n 's/^.*s__/s__/p' ${o}_BGC_metaphlan3.txt >${o}_BGC_metsp.txt
rm ${o}_BGC_metaphlan3.txt
awk -F"\t" -v OFS="\t" 'FNR==NR{a[$1]=$2;next} ($2 in a){print $1}' ${o}_BGC_metsp.txt ${t}TaxiBGC_MiBIG_metaphlan_database.txt >${o}_BGC_Step1.txt
grep -Fw -f ${o}_BGC_Step1.txt ${o}_BGC_gene_presence_pred_raw.txt >${o}_BGC_Step1_1.txt
rm ${o}_BGC_gene_presence_pred_raw.txt
rm ${o}_BGC_Step1.txt
awk -F"\t" -v OFS="\t" '{print $1}' ${o}_BGC_Step1_1.txt >${o}_BGC_prediction.txt
rm ${o}_BGC_Step1_1.txt
grep -Fw -f ${o}_BGC_prediction.txt ${t}BGC_SMs_MiBIG_database.txt >${o}_BGC_FINAL_RESULT.txt
rm ${o}_BGC_prediction.txt

