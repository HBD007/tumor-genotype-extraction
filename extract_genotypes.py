import pdfplumber
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
matcher.add("GENE_VARIANT", [[
    {"TEXT": {"REGEX": "^[A-Z0-9]+$"}},
    {"TEXT": {"REGEX": "^[A-Z][0-9]+[A-Z]$"}}
]])

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_genotypes(text):
    doc = nlp(text)
    matches = matcher(doc)
    genotypes = []
    for match_id, start, end in matches:
        span = doc[start:end]
        parts = span.text.split()
        if len(parts) == 2:
            gene, variant = parts
            genotypes.append((gene, variant))
    return genotypes