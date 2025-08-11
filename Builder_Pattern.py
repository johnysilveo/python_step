class ReportBuilder:
    def __init__(self):
        self.report = {'title': "", 'date': "", 'content': ""}

    def set_title(self, title):
        self.report['title'] = title
        return self

    def set_date(self, date):
        self.report['date'] = date
        return self

    def set_content(self, content):
        self.report['content'] = content
        return self

    def build(self):
        return self.report

builder = ReportBuilder()
report = builder.set_title('Python').set_date('2025-08-04').set_content('news py').build()
print(report)
