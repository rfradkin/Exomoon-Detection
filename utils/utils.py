
###
# change this shit
# make work w path, not just filename
###
def return_TIC_id(filen):
    '''Find TIC ID from fits filename.'''
    hyphe = []
    for i in range(len(filen)):
        if filen[i] == '-':
            hyphe.append(i)
    return int(filen[hyphe[1] + 1:hyphe[2]])