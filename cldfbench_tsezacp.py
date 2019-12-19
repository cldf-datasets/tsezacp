import pathlib
import itertools
import collections

from cldfbench import Dataset as BaseDataset

TSEZ = 'dido1241'
EN = 'stan1293'
RU = 'russ1263'

# word.csv, line 42203 -> unsegmented!


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "tsezacp"

    def cmd_download(self, args):
        pass

    def cmd_makecldf(self, args):
        args.writer.cldf.add_component('LanguageTable')
        for name, id_ in [('Tsez', TSEZ), ('English', EN), ('Russian', RU)]:
            args.writer.objects['LanguageTable'].append(dict(ID=id_, Name=name, Glottocode=id_))

        args.writer.cldf.add_table('texts.csv', 'ID', 'Name', 'Description')
        for text in self.raw_dir.read_csv('text.csv', dicts=True):
            args.writer.objects['texts.csv'].append(dict(
                ID=text['Number'],
                Name=text['Title_in_Tsez'],
                Description=text['Title_in_English'],
            ))

        args.writer.cldf.add_component(
            'ExampleTable',
            'Text_ID',
            'Russian_Translation',
            {
                "name": "Part_of_Speech",
                "required": False,
                "datatype": "string",
                "separator": "\t",
            },
        )

        # FIXME: specify: hyphens separate morphemes!

        lines_by_id = collections.OrderedDict([
            (l['id'], l) for l in self.raw_dir.read_csv('line.csv', dicts=True)])

        words_by_line = {
            lid: list(words) for lid, words in itertools.groupby(
                sorted(
                    self.raw_dir.read_csv('word.csv', dicts=True),
                    key=lambda w: (int(w['to_Line_id']), int(w['Lex_Position']))),
                lambda w: w['to_Line_id'])}
        morphemes_by_word = {
            wid: list(morphemes) for wid, morphemes in itertools.groupby(
                sorted(
                    self.raw_dir.read_csv('morpheme.csv', dicts=True),
                    key=lambda m: (int(m['to_Word_id']), int(m['Position'])),
                ),
                lambda m: m['to_Word_id'])}

        def chunks(line, type_):
            return [
                ''.join(m[type_] for m in morphemes_by_word[w['id']])
                if w['id'] in morphemes_by_word
                else (w['Word_Clear'] if type != 'Part_of_Speech' else '')
                for w in words_by_line[line['id']]]

        for text_id, lines in itertools.groupby(
            sorted(
                lines_by_id.values(),
                key=lambda l: (int(l['to_Text_id']), int(l['Line_Position']))),
            lambda l: l['to_Text_id']
        ):
            for line in lines:
                args.writer.objects['ExampleTable'].append(dict(
                    ID='{0}-{1}'.format(text_id, line['Line_Position']),
                    Text_ID=text_id,
                    Language_ID=TSEZ,
                    Primary_Text=line['Tsez_Line'],
                    Analyzed_Word=chunks(line, 'Value'),
                    Gloss=chunks(line, 'Gloss'),
                    Part_of_Speech=chunks(line, 'Part_of_Speech'),
                    Translated_Text=line['English_Translation'],
                    Russian_Translation=line['Russian_Translation'],
                    Meta_Language_ID=EN,
                ))
