# gdal2tiles (ondemand patch)
## はじめに
[gdal2tiles](https://github.com/tehamalab/gdal2tiles)は、GDALを使用してGeoTIFFをタイル化するためのツールです。  
このリポジトリは、タイル画像をダイナミックに生成する関数を拡張しています。  
動的に変化するラスターデータをXYZタイルとして配信することができます。

## 使い方
```
def create_ondemand_tiles(input_file, output_folder, z, x, y)
```
- `input_file`: タイル化するGeoTIFFファイルのパス
- `output_folder`: タイル画像を保存するフォルダのパス
- `z`: ズームレベル
- `x`: タイルのX座標
- `y`: タイルのY座標

## 実装例
djangoを使用した実装例を以下に示します。

#### urls.py
```python
from django.urls import path
from . import views
urlpatterns = [
    path('xyz/<int:z>/<int:x>/<int:y>.png', views.outputtile, name='outputtile'),
]
```
#### views.py
```python 
from django.http import HttpResponse
from gdal2tiles import *

def outputtile(request, z, x, y):
    input_file = 'path/to/your/geotiff/file.tif'
    output_folder = 'path/to/output/folder'
    
    # タイル画像が生成済みか確認
    tile_path = f"{output_folder}/{z}/{x}/{y}.png"
    if not os.path.exists(tile_path):
        # タイルを生成（指定された座標によっては、タイル画像が生成されない場合がある)
        create_ondemand_tiles(input_file, output_folder, z, x, y)

    # タイル画像を返す
    if os.path.exists(tile_path):
        max_age = 3660  # キャッシュの寿命を適切に設定
         with open(tile_path, 'rb') as f:
            res = HttpResponse(f.read(), content_type='image/png')
            res['Cache-Control'] = f'max-age={max_age}'
            return res
    return HttpResponse('Not Found', status=404)
```


### [オリジナルのREADMEへ](README_ORG.rst)
