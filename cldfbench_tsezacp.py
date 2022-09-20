import re
import pathlib
import itertools
import collections

from pyigt import IGT
from cldfbench import Dataset as BaseDataset, CLDFSpec

TSEZ = 'dido1241'
EN = 'stan1293'
RU = 'russ1263'


def iterwords(allrows):
    innerhyphen = re.compile(r'([^-]+)-([^-]+)')

    def replace_innerhyphen(s, repl):
        while innerhyphen.search(s):
            s = ''.join(innerhyphen.sub(
                lambda m: '{}{}{}'.format(m.groups()[0], repl, m.groups()[1]), s))
        return s

    def iterrows(wid, rows):
        for row in rows:
            # Fix whitespace in morphemes or gloss.
            if row['id'] == '507':
                yield dict(to_Word_id=wid, Value='eniw', Gloss='mother', Part_of_Speech='n2')
                yield dict(to_Word_id=wid, Value='y-', Gloss='II-', Part_of_Speech='pref-')
            elif row['id'] in ['1288', '9059']:
                yield dict(to_Word_id=wid, Value='-a-', Gloss='-ERG-', Part_of_Speech='-nsuf-')
            elif row['id'] == '10160':
                row['Gloss'] = row['Gloss'].replace(' ', '.')
                yield row
            elif row['id'] == '13182':
                yield dict(to_Word_id=wid, Value='hay', Gloss='so.then', Part_of_Speech='excl')
                yield dict(to_Word_id=wid, Value='i', Gloss='and', Part_of_Speech='excl')
                yield dict(to_Word_id=wid, Value='wele', Gloss='look.out', Part_of_Speech='excl')
            elif row['id'] == '58290':
                yield dict(to_Word_id=wid, Value='hudu', Gloss='so', Part_of_Speech='excl')
                yield dict(to_Word_id=wid, Value='-law', Gloss='-VOC', Part_of_Speech='-nsuf')
            elif row['id'] == '64548':
                yield dict(to_Word_id=wid, Value='eliz', Gloss='we.SPEC.GEN1.GEN2', Part_of_Speech='pron')
            elif row['id'] == '74550':
                #74550,37523,1,"ir -n", "II-   let  -PST.UNW","pref- v    -vsuf"
                yield dict(to_Word_id=wid, Value='yeg-', Gloss='II-', Part_of_Speech='pref-')
                yield dict(to_Word_id=wid, Value='ir', Gloss='let', Part_of_Speech='v')
                yield dict(to_Word_id=wid, Value='-n', Gloss='-PST.UNW', Part_of_Speech='-vsuf')
            elif row['id'] == '75446':
                #37979, 1, ya, "II-   bring.IMP", "pref- v"
                row.update(Gloss='neither', Part_of_Speech='conj')
                yield row
            elif row['id'] == '77554':
                #39030, 1, "žanaza", "DEM1.SG -TOP -IN.VERS.DIST", "pron    -suf -nsuf"
                row.update(Gloss='corpse', Part_of_Speech='n3')
                yield row
            elif row['id'] == '83772':
                #42123, 1, "esnałin", "brother -CNC.CVB", "n1      -vsuf"
                yield dict(to_Word_id=wid, Value='esna', Gloss='brother', Part_of_Speech='n1')
                yield dict(to_Word_id=wid, Value='-łin', Gloss='-CNC.CVB', Part_of_Speech='-vsuf')
            elif row['id'] == '100596':
                #50579, 1, saso, "noise -IMPR", "n3    -vsuf"
                row.update(Gloss='darkness', Part_of_Speech='n')
                yield row
            elif row['id'] == '103260':
                # 51941, 4, -tow, "-EMPH H", -suf
                row.update(Gloss='-EMPH')
                yield row
            elif row['id'] == '105021':
                # 52839, 3, "-n       or", "-PFV.CVB k", -vsuf
                yield dict(to_Word_id=wid, Value='-n', Gloss='-PFV.CVB', Part_of_Speech='-vsuf')
                yield dict(to_Word_id=wid, Value='xizor', Gloss='back', Part_of_Speech='adv')
            else:
                yield row

    for wid, rows in itertools.groupby(allrows, lambda r: r['to_Word_id']):
        morphs = []
        for row in iterrows(wid, rows):
            assert not any(' ' in row[a] for a in 'Gloss Value Part_of_Speech'.split())

            # Fix morpheme-internal hyphens:
            row['Value'] = replace_innerhyphen(row['Value'], '–')
            row['Gloss'] = replace_innerhyphen(row['Gloss'], '.')
            # Normalize POS:
            row['Part_of_Speech'] = {
                'n1.pl': 'n1pl',
                '-su': '-suf',
                '-vsuf\\': '-vsuf',
                '-***': '-',
            }.get(row['Part_of_Speech'].strip(), row['Part_of_Speech'].strip())

            # Fix hyphens used to set off parenthetical:
            if row['Value'] == row['Gloss'] == row['Part_of_Speech'] == '-':
                row.update(Value='—', Gloss='—', Part_of_Speech='')
            row['Part_of_Speech'] = row['Part_of_Speech'].replace('-', '')

            if row['Value'].endswith(' -'):
                row['Value'] = row['Value'][:-2] + '-'
            if row['Value'].startswith('- '):
                row['Value'] = '-' + row['Value'][2:]
            if (morphs and morphs[-1]['Value'].endswith('-')) or row['Value'].startswith('-'):
                morphs.append(row)
            else:
                if morphs:
                    yield morphs
                morphs = [row]
        if morphs:
            yield morphs


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "tsezacp"

    def cldf_specs(self):
        return CLDFSpec(
            dir=self.cldf_dir,
            module='Dictionary',
            data_fnames={
                'EntryTable': 'morphemes.csv',
                'ContributionTable': 'texts.csv',
                'ExampleTable': 'lines.csv',
            }
        )

    def cmd_download(self, args):
        pass

    def cmd_makecldf(self, args):
        args.writer.cldf['ContributionTable'].common_props['dc:description'] = \
            "The texts of the Tsez annotated corpus are modeled as contributions."
        args.writer.cldf['ExampleTable'].common_props['dc:description'] = \
            "Each entry in this table corresponds to one line in a text of this corpus."
        args.writer.cldf['EntryTable'].common_props['dc:description'] = \
            "This table represents a morpheme concordance for the corpus."
        args.writer.cldf['SenseTable'].common_props['dc:description'] = \
            "Morpheme senses are aggregated from the glosses used for a morpheme in the " \
            "glossed texts."
        args.writer.cldf.add_columns(
            'EntryTable',
            {
                'name': 'Example_IDs',
                'separator': ' ',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#exampleReference'},
        )
        args.writer.cldf.add_component('LanguageTable')
        args.writer.cldf.add_columns(
            'ContributionTable',
            {
                'name': 'Source',
                'separator': ';',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#source'},
        )
        args.writer.cldf.add_columns(
            'ExampleTable',
            {
                "name": "Text_ID",
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#contributionReference',
            },
            'Russian_Translation',
            {
                "name": "Part_of_Speech",
                "required": False,
                "datatype": "string",
                "separator": "\t",
            },
        )
        args.writer.cldf['ExampleTable', 'Gloss'].separator = '\t'
        args.writer.cldf['ExampleTable', 'Analyzed_Word'].separator = '\t'

        args.writer.cldf.sources.add(
            """@book{Abdulaev2010,
    author = {Abdulaev, A.K. and I. K. Abdullaev},
    year = {2010},
    title = {Cezyas folklor/Dido (Tsez) folklore/Didojskij (cezskij) fol\u00b4klor},
    address = {Leipzig\u2013Makhachkala},
    publisher = {Lotos}
}""")

        for name, id_ in [('Tsez', TSEZ), ('English', EN), ('Russian', RU)]:
            args.writer.objects['LanguageTable'].append(dict(ID=id_, Name=name, Glottocode=id_))

        for text in self.raw_dir.read_csv('text.csv', dicts=True):
            args.writer.objects['ContributionTable'].append(dict(
                ID=text['Number'],
                Name=text['Title_in_Tsez'],
                Description=text['Title_in_English'],
                Source=['Abdulaev2010'],
            ))

        lines_by_id = collections.OrderedDict([
            (l['id'], l) for l in self.raw_dir.read_csv('line.csv', dicts=True)])

        words_by_line = {
            lid: list(words) for lid, words in itertools.groupby(
                sorted(
                    self.raw_dir.read_csv('word.csv', dicts=True),
                    key=lambda w: (int(w['to_Line_id']), int(w['Lex_Position']))),
                lambda w: w['to_Line_id'])}

        words_by_word = collections.defaultdict(list)
        for word in iterwords(sorted(
            self.raw_dir.read_csv('morpheme.csv', dicts=True),
            key=lambda m: (int(m['to_Word_id']), int(m['Position'])),
        )):
            words_by_word[word[0]['to_Word_id']].append(word)

        def joinm(morphemes, what, sep=''):
            res = sep.join(m[what] for m in morphemes)
            if res.endswith('-'):
                res = res[:-1]
            return res

        entries = collections.defaultdict(set)
        entry2line = collections.defaultdict(list)
        for text_id, lines in itertools.groupby(
            sorted(
                lines_by_id.values(),
                key=lambda l: (int(l['to_Text_id']), int(l['Line_Position']))),
            lambda l: l['to_Text_id']
        ):
            for line in lines:
                wids = [w['id'] for w in words_by_line[line['id']]]
                words = list(itertools.chain(*[words_by_word[wid] for wid in wids]))

                lid = '{0}-{1}'.format(text_id, line['Line_Position'])
                igt = IGT(
                    phrase=[joinm(w, 'Value') for w in words],
                    gloss=[joinm(w, 'Gloss') for w in words])
                assert igt.is_valid(strict=True)
                for gw, word in zip(igt.glossed_words, words):
                    for gm, m in zip(gw, word):
                        if gm.morpheme:
                            pos = m['Part_of_Speech'].replace('pl', '')
                            for s in '1 2 3 4'.split():
                                pos = pos.replace(s, '')
                            entries[gm.morpheme, pos].add(gm.gloss)
                            entry2line[gm.morpheme, pos].append(lid)

                args.writer.objects['ExampleTable'].append(dict(
                    ID='{0}-{1}'.format(text_id, line['Line_Position']),
                    Text_ID=text_id,
                    Language_ID=TSEZ,
                    Primary_Text=line['Tsez_Line'],
                    Analyzed_Word=[gw.word_from_morphemes for gw in igt.glossed_words],
                    Gloss=[gw.gloss_from_morphemes for gw in igt.glossed_words],
                    Part_of_Speech=[joinm(w, 'Part_of_Speech', sep='-') for w in words],
                    Translated_Text=line['English_Translation'],
                    Russian_Translation=line['Russian_Translation'],
                    Meta_Language_ID=EN,
                ))

        for i, (entry, senses) in enumerate(sorted(entries.items()), start=1):
            args.writer.objects['EntryTable'].append(dict(
                ID=str(i),
                Language_ID=TSEZ,
                Headword=entry[0],
                Part_Of_Speech=entry[1],
                Example_IDs=entry2line[entry],
            ))
            for j, sense in enumerate(sorted(senses), start=1):
                args.writer.objects['SenseTable'].append(dict(
                    ID='{}-{}'.format(i, j),
                    Description=sense,
                    Entry_ID=str(i),
                ))
