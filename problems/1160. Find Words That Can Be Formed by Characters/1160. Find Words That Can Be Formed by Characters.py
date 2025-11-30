from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """accepted"""
        map = {}
        for letter in chars:
            print(letter)
            if letter in map:
                print(map.get(letter), map.get(letter) + 1)
                map[letter] = map.get(letter) + 1
                continue
            map[letter] = 1
        print(map)
        count = 0
        for word in words:
            word_map = map.copy()
            print(word)
            is_valid = True
            for letter in word:
                if not word_map.get(letter):
                    print("\t", letter, "not found")
                    is_valid = False
                # if not is_valid:
                    break
                print(
                    f"\t {letter}: {word_map.get(letter)} -> {word_map.get(letter) - 1}")
                word_map[letter] = word_map.get(letter) - 1
            if is_valid:
                count += len(word)
                # print(word)
            # print(word_map)
        return count


if __name__ == "__main__":
    S = Solution()
    inps = [
        (["cat", "bt", "hat", "tree"], "atach"),
        (["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin", "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh", "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx", "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop", "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx", "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl",
         "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp", "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz", "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue", "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv", "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob", "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs", "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"], "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"),
        (["hello", "world", "leetcode"], "welldonehoneyr"),
    ]
    inp = inps[-1]
    print(S.countCharacters(inp[0], inp[1]))

    # for i in inp[0]:
    #     print(S.countCharacters([i], inp[1]))

    # print(S.countCharacters([inp[0][3]], inp[1]))
