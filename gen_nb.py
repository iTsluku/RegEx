import json
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb["cells"] = []

# generate md and code cells
# header
header = """
# RegEx
A practical introduction to regular expressions using Python.
"""
nb['cells'].append(nbf.v4.new_markdown_cell(header))

# load tasks
tasks = []
with open('tasks.json') as f:
    tasks = json.load(f)

# table of contents
toc = """
<a id="tableofcontents"></a>
# Table of contents
1. [Tasks](#tasks)
"""
for task in tasks:
    toc+="\n\t"
    toc+=f'1. [{task["title"]}](#task-{task["title"]})'
toc+="\n"
toc+="1. [Solutions](#solutions)"
for task in tasks:
    toc+="\n\t"
    toc+=f'1. [{task["title"]}](#solution-{task["title"]})'
toc+="\n"
toc+="1. [References](#references)"
nb['cells'].append(nbf.v4.new_markdown_cell(toc))

# contents
tasks_section = """
<a id="tasks"></a>
# Tasks
"""
nb['cells'].append(nbf.v4.new_markdown_cell(tasks_section))
for task in tasks:
    description = f'<a id="task-{task["title"]}"></a>\n'
    description+=f'## Task: {task["title"]}\n'
    description+=task["description"]
    nb['cells'].append(nbf.v4.new_markdown_cell(description))
    
    task_code_skeleton = """""" #TODO
    nb['cells'].append(nbf.v4.new_code_cell(task_code_skeleton))
    
solutions = """
<a id="solutions"></a>
# Solutions
The approaches below illustrate only one variant of solving the tasks.
"""
nb['cells'].append(nbf.v4.new_markdown_cell(solutions))
for task in tasks:
    description = f'<a id="solution-{task["title"]}"></a>\n'
    description+=f'## Solution: {task["title"]}\n'
    description+=task["description"]
    nb['cells'].append(nbf.v4.new_markdown_cell(description))
    
    task_code_solution = """""" #TODO
    nb['cells'].append(nbf.v4.new_code_cell(task_code_solution))

# references
references ="""
<a id="references"></a>
## References
**[1]** Python docs: https://docs.python.org/3/library/re.html#
"""
nb['cells'].append(nbf.v4.new_markdown_cell(references))

NB_NAME = "RegEx.ipynb"

with open(NB_NAME, "w", encoding='utf-8') as f:
    nbf.write(nb, f)
    