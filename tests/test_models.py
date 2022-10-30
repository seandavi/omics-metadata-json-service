from oidx_mds.models import EutilsSearchEnvelope, EutilsSearchResult

sample_result = {
    "header": {"type": "esearch", "version": "0.3"},
    "esearchresult": {
        "count": "21831936",
        "retmax": "20",
        "retstart": "0",
        "querykey": "1",
        "webenv": "MCID_635d8e1757981866440720fc",
        "idlist": [
            "25039505",
            "25039504",
            "25039503",
            "25039502",
            "25039501",
            "25039500",
            "25039499",
            "25039498",
            "25039497",
            "25039496",
            "25039495",
            "25039494",
            "25039493",
            "25039492",
            "25039491",
            "25039490",
            "25039489",
            "25039488",
            "25039487",
            "25039486",
        ],
        "translationset": [],
        "translationstack": [
            {"term": "2001/01/01[MDAT]", "field": "MDAT", "count": "0", "explode": "N"},
            {"term": "2030/01/01[MDAT]", "field": "MDAT", "count": "0", "explode": "N"},
            "RANGE",
            "GROUP",
        ],
        "querytranslation": "2001/01/01[MDAT] : 2030/01/01[MDAT]",
    },
}


def test_eutils_results_model():
    envelope = EutilsSearchEnvelope(**sample_result)
    assert envelope.header["type"] == "esearch"
    assert envelope.header["version"] == "0.3"
    assert type(envelope.esearchresult.count) == int
    assert envelope.esearchresult.count == 21831936
    assert envelope.esearchresult.retmax == 20
    assert envelope.esearchresult.retstart == 0
    assert envelope.esearchresult.querykey == 1
    assert envelope.esearchresult.webenv == "MCID_635d8e1757981866440720fc"
    assert type(envelope.esearchresult.retmax) == int
    assert type(envelope.esearchresult.retstart) == int
    assert type(envelope.esearchresult.querykey) == int
    assert type(envelope.esearchresult.idlist) == list
    assert type(envelope.esearchresult.idlist[0]) == str
