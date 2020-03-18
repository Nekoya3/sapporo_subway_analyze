#凡例のカラーパレット
#0->4 より混雑
CROWD_RGBs = [
    [255, 255, 255],
    [112, 200, 241],
    [57, 83, 164],
    [246, 235, 20],
    [237, 32, 36]
]

#PDF左表の左上のセルの中心点の座標
LEFT_START_CELL = (100,830)
#PDF右表の左上のセルの中心点の座標
RIGHT_START_CELL = (1050,830)
#PDFのセルひとつあたりのサイズ
CELL_SIZE = (95, 68)

#PDFのセルの数
COL_COUNT = 6
ROW_COUNT = 15

#CSVのヘッダー
CSV_HEADER = [
    "出発駅",
    "到着駅",
    "7:00 - 7:29",
    "7:30 - 7:59",
    "8:00 - 8:29",
    "8:30 - 8:59",
    "9:00 - 9:29",
    "9:30 - 9:59",
]

#CSVの列タイトル
STOP_NAMES = {
    'namboku':[
        "麻生",
        "北34条",
        "北24条",
        "北18条",
        "北12条",
        "さっぽろ",
        "大通",
        "すすきの",
        "中島公園",
        "幌平橋",
        "中の島",
        "平岸",
        "南平岸",
        "澄川",
        "自衛隊前",
        "真駒内",
    ],
    'tozai':[
        '宮の沢',
        '発寒南',
        '琴似',
        '二十四軒',
        '西28丁目',
        '円山公園',
        '西18丁目',
        '西11丁目',
        '大通',
        'バスセンター前',
        '菊水',
        '東札幌',
        '白石',
        '南郷7丁目',
        '南郷13丁目',
        '南郷18丁目',
        '大谷地',
        'ひばりが丘',
        '新さっぽろ'
    ],
    'toho':[
        '堺町',
        '新道東',
        '元町',
        '環状通東',
        '東区役所前',
        '北13条東',
        'さっぽろ',
        '大通',
        '豊水すすきの',
        '学園前',
        '豊平公園',
        '美園',
        '月寒中央',
        '福住'
    ]
}