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
5. **요구사항**
6. **Usecase**
7. **모듈 구조**
8. **DB 구조**
9. **추가사항**



## 개요

**프로젝트 명**

KMU - LIKELION WEB SERVICE

기간

목적 / 목표



## 조직도

- **역할 및 책임**

  - 이정현 [Frontend]
    - React.js
    - JS / Jquery / Ajax
  - 강승원 [Backend]
    - App : Accounts, JoinForm, Study
  - 이정우 [Backend]

  

## 요구사항

![요구사항](C:\Users\labiss96\Desktop\LikeLion\KMU-LikeLion\KMU-LIKELION\요구사항.PNG)



## UseCase (보류)

## 모듈 구조

#### App

- **Accounts**
  - 로그인
  - 마이페이지(작성/수정)

- **JoinForm**
  - 신청폼(작성/수정/읽기) -> 비회원
  - 신청자리스트 -> 운영진
  - 이력서 열람 페이지(선발기능)  -> 운영진
- **Study**
  - 게시판 리스트
  - 신청폼
  - 게시판 detail
- **project(가제)  - 프로젝트 인원모집**
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



## DB 구조

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