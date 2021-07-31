#!/bin/bash
cd ~/gatk-4.1.6.0
cmd="./gatk ValidateVariants -V /Users/chalermpong/pharmvip/website/media/storage/1/1/input/vcf/390.vcf -R /Users/chalermpong/pharmvip/website/media/storage/reference_gvcf/resources-broad-hg38-v0-Homo_sapiens_assembly38.fasta --validate-GVCF -gvcf --tmp-dir=/Users/chalermpong/pharmvip/website/media/storage/1/1/input/vcf/"
eval $cmd