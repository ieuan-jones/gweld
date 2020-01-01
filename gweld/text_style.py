class TextStyle:
    def __init__(self, text_type):
        self.text_type = text_type 

        self.size = 12
        self.angle = 0
        self._anchor = 'start'
        self.baseline = 'bottom'

    @property
    def anchor(self):
        return self._anchor if self.angle == 0 else 'start'

    @anchor.setter
    def anchor(self, anchor):
        self._anchor = anchor

    @property
    def css(self):
        return f'''
            .{self.text_type}_label {{
                font-size: {self.size}px;
                text-anchor: {self.anchor};
                dominant-baseline: {self.baseline};
            }}
        '''
