# 🚀 TeDDie-RagAPI

TeDDie 프로젝트를 위한 RAG(Retrieval-Augmented Generation) 검색 API 서버입니다.  
우아한테크코스 프리코스 과제 데이터를 기반으로 유사도 검색을 제공합니다.

## 📋 목차

- [프로젝트 개요](#-프로젝트-개요)
- [기능 체크리스트](#-기능-체크리스트)
- [프로젝트 구조](#-프로젝트-구조)
- [설치 및 실행](#-설치-및-실행)
- [API 명세](#-api-명세)
- [개발 가이드](#-개발-가이드)

---

## 🎯 프로젝트 개요

### 목적
Java로 작성된 TeDDie 애플리케이션에서 HTTP 요청으로 우테코 과제 검색 기능을 사용할 수 있도록 FastAPI 기반 REST API를 제공합니다.

### 아키텍처
```
[TeDDie (Java)]
    ↓ HTTP POST
[TeDDie-RagAPI (FastAPI)]
    ↓ import & call
[TeDDie-RagSystem (Python RAG Library)]
```

### 기술 스택
- **Framework**: FastAPI 0.104.1
- **Server**: Uvicorn 0.24.0
- **Testing**: pytest 7.4.3, httpx 0.25.2
- **Python**: 3.10+

---

## ✅ 기능 체크리스트

### Phase 1: 기본 인프라 구축
- [X] **1.1 프로젝트 초기 설정**
  - [X] Repository 생성
  - [X] 폴더 구조 생성 (`api/`, `test/`)
  - [X] `.gitignore` 작성
  - [X] `requirements.txt` 작성
  - [X] 가상환경 생성 및 의존성 설치
  - [X] README.md 작성

- [X] **1.2 기본 FastAPI 앱 생성**
  - [X] `api/__init__.py` 생성
  - [X] `api/app.py` 생성 (FastAPI 앱 정의)
  - [X] 루트 엔드포인트 (`/`) 구현
  - [X] `main.py` 생성 (서버 실행 스크립트)

- [X] **1.3 기본 API 테스트**
  - [X] `test/__init__.py` 생성
  - [X] `test/test_app.py` 생성
  - [X] 루트 엔드포인트 200 응답 테스트
  - [X] 루트 엔드포인트 JSON 응답 테스트
  - [X] 서비스 정보 포함 여부 테스트
  - [X] 테스트 실행 및 통과 확인

### Phase 2: 헬스체크 기능
- [X] **2.1 c 엔드포인트**
  - [X] `/health` 엔드포인트 테스트 작성
  - [X] `/health` GET 요청 시 200 응답
  - [X] 응답에 `status` 필드 포함
  - [X] 응답에 `timestamp` 필드 포함
  - [X] 테스트 통과 확인

- [X] **2.2 RAG 시스템 연동 상태 체크**
  - [X] RAG 인덱스 로드 상태 확인 테스트
  - [X] `index_loaded` 필드 응답에 포함
  - [X] 인덱스 미로드 시 `false` 반환
  - [X] 인덱스 로드 시 `true` 반환
  - [X] 테스트 통과 확인

### Phase 3: RAG 시스템 통합
- [X] **3.1 의존성 주입 설정**
  - [X] `api/dependencies.py` 생성
  - [X] RAG 시스템 싱글톤 인스턴스 관리
  - [X] `get_rag_system()` 함수 구현
  - [X] 의존성 주입 테스트 작성
  - [X] 테스트 통과 확인

- [X] **3.2 서버 시작 시 인덱스 로드**
  - [X] `@app.on_event("startup")` 이벤트 핸들러 작성
  - [X] FAISS 인덱스 파일 경로 설정
  - [X] 인덱스 로드 성공 로그 출력
  - [X] 인덱스 로드 실패 시 에러 핸들링
  - [X] 시작 이벤트 테스트 작성
  - [X] 테스트 통과 확인

### Phase 4: 검색 API 구현
- [X] **4.1 Pydantic 모델 정의**
  - [X] `api/models.py` 생성
  - [X] `SearchRequest` 모델 정의 (query, top_k)
  - [X] `SearchResult` 모델 정의 (repo, text, url, similarity_score)
  - [X] `SearchResponse` 모델 정의 (query, results)
  - [X] 모델 유효성 검증 테스트
  - [X] 테스트 통과 확인

- [X] **4.2 검색 엔드포인트 구현**
  - [X] `test/test_search.py` 생성
  - [X] `/search` POST 엔드포인트 테스트 작성
  - [X] 정상 요청 시 200 응답 테스트
  - [X] 검색 결과 반환 테스트
  - [X] `SearchResponse` 형식 준수 테스트
  - [X] `/search` 엔드포인트 구현
  - [X] 테스트 통과 확인

- [X] **4.3 검색 파라미터 검증**
  - [X] 빈 쿼리 요청 시 422 응답 테스트
  - [X] `top_k` 범위 검증 (1-10) 테스트
  - [X] 잘못된 타입 요청 시 에러 테스트
  - [X] 파라미터 검증 로직 구현
  - [X] 테스트 통과 확인

- [X] **4.4 검색 결과 정렬 및 포맷팅**
  - [X] 유사도 순 정렬 테스트
  - [X] `similarity_score` 필드 존재 테스트
  - [X] 요청한 `top_k` 개수만큼 반환 테스트
  - [X] 정렬 및 포맷팅 구현
  - [X] 테스트 통과 확인

### Phase 5: 문서화 및 배포 준비
- [X] **5.1 API 문서화**
  - [X] OpenAPI (Swagger) 문서 자동 생성 확인
  - [X] 각 엔드포인트에 description 추가
  - [X] 예제 요청/응답 추가
  - [X] `/docs` 페이지 확인

### Phase 6: Java 연동 테스트
- [ ] **6.1 Java에서 API 호출**
  - [ ] Java `HttpClient` 코드 작성
  - [ ] 검색 API 호출 테스트
  - [ ] 응답 JSON 파싱 테스트
  - [ ] 연동 성공 확인

- [ ] **6.2 TeDDie 통합**
  - [ ] `MissionService`에 RAG API 호출 추가
  - [ ] 검색 결과를 프롬프트에 통합
  - [ ] End-to-End 테스트
  - [ ] 최종 동작 확인

---

## 📁 프로젝트 구조

```

```

---

## 🔧 설치 및 실행

### 1. 사전 요구사항
- Python 3.10 이상
- pip

### 2. 설치

```bash
# Repository 클론
git clone https://github.com/your-username/TeDDie-RagAPI.git
cd TeDDie-RagAPI

# 가상환경 생성 (선택)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 3. 환경 설정

`.env` 파일 생성:
```bash
cp .env.example .env
```

`.env` 파일 수정:
```env
# API 설정
API_HOST=0.0.0.0
API_PORT=8000

# RAG 설정
FAISS_INDEX_PATH=../TeDDie-RagSystem/faiss_index.bin
RAG_DATASET_PATH=../TeDDie-RagSystem/woowacourse_rag_dataset.jsonl
```

### 4. 서버 실행

#### 개발 모드 (Hot Reload)
```bash
python main.py
```

#### 프로덕션 모드
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

### 5. 접속 확인

- **API Root**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

---

## 📡 API 명세

### 1. Root Endpoint

**GET** `/`

서비스 정보를 반환합니다.

**응답 예시:**
```json
{
  "service": "TeDDie RAG API",
  "version": "1.0.0",
  "status": "running"
}
```

---

### 2. Health Check

**GET** `/health`

서버 상태를 확인합니다.

**응답 예시:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-10T10:30:00",
  "index_loaded": true
}
```

---

### 3. Search

**POST** `/search`

우테코 과제를 검색합니다.

**요청 본문:**
```json
{
  "query": "자동차 경주 게임",
  "top_k": 3
}
```

**파라미터:**
| 필드 | 타입 | 필수 | 설명 | 기본값 |
|------|------|------|------|--------|
| query | string | ✅ | 검색 쿼리 | - |
| top_k | integer | ❌ | 반환할 결과 개수 (1-10) | 3 |

**응답 예시:**
```json
{
  "query": "자동차 경주 게임",
  "results": [
    {
      "repo": "java-racingcar-6",
      "text": "# 미션 - 자동차 경주\n\n## 🔍 진행 방식...",
      "url": "https://github.com/woowacourse-precourse/java-racingcar-6",
      "similarity_score": 0.234
    },
    {
      "repo": "java-racingcar-7",
      "text": "# java-racingcar-precourse...",
      "url": "https://github.com/woowacourse-precourse/java-racingcar-7",
      "similarity_score": 0.456
    }
  ]
}
```

**에러 응답:**

- **422 Unprocessable Entity**: 잘못된 요청 파라미터
  ```json
  {
    "detail": [
      {
        "loc": ["body", "query"],
        "msg": "field required",
        "type": "value_error.missing"
      }
    ]
  }
  ```

- **503 Service Unavailable**: RAG 인덱스 미로드
  ```json
  {
    "detail": "RAG index not loaded"
  }
  ```

---

## 👨‍💻 개발 가이드

### 프로젝트 설정

1. **가상환경 활성화**
   ```bash
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. **개발 의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **코드 스타일 체크 (선택)**
   ```bash
   pip install black flake8
   black .
   flake8 .
   ```

### TDD 개발 프로세스

1. **테스트 작성** (`test/test_*.py`)
2. **테스트 실행** (실패 확인)
   ```bash
   pytest test/test_*.py -v
   ```
3. **코드 구현** (`api/*.py`)
4. **테스트 재실행** (통과 확인)
5. **리팩토링**
6. **커밋**

### 브랜치 전략

- `main`: 배포 가능한 안정 버전
- `develop`: 개발 중인 기능 통합
- `feature/*`: 각 기능 개발

---