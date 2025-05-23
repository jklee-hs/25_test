import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["전략기획가", "데이터 과학자", "시스템 분석가"],
    "INTP": ["연구원", "개발자", "이론 물리학자"],
    "ENTJ": ["경영 컨설턴트", "스타트업 창업가", "프로젝트 매니저"],
    "ENTP": ["기획자", "광고 전문가", "혁신 컨설턴트"],
    "INFJ": ["심리상담가", "작가", "교육자"],
    "INFP": ["예술가", "카운슬러", "콘텐츠 크리에이터"],
    "ENFJ": ["HR매니저", "커뮤니케이터", "교육 트레이너"],
    "ENFP": ["마케터", "브랜드 매니저", "이벤트 플래너"],
    "ISTJ": ["회계사", "공무원", "법률 사무원"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    "ESTJ": ["운영 관리자", "군인", "행정 담당자"],
    "ESFJ": ["영업 관리자", "고객지원 담당자", "병원 코디네이터"],
    "ISTP": ["엔지니어", "기술 전문가", "기계 정비사"],
    "ISFP": ["디자이너", "플로리스트", "사진작가"],
    "ESTP": ["기업가", "세일즈 전문가", "응급 구조사"],
    "ESFP": ["배우", "MC", "이벤트 코디네이터"]
}

# 앱 UI
st.markdown("<h1 style='text-align: center;'>💼 MBTI 기반 직업 추천</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>당신의 MBTI 유형을 선택하면, 어울리는 직업을 추천해드릴게요.</p>", unsafe_allow_html=True)

selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요:", sorted(mbti_jobs.keys()))

if selected_mbti:
    st.markdown(f"### 🧠 {selected_mbti} 유형에게 어울리는 직업 추천")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
