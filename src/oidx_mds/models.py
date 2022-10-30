import pydantic
from typing import Optional
from enum import Enum
from pendulum.date import Date


class DbType(str, Enum):
    sra = "sra"
    pubmed = "pubmed"
    geo = "geo"


class EutilsSearchQuery(pydantic.BaseModel):
    """Eutils search query"""

    # assumes that retmode is always json, so it's not included here
    # assumes that usehistory is always true, so it's not included here
    db: DbType
    term: Optional[str]
    startdate: Optional[Date]
    enddate: Optional[Date]
    datetype: Optional[str]
    retmax: Optional[int] = 20
    rettype: Optional[str]
    api_key: Optional[str]


class EutilsSearchResult(pydantic.BaseModel):
    """EutilsSearchResult model

    See https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
    """

    count: int
    retmax: int
    retstart: int
    querykey: int
    webenv: str
    idlist: list[str]
    querytranslation: str


class EutilsSearchEnvelope(pydantic.BaseModel):
    """EutilsSearchEnvelope model

    See https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
    """

    header: dict[str, str]
    esearchresult: EutilsSearchResult
