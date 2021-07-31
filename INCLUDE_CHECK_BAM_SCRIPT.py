########## INCLUDE CHECK BAM SCRIPT ##########

                            if bam_ins.bam_checked == False:
                                checked_bam_sh_path = settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/bam/check_script.sh'
                                echo = "echo 'all ok' || echo 'some files failed check, see bad_bams.fofn'"
                                cmd = 'samtools quickcheck -v '+settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/bam/390.bam > '+settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/bam/bad_bams.fofn && '+echo
                                checked_bam_sh = ["#!/bin/bash\n", 'cmd='+'"'+cmd+'"'+'\n', "eval $cmd"]
                                with open (checked_bam_sh_path, 'w') as rsh:
                                    rsh.writelines(checked_bam_sh)
                                subprocess.call(['chmod', '+x', checked_bam_sh_path])
                                subprocess.call(checked_bam_sh_path)
                                checked_results = open(settings.MEDIA_ROOT+'/storage/'+user_id+'/'+project_id+'/input/bam/bad_bams.fofn', 'r')
                                if checked_results.mode == 'r':
                                    checked = checked_results.readline()
                                    if checked != ' ':
                                        if bam_form.is_valid():
                                            update = bam_form.save(commit=False)
                                            update.bam_checked = True
                                            update.save()
                                    else:
                                        if bam_form.is_valid():
                                            update = bam_form.save(commit=False)
                                            update.bam_checked = False
                                            update.save()