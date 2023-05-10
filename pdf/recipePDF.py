#
# Purpur Tentakel
# Cocking Book
# 05.05.2023
#

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table

from helper import log
from database import select as s

import webbrowser

_title: str | None = None


class RecipePDF:
    def __init__(self) -> None:
        self.dir_name: str = str()
        self.file_name: str = str()
        self.style_sheet = getSampleStyleSheet()
        self.custom_styles: dict = dict()
        self._add_styles()

        self._last_export_path: str = str()

    def _add_styles(self) -> None:
        self.custom_styles['CustomTitle'] = (ParagraphStyle(name='CustomTitle', parent=self.style_sheet['Title'],
                                                            fontSize=35, leading=1.2 * cm))
        self.custom_styles['CustomHeading'] = (ParagraphStyle(name='CustomHeading', parent=self.style_sheet['Heading1'],
                                                              fontSize=15))
        self.custom_styles['CustomBodyTextLeft'] = (ParagraphStyle(name='CustomBodyTextRight',
                                                                   parent=self.style_sheet['BodyText'], fontSize=10,
                                                                   leading=0.2 * cm))
        self.custom_styles['CustomBodyTextRight'] = (ParagraphStyle(name='CustomBodyTextRight',
                                                                    parent=self.style_sheet['BodyText'], fontSize=10,
                                                                    alignment=TA_RIGHT))
        self.custom_styles['CustomBodyTextCenter'] = (ParagraphStyle(name='CustomBodyTextCenter',
                                                                     parent=self.style_sheet['BodyText'], fontSize=10,
                                                                     alignment=TA_CENTER))
        self.custom_styles['CustomBodyTextSmall'] = (ParagraphStyle(name='CustomBodyTextSmall',
                                                                    parent=self.style_sheet['BodyText'], fontSize=6,
                                                                    leading=0.23 * cm))
        self.custom_styles['CustomBodyTextSmallCenter'] = (ParagraphStyle(name='CustomBodyTextSmallCenter',
                                                                          parent=self.style_sheet['BodyText'],
                                                                          fontSize=6, leading=0.23 * cm,
                                                                          alignment=TA_CENTER))
        self.custom_styles['CustomCenterHeading3'] = (ParagraphStyle(name='CustomCenterHeading3',
                                                                     parent=self.style_sheet['Heading3'],
                                                                     alignment=TA_CENTER))

    def open_last_export(self) -> bool:
        if not self._last_export_path.strip():
            return False

        webbrowser.open_new(self._last_export_path)
        return True

    def export(self, e_dir: str, file_name: str, ID: int) -> bool:
        self.dir_name = e_dir
        self.file_name = file_name

        doc: SimpleDocTemplate = self._get_doc()
        recipe_result = s.select.select_recipe_by_ID(ID)
        if not recipe_result.valid:
            log.message(log.LogType.ERROR, "recipePDF.py", "self.export()",
                        f"failed to load recipe data with ID -> {ID}")
            return False

        elements: list = list()
        elements.extend(self._get_headline(recipe_result.entry))
        elements.extend(self._get_tags(ID))
        elements.extend(self._get_ingredients(ID, self._get_scale_factor(recipe_result.entry)))
        elements.extend(self._get_description(recipe_result.entry))

        return self._export(doc=doc, elements=elements)

    def _get_headline(self, recipe_data: list) -> list:
        _, title, _, _, scale_serving_count = recipe_data
        elements: list = list()

        global _title
        _title = title

        elements.append(Paragraph(title, self.custom_styles["CustomTitle"]))
        elements.append(
            Paragraph(f"{scale_serving_count} servings", self.custom_styles['CustomBodyTextCenter']))
        elements.append(Spacer(width=0, height=1 * cm))

        return elements

    def _get_tags(self, ID: int) -> list:
        tag_result = s.select.select_type_by_recipe_ID(ID)
        if not tag_result.valid:
            log.message(log.LogType.ERROR, "recipePDF.py", "self._get_tags()",
                        f"could not load tags from recipe id -> {ID}")
            return list()

        elements: list = list()
        elements.append(Paragraph("Tags:", self.custom_styles['CustomHeading']))

        if len(tag_result.entry) == 0:
            elements.append(Paragraph("no tags", self.custom_styles['CustomBodyTextLeft']))
        else:
            for _, _, raw_type_ID_s in tag_result.entry:
                raw_type_result = s.select.select_raw_type_by_ID(raw_type_ID_s)
                if not raw_type_result.valid:
                    log.message(log.LogType.ERROR, "recipePDF.py", "self._get_tags()",
                                f"could not load tag from tag ID -> {ID}")
                    continue
                elements.append(Paragraph(f"- {raw_type_result.entry}", self.custom_styles['CustomBodyTextLeft']))

        elements.append(Spacer(width=0, height=1 * cm))
        return elements

    def _get_ingredients(self, ID: int, scale_factor: float) -> list:
        ingredient_result = s.select.select_all_ingredients_from_recipe(ID)
        if not ingredient_result.valid:
            log.message(log.LogType.ERROR, "recipePDF.py", "self._get_ingredients()",
                        f"could not load ingredients from recipe id ->{ID}")
            return list()

        elements: list = list()
        elements.append(Paragraph("Ingredients", self.custom_styles['CustomHeading']))

        if len(ingredient_result.entry) == 0:
            elements.append(Paragraph("no ingredients", self.custom_styles['CustomBodyTextLeft']))
        else:
            table_data: list = list()
            for _, _, amount, unit, ingredient in ingredient_result.entry:
                table_data.append([f"{amount * scale_factor} {unit}", ingredient])
            table = Table(table_data, hAlign='LEFT', rowHeights=0.5 * cm)
            elements.append(table)

        elements.append(Spacer(width=0, height=1 * cm))
        return elements

    def _get_description(self, recipe_data: list) -> list:
        _, _, description, *_ = recipe_data
        description: str
        description = description.replace("\n", "<br/>")
        elements: list = list()

        elements.append(Paragraph("Description:", self.custom_styles["CustomHeading"]))
        elements.append(Paragraph(description, self.style_sheet['BodyText']))

        return elements

    def _paragraph(self, value) -> Paragraph:
        if isinstance(value, list):
            return Paragraph(str(value[0]) + ": " + str("---" if not value[1] else value[1]),
                             self.style_sheet["BodyText"])
        else:
            return Paragraph(str("---" if not value else value), self.style_sheet["BodyText"])

    def _get_doc(self) -> SimpleDocTemplate:
        self._last_export_path = f"{self.dir_name}/{self.file_name}"
        return SimpleDocTemplate(self._last_export_path, showBoundary=0, pagesize=A4, rightMargin=1.5 * cm,
                                 leftMargin=1.5 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm)

    def _export(self, doc: SimpleDocTemplate, elements: list, numbered: bool = True) -> bool:
        global _title
        try:
            if numbered:
                doc.build(elements, canvasmaker=NumberedCanvas)
            else:
                doc.build(elements)
            _title = None
            return True
        except PermissionError:
            log.message(log.LogType.ERROR, "recipePDF.py", "self._export()",
                        f"no premission to export PDF -> {self.dir_name}\\{self.file_name}")
            _title = None
            return False

    @staticmethod
    def _get_scale_factor(recipe_data: list) -> float:
        if len(recipe_data) == 0:
            return 1.0

        _, _, _, standard, scale = recipe_data
        return scale / standard


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs) -> None:
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self) -> None:
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self) -> None:
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count) -> None:
        self.setFont("Helvetica", 10)
        entry: str = f"{_title} | page {self._pageNumber} of {page_count}" if _title else f"page {self._pageNumber} of {page_count}"
        self.drawRightString(20 * cm, 2 * cm, entry)
