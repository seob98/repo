2d 기말 과제 계획서
===================
# 게임소개
1. 제목   
<2d run sim>
2. copy game / 원 게임 정보 / 스크린샷   
<레바런> / 장애물을 점프, 숙이기 등을 활용해 장애물을 피하고 치킨(코인)을 획득한다. / ![revarun](./image/revarun.png)
3. 게임의 목적, 방법 등 간단한 설명   
점프기능과 점프를 위한 장애물을 우선적으로 구현하고, 구현이 완료되면 장애물 종류를 더하고 액션의 가짓수를 더한다 (ex.슬라이드, 빅점프, 장애물 파괴 공격)   
장애물 여러가지 구현이 완료되면 코인을 구현하고, 획득하는 코인 수를 화면 위에 or 게임이 끝나고 나오는 gameover_state에 표시한다.
## GameState(scene)의 수 및 각각의 이름
logo_state / title_state / stage1_state / stage2_state
### 각 GameState별 다음항목 
1. 한줄 설명   
logo_state : 로고 이미지 출력, 일정시간 후 title로 자동이동   
title_state : 타이틀 이미지 출력, space 키 입력을 통해 stage1_state 이동   
stage1_state : stage1에서 출력할 장애물, 코인, 캐릭터, 맵(지면) 등을 출력   
stage2_state : 동일하지만 stage2의 요소로 변경
2. 화면에 표시할 객체 목록   
logo_state : 로고 이미지   
title_state : 타이틀 이미지 출력   
stage1_state : stage1의 캐릭터, 장애물, 코인, 맵(지면) 등을 출력   
stage2_state : stage1의 객체와 동일하나 2의 버전으로   
3. 처리할 키/마우스 이벤트   

4. 다른 state로 이동한다면 , 각 이동에 대한 조건 및 방법 (다이어그램 형식이면 더 좋다)
### 필요한 기술
1. 다른 과목에서 배운 기술
2. 이 과목에서 배울것으로 기대되는 기술
3. 다루지 않을 것 같아서 수업에서 다루어 달라고 요청할 기술
