from fpdf import FPDF

class ReportGenerator:

    def count_words(self, text):
        return len(text.split())

    def save_text_report(self, topic, content):
        filename = f"reports/{topic.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return filename

    def save_pdf_report(self, topic, content):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for line in content.split("\n"):
            pdf.multi_cell(0, 8, line)

        filename = f"reports/{topic.replace(' ', '_')}.pdf"
        pdf.output(filename)
        return filename