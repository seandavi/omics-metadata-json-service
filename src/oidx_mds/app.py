from fastapi import FastAPI
from .models import EutilsSearchEnvelope, EutilsSearchResult, EutilsSearchQuery
import httpx
from omicidx.sra import parser as sp
import io
from typing import Mapping, Any

app = FastAPI()


@app.post("/ncbi/eutils/esearch")
async def ncbi_eutils_esearch(query: EutilsSearchQuery) -> EutilsSearchEnvelope:
    """Perform an eutils search"""
    params = {
        "db": query.db,
        "retmax": query.retmax,
        "usehistory": query.usehistory,
        "retmode": "json",
    }
    if query.term:
        params["term"] = query.term
    if query.startdate and query.enddate:
        params["term"] = (
            f"({query.startdate.strftime('%Y/%m/%d')}[{query.datetype}]"
            f" : {query.enddate.strftime('%Y/%m/%d')}[{query.datetype}])"
        )

    print(
        httpx.URL(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=params
        )
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            params=params,
        )
        envelope = EutilsSearchEnvelope(**response.json())

    return envelope


@app.get("/ncbi/eutils/efetch")
async def ncbi_eutils_efetch(
    db: str, query_key: int, webenv: str, retmax: int = 500, retstart=0
):
    """Perform an eutils fetch"""
    params = {
        "db": db,
        "query_key": query_key,
        "webenv": webenv,
        "retstart": retstart,
        "retmax": retmax,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
            params=params,
        )
        return response.text


@app.get("/ncbi/eutils/efetch/sra")
async def get_parsed_sra_results(
    webenv: str, query_key: int, retmax: int = 500, retstart: int = 0
):
    """Get parsed SRA results"""
    params: Mapping[str, Any] = {
        "db": "sra",
        "query_key": query_key,
        "webenv": webenv,
        "retstart": retstart,
        "retmax": retmax,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
            params=params,
        )
        ret = []
        for entity in sp.sra_object_generator(io.BytesIO(response.content)):
            d = entity.data
            d["type"] = (
                entity.__class__.__name__.lower()
                .replace("sra", "")
                .replace("record", "")
                .title()
            )

            ret.append(d)
        return ret
