# 1. HttpResponse

## 1.1 普通响应类

继承于`HttpResponseBase`, 此类是作为普通响应的, 参数如下

```python
class HttpResponse(HttpResponseBase):
	def __init__(self, content=b'', *args, **kwargs):
    	super().__init__(*args, **kwargs)
        
class HttpResponseBase:
    status_code = 200
    def __init__(self, content_type=None, status=None, reason=None, charset=None):
        ...
```

### 1.1.1 发送流(excel)

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



## 1.2 参数说明

| 参数         | 类型      | 关键字 | 说明                                |
| ------------ | --------- | ------ | ----------------------------------- |
| content      | str/bytes | 否     | 需要发送前端的数据                  |
| content_type | str       | 否     | 数据类型                            |
| status       | int       | 否     | 响应码                              |
| reason       | str       | 否     | 提供响应头部中的`reason_phrase`属性 |
| charset      | str       | 否     | 需要解析的字符集                    |

## 1.3 响应头部信息传递

```python
def get(self, request):
	response = HttpResponse()
	response["xxx"] = yy
    return response
```



# 2. JsonResponse

## 2.1 响应json数据

继承于`HttpResponseBase`, 此类是作为json响应的, 参数如下

```python
 def __init__(self, data, encoder=DjangoJSONEncoder, safe=True,
                 json_dumps_params=None, **kwargs):
```

## 2.2 参数说明

| 参数              | 类型  | 关键字 | 说明                                          |
| ----------------- | ----- | ------ | --------------------------------------------- |
| data              | dict  | 是     | 需要发送前端的数据                            |
| encoder           | class | 否     | 用于序列化json的类, 默认为`DjangoJSONEncoder` |
| safe              | bool  | 否     | 是否对传入的data数据进行安全校验              |
| json_dumps_params | dict  | 否     | `json.dumps`中的关键字参数的中转字典          |
| content_type      | str   | 否     | 数据类型                                      |
| status            | int   | 否     | 响应码                                        |
| reason            | str   | 否     | 提供响应头部中的`reason_phrase`属性           |
| charset           | str   | 否     | 需要解析的字符集                              |

# 10. 异常类

| 类                            | 状态码 |
| ----------------------------- | ------ |
| HttpResponseRedirect          | 301    |
| HttpResponsePermanentRedirect | 302    |
| HttpResponseNotModified       | 304    |
| HttpResponseBadRequest        | 400    |
| HttpResponseNotFound          | 404    |
| HttpResponseForbidden         | 403    |
| HttpResponseNotAllowed        | 405    |
| HttpResponseGone              | 410    |
| HttpResponseServerError       | 500    |



