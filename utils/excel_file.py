import io
import openpyxl


async def generate_excel_file(user_ids):
    # Создаем новую книгу Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Users"

    # Заголовки столбцов
    sheet['A1'] = "User ID"

    # Заполняем данными
    for user_id in user_ids:
        sheet.append([str(user_id)])

    # Создаем бинарный поток для записи в файл
    excel_buffer = io.BytesIO()
    workbook.save(excel_buffer)
    excel_buffer.seek(0)

    return excel_buffer
