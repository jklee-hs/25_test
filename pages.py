import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

# MBTI별 직업 및 설명 데이터
mbti_jobs = {
    "INTJ": {
        "전략기획가": "기업의 장기적인 방향을 설정하고 전략을 수립하는 전문가입니다.",
        "데이터 과학자": "데이터를 분석하여 통찰을 얻고 비즈니스 의사결정을 지원합니다.",
        "시스템 분석가": "IT 시스템의 구조와 기능을 분석하고 개선점을 제안합니다."
    },
    "ENFP": {
        "마케터": "창의적인 아이디어로 제품과 서비스를 고객에게 효과적으로 전달합니다.",
        "브랜드 매니저": "브랜드의 정체성과 시장에서의 입지를 관리합니다.",
        "이벤트 플래너": "행사 기획과 운영을 총괄하여 감동적인 경험을 제공합니다."
    },
    # 필요한 MBTI 유형을 추가로 작성하세요...
}

# 타이틀
st.markdown("<h1 style='text-align: center;'>💼 MBTI 기반 직업 추천</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>MBTI 유형을 선택하고, 관심 있는 직업을 클릭해보세요!</p>", unsafe_allow_html=True)

# MBTI 선택
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요:", sorted(mbti_jobs.keys()))

# 직업 선택 및 설명 출력
if selected_mbti:
    st.markdown(f"### 🧠 {selected_mbti}에게 어울리는 직업")

    selected_job = None
    for job_title in mbti_jobs[selected_mbti]:
        if st.button(job_title):
            selected_job = job_title

    if selected_job:
        st.markdown("---")
        st.markdown(f"### 💡 {selected_job} 소개")
        st.info(mbti_jobs[selected_mbti][selected_job])
