import argparse
from lxml import etree
import csv
import os


DISPLAY_NAME = "display_name"
ORG = "org"
COURSE = "course"
URL_NAME = "url_name"
FIRST_ROW = ["index", "section", "subsection", "unit", "section_id",
             "subsection_id", "unit_id", "type_name", "element_id"]


def parse_args():

    parser = argparse.ArgumentParser(prog='edx-crawler',
                                     description='Crawling text from the OpenEdX platform')

    # optional arguments
    parser.add_argument('-o',
                        '--output',
                        dest='output',
                        required=False,
                        action='store',
                        help='output name, default is TokyoTechX+######+#####.csv')
    parser.add_argument('-i',
                        '--input',
                        dest='input',
                        required=False,
                        action='store',
                        help='input name, default is course.xml')
    args = parser.parse_args()

    return args


def getCourseStructure(input_file, output_name=None):

    # Check if file exists
    file_exists = os.path.exists(input_file)
    if not file_exists:
        print("❌ Input file does not exist")
        return

    # Get abs outpath and abs input path
    OUTPUT_PATH = os.path.abspath(output_name) if output_name else None

    INPUT_NAME = os.path.abspath(input_file)

    ABSOLUTE_PATH = "/".join(INPUT_NAME.split("/")[:-1])

    # Work inside local path
    os.chdir(ABSOLUTE_PATH)

    # Open the input file
    with open(f"{INPUT_NAME}", "r") as f:
        main_root = etree.fromstring(f.read())

    # Get attributes of input file
    course_url_name = main_root.attrib.get(URL_NAME)
    course_org = main_root.attrib.get(ORG)
    course_course = main_root.attrib.get(COURSE)

    # Define the output file name based on the attributes of the input file
    output_name_final = OUTPUT_PATH if OUTPUT_PATH else "+".join(
        [course_org, course_course, course_url_name])

    # Prepate the output file to write as csv
    with open(f'{output_name_final}.csv', 'w') as csv_f:
        writer = csv.writer(csv_f)

        # Write the first row of the csv file(headers)
        writer.writerow(FIRST_ROW)

        # Open xml file in course folder based on the url_name
        with open(f"course/{course_url_name}.xml", "r") as f:
            course_root = etree.fromstring(f.read())

        # Init index of table
        index = 1

        # course_display_name = course_root.attrib.get(DISPLAY_NAME) ### Course name is not needed

        # Iterate over earch chapter
        for course_chapter in course_root.findall(".//chapter"):
            # Get chapter id
            chapter_url_name = course_chapter.attrib.get(URL_NAME)

            with open(f"chapter/{chapter_url_name}.xml") as f:
                chapter_root = etree.fromstring(f.read())

            # Get Chapter Name
            chapter_display_name = chapter_root.attrib.get(DISPLAY_NAME)
            # Iterate over each section
            for chapter_sequential in chapter_root.findall(".//sequential"):
                # Get section id
                sequential_url_name = chapter_sequential.attrib.get(URL_NAME)

                with open(f"sequential/{sequential_url_name}.xml") as f:
                    sequential_root = etree.fromstring(f.read())
                # Get section name
                sequential_display_name = sequential_root.attrib.get(
                    DISPLAY_NAME)

                # Iterate over each unit
                for sequential_vertical in sequential_root.findall(".//vertical"):
                    # Get unit id
                    vertical_url_name = sequential_vertical.attrib.get(
                        URL_NAME)

                    with open(f"vertical/{vertical_url_name}.xml", "r") as f:
                        vertical_root = etree.fromstring(f.read())
                    # Get unit name
                    vertical_display_name = vertical_root.attrib.get(
                        DISPLAY_NAME)

                    # Iterate over each child of unit (video, html, problem)
                    for vertical_child in vertical_root:
                        # Get type of child(video, html, problem)
                        type_name = vertical_child.tag
                        # Get element id
                        vertical_child_url_name = vertical_child.attrib.get(
                            URL_NAME)
                        row = [index,
                               chapter_display_name,
                               sequential_display_name,
                               vertical_display_name,
                               chapter_url_name,
                               sequential_url_name,
                               vertical_url_name,
                               type_name,
                               vertical_child_url_name]
                        index += 1
                        # Write row to csv file
                        writer.writerow(row)

        print("🚀 Finished creating course structure")


if __name__ == '__main__':
    # Read all arguments
    args = parse_args()

    input_name = args.input if args.input else "course"
    output_name = args.output

    getCourseStructure(input_name, output_name)
