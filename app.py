import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HDFC Custom LLM Pipeline",
    page_icon="🏦",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🏦 HDFC Custom LLM Development Pipeline")

st.caption(
    "Agentic AI • Banking RAG • Safety • "
    "Web Search • Governance • Audit"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("System")

st.sidebar.success("API Connected")


# ------------------------------------------------------------
# Policy PDF Upload
# ------------------------------------------------------------

if st.sidebar.button(
    "📄 Policy PDF Upload",
    use_container_width=True
):
    st.session_state["page"] = "Policy PDF Upload"


# ------------------------------------------------------------
# Main Modules
# ------------------------------------------------------------

page = st.sidebar.selectbox(
    "Select Module",
    [
        "AI Assistant",
        "EMI Calculator",
        "Dataset Governance",
        "Audit Logs",
        "Model Registry",
        "Monitoring",
        "Evaluation"
    ]
)


# ------------------------------------------------------------
# PDF page override
# ------------------------------------------------------------

if st.session_state.get("page") == "Policy PDF Upload":
    page = "Policy PDF Upload"


# ============================================================
# AI ASSISTANT
# ============================================================

if page == "AI Assistant":

    st.header("🤖 Banking AI Assistant")

    question = st.text_area(
        "Ask your question",
        placeholder="Example: What is a personal loan?",
        height=120
    )

    if st.button(
        "Ask Assistant",
        type="primary"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                with st.spinner(
                    "Generating answer..."
                ):

                    response = requests.post(
                        f"{API_URL}/v1/inference",
                        json={
                            "question": question.strip()
                        },
                        timeout=60
                    )

                    response.raise_for_status()

                    data = response.json()


                # ------------------------------------------------
                # ONLY CUSTOMER-FACING ANSWER
                # ------------------------------------------------

                st.subheader("Answer")

                answer = data.get(
                    "answer",
                    "No answer available."
                )

                st.write(answer)


            except requests.RequestException as error:

                st.error(
                    f"API Error: {error}"
                )

            except Exception as error:

                st.error(
                    f"Unexpected Error: {error}"
                )


# ============================================================
# POLICY PDF UPLOAD
# ============================================================

elif page == "Policy PDF Upload":

    st.header("📄 Banking Policy PDF Upload")

    st.write(
        "Upload a banking policy PDF to the "
        "document intelligence system."
    )

    st.info(
        "Supported format: PDF"
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Only PDF files are supported."
    )

    if uploaded_file is not None:

        st.success(
            f"Selected File: {uploaded_file.name}"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "File Size",
                f"{uploaded_file.size / 1024:.2f} KB"
            )

        with col2:

            st.metric(
                "File Type",
                "PDF"
            )

        if st.button(
            "⬆️ Upload PDF",
            type="primary"
        ):

            try:

                with st.spinner(
                    "Uploading and processing PDF..."
                ):

                    response = requests.post(
                        f"{API_URL}/v1/policies/upload",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                "application/pdf"
                            )
                        },
                        timeout=120
                    )

                try:

                    data = response.json()

                except ValueError:

                    data = {
                        "detail": response.text
                    }

                if response.status_code in (200, 201):

                    st.success(
                        "✅ PDF uploaded successfully!"
                    )

                    st.subheader(
                        "Upload Details"
                    )

                    st.json(data)

                else:

                    st.error(
                        f"Upload failed: {response.status_code}"
                    )

                    st.write(
                        data.get(
                            "detail",
                            "Unable to upload PDF."
                        )
                    )

            except requests.RequestException as error:

                st.error(
                    f"API Error: {error}"
                )

                st.info(
                    "Make sure FastAPI backend is running."
                )

    else:

        st.caption(
            "Please select a PDF file to begin."
        )


# ============================================================
# EMI CALCULATOR
# ============================================================

elif page == "EMI Calculator":

    st.header("💰 Banking EMI Calculator")

    principal = st.number_input(
        "Loan Amount",
        min_value=1.0,
        value=500000.0
    )

    rate = st.number_input(
        "Annual Interest Rate (%)",
        min_value=0.0,
        value=10.0
    )

    months = st.number_input(
        "Tenure (Months)",
        min_value=1,
        value=60
    )

    if st.button(
        "Calculate EMI",
        type="primary"
    ):

        try:

            response = requests.post(
                f"{API_URL}/v1/emi",
                json={
                    "principal": principal,
                    "annual_rate": rate,
                    "months": months
                },
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            result = data["result"]

            st.success(
                f"Monthly EMI: ₹{result['emi']:,.2f}"
            )

        except Exception as error:

            st.error(
                f"Error: {error}"
            )


# ============================================================
# DATASET GOVERNANCE
# ============================================================

elif page == "Dataset Governance":

    st.header("📊 Dataset Governance")

    if st.button(
        "Load Registry"
    ):

        try:

            response = requests.get(
                f"{API_URL}/datasets/registry",
                timeout=30
            )

            response.raise_for_status()

            st.json(
                response.json()
            )

        except Exception as error:

            st.error(
                f"API Error: {error}"
            )


# ============================================================
# AUDIT LOGS
# ============================================================

elif page == "Audit Logs":

    st.header("📝 Audit Trail")

    if st.button(
        "Load Audit Logs"
    ):

        try:

            response = requests.get(
                f"{API_URL}/audit/logs",
                timeout=30
            )

            response.raise_for_status()

            st.json(
                response.json()
            )

        except Exception as error:

            st.error(
                f"API Error: {error}"
            )


# ============================================================
# MODEL REGISTRY
# ============================================================

elif page == "Model Registry":

    st.header("🧠 Model Registry")

    if st.button(
        "Load Models"
    ):

        try:

            response = requests.get(
                f"{API_URL}/v1/models",
                timeout=30
            )

            response.raise_for_status()

            st.json(
                response.json()
            )

        except Exception as error:

            st.error(
                f"API Error: {error}"
            )


# ============================================================
# MONITORING
# ============================================================

elif page == "Monitoring":

    st.header("📈 System Monitoring")

    if st.button(
        "Load Metrics"
    ):

        try:

            response = requests.get(
                f"{API_URL}/v1/monitoring",
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Requests",
                    data.get(
                        "requests",
                        0
                    )
                )

            with col2:

                st.metric(
                    "Errors",
                    data.get(
                        "errors",
                        0
                    )
                )

            with col3:

                st.metric(
                    "Safety Blocks",
                    data.get(
                        "safety_blocks",
                        0
                    )
                )

            st.subheader(
                "Routes"
            )

            st.json(
                data.get(
                    "routes",
                    {}
                )
            )

        except Exception as error:

            st.error(
                f"API Error: {error}"
            )


# ============================================================
# EVALUATION
# ============================================================

elif page == "Evaluation":

    st.header("🧪 Evaluation Center")

    if st.button(
        "Run Evaluation"
    ):

        import subprocess
        import sys

        try:

            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "src.evaluator"
                ],
                capture_output=True,
                text=True,
                timeout=180
            )

            if result.returncode == 0:

                st.success(
                    "Evaluation completed successfully."
                )

            else:

                st.error(
                    "Evaluation completed with errors."
                )

            st.subheader(
                "Evaluation Output"
            )

            st.code(
                result.stdout
            )

            if result.stderr:

                with st.expander(
                    "Error Details"
                ):

                    st.code(
                        result.stderr
                    )

        except Exception as error:

            st.error(
                f"Evaluation Error: {error}"
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "HDFC Custom LLM Development Pipeline | "
    "Agentic AI | RAG | Data Governance | AI Safety"
)