class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('result.html', 'w')

        fout.write("<html>")

        fout.write("<head>")
        # fout.write("<meta charset='utf-8'>")
        fout.write("</head>")

        fout.write("<body>")
        fout.write("<table>")

        # ASCII
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data.url)

            for title in data.titles:
                fout.write("<td>%s</td>" % title)
            fout.write("</tr>")

        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")

        fout.close()