# EDX course structure generator

This tool will create a `.csv` file that sumurizes the structure of a EDX course from `.xml` files dowloaded from EDX plataform 🚀.

# Folder structure

```sh
├── JASD_ARCH301x
│   ├── {INPUT_NAME}.xml # Input File course.xml
│   ├── {OUTPUT_NAME}.csv # TokyoTechX+ARCH301x+2T2021
│   ├── chapter
│   ├── course
│   │   ├── XXXXX.xml
.   .   .   .   .
.   .   .   .   .
.   .   .   .   .
│   ├── html
│   │   ├── XXXXX.xml
│   │   ├── XXXXX.html
.   .   .   .   .
.   .   .   .   .
.   .   .   .   .
│   ├── problem
│   │   ├── XXXXX.xml
.   .   .   .   .
.   .   .   .   .
.   .   .   .   .
│   ├── sequential
│   │   ├── XXXXX.xml
.   .   .   .   .
.   .   .   .   .
.   .   .   .   .
│   ├── vertical
│   │   ├── XXXXX.xml
│   ├── video
│   │   ├── XXXXX.xml
.   .   .   .   .
.   .   .   .   .
.   .   .   .   .
```

# Instructions to run script

1. Run main file using the optinal arguments

```bash
python3 course_structure.py -i JASD_ARCH301x/course.xml -o JASD_ARCH301x/output.xml
```

Without any arguments, you must be inside the course folder that contains `course.xml` and the output file will be at the same parent level as `course.xml`

```bash
python3 course_structure.py -i JASD_ARCH301x/course.xml -o JASD_ARCH301x/output.xml
```

# Install as pip library
```sh
# PyPI
pip3 install git+https://github.com/sarmientoSD/edx_course_structure.git
```
``` python
from edx_course_structure import getCourseStructure
getCourseStructure("course.xml")
```
# Dependencies

- `lxml`
- `csv`
- `argparse`
