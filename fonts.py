from PyQt6.QtGui import QFont, QFontDatabase


class FontManager:
    def __init__(self):
        self.fonts = {
            "swiss911": "./resources/fonts/swiss-911.ttf",
            "korina": "./resources/fonts/korina-bold.ttf"
        }
        self.font_ids = {}

        for k, v in self.fonts.items():
            font_id = QFontDatabase.addApplicationFont(v)
            self.font_ids[k] = font_id

    def get_custom_font(self, font, point_size):
        font = QFontDatabase.applicationFontFamilies(self.font_ids[font])[0]
        return QFont(font, point_size)
