def uppercase(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @uppercase
    def format_text(self, text):
        return text

    def generate(self, template="default"):
        return self.templates[template].format(
            title=self.title,
            content=self.content
        )

    def __str__(self):
        return self.generate()


# Define templates
Report.add_template("default", "REPORT: {title}\n{content}")
Report.add_template("simple", "{title}\n---\n{content}")

# Create report
report = Report("Monthly Sales", "Sales increased by 20%.")

print(report.generate("default"))
print(report.generate("simple"))

# Decorator formatting
print(report.format_text("hello world"))
