# merge PDF with bookmark

unit1.pdf + unit2.pdf = merge.pdf, and merge.pdf has 2 bookmarks.

```
pip3 install PyPDF2
```

## version

```py
from PyPDF2 import PdfMerger
import argparse
import os


def scanPDF(pdf_path):
    pdf_list = []
    for file in os.listdir(pdf_path):
        if file.endswith('.pdf'):
            pdf_list.append(file)
    return pdf_list


def mergePDF(input_pdf_list, merged_pdf_path):
    assert(input_pdf_list != [])
    merger = PdfMerger()
    for pdf in input_pdf_list:
        assert pdf.endswith('.pdf')
        bookmark = pdf.split('.')[0]
        merger.append(pdf, outline_item=bookmark)
    merger.write(merged_pdf_path)
    merger.close()


if __name__ == '__main__':
    # parse command line parameters
    parser = argparse.ArgumentParser(
        description='Merge pdf files with bookmark.')
    parser.add_argument('-i', dest='input_pdf_path',
                        help='input pdf files name path')
    parser.add_argument('-o', dest='merged_pdf_path',
                        default='./merged.pdf', help='merged pdf file path')
    results = parser.parse_args()

    # merge PDF
    if os.path.isdir(results.input_pdf_path):
        input_pdf_list = scanPDF(results.input_pdf_path)
        # TODO: so ugly!
        input_pdf_list.sort(key=lambda x: int(
            x.split('_')[0].replace('u', '')))
        os.chdir(results.input_pdf_path)
        # print(input_pdf_list)
        mergePDF(input_pdf_list, results.merged_pdf_path)
        print('\n Successfully merged {}'.format(results.merged_pdf_path))
```

## useage

```bash
python3 temp.py -i unit1.pdf unit2.pdf -o merged.pdf
```


## ref 

https://pypdf2.readthedocs.io/en/latest/index.html



