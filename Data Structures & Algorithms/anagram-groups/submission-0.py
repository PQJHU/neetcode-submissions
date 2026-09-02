class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dictionary = dict()
        for string in strs:
            canonical_form = "".join(sorted([letter for letter in string])) #nlogn
            anagram_dictionary.setdefault(canonical_form, [])
            anagram_dictionary[canonical_form] = anagram_dictionary[canonical_form] + [string]

        anagram_books = [book for book in anagram_dictionary.values()]
        return anagram_books
        