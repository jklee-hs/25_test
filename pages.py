import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

# MBTI별 직업 및 설명 데이터 (각 MBTI당 5개 이상)
mbti_jobs = {
    "INTJ": {
        "전략기획가": "기업의 미래를 설계하고 실행 전략을 수립하는 전문가입니다.",
        "데이터 과학자": "방대한 데이터를 분석하여 통찰을 도출합니다.",
        "시스템 분석가": "정보 시스템을 분석하고 개선안을 제안합니다.",
        "기술 컨설턴트": "기업에 IT 기반 솔루션을 제공합니다.",
        "UX 디자이너": "사용자 중심의 디자인을 설계합니다."
    },
    "INFP": {
        "작가": "감정을 언어로 표현하는 창의적 작업을 합니다.",
        "심리상담가": "개인의 내면과 감정을 이해하고 돕습니다.",
        "콘텐츠 크리에이터": "영상, 블로그, SNS 등 다양한 매체를 통해 메시지를 전달합니다.",
        "일러스트레이터": "감성을 그림으로 표현하는 디자이너입니다.",
        "인문학 연구자": "인간과 사회를 깊이 있게 탐구합니다."
    },
    "ENFP": {
        "마케터": "고객의 니즈를 파악하고 브랜드를 알리는 역할을 합니다.",
        "브랜드 매니저": "브랜드 이미지와 전략을 총괄합니다.",
        "이벤트 플래너": "행사와 이벤트를 기획하고 실행합니다.",
        "방송 작가": "방송 콘텐츠를 기획하고 대본을 씁니다.",
        "기획자": "새로운 아이디어를 실제 프로젝트로 만듭니다."
    },
    "ISTJ": {
        "회계사": "기업의 재무를 관리하고 감사합니다.",
        "공무원": "국가나 지자체의 공공 서비스를 수행합니다.",
        "법률 사무원": "법률 관련 문서를 정리하고 행정을 보조합니다.",
        "품질 관리자": "제품이나 서비스의 품질을 관리하고 검사합니다.",
        "데이터 관리자": "정확한 데이터 관리를 통해 업무의 기반을 다집니다."
    },
    "ESFP": {
        "배우": "무대나 화면에서 다양한 역할을 연기합니다.",
        "MC": "행사나 방송에서 진행을 맡아 분위기를 이끕니다.",
        "이벤트 코디네이터": "다양한 행사를 기획하고 운영합니다.",
        "스타일리스트": "패션 감각으로 사람을 꾸미는 전문가입니다.",
        "여행 가이드": "여행을 재미있고 알차게 이끌어줍니다."
    }
    # 다른 MBTI들도 추가 가능 (필요시 요청해주세요)
}

# 타이틀
st.markdown("<h1 style='text-align: center;'>💼 MBTI 기반 직업 추천</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>MBTI 유형을 선택하고, 관심 있는 직업을 클릭해보세요!</p>", unsafe_allow_html=True)

# MBTI 선택
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요:", sorted(mbti_jobs.keys()))

# 직업 선택 및 설명 출력
if selected_mbti:
    st.markdown(f"### 🧠 {selected_mbti} 유형에게 어울리는 직업 추천")

    selected_job = None
    for job_title in mbti_jobs[selected_mbti]:
        if st.button(job_title):
            selected_job = job_title

    if selected_job:
        st.markdown("---")
        st.markdown(f"### 💡 {selected_job} 소개")
        st.info(mbti_jobs[selected_mbti][selected_job])
