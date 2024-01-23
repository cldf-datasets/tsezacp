
from cldfbench_tsezacp import iterwords


def test_iterwords():
    rows = [l.strip().split(',') for l in """
    103257,51941,1,r-,IV.PL-,pref-
    103258,51941,2,iti,touch,v
    103259,51941,3,-run,-IMM.ANT.CVB,-vsuf
    103260,51941,4,-tow,"-EMPH H",-suf
    103261,51941,5,ža,DEM1.SG,pron
    103262,51941,6,qoq,cliff,n4
    103263,51941,7,b-,III-,pref-
    103264,51941,8,ˤaɣˤi,open,v
    103265,51941,9,-ł,-POT,-vsuf
    103266,51941,10,-n,-PFV.CVB,-vsuf
    103267,51941,11,nex,come,v
    """.strip().splitlines(keepends=False)]
    header = "id,to_Word_id,Position,Value,Gloss,Part_of_Speech".split(',')
    words = list(iterwords([dict(zip(header, row)) for row in rows]))
    print([''.join(m['Value'] for m in w) for w in words])
    assert len(words) == 5
    # should be "r-iti-run-tow ža qoq b-ˤaɣˤi-ł-n nex" not "r-iti-run-towžaqoqb-ˤaɣˤi-ł-nnex"


def test_valid(cldf_dataset, cldf_sqlite_database, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)
    assert cldf_dataset.texts[0].sentences[0].alternative_translations[0].cldf.metaLanguageReference == 'russ1263'
    res = cldf_sqlite_database.query(
        "select json_extract(cldf_position, '$[0]') as tid from exampletable where json_array_length(cldf_position) > 0 order by tid")
    assert res[-1][0] == 78
