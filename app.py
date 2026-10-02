
import streamlit as st
import requests
import pandas as pd


# Backend API address
API_URL = "http://127.0.0.1:8000"


# Page configuration
st.set_page_config(
    page_title="HDFC Custom LLM Pipeline",
    page_icon="🏦",
    layout="wide"
)


# Dashboard heading
st.title("HDFC Custom LLM Development Pipeline")

st.subheader("Dataset Governance Workspace")

st.caption(
    "Local demonstration using synthetic banking data only."
)


# Function to communicate with backend
def call_api(endpoint, method="GET", payload=None):

    url = f"{API_URL}{endpoint}"

    try:

        if method == "POST":

            response = requests.post(
                url,
                json=payload,
                timeout=10
            )

        else:

            response = requests.get(
                url,
                timeout=10
            )

        response.raise_for_status()

        return response.json(), None

    except requests.exceptions.RequestException as error:

        return None, str(error)


# Check backend health
health, health_error = call_api("/health")

if health_error:

    st.error("Backend API is not available.")

    st.info(
        "Please start the FastAPI server in another terminal."
    )

    st.code(
        "python -m uvicorn src.api:app --reload"
    )

    st.stop()

else:

    st.success("Backend API is connected.")


st.divider()


# Load demo dataset information
st.header("Dataset Overview")

dataset, dataset_error = call_api("/datasets/demo")

if dataset_error:

    st.error(f"Could not load dataset: {dataset_error}")

else:

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Dataset ID",
            dataset["dataset_id"]
        )

    with col2:

        st.metric(
            "Dataset Version",
            dataset["dataset_version"]
        )

    with col3:

        st.metric(
            "Total Records",
            dataset["record_count"]
        )

    st.write("**Data Source:**", dataset["source"])

    st.write("**Purpose:**", dataset["purpose"])

    st.write(
        "**Classification:**",
        dataset["classification"]
    )


st.divider()


# Dataset validation section
st.header("Dataset Validation")

st.write(
    "Click the button to run the backend validation workflow."
)

if st.button("Validate Demo Dataset"):

    with st.spinner("Validating dataset..."):

        result, validation_error = call_api(
            "/datasets/validate",
            method="POST",
            payload={
                "dataset_id": "HDFC-DEMO-001"
            }
        )

    if validation_error:

        st.error(
            f"Validation request failed: {validation_error}"
        )

    else:

        if result["validation_status"] == "PASSED":

            st.success("Dataset validation PASSED.")

        else:

            st.error("Dataset validation FAILED.")

        st.json(result)


st.divider()


# Dataset registry section
st.header("Dataset Registry")

registry, registry_error = call_api(
    "/datasets/registry"
)

if registry_error:

    st.error(
        f"Could not load registry: {registry_error}"
    )

else:

    st.write(
        "Registry Name:",
        registry["registry_name"]
    )

    st.write(
        "Registry Version:",
        registry["registry_version"]
    )

    registry_records = registry.get("datasets", [])

    if registry_records:

        registry_table = pd.DataFrame(registry_records)

        st.dataframe(
            registry_table,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No dataset records found.")


st.divider()

st.caption(
    "Prototype only. This dashboard does not represent "
    "an authorized HDFC Bank production system."
)
