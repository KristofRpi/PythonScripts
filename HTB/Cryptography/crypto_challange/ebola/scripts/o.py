from itertools import izip_longest
import base64

B64 = {}

#seq = 'CTGA AATG TTCC GCGA GCCG AACC GATT CACC GCCT AGAA ACGT ATTG TGCT GGTG TGCG GCGG TTAG AGAT ATTA GGTA GCGC CGTT ACTC TAAC ATTT CGAA TCAA CCTT TCAG GGGA GTCA CTGC CATC GTAA GTAG AGTA CTTA GCAT CGAT GGCC ATGC CTAC TAAT TACA GGCT GAAT GACA CTAA ACCT TAGT TCAC TGAC CCGT TTTG TCAT GTAC TCTT GTGG TATG GGTC TTCA AATT GATC TGAT TGGG AAGA TAGA AAAA CGGC TCTA TCCT GGGT CGAG CCTC CCAT GAAG CAGT CAAG GGGC CGCG AGGA CTTC GATA CTTG CCCT GCTC GAGC ACAT TTTA AAGC TTAT TCCA CATA CTAG ACTT ACCC CCCG GCGT GTCG TACT GGAA GGTT AAAC CTCT TGAG TTGA TCTG ACAA CCTA GACG CGTG CCAC GTTG TGTG GGAT AGGT CACT CTCA TTTC CACG AGGG ACCA GAAC CTTT GGCA ATCC AGTT ATTC TGCA CTCG TGGC CGCC TCTC CTGG CAGG GGAC CGGT AAGT TTGC GTAT TCGC CGGG GAGT GGAG ACGG ATCG TCGT ACAC TGTT TCGA AAAT TTTT GAGG ATGG AGAG CAGA GCTA TTGG ATAA ACGC TTGT ACAG GTTC AATA CTAT TAGC AACG TGCC ACCG GCAC AGCT ATCT CTGT TTCG CATG AAAG AGCC GTTA ATCA CGAC GTTT AATC GAAA CACA TACC GATG GTCT ACGA ATAT TATA TCCG ATAC TAAG TCGG CCGC CGCA GTCC AGAC GCCA TATC GCTT TGAA GACC CCAA GGCG AACA TTAA CCGG TACG AGCA ACTG CGGA GTGC CCTG CAAT AGTC CGTC TGTA AAGG GCCC AGGC TAGG GCAA ATAG TCCC TAAA ACTA GAGA TGGT CAAC CGCT ATGT GGGG CATT CTCC GTGA GACT CAGC CGTA TTAC AGTG AGCG TATT CCCA AACT CCCC TTCT GTGT ATGA CCAG TGTC GCTG CAAA TGGA CCGA GCAG'
seq = 'CTG AAA TGT TCC GCG AGC CGA ACC GAT TCA CCG CCT AGA AAC GTA TTG TGC TGG TGT GCG GCG GTT AGA GAT ATT AGG TAG CGC CGT TAC TCT AAC ATT TCG AAT CAA CCT TTC AGG GGA GTC ACT GCC ATC GTA AGT AGA GTA CTT AGC ATC GAT GGC CAT GCC TAC TAA TTA CAG GCT GAA TGA CAC TAA ACC TTA GTT CAC TGA CCC GTT TTG TCA TGT ACT CTT GTG GTA TGG GTC TTC AAA TTG ATC TGA TTG GGA AGA TAG AAA AAC GGC TCT ATC CTG GGT CGA GCC TCC CAT GAA GCA GTC AAG GGG CCG CGA GGA CTT CGA TAC TTG CCC TGC TCG AGC ACA TTT TAA AGC TTA TTC CAC ATA CTA GAC TTA CCC CCC GGC GTG TCG TAC TGG AAG GTT AAA CCT CTT GAG TTG ATC TGA CAA CCT AGA CGC GTG CCA CGT TGT GTG GGA TAG GTC ACT CTC ATT TCC ACG AGG GAC CAG AAC CTT TGG CAA TCC AGT TAT TCT GCA CTC GTG GCC GCC TCT CCT GGC AGG GGA CCG GTA AGT TTG CGT ATT CGC CGG GGA GTG GAG ACG GAT CGT CGT ACA CTG TTT CGA AAA TTT TTG AGG ATG GAG AGC AGA GCT ATT GGA TAA ACG CTT GTA CAG GTT CAA TAC TAT TAG CAA CGT GCC ACC GGC ACA GCT ATC TCT GTT TCG CAT GAA AGA GCC GTT AAT CAC GAC GTT TAA TCG AAA CAC ATA CCG ATG GTC TAC GAA TAT TAT ATC CGA TAC TAA GTC GGC CGC CGC AGT CCA GAC GCC ATA TCG CTT TGA AGA CCC CAA GGC GAA CAT TAA CCG GTA CGA GCA ACT GCG GAG TGC CCT GCA ATA GTC CGT CTG TAA AGG GCC CAG GCT AGG GCA AAT AGT CCC TAA AAC TAG AGA TGG TCA ACC GCT ATG TGG GGC ATT CTC CGT GAG ACT CAG CCG TAT TAC AGT GAG CGT ATT CCC AAA CTC CCC TTC TGT GTA TGA CCA GTG TCG CTG CAA ATG GAC CGA GCA'
bins = [('00', '01', '10', '11'), ('00', '01', '11', '10'), ('00', '10', '01', '11'), ('00', '10', '11', '01'), ('00', '11', '01', '10'), ('00', '11', '10', '01'), ('01', '00', '10', '11'), ('01', '00', '11', '10'), ('01', '10', '00', '11'), ('01', '10', '11', '00'), ('01', '11', '00', '10'), ('01', '11', '10', '00'), ('10', '00', '01', '11'), ('10', '00', '11', '01'), ('10', '01', '00', '11'), ('10', '01', '11', '00'), ('10', '11', '00', '01'), ('10', '11', '01', '00'), ('11', '00', '01', '10'), ('11', '00', '10', '01'), ('11', '01', '00', '10'), ('11', '01', '10', '00'), ('11', '10', '00', '01'), ('11', '10', '01', '00')]
codons = ('A','C','T','G')

for combination in bins:
    key = list(zip(codons, combination))
    d = dict(key)
    seq_cpy = '%s' % seq
#    print seq_cpy
    for k in d.keys():
        seq_cpy = seq_cpy.replace(k,d[k])
#    print seq_cpy
    seq_lst = seq_cpy.split(' ')
    rst = []
    for b in seq_lst:
        rst += [int(b,2)]
#    print rst
    out = [B64[i] for i in rst]
#    print out
    out_s = ''.join(out)
    print out_s
#    dec = base64.b64decode(out_s)
#    print dec
