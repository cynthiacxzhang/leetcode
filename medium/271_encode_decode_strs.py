class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""

        encoded = []

        for s in strs:
            metadata = "{:4}".format(len(s)) # 4 char string with length of curr string

            # append padding and string
            encoded.append(metadata)
            encoded.append(s)
        
        # join metadata and strings for final encoded string
        to_send = "".join(encoded) # cannot pad with spaces, breaks decoding

        return to_send

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""

        decoded = []

        i = 0
        while i < len(s):
            word_size = int(s[i:i+4]) # slicing string from i to (but not including) i + 4
            i += 4

            curr_str = str(s[i:i + word_size]) # slicing string from after length val to end of curr word
            decoded.append(curr_str)
            i += word_size

        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))