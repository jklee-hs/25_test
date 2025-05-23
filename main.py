import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="이재경 소개", page_icon="👋", layout="centered")

# 제목과 간단한 소개
st.title("안녕하세요! 👋")
st.subheader("저는 이재경입니다.")

# 본문 소개
st.markdown("""
저는 **[직업/전문 분야]**로 활동하고 있으며,  
**[관심사/기술스택]**에 깊은 관심이 있습니다.

- 🔭 현재 진행 중인 프로젝트: [프로젝트 설명]
- 🌱 최근 배우고 있는 것: [학습 중인 기술이나 주제]
- 💬 언제든지 연락 주세요: [이메일, 링크드인 등]

---

**이 페이지는 Streamlit으로 제작되었습니다.**
""")

# 연락처 버튼
st.markdown("[📧 이메일로 연락하기](mailto:your@email.com)")
