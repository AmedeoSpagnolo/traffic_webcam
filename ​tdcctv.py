import time
import urllib

cameras = {
    "tung_chung": {
        "name": "Tung Chung",
        "type": "Hwy",
        "code": "NL128F"},
    "pak_mong": {
        "name": "Pak Mong",
        "type": "Hwy",
        "code": "NL126F"},
    "lantau_link": {
        "name": "Lantau Link",
        "type": "Tol",
        "code": "TC573F"},
    "kap_shui_mun": {
        "name": "Kap Shui Mun",
        "type": "Bridge",
        "code": "TC551F"},
    "siu_ho_wan": {
        "name": "Siu Ho Wan",
        "type": "Hwy",
        "code": "NL124F"},
    "sunny_bay": {
        "name": "Sunny Bay",
        "type": "Hwy",
        "code": "NL121F"},
    "tsing_ma": {
        "name": "Tsing Ma",
        "type": "Bridge",
        "code": "TC560F"},
    "kwai_chung_road": {
        "name": "Kwai Chung Road",
        "type": "Hwy",
        "code": "TW102F"}
}

def download_screenshot(_url,_name):
    urllib.urlretrieve(_url,"export/"+str(_name))
    time.sleep(0.5)

def url(_camera, _time):
    return "http://tdcctv.data.one.gov.hk/%s.JPG?time=%s" % (_camera, _time)

while True:
    ts = str(time.time()).split('.')[0]
    for c in cameras.keys():
        filename = c + "_" + str(ts) + ".JPG"
        image = url(cameras[c]["code"],ts)
        print "saving " + filename + " from " + image
        download_screenshot(image, filename)
    time.sleep(10)
