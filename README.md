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

#### Accounts

**User [Accounts]**

- major ( charfield) //학과
- student_id (charfield) //학번
- user_type (integerfield) // 유저 타입
  - 0: 회장
  - 1: 운영진
  - 2: 부원
- start_number(charfield) //기수 (ex 7기, 7.5기)
- sns_id (charfield) //sns id
- image(imageField) //유저 이미지.

<보류>

- 과제점수 subject (floatfield)(그 해 기수만 있음)
- 출석통계 attendance(floatfield)(그 해 기수만 있음)

**Mentoring [Accounts]**

- pub_date(datefield)
- mentor(FK, User)
- mentee(FK, User)

**Portfolio [Accounts]** // 본인 이력 (수상내역 등)

- title (charfield) // 제목
- contents (textfield) //내용
- link (textfield) //소스링크 등
- image(imageField) //포트폴리오 이미지.
- user_id(FK, User)

**StudyGroup [Account]** //스터디 그룹

- name(charfield) //그룹명
- pub_date(datefield) //그룹 생성일
- introduction(textField) //소개글
- image(imageField) //그룹 이미지.

**Group_User [Account]** //스터디 그룹

- user_id(FK, User)
- group_id(FK, Group)
- is_captain(Boolean) //스터디 장일 시 True.

-------------------------------------

#### Study

**Board:Abstract [Board]**

- title(charfield)
- body(textfield)
- user_id(FK, User)
- pub_date = models.DateTimeField(auto_now_add=True) //게시물 등록 시간 생성
- update_date = models.DateTimeField(auto_now=True) // 업데이트 될 때만 정보 바뀔때 마다
- like = ManyToManyField(User)
- image(imagefield)
- file(filefield)

**StudyBoard(Board) [Board]** //각 스터디 그룹 게시판

- study_type(integerfield)
  - 0: 공식 모임
  - 1: 정보공유
  - 2: 기타
- personnel(integerfield) //참여 인원 수.
- group_id(FK, StudyGroup)

**NoticeBoard(Board) [Board]** //공지사항

- scheduled_date(datefield) //공지관련 예정된 날짜

**QnABoard(Board) [Board]** //QnA 게시판

- subject(charfield) //질문주제

**RecruitBoard(Board) [Board]** //공지사항

- purpose(charfield) //무슨 목적의 팀인지



**Comments:Abstract [Board]**

- body(textfield)
- pub_date(datetimefield)
- update_date(datetimefield)
- user_id(FK, User)





**StudyComments(Comments)**

- board_id(FK, StudyBoard)

**NoticeComments(Comments)**

- board_id(FK, NoticeBoard)

**QnAComments(Comments)**

- board_id(FK, QnABoard)

**RecruitComments(Comments)**

- board_id(FK, RecruitBoard)

--------------------------------------------

#### Admission

**JoinForm [Admission]** //입부신청(이력서)

- name(charfield)
- phone_number(charfield) //전화번호 (합격여부 연락을 하기 위함)
- birth(datefield) //생일(나이를 알기 위함)
- sex(charfield) -> enum //성
- major(charfield) //학과
- E-mail(charfield) //이메일

**Question [Admission]** //운영진이 제시할 이력서 질문

- question_id(Integer)
- question(charfield)

**Answer [Admission]** //입부자가 제출할 문항 별 답변

- answer(charfield)
- Joinform_id(FK, JoinForm)
- question_id(FK, Question)

**Evaluation[Admission]** //입부인원에 대한 평가

- joinform_id(FK, JoinForm)
- user_id(FK, User)
- body(textfield)
- score(integerfield)
- pub_date(datefield)



----------------------------------

**Career [Main]** //동아리 커리어

- title(charfield)
- pub_date(DateTimeField)
- link(URLField)
- participants(ManyToManyField, User) //참여자
- body(ckeditor.fields.RichTextField)

**Hashtag [Main]**

- hash_name(Char)
- 보류....

**Calendar [Main]** //동아리 스케줄 달력

- start_date(datefield)
- end_date(datefield)
- contents(charfield)
- plan_type(charfield)
  - "notice" //공지글 작성 시 달력기입 체크했다면 캘린더데이터도 생성됨.
  - "normal"
- notice_id(FK, NoticeBoard null=true) //plan_type이 notice일 시에만 사용



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

---- 20.02.08 17:00 피드백 적용완료 -----