from nltk.tree import *
import pandas as pd

# Lesa inn textaskrár sem innihalda setningar sem hafa verið þáttaðar með liðgerðarþáttaranum
def read_text_files(file_names):
    data = []
    for filename in file_names:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            data.extend([(line, filename[11]) for line in lines])
    df = pd.DataFrame(data, columns=["Sentence", "File"])
    return df

files = ["parsedA1.txt", "parsedA2.txt", "parsedB1.txt", "parsedB2.txt", "parsedC1.txt", "parsedC2.txt"]
df = read_text_files(files)

# Telja meðalhæð trjáa, fjölda mismunandi IP og CP setninga
level = []
tree_height = []
IP_count = []
IP_MAT_count = []
IP_INF_count = []
IP_SUB_count = []
IP_PPL_count = []
IP_IMP_count = []
IP_SMC_count = []
CP_count = []
CP_REL_count = []
CP_THT_count = []
CP_QUE_count = []
CP_CMP_count = []
CP_ADV_count = []
CP_EOP_count = []
CP_CAR_count = []
CP_CLF_count = []
CP_DEG_count = []
CP_FRL_count = []
clause_count = []
NP_count = []
NP_length = []

count = 0
for setning in df['Sentence']:
    # Meðallengd nafnliða
    np_length = 0
    np_count = 0
    tree = ParentedTree.fromstring(setning)
    for subtree in tree.subtrees():
        if str(subtree).startswith(("(NP-", "(NP ")):
            np_count += 1
            np_length += len(subtree.leaves())
    NP_count.append(np_count)
    NP_length.append(np_length)
    # Telja ýmsa liði, t.d. IP_MAT
    level.append(df.iloc[count, 1])
    tree_height.append(Tree.fromstring(setning).height() - 1) # -1 afþví að ROOT er ennþá inni og á ekki að teljast með
    ip = 0
    ip_mat = 0
    ip_inf = 0
    ip_sub = 0
    ip_ppl = 0
    ip_imp = 0
    ip_smc = 0
    cp = 0
    cp_rel = 0
    cp_tht = 0
    cp_que = 0
    cp_cmp = 0
    cp_adv = 0
    cp_eop = 0
    cp_car = 0
    cp_clf = 0
    cp_deg = 0
    cp_frl = 0
    clauses = 0
    count += 1
    for word in setning.split():
        word = word.replace("(", "")
        if word in ['ADJP', 'ADVP', 'CODE', 'CONJP', 'CP*ADV', 'CP*CAR', 'CP*CLF', 'CP*CMP', 'CP*COM', 'CP*DEG', 'CP*EOP', 'CP*EXL', 'CP*FRL', 'CP*QUE', 
                    'CP*REL', 'CP*THT', 'CP*TMC', 'CP*TMP', 'DON', 'ENGLISH', 'FOREIGN', 'FRAG', 'FRENCH', 'FS', 'INTJP', 'IP*ABS', 'IP*IMP', 'IP*INF', 
                    'IP*MAT', 'IP*PPL', 'IP*SMC', 'IP*SUB', 'LATIN', 'LS', 'META', 'N*D', 'N*G', 'N*N', 'NP', 'NP*ADT', 'NP*ADV', 'NP*CMP', 'NP*COM', 
                    'NP*DIR', 'NP*LFD', 'NP*MSR', 'NP*OB1', 'NP*OB2', 'NP*OB3', 'NP*POS', 'NP*PRD', 'NP*PRN', 'NP*RSP', 'NP*SBJ', 'NP*SPE', 'NP*SPR', 
                    'NP*TMP', 'NP*TTT', 'NP*VOC', 'NS*A', 'NS*D', 'NS*N', 'NUMP', 'PP', 'QP', 'QP4', 'QTP', 'REF', 'REP', 'RP', 'RRC', 'VAN', 'VB', 
                    'VBDI', 'VBDS', 'VBI', 'VBN', 'VBPI', 'VBPS', 'VP', 'WADJP', 'WADVP', 'WNP', 'WPP', 'WQP', 'XP', 'XXX']:
            clauses += 1
        if word == "IP*MAT":
            ip += 1
            ip_mat += 1
        if word == "IP*INF":
            ip += 1
            ip_inf += 1
        if word == "IP*SUB":
            ip += 1
            ip_sub += 1
        if word == "IP*PPL":
            ip += 1
            ip_ppl += 1
        if word == "IP*IMP":
            ip += 1
            ip_imp += 1
        if word == "IP*SMC":
            ip += 1
            ip_smc += 1
        if word == "CP*REL":
            cp += 1
            cp_rel += 1
        if word == "CP*THT":
            cp += 1
            cp_tht += 1
        if word == "CP*QUE":
            cp += 1
            cp_que += 1
        if word == "CP*CMP":
            cp += 1
            cp_cmp += 1
        if word == "CP*ADV":
            cp += 1
            cp_adv += 1
        if word == "CP*EOP":
            cp += 1
            cp_eop += 1
        if word == "CP*CAR":
            cp += 1
            cp_car += 1
        if word == "CP*CLF":
            cp += 1
            cp_clf += 1
        if word == "CP*DEG":
            cp += 1
            cp_deg += 1
        if word == "CP*FRL":
            cp += 1
            cp_frl += 1
    IP_count.append(ip)
    IP_MAT_count.append(ip_mat)
    IP_INF_count.append(ip_inf)
    IP_SUB_count.append(ip_sub)
    IP_PPL_count.append(ip_ppl)
    IP_IMP_count.append(ip_imp)
    IP_SMC_count.append(ip_smc)
    CP_count.append(cp)
    CP_REL_count.append(cp_rel)
    CP_THT_count.append(cp_tht)
    CP_QUE_count.append(cp_que)
    CP_CMP_count.append(cp_cmp)
    CP_ADV_count.append(cp_adv)
    CP_EOP_count.append(cp_eop)
    CP_CAR_count.append(cp_car)
    CP_CLF_count.append(cp_clf)
    CP_DEG_count.append(cp_deg)
    CP_FRL_count.append(cp_frl)
    clause_count.append(clauses)


# Prenta upplýsingarnar úr pandas DataFrame í Excel skjal
columns1 = ['level', 'tree_height', "IP_count", "IP_MAT_count", "IP_INF_count", "IP_SUB_count", "IP_PPL_count", "IP_IMP_count", "IP_SMC_count",
            "CP_count", "CP_REL_count", "CP_THT_count", "CP_QUE_count", "CP_CMP_count", "CP_ADV_count", "CP_EOP_count", "CP_CAR_count", "CP_CLF_count", "CP_DEG_count", "CP_FRL_count", "clause_count", "NP_count", "NP_length"]
df1 = pd.DataFrame(list(zip(level, tree_height, 
                            IP_count, IP_MAT_count, IP_INF_count, IP_SUB_count, IP_PPL_count, IP_IMP_count, IP_SMC_count,
                            CP_count, CP_REL_count, CP_THT_count, CP_QUE_count, CP_CMP_count, CP_ADV_count, CP_EOP_count, CP_CAR_count, CP_CLF_count, CP_DEG_count, CP_FRL_count, clause_count, NP_count, NP_length
                            )), columns=columns1)

df3 = df1.groupby('level').agg({'tree_height': 'mean',
                               'IP_count': 'sum',
                               'IP_MAT_count': 'sum',
                               'IP_INF_count': 'sum',
                               'IP_SUB_count': 'sum',
                               'IP_PPL_count': 'sum',
                               'IP_IMP_count': 'sum',
                               'IP_SMC_count': 'sum',
                               'CP_count': 'sum',
                               'CP_REL_count': 'sum',
                               'CP_THT_count': 'sum',
                               'CP_QUE_count': 'sum',
                               'CP_CMP_count': 'sum',
                               'CP_ADV_count': 'sum',
                               'CP_EOP_count': 'sum',
                               'CP_CAR_count': 'sum',
                               'CP_CLF_count': 'sum',
                               'CP_DEG_count': 'sum',
                               'CP_FRL_count': 'sum',
                               'clause_count': 'sum',
                               'NP_count': 'sum',
                               'NP_length': 'sum'
                               }).reset_index()

# Reikna út hlutfall mismunandi IP og CP setninga
df3['IP_MAT_ratio'] = df3.apply(lambda row: row['IP_MAT_count'] / row['IP_count'] if row['IP_count'] != 0 else 0, axis=1)
df3['IP_INF_ratio'] = df3.apply(lambda row: row['IP_INF_count'] / row['IP_count'] if row['IP_count'] != 0 else 0, axis=1)
df3['IP_SUB_ratio'] = df3.apply(lambda row: row['IP_SUB_count'] / row['IP_count'] if row['IP_count'] != 0 else 0, axis=1)
df3['IP_PPL_ratio'] = df3.apply(lambda row: row['IP_PPL_count'] / row['IP_count'] if row['IP_count'] != 0 else 0, axis=1)
df3['IP_IMP_ratio'] = df3.apply(lambda row: row['IP_IMP_count'] / row['IP_count'] if row['IP_count'] != 0 else 0, axis=1)
df3['IP_SMC_ratio'] = df3.apply(lambda row: row['IP_SMC_count'] / row['IP_count'] if row['IP_count'] != 0 else 0, axis=1)
df3['CP_REL_ratio'] = df3.apply(lambda row: row['CP_REL_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_THT_ratio'] = df3.apply(lambda row: row['CP_THT_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_QUE_ratio'] = df3.apply(lambda row: row['CP_QUE_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_CMP_ratio'] = df3.apply(lambda row: row['CP_CMP_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_ADV_ratio'] = df3.apply(lambda row: row['CP_ADV_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_EOP_ratio'] = df3.apply(lambda row: row['CP_EOP_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_CAR_ratio'] = df3.apply(lambda row: row['CP_CAR_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_CLF_ratio'] = df3.apply(lambda row: row['CP_CLF_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_DEG_ratio'] = df3.apply(lambda row: row['CP_DEG_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['CP_FRL_ratio'] = df3.apply(lambda row: row['CP_FRL_count'] / row['CP_count'] if row['CP_count'] != 0 else 0, axis=1)
df3['NP_avg_len'] = df3.apply(lambda row: row['NP_length'] / row['NP_count'] if row['NP_count'] != 0 else 0, axis=1)

with pd.ExcelWriter('conparse_stats.xlsx') as writer:
    df3.to_excel(writer, sheet_name='Levels', index=False)
    df1.to_excel(writer, sheet_name='Sentences', index=False)
