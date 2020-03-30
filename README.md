# jjambot (짬봇)


## 설치 안내 (Installation Process)

### nvm 설치

- 관련 패키지 설치하기

ubuntu에 nvm을 설치하기 위해, apt를 이용하여 설치
npm 및 nodejs 관련 모듈을 설치하기 위해 apt로 다음과 같은 모듈을 먼저 설치

```bash
$ sudo apt-get install build-essential libssl-dev
```





- nvm 설치
curl을 이용하여 nvm을 설치 (0.35.3 버전 기준)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

Information.

	[리눅스] https://github.com/creationix/nvm#installation
	[윈도우] https://github.com/coreybutler/nvm-windows


- bashrc를 통해 적용
bashrc를 업데이트 합니다. 

```bash
$ source ~/.bashrc
```

- nvm 설치 확인
nvm이 정상적으로 설치되었는지를 확인해보기 위해서, nvm version을 확인해 봅니다.

```bash
$ nvm --version
```

	예시: 0.35.3


---

### nodejs 설치

- nodejs 설치

nvm의 설치 후 nodejs 설치 가능.

lts(long term support) 버전으로 설치.


```bash
$ nvm install --lts
```

- node의 설치 확인
node가 정상적으로 설치되었는지를 확인.

```bash
$ node -v
```

	예시: v10.13.0


---



### expressjs 설치

- expressjs 설치

nodejs에서 제일 많이 사용되는 웹 프레임워크. 간단한 코드로 높은 성능을 내고 다양한 기능을 가진 웹 서버를 생성할 수 있음.


```bash
$ npm i --save express
```

- morgan, body-parser 라이브러리를 추가

morgan은 로깅을 담당하고 body-parser는 http 요청의 body를 추출합니다.


```bash
$ npm i --save morgan body-parser
```



---


### 추가 모듈 설치

- xml-js

XML to JSON converters


```bash
$ npm install --save xml-js
```



---






## 참고자료

https://i.kakao.com/docs/skill-build#%EC%98%88%EC%A0%9C-%EC%8A%A4%ED%82%AC-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0
