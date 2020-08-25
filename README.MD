# Python E2E Test Tool

PythonでSeleniumを動かすときの覚書

# :key: Features

E2Eのテストツール

# :red_circle: Requirement

必要なライブラリ

* python 3.8
* selenium
* ChromeDriver

# :arrow_double_down: Installation

* python 3.8

https://prog-8.com/docs/python-env

 * Chrome Driver

```bash
$ brew cask install chromedriver
```

# :star: Usage

 ```bash
$ python demo.py
$ pytest demo_ide.py 
$ pytest demo_download.py && python demo_filecontrol.py
 ```

# :blue_book: Note

Selenium IDEからエクスポートして、Pythonのコードを自動生成可能。

**ポイント**

- 要素指定について自動生成されたものは修正が必要。find_elementで記載されている箇所は以下ドキュメントから修正する

https://selenium-python.readthedocs.io/locating-elements.html

- selfで参照している箇所は自身のローカル変数に入れ直せば、各必要なし

