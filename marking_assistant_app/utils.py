import os
import openpyxl

from marking_assistant_project import settings

def generate_marking_results_excel(marking_results_data):
    # Create a new Excel workbook and add data to it
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Student Number", "Assignment Number", "Task Number", "Marks", "Feedback"])

    for result in marking_results_data:
        ws.append([result["student_number"], int(result["assignment_number"]), int(result["task_number"]),
                   float(result["marks"]), result["feedback"]])

    # Save the Excel file temporarily on the server
    filename = "marking_results.xlsx"
    excel_file_path = os.path.join(settings.MEDIA_ROOT, filename)
    wb.save(excel_file_path)

    return excel_file_path