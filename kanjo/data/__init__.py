import csv
import esmre
import json
import pkg_resources

class Resource(object):
    _instance = None
    _cached = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Resource, cls).__new__(cls)
        return cls._instance


    def _load_file(self, package, path):
        return pkg_resources.resource_stream(package, path)


    def _load_json(self, package, path):
        return json.load(self._load_file(package, path))


    def _load_tsv(self, package, path):

        data = []
        with self._load_file(package, path) as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                data.append(row)
        return data


    def lazy_load(self, loader, package, path):
        try:
            return self._cached[path]
        except KeyError:
            data = loader(package, path)
            self._cached[path] = data
            return data


class Geo(Resource):

    @property
    def state_coordinates(self):
        path = 'geo/state_coordinates.json'
        package = __name__
        return self.lazy_load(self._load_json, package, path)


    @property
    def state_regions_divisions(self):
        path = 'geo/state_regions_divisions.json'
        package = __name__
        return self.lazy_load(self._load_json, package, path)


class Lexicons(Resource):
  
    @property
    def AFINN(self):
        path = 'lexicons/AFINN-111.tsv'
        package = __name__
        return self.lazy_load(self._load_tsv, package, path)


    @property
    def AFINN_index(self):
        name = 'AFINN_index'
        try:
            return self._cached[name]
        except KeyError:
            data = self.AFINN
            index = esmre.Index()
            for word, score in data:
                index.enter(word, (word, int(score)))

            self._cached[name] = index
            return index


    @property
    def Emoticons(self):
        path = 'lexicons/EmoticonLookupTable.tsv'
        package = __name__
        return self.lazy_load(self._load_tsv, package, path)


    @property
    def NRCHashtags(self):
        path = 'lexicons/NRC-Hastag-Sentiment-Lexicon-unigrams-pmilexicon.tsv'
        package = __name__
        return self.lazy_load(self._load_tsv, package, path)


    @property
    def NRCHashtags_lkp(self):
        name = 'NRCHashtags_lkp'
        try:
            return self._cached[name]
        except KeyError:
            data = self.NRCHashtags
            lkp = {x[0] : float(x[1]) for x in data}
            self._cached[name] = lkp
            return lkp    


    @property
    def Slangs(self):
        path = 'lexicons/SlangLookupTable.tsv'
        package = __name__
        return self.lazy_load(self._load_tsv, package, path)


    @property
    def Slangs_index(self):
        name = 'Slangs_index'
        try:
            return self._cached[name]
        except KeyError:
            data = self.Slangs
            index = esmre.Index()
            for slang, replacement in data:
                index.enter(slang, (slang, replacement))

            self._cached[name] = index
            return index

geo = Geo()
lexicons = Lexicons()