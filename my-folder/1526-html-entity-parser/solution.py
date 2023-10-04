class Solution:
    def entityParser(self, text: str) -> str:
        '''
        html_entities = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        # Regular expression to match valid HTML entities
        pattern = re.compile(r'&quot;|&apos;|&amp;|&gt;|&lt;|&frasl;')
        
        # Replace valid HTML entities with special characters
        def replace_entities(match):
            return html_entities.get(match.group())
        
        # Use regular expression substitution to replace entities
        return pattern.sub(replace_entities, text)
        '''
        html_symbol = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = text.replace( html_sym , formal_sym )
        
        return text

