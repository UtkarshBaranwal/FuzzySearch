from django.http import HttpResponse
import json
from django.shortcuts import render
import openpyxl

# Create one array
list_data = []


def index(request):
    # location of the file
    loc = "C:/Users/ubaranwal/Pictures/word_search.xlsx"

    # you may put validations here to check extension or file size
    wb = openpyxl.load_workbook(loc)
    # getting a particular sheet by name out of many sheets
    worksheet = wb["word_search"]

    excel_data = list()

# iterating over the rows and getting value from each cell in row
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
        list_data.append(row_data[0])

    return render(request, "sub_module/test.html")


def company_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")

        print([i for i in list_data if query in i])
        data = json.dumps([i for i in list_data if query in i])

    mimetype = "application/json"
    return HttpResponse(data, mimetype)





