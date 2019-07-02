import urllib.request


def get_html(url):
    headers = (
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    try:
        page = opener.open(url, timeout=2)
    except Exception as e:
        print('错误：'+str(e)+' ，已跳过，请检查网络连接或修改最长等待时间')
        return ''
    try:
        html = page.read()
    except Exception as e:
        print('错误：'+str(e)+' ，已跳过，请检查网络连接或修改最长等待时间')
        return ''
    html = html.decode("utf8", "ignore")
    return html