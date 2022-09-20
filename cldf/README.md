<a name="ds-dictionarymetadatajson"> </a>

# Dictionary The Tsez Annotated Corpus Project

**CLDF Metadata**: [Dictionary-metadata.json](./Dictionary-metadata.json)

**Sources**: [sources.bib](./sources.bib)

The texts that constitute this corpus were collected by Arsen Kurbanovič Abdulaev and Isa Kurbanovič Abdullaev and published with Russian translation as Abdulaev and Abdullaev (2010). The intended audience of this book publication was primarily the Tsez-speaking community and Russian-speaking readers interested in folklore. Work on the book was sponsored by the [Max Planck Institute for Evolutionary Anthropology (MPI-EVA)](https://www.eva.mpg.de/) and part of the agreement was that the institute would be allowed to post on-line a version of the text suitable for scientific use by linguists, with morpheme glosses and an English translation added to the materials available in the book. Work on the glossing of the texts has been carried out by A.K. Abdulaev, André Müller, and Evgeniya Zhivotova. The material is hereby provided for scientific research under the CC-BY license.

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Abdulaev, A.K. & I. K. Abdullaev. 2010. Cezyas folklor/Dido (Tsez) folklore/Didojskij (cezskij) fol´klor. Leipzig–Makhachkala: “Lotos”.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Dictionary](http://cldf.clld.org/v1.0/terms.rdf#Dictionary)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://tsezacp.clld.org
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/cldf-datasets/tsezacp
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/cldf-datasets/tsezacp/tree/2439847">cldf-datasets/tsezacp 2439847</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.6">Glottolog v4.6</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | tsezacp
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-morphemescsv"></a>Table [morphemes.csv](./morphemes.csv)

This table represents a morpheme concordance for the corpus.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF EntryTable](http://cldf.clld.org/v1.0/terms.rdf#EntryTable)
[dc:extent](http://purl.org/dc/terms/extent) | 2388


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Headword](http://cldf.clld.org/v1.0/terms.rdf#headword) | `string` | 
[Part_Of_Speech](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech) | `string` | 
[Example_IDs](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) | list of `string` (separated by ` `) | References [lines.csv::ID](#table-linescsv)

## <a name="table-sensescsv"></a>Table [senses.csv](./senses.csv)

Morpheme senses are aggregated from the glosses used for a morpheme in the glossed texts.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable)
[dc:extent](http://purl.org/dc/terms/extent) | 2782


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | References [entries.csv::ID](#table-entriescsv)

## <a name="table-textscsv"></a>Table [texts.csv](./texts.csv)

The texts of the Tsez annotated corpus are modeled as contributions.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 78


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)

## <a name="table-linescsv"></a>Table [lines.csv](./lines.csv)

Each entry in this table corresponds to one line in a text of this corpus.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 4949


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `	`) | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `	`) | The sequence of glosses aligned with the words of the primary text
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | The translation of the example text in a meta language
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References the language of the translated text<br>References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Text_ID](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | `string` | References [texts.csv::ID](#table-textscsv)
`Russian_Translation` | `string` | 
`Part_of_Speech` | list of `string` (separated by `	`) | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 

