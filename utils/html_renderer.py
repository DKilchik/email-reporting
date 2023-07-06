from jinja2 import Environment, FileSystemLoader
import os

class HTML:

    def __init__(self, template: str, output, title: str, pack_name: str, features: int, total: int, failed: int, tests: list):
        self.template = template
        self.output = output
        self.title = title
        self.pack_name = pack_name
        self.features = features
        self.total = total
        self.failed = failed
        self.tests = tests

    def __get_style(self):
        with open("templates/static/bootstrap.min.css", "r") as f:
            css = f.read()
        return css
            
    def __render(self):
        template_folder, template = os.path.split(self.template)
        environment = Environment(loader=FileSystemLoader(template_folder))
        template = environment.get_template(template)
        with open(self.output, "w") as fh:
            fh.write(
                template.render(
                style = self.__get_style(),
                title = self.title,
                pack_name = self.pack_name,
                features = self.features,
                total = self.total,
                passed = self.total - self.failed,
                failed = self.failed,
                tests = self.tests
                ))
            
    def __get_html(self) -> str:
        with open(self.output, "r") as f:
            html = f.read()
        return html
    
    @property
    def render(self) -> str:
        self.__render()
        return self.__get_html()
    
    