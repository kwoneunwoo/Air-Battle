# Air battle
Python game which made with the pygame module.

교내 CIT 활동을 계기로 Pygame 모듈을 통해 제작한 프로젝트입니다.

게임을 제작하며 파이썬의 객체(Class)에 대해 공부하며 자세히 알게 되었고,
파이썬에서 폴더를 기준으로 파일을 분리하여 라이브러리를 만드는 방법 또한 알게되었습니다.

# 실행 방법
현재 프로젝트에서는 내장 모듈인 os와 pygame만 사용하여 외부 모듈 다운로드 없이 즉시 실행 가능합니다.
다만 현 프로젝트는 main 브런치 하나만 사용하고 있으므로 레포지토리의
**[Releases](https://github.com/kwoneunwoo/Air-Battle/releases)에서 최신 버전을 다운로드하는 것을 권장**합니다. 

```
개발 환경:
- Python 3.11.2
- pygame 2.5.2
```

# 조작 방법
- main.py를 실행합니다.
- 시작 화면
    - `스페이스 키`를 누를시 시작됩니다.
    - 좌측 상단 기어 이미지 클릭시 설정창으로 진입합니다.
- 설정 화면
    - 모든 설정은 조작 즉시 적용됩니다.
    - `Esc 키` 혹은 돌아가기 버튼을 누를시 설정창에서 빠져나올 수 있습니다.
- 게임 화면
    - 키보드의 `화살표 키`를 이용하여 전투기를 상하좌우로 조작할 수 있습니다.
    - `Ctrl 키` 혹은 `스페이스 키`를 이용하여 총알을 발사할 수 있습니다.
    - `Esc 키`를 누를시 게임이 즉시 종료됩니다.
- 종료 화면
    - `R 키`를 통해 게임을 재시작 할 수 있습니다.
    - `Esc 키`를 누를시 게임이 즉시 종료됩니다.

# 파일 구조
```bash
📦Air-Battle
 ┣ 📜main.py
 ┣ 📜config.py
 ┣ 📜LICENCE
 ┣ 📜README.md
 ┣ 📜resource source.txt
 ┣ 📂objects
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜image.py
 ┃ ┣ 📜image_button.py
 ┃ ┣ 📜int_button.py
 ┃ ┗ 📜toggle_button.py
 ┣ 📂resources
 ┃ ┣ 📂fonts
 ┃ ┣ 📂images
 ┃ ┗ 📂sounds
 ┗ 📂screens
   ┣ 📜__init__.py
   ┣ 📜ending.py
   ┣ 📜game.py
   ┣ 📜setting.py
   ┗ 📜start.py

```