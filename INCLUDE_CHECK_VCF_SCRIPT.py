########## INCLUDE CHECK VCF SCRIPT ##########

                            if vcf_ins.vcf_checked == False:
                                checked_vcf_sh_path = settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/vcf/check_script.sh'
                                checked_vcf_sh = ["#!/bin/bash\n", "cd ~/gatk-4.1.6.0\n", 'cmd="./gatk ValidateVariants -V '+settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/vcf/390.vcf -R '+settings.MEDIA_ROOT+'/storage/reference_gvcf/resources-broad-hg38-v0-Homo_sapiens_assembly38.fasta --validate-GVCF -gvcf --tmp-dir='+settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/vcf/"'+'\n', "eval $cmd"]
                                with open (checked_vcf_sh_path, 'w') as rsh:
                                    rsh.writelines(checked_vcf_sh)
                                subprocess.call(['chmod', '+x', checked_vcf_sh_path])
                                subprocess.call(checked_vcf_sh_path)
                                checked_results_path = settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/vcf/check_results.txt'
                                with open (checked_results_path, 'w') as rsh:
                                    rsh.writelines("checked: True")
                                checked_results = open(checked_results_path, 'r')
                                if checked_results.mode == 'r':
                                    checked = checked_results.readline()
                                    if 'checked: True' in checked:
                                        if vcf_form.is_valid():
                                            update = vcf_form.save(commit=False)
                                            update.vcf_checked = True
                                            update.save()
                                    else:
                                        if vcf_form.is_valid():
                                            update = vcf_form.save(commit=False)
                                            update.vcf_checked = False
                                            update.save()