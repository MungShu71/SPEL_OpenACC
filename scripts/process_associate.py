def get_rid_of_associate(sub, overwrite=False):
    """
    this function preprocesses the subroutine to get rid of the associate clauses
    in order to more easily find out the written to variables of the subroutine

    subname:  name of subroutine

    """
    import re
    from mod_config import elm_files

    iofile = open(elm_files+sub.filepath, 'r')
    # status intitialized to False -- routine needs analysis
    status = False
    lines = iofile.readlines()
    iofile.close()
    #print(lines[0])
    subroutine_name = sub.name
    subroutine_start_line = sub.startline
    subroutine_end_line = sub.endline

    associate_vars = {}

    associate_start = 0
    associate_end = 0
    print("file has %i number of lines" %len(lines))
    ct = subroutine_start_line
    while (ct < subroutine_end_line):
        line = lines[ct]
        line = line.strip().split('!')[0]
        ct = ct + 1
        match = re.search(r'\bassociate\b(?=\()' , line) #find start of assoicate(
        if(match and ct < subroutine_end_line):
            associate_start = ct
            continue
        # => should give last association
        match = re.search(r'\s*\S+\s+=>\s*\S+', line)
        if(match):
            if(ct > subroutine_start_line and ct < subroutine_end_line and associate_start != 0):
                associate_end = ct
                line = line.replace(',',' ')
                line = line.replace(')', ' ')
                parsed = line.split()
                find_ex = parsed[0]
                repl_ex = parsed[2]
                if('bounds' not in repl_ex):
                    associate_vars.setdefault(find_ex,[]).append(repl_ex)

        continue

    if(associate_start == 0):
        print("no derived types found")
        status = True  ## means no more analysis is needed

    return associate_vars, status, associate_start, associate_end
