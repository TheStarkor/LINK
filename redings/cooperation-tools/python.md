# Python

### Virtualenv

* freeze 한 후 git에 push한다.

python의 대표적인 가상환경 모듈이다. 외부 환경과 분리되어 버전 및 패키지간 conflict를 막을 수 있고 서로의 개발환경을 공유 할 수 있다.

```text
$ pip install virtualenv
$ virtualenv <env name>            # 가상환경 생성
$ source <env name>/bin/activate   # 가상환경 실행
$ pip list                         # 설치된 패키지 목록
$ pip freeze > requirement.txt     # 패키지 목록 저장
$ pip install -r requirement.txt   # 패키지 목록 설
```

#### Vscode 실행 시 virtualenv 자동 실행 

```text
# .vscode/settings.json


{
  "python.pythonPath": "..\\venv\\Scripts\\python38.exe"
}
```



### Black

* 수정한 파일들을 formatting 한 후 push한다.

Python의 대표적인 code formatter다. git에 push 

```text
$ pip install black
$ black *<filename.py>
```

#### Vscode 에 파일 저장 시 자동 실행

```text
# .vscode/settings.json

{
  "editor.formatOnSave": true,
  "python.formatting.provider": "black"
}
```

