import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="내 소개", page_icon="👋", layout="centered")

# 제목
st.title("안녕하세요! 👋")
st.subheader("저는 [당신의 이름]입니다.")

# 본문
st.markdown("""
저는 **[직업/전문 분야]**로 일하고 있으며,  
**[관심사, 기술 스택]**에 관심이 많습니다.

- 🔭 현재 하고 있는 프로젝트: [설명]
- 🌱 배우고 있는 것: [내용]
- 💬 연락주세요: [이메일, 링크드인, 인스타 등]

---  
""")

# 프로필 이미지
st.image("profile.jpg", width=200)

# 연락처 버튼
st.markdown("[📧 이메일로 연락하기](mailto:your@email.com)")

# 추가 요소 (선택 사항)
st.markdown("Made with ❤️ using Streamlit")
