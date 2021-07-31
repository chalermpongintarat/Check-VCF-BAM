#!/bin/bash
cmd="samtools quickcheck -v /Users/chalermpong/pharmvip/website/media/storage/1/1/input/bam/390.bam > /Users/chalermpong/pharmvip/website/media/storage/1/1/input/bam/bad_bams.fofn && echo 'all ok' || echo 'some files failed check, see bad_bams.fofn'"
eval $cmd