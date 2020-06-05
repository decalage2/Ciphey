from SimpleClassifier.encoding import all_encoding_classifiers, all_encodings
from SimpleClassifier.hashes import all_hash_classifiers, all_hashes


class filterResults:
    failed_encodings = set()
    failed_hashes = set()
    lengths = set()


def filterOut(data: str) -> filterResults:
    """Filters out options which it cannot be
        
        For example, it cannot be binary if it contains a 6.

        args:
            data -> the data we want to check for filtration

        results:
            filterResults -> the results of the filtration system

        """
    ret = filterResults()
    ret.lengths.add(len(data))
    # First, gather the encodings, so that we can get the lengths
    for encoding in all_encoding_classifiers:
        res = encoding.classify(data)
        if res:
            ret.lengths |= res
        else:
            ret.failed_encodings.add(encoding.name())

    # Now we can iterate over the rest
    for hash in all_hash_classifiers:
        if hash.isImpossible(data, ret.lengths):
            ret.failed_hashes.add(hash.name())

    return ret
