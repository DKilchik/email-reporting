from utils.data_parser import CucumberReport, By
from utils.html_renderer import HTML

import os

report = CucumberReport("/home/dmitry/peronalProjects/eshop-atf/eshop-atf/target/cucumber-reports")

report.merge()
report.sort(By.FEATURE)

features = report.get_total_features
total = report.get_total
failed = report.get_failed
tests = report.get_results


root = os.path.dirname(os.path.abspath(__file__))
template = os.path.join(root, 'templates', 'bootstrap.html')
output = os.path.join(root, 'html', 'index.html')

HTML(template=template,
     output=output,
     title="E-Shot Testing",
     pack_name="Smoke pack",
     features=features,
     total=total,
     failed=failed,
     tests=tests).render