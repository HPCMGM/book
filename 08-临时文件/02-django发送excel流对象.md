```python
    def send_data(self, filename, results, fields):
        f = xlwt.Workbook(encoding="utf-8")
        sheet = f.add_sheet("sheet1", cell_overwrite_ok=True)

        columns = [field[1] for field in fields]
        font_style_header = xlwt.XFStyle()
        font_style_header.font.bold = True
        font_style_body = xlwt.XFStyle()
        row_num = 0

        for col_num in range(len(columns)):
            sheet.write(row_num, col_num, columns[col_num], font_style_header)

        for rows in results:
            row_num += 1
            for col_num in range(len(fields)):
                res = rows.get(fields[col_num][0], "")
                if len(fields[col_num]) >= 3:
                    res = fields[col_num][2].get(res, "")
                sheet.write(row_num, col_num, res, font_style_body)
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        f.save(response)
        return response
```

