# KMU-LIKELION

[Django/React/Python] Kookmin Univ. LikeLion Club Web Service Project

## Index

1. **개요**
   1. **프로젝트명**
   2. **기간**
   3. **목적 / 목표**
2. **조직도**
   1. **역할 및 책임**
3. **제작방안**
   1. **기술**
4. **일정**
   1. **프로젝트 추진 일정**
   2. **단계별 세부일정**
5. **요구사항** / **Usecase**
6. **구조도**
   1. **모듈구조**
   2. **사이트맵 구조**
   3. **DB구조**
7. **추가사항**

## 1. 개요

**프로젝트 명**

KMU - LIKELION WEB SERVICE

기간

목적 / 목표

## 2. 조직도

- **역할 및 책임**

  - 이정현 [Frontend]
    - React.js
    - JS / Jquery / Ajax
  - 박종민 [Frontend]
    - React.js
  - 강승원 [Backend]
  - App : Accounts, JoinForm, Study
  - 이정우 [Backend]

## 5. 요구사항

<img src = "https://user-images.githubusercontent.com/42925501/73937125-b3f5bd00-4927-11ea-9ef1-65211a71548f.PNG">

## UseCase (보류)

## 6. 구조도

### 6-1. 모듈 구조

#### App

- **Accounts**

  - 로그인
  - 마이페이지(작성/수정)

- **JoinForm**
  - 신청폼(작성/수정/읽기) -> 비회원
  - 신청자리스트 -> 운영진
  - 이력서 열람 페이지(선발기능) -> 운영진
- **Study**
  - 게시판 리스트
  - 신청폼
  - 게시판 detail
- **project(가제) - 프로젝트 인원모집**
  - 아이디어 제출폼 ,수정 폼
  - 아이디어 detail(댓글,삭제, 신청한 사람)아이디어 list (제출 버튼)
- **Notice (공지)**

  - 공지 글 (작성/수정, 운영진만 사용)
  - 공지 list
  - 공지 detail

- **QnA**

  - 질문 폼(생성/수정)
  - 질문 list
  - 질문 detail (comment, like)

- **Main**
  - 달력
  - main page

#### Project

- KMU-LikeLion-Project

### 6-2. 사이트맵 구조

- **Main page**
  - Nav-bar
    - KMU-LIKELION logo
    - Menu
      - 스터디 게시판
      - 공지사항
      - QnA
      - 멤버(동아리 구성원 리스트)
      - What We Made
    - Mypage Icon
      - 로그인 시 - 마이페이지
      - 로그아웃 시 - 로그인 / 입부신청(입부기간 시만)
  - Body
    - Carousel(logo, 활동사진 등)
    - 최근 게시물 or Best 게시물
    - 일정 (달력 표시)
    - What We Made(베스트 3~4개만 표시)
  - Footer
    - Contact
    - 주소 및 어드레스 + copyright

### 6.3 DB 구조

-- ModelName [AppName] --

**Profile [Accounts]**

- name
- password
- major ( charfield) //학과
- student_ID (charfield) //학번
- is_manager (booleanfield) // 운영진 여부
- study(foreign key, Study) //소속 스터디
- start_number(charfield) //기수 (ex 7기, 7.5기)
- sns_id (charfield) //sns id
- etc(TextField) //기타
- **hashtag(ManyToMany, Hashtag)**

<보류>

- 과제점수 subject (floatfield)(그 해 기수만 있음)
- 출석통계 attendance(floatfield)(그 해 기수만 있음)

**Mentoring [Accounts]**

- pub_date(datefield)
- mentor(FK, Profile)
- mentee(FK, Profile)

**Record [Accounts]** // 본인 이력 (수상내역 등)

- contents (charfield) //내용
- link (charfield) //소스링크 등
- belong_to_user(foreignkey, Profile)

**StudyBoard [Study]** //각 스터디 그룹 게시판

- title(charfield)
- reader(foreign key)
- description(textField)
- belong_to_group(FK, StudyGroup)
- **hashtag(ManyToMany, Hashtag)**

**StudyGroup [Study]** //스터디 그룹

- name(charfield)
- pub_date(datefield)
- introduction(textField)
- **hashtag(ManyToMany, Hashtag)**
- 추가기능...보류

**Notice [notice]** //공지사항

- writer(FK, Profile)
- title(charfield)
- description(charfield)
- pub_date(datefield)
- **hashtag(ManyToMany, Hashtag)**

**JoinForm [JoinForm]** //입부신청(이력서)

- name(charfield)
- phone_number(charfield)
- major(charfield)
- E-mail(charfield)

**Question [JoinForm]** //운영진이 제시할 이력서 질문

- Question_id(Integer)
- Question(charfield)

**Answer [JoinForm]** //입부자가 제출할 문항 별 답변

- Answer(charfield)
- belong_to_Join(FK, JoinForm)
- belong_to_Question(FK, Question)

**Hashtag [Main]**

- hash_name(Char)
- 보류....

**Calendar [Main]** //동아리 스케줄 달력

- start_date(datefield)
- end_date(datefield)
- contents(Char)
- type(Char)
- post_id(Integer)



-----------------------------------------

### Feedback

**필드 및 모델 명 수정**

- Profile 모델명 -> User 수정
- record 모델의 belong_to_user 필드 -> user_id로 수정(다른 모델의 필드들도 확인하여 수정)
- Answer 모델의 answer 필드 -> content나 body로..
- 유저모델의 is_manager필드 -> user_type 수정 (integer 형으로 타입수정)
  - 0 : 회장
  - 1: 일반 운영진
  - 2: 교육팀
  - 3: 일반유저

