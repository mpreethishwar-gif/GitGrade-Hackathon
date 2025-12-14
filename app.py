import streamlit as st

example_outputs = {
    "https://github.com/rahul-dev-ai/todo-app": {
        "score": 78,
        "summary": "Strong code consistency and folder structure; needs more tests and documentation.",
        "roadmap": [
            "Add unit tests",
            "Improve README with project instructions",
            "Introduce CI/CD using GitHub Actions"
        ]
    },
    "https://github.com/sneha-codes/weather-dashboard": {
        "score": 42,
        "summary": "Basic project structure but poor documentation and inconsistent commits.",
        "roadmap": [
            "Add README with setup instructions",
            "Restructure folders",
            "Commit regularly with meaningful messages"
        ]
    },
    "https://github.com/manish-projects/ecommerce-site": {
        "score": 91,
        "summary": "Excellent project depth and clean codebase.",
        "roadmap": [
            "Add automated tests",
            "Improve issue tracking",
            "Contribute project to open-source"
        ]
    }
}

st.title("GitGrade – GitHub Repository Analyzer")
repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Analyze"):
    if repo_url in example_outputs:
        data = example_outputs[repo_url]
        st.subheader(f"Score: {data['score']} / 100")
        st.write(f"Summary: {data['summary']}")
        st.write("Roadmap:")
        for item in data['roadmap']:
            st.markdown(f"- {item}")
    else:
        st.error("Repo not found in examples. Try one of the example URLs.")
