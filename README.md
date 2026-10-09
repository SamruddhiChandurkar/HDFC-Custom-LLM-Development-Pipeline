# 🏦 HDFC Custom LLM Pipeline — Enterprise AI Factory & RAG Infrastructure
[![Live Demo Video](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0056b3?style=for-the-badge&logo=github)](https://drive.google.com/file/d/1fEeDcDbUbt-F-6jUgMBm7FX-Hual4McS/view?usp=drive_link)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq-F55036?style=for-the-badge)](https://groq.com/)
[![RAG](https://img.shields.io/badge/AI-RAG%20Pipeline-7C3AED?style=for-the-badge)](https://github.com/shivamtayal2013/HDFC-Custom-LLM-Development-Pipeline)
[![Status](https://img.shields.io/badge/Project-Academic%20Prototype-blue?style=for-the-badge)](https://github.com/shivamtayal2013/HDFC-Custom-LLM-Development-Pipeline)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open%20App-2E8B57?style=for-the-badge&logo=streamlit)](https://drive.google.com/file/d/1fEeDcDbUbt-F-6jUgMBm7FX-Hual4McS/view?usp=drive_link)(<= Click here for Live Demo)

[![Project Overview](https://img.shields.io/badge/Project%20Overview-Group%20Presentation%20Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://drive.google.com/file/d/1sgbj5XC-fPLdUu9bGWGvOn9ETPR3I0F8/view?usp=drive_link)(<= Click here for Project Overview)


**An AI-powered banking assistant using RAG, LLMs,
official-source retrieval, and a governed API workflow.**

Project README & Technical Documentation
Academic Prototype | RAG + Governed Banking AI Workflow
DOMAIN
Banking AI	FRONTEND
Streamlit	BACKEND
FastAPI	LLM
Groq

## 🔗 Project URLs & Resources
(https://hdfc-custom-llm-development-pipeline-9sry.onrender.com/)

## 📸 Project Dashboard Screenshots
(https://drive.google.com/drive/folders/1PVtPnAAw9Wd2z1rBf-AJs921tUpPBKBk?usp=sharing)

## 🎥 Project Overview – Group Presentation
(https://drive.google.com/file/d/1fEeDcDbUbt-F-6jUgMBm7FX-Hual4McS/view?usp=drive_link)

## 🌐 Live Demo
(https://drive.google.com/file/d/1sgbj5XC-fPLdUu9bGWGvOn9ETPR3I0F8/view?usp=drive_link)

Document positioning
This document turns the current project README into a presentation-ready technical document. It uses the implementation details from File 1, the structural/reference style of File 2, and the project brief and submission requirements from File 3. The ER diagram is explicitly presented as a proposed logical schema where the source materials do not define a physical database schema.

                         USER
                           |
                           v
                  STREAMLIT DASHBOARD
                           |
                           v
                    FASTAPI BACKEND
                           |
                           v
                HDFC BANKING AGENT
                           |
             +-------------+-------------+
             |                           |
             v                           v
       SAFETY / PII                INTENT DETECTION
             |                           |
             +-------------+-------------+
                           |
                           v
                 RETRIEVAL ORCHESTRATION
                           |
             +-------------+-------------+
             |                           |
             v                           v
      HDFC OFFICIAL WEB              RAG SYSTEM
          SEARCH                         |
             |                           |
             +-------------+-------------+
                           |
                           v
                      GROQ LLM
                           |
                           v
                 RESPONSE EVALUATION
                           |
                           v
                     AUDIT LOG
                           |
                           v
                    FINAL ANSWER

Dataset Governance Architecture

Dataset Intake
      |
      v
Validation
      |
      v
Dataset Registry
      |
      v
Approval Workflow
      |
      v
Governed Dataset
      |
      v
Retrieval / Future Fine-Tuning
      |
      v
Audit Log

Application Architecture

Streamlit
   |
   v
FastAPI
   |
   +-------------------+
   |                   |
   v                   v
Loan Assistant       Governance APIs
   |                   |
   v                   +------ Dataset Registry
RAG / Web Search      |
   |                   +------ Audit Logs
   v                   |
Groq LLM               +------ Model Registry
   |                   |
   v                   +------ Monitoring
Evaluation
   |
   v
Final Response

Prepared for project submission / review
Contents
•	1. Executive Summary
•	2. Business Problem and Product Goal
•	3. Target Users, Inputs and Outputs
•	4. Project Scope: Current Prototype vs. Planned Lifecycle
•	5. Key Features
•	6. System Architecture
•	7. End-to-End AI Workflow
•	8. RAG and HDFC Official Web Retrieval
•	9. Safety, Security and Guardrails
•	10. Dataset Governance and Knowledge Management
•	11. Evaluation and Auditability
•	12. Application, API and Dashboard Architecture
•	13. Technology Stack
•	14. Project Structure
•	15. Proposed ER Diagram and Data Model
•	16. Data Dictionary
•	17. Run and Deployment Instructions
•	18. Testing and Verification
•	19. Limitations
•	20. Future Enhancements
•	21. Submission Readiness Checklist
•	22. Disclaimer
Important implementation note
The current project is an academic/local prototype. Claims about LoRA/QLoRA, private model serving, canary rollout, advanced observability, or production compliance are documented as planned/future lifecycle extensions rather than current capabilities.

1. Executive Summary
The HDFC Custom LLM Development Pipeline is an academic prototype that demonstrates how a governed banking AI assistant can combine structured dataset governance, Retrieval-Augmented Generation (RAG), official web retrieval, intent-aware orchestration, LLM response generation, safety controls, response evaluation, and audit logging. The implementation is designed around a controlled workflow rather than a single unrestricted prompt-to-answer step.
The current user-facing assistant supports banking-oriented queries including personal loans, eligibility, credit, documents, interest, tenure, EMI calculations, current information, and general banking questions. The prototype uses a synthetic banking knowledge base for internal retrieval and can retrieve current public information from the HDFC Bank official website through Tavily when current information is required.
The project also exposes a governance-oriented application layer containing dataset intake/validation, dataset registry concepts, policy document upload, evaluation, audit logs, model registry, monitoring, and controlled API integration. This creates a bridge between a working RAG assistant and the larger Custom LLM lifecycle defined in the project brief.
Core value proposition
Keep frequently changing banking information in governed retrieval sources, apply safety checks before generation, and create a traceable response workflow from user request through retrieval, LLM generation, evaluation, and audit logging.

2. Business Problem and Product Goal
2.1 Business problem
Generic LLMs can produce fluent answers but banking workflows require controlled terminology, policy-aware answers, careful handling of sensitive information, and clear boundaries around unsupported financial claims. A generic model may also be outdated for current rates, eligibility criteria, product rules, or public banking information.
2.2 Product goal
The project goal is to demonstrate a governed Custom LLM-style development and application pipeline for a narrow banking use case. The application should provide grounded banking responses, use internal knowledge retrieval where available, consult official HDFC information for time-sensitive public questions, evaluate the generated response, and preserve an audit trail.
2.3 Release intent
For the academic prototype, the release intent is to prove the end-to-end controlled workflow and its supporting governance components. The project brief further describes an extended lifecycle from approved datasets to fine-tuning, model registration, controlled serving, application integration, monitoring, and rollback.
3. Target Users, Inputs and Outputs
Area	Project definition
Primary user	A banking-information seeker using the AI assistant / Streamlit dashboard.
Governance user	Project or admin user managing datasets, approvals, evaluation, audit records, model-related information, and monitoring views.
Inputs	Natural-language banking queries, synthetic banking FAQ knowledge, policy/document uploads, and public HDFC website information retrieved when required.
Outputs	Grounded banking response, intent classification, retrieval context, safety decisions, evaluation information, source-related trace data, and audit records.
Deterministic utility	An EMI calculator is provided separately from LLM generation so numerical calculations remain reproducible.

4. Project Scope: Current Prototype vs. Planned Lifecycle
Capability	Current prototype	Planned / extension
Dataset governance	Dataset intake, validation, registry/status concepts and synthetic knowledge base are demonstrated.	Immutable versioning, formal lineage, richer quality reports and approval evidence.
RAG	Synthetic banking FAQ retrieval with intent-aware source filtering.	Broader governed retrieval corpus, richer provenance and retrieval-quality monitoring.
Web retrieval	Tavily search restricted to the HDFC official website.	More advanced controlled tool orchestration and source-policy management.
LLM	Groq-hosted LLM for response generation.	LoRA/QLoRA adaptation, experiment tracking and model-specific evaluation.
Safety	PII checks, prompt-injection protection, restricted banking request handling and fallback logic.	Adversarial testing, stronger policy engines and expanded challenge sets.
Evaluation	Automated response evaluation for groundedness/supporting evidence and related signals.	Full banking/safety/privacy/security/robustness suite with formal release gates.
Model registry	Dashboard component for model-related tracking.	Signed artifacts, model cards, promotion gates, canary traffic and rollback.
Serving	Local academic application integration.	Private model serving and governed model gateway.
Monitoring	System-level monitoring section.	Latency, errors, retrieval quality, guardrail events, drift and observability stack.
Deployment	Docker / Docker Compose supported in the prototype.	Production orchestration, controlled rollout and operational SLO management.

5. Key Features
Dataset Governance: Dataset intake and validation, dataset registry, metadata management, approval workflow, status tracking and audit trail for dataset activities.
RAG Knowledge Retrieval: Synthetic banking FAQ knowledge base, intent-aware retrieval, context generation, grounded answers and source tracking.
HDFC Official Website Search: Tavily integration, HDFC-only domain restriction, site:hdfcbank.com style search, official-source filtering and current public information retrieval.
Banking AI Assistant: Supports eligibility, personal loan, credit, EMI, documents, interest, tenure, current-information and general banking intents.
Intent Detection: Classifies banking requests before response generation so the retrieval and response path can be selected intentionally.
Groq LLM Integration: Uses governed prompts to prefer official HDFC information for HDFC-specific questions and avoid invented rates, fees, eligibility criteria, documents or loan guarantees.
Safety & Security: PII detection, prompt injection protection, restricted request handling, source grounding and controlled fallback responses.
Audit Logging: Captures user requests, intent, processing route, LLM usage, web search usage, evaluation results, safety decisions, dataset events and system events.
Evaluation: Considers groundedness, source availability, confidence, web verification, internal knowledge usage, LLM usage and safety outcomes.
Policy PDF Upload: Provides a document/policy upload workflow to add banking policy material as governed retrieval content.
EMI Calculator: Deterministic financial calculation separated from LLM-generated text.
Model Registry & Monitoring: Provides dashboard components for model tracking and operational monitoring, with more complete lifecycle capabilities identified as future work.
6. System Architecture
The current application separates the user interface, API/backend layer, banking agent, safety and intent logic, retrieval orchestration, external web retrieval, internal RAG, LLM generation, evaluation and audit logging. This mirrors the implementation structure documented in the current README.
 
Figure 1. Current prototype architecture.
6.1 Component responsibilities
Component	Responsibility
Streamlit Dashboard	Provides the interactive banking assistant and governance-oriented application modules.
FastAPI Backend	Exposes backend services for assistant interaction, dataset intake/governance, evaluation, audit logging, model-related operations, monitoring, and health/status checks.
Banking AI Agent	Coordinates the user query through safety, intent and retrieval/generation stages.
Safety / PII	Detects potentially sensitive information, prompt injection or restricted requests before generation.
Intent Detection	Assigns an intent category that can influence the retrieval/response route.
Retrieval Orchestration	Decides how internal knowledge and official web information should be combined.
RAG System	Provides relevant context from the synthetic banking FAQ knowledge base.
HDFC Web Search	Retrieves current official public information via Tavily and HDFC domain restriction.
Groq LLM	Generates the customer-facing answer from grounded context.
Evaluation	Assesses whether the response has adequate evidence/support and records related signals.
Audit Log	Creates traceability for important workflow events and governance actions.

7. End-to-End AI Workflow
 
Figure 2. End-to-end user-query workflow.
1.	User submits a banking query.
2.	Safety and PII validation is performed before normal processing.
3.	Intent detection classifies the request.
4.	The workflow determines whether current official web information is required.
5.	When needed, the system searches the HDFC Bank official website through Tavily.
6.	Relevant internal banking knowledge is retrieved from the RAG knowledge base.
7.	Grounded context is assembled for response generation.
8.	The Groq-hosted LLM generates a customer-facing response.
9.	The response is evaluated for groundedness/support and related signals.
10.	Audit information is recorded.
11.	The final answer is returned to the user.
8. RAG and HDFC Official Web Retrieval
8.1 Internal RAG flow
The RAG layer uses a synthetic banking FAQ knowledge base as the internal source of stable banking knowledge. Retrieval is intended to provide relevant context to the LLM rather than expecting the model to memorize every banking fact.
8.2 Official web retrieval flow
For information that may change over time, the project can use Tavily to search only the official HDFC Bank website. The documented strategy uses HDFC-only search restrictions and passes retrieved web context into the LLM.
Source-grounding rule
Current policies, rates, eligibility criteria and other changing information should be retrieved from controlled sources rather than assumed to be permanently stored in the model.

8.3 Retrieval decision logic
Query type	Preferred source	Reason
General banking / stable FAQ	Synthetic RAG knowledge base	Use approved internal knowledge for recurring domain questions.
HDFC-specific current information	HDFC official web search + RAG where relevant	Current public information should be sourced from the official website.
Unsupported / unsafe banking request	Safety fallback	Do not generate unsupported financial claims or unsafe content.
Deterministic EMI calculation	EMI calculator	Keep arithmetic separate from generative response generation.

9. Safety, Security and Guardrails
Safety controls are placed around the generation workflow so that the system does not rely only on the LLM to enforce boundaries.
Control	Purpose	Prototype behavior
PII protection	Detect potentially sensitive personal information before processing.	PII detection / validation is part of the workflow.
Prompt-injection protection	Prevent instruction-manipulation attacks from changing model behavior.	Potentially malicious prompts are detected and handled by safety logic.
Restricted banking request protection	Handle unsafe or unsupported banking requests safely.	Controlled fallback responses are used.
Source grounding	Reduce unsupported HDFC-specific claims.	Current official web information can be injected into context.
Error handling	Maintain controlled behavior when retrieval, web, LLM or API calls fail.	Fallback responses are part of the documented workflow.
Secret handling	Prevent API keys and secrets from being committed to source control.	Environment variables are used for GROQ_API_KEY and TAVILY_API_KEY.

9.1 LLM response policy
•	Prefer HDFC official website information for HDFC-specific questions.
•	Use approved internal banking knowledge for supported topics.
•	Avoid inventing rates, fees, eligibility criteria or document requirements.
•	Avoid unsupported financial claims and loan-approval guarantees.
•	Clearly indicate when information cannot be verified.
•	Generate customer-facing responses only.
10. Dataset Governance and Knowledge Management
 
Figure 3. Dataset governance and retrieval lifecycle represented by the prototype.
10.1 Current governance components
•	Dataset intake and validation.
•	Dataset registry and metadata.
•	Dataset approval/status workflow.
•	Synthetic banking knowledge base.
•	Policy/document upload workflow.
•	Audit trail for dataset activities.
10.2 Extended governance design from the project brief
The project brief defines a more complete data lifecycle: register and classify sources, scan and quarantine sensitive content, parse and normalize documents, de-identify restricted information, create typed task records, deduplicate and split data, validate quality, and freeze an immutable dataset version. This extended lifecycle is the natural next step for the prototype.
11. Evaluation and Auditability
11.1 Evaluation dimensions
Evaluation signal	What it checks
Groundedness	Whether the response is adequately supported by retrieved evidence.
Source availability	Whether supporting source information exists for the answer.
Confidence	A system-level signal associated with response support / retrieval evidence.
Web verification	Whether HDFC-specific current information could be verified through official web retrieval.
Internal knowledge usage	Whether relevant approved internal RAG knowledge was available and used.
LLM usage	Whether generation relied on the LLM stage.
Safety outcome	Whether the request or response triggered safety-related decisions.

11.2 Audit logging
The audit layer records key activities such as user requests, intent, processing route, LLM usage, web search usage, evaluation results, safety decisions, dataset activities and system events. The purpose is traceability: a reviewer should be able to understand what route the system followed for a response.
11.3 Extended release-gate design
The project brief calls for stronger pre-release evaluation covering banking task quality, safety, compliance, privacy, bias, security, latency and robustness, with comparison against base and currently approved models. In the current prototype, this should be treated as an extension of the existing evaluation layer rather than a claim that all enterprise gates are already implemented.
12. Application, API and Dashboard Architecture
12.1 Dashboard modules
Module	Purpose
AI Assistant	Interactive banking question-answering workflow.
Policy PDF Upload	Add policy/document material for governed knowledge workflows.
EMI Calculator	Deterministic EMI calculation.
Dataset Governance	Dataset intake, validation, registry/status and approval-oriented views.
Audit Logs	Review recorded workflow and governance events.
Model Registry	Track model-related information and lifecycle concepts.
Monitoring	Observe system-level status and operational information.
Evaluation	Review response-evaluation outputs and supporting evidence.

12.2 API responsibility areas
The FastAPI backend is documented as providing service areas for banking assistant interaction, dataset intake and governance, dataset approval, audit logging, evaluation, model-related operations, monitoring and health/status checks. FastAPI also provides automatically generated API documentation.

13. Technology Stack
Layer	Technology	Purpose
Frontend	Streamlit	Interactive project dashboard / user experience.
Backend	Python + FastAPI	REST APIs, orchestration and service layer.
Validation	Pydantic	Typed request/response validation.
LLM	Groq	Hosted LLM response generation.
Retrieval	RAG + synthetic banking FAQ knowledge base	Internal contextual retrieval.
Web retrieval	Tavily Search	Current HDFC official website retrieval.
Security	PII detection + prompt injection detection + controlled tools	Safety boundary around the AI workflow.
Data governance	Dataset Registry + validation + approval + audit logging	Governance and traceability.
Deployment	Docker + Docker Compose	Containerized local execution.
Testing	Pytest	Automated testing.

Planned stack mentioned by the project brief
The project brief describes future components such as PEFT/LoRA/QLoRA, MLflow, private vLLM/TGI serving, model gateway controls, OpenTelemetry, Prometheus/Grafana and richer evaluation suites. These belong in the planned lifecycle unless separately implemented in the actual codebase.

14. Project Structure
HDFC-Custom-LLM-Pipeline/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
│
├── src/
│   ├── api.py
│   ├── agent.py
│   ├── loan_assistant.py
│   ├── rag.py
│   ├── web_search.py
│   ├── llm_client.py
│   ├── security.py
│   ├── audit_log.py
│   ├── dataset_registry.py
│   └── ...
│
├── data/
│   ├── faq/
│   ├── datasets/
│   ├── policies/
│   └── audit/
│
├── tests/
│   └── ...
│
└── configs/
    └── ...

This structure is aligned with the current README. The project brief proposes a larger enterprise repository structure with separate applications, services, packages, infrastructure and documentation; that broader structure is a future refactoring target rather than a statement of the current repository.
15. Proposed ER Diagram and Data Model
Important schema note
The source files describe governance modules and audit concepts but do not provide a definitive physical SQL schema. The diagram below is therefore a proposed logical ER model for documentation and design discussion. It should be validated against the actual database/code before being presented as an implemented schema.

 
Figure 4. Proposed logical ER diagram aligned to the documented project modules.
15.1 Relationship summary
Relationship	Meaning
Dataset → Document	A dataset can contain multiple policy/source documents.
Document → Chunk	Each document is split into retrievable chunks for RAG.
Query → Intent	Each query receives an intent classification.
Query → Safety Check	Each query can have a safety/PII decision.
Query → Retrieval Event	A query can generate multiple retrieval events from RAG and web sources.
Query → Web Search	A query may trigger zero or more official-web retrieval actions.
Query → LLM Response	The query can produce one or more response records.
Response → Evaluation	A response can be evaluated using one or more evaluation records.
Query → Audit Log	Multiple audit events can be recorded during request processing.
Model Registry → Deployment	A registered model/version can have one or more deployment records.

16. Data Dictionary
Entity	Key fields	Purpose
DATASET	dataset_id, name, status	Tracks an approved/registered knowledge or dataset source.
DOCUMENT	document_id, dataset_id, title, source_url, effective_date	Stores source-level metadata for policy/knowledge material.
CHUNK	chunk_id, document_id, chunk_text, chunk_index	Stores retrievable document fragments and vector references.
QUERY	query_id, query_text, created_at, session_id	Represents a user banking request.
INTENT	intent_id, query_id, intent_name, confidence	Stores intent classification result.
SAFETY_CHECK	safety_id, query_id, pii_flag, injection_flag, decision	Stores pre-generation safety decision signals.
RETRIEVAL_EVENT	retrieval_id, query_id, source_type, source_ref, relevance_score	Tracks internal/external evidence retrieved for a query.
WEB_SEARCH	web_id, query_id, domain, search_query, result_url, retrieved_at	Tracks official-web search details.
LLM_RESPONSE	response_id, query_id, model_name, response_text, created_at	Stores the generated banking answer and model reference.
EVALUATION	evaluation_id, response_id, groundedness, confidence, result	Stores evaluation outputs for the generated response.
AUDIT_LOG	audit_id, query_id, event_type, route, status, timestamp	Preserves workflow and governance traceability.
MODEL_REGISTRY	model_id, model_name, version, status, approval_state	Represents model lifecycle metadata.
DEPLOYMENT	deployment_id, model_id, environment, traffic_split, status	Represents deployment state for a registered model.

17. Run and Deployment Instructions
17.1 Install dependencies
pip install -r requirements.txt

17.2 Start FastAPI backend
python -m uvicorn src.api:app --reload

17.3 Start Streamlit dashboard
streamlit run app.py

17.4 Environment variables
# .env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

Never commit real API keys or secrets to the repository.
17.5 Docker
docker compose up --build
docker compose ps

18. Testing and Verification
pytest -v

The project documentation identifies Pytest as the automated testing tool. The project brief additionally expects unit, integration, contract, security and end-to-end tests for the mature pipeline. For this academic prototype, the key verification focus should be end-to-end execution, safety behavior, retrieval grounding, fallback handling and API health.
18.1 Verification checklist
•	Application starts successfully and the Streamlit dashboard loads.
•	FastAPI backend responds and its Swagger / ReDoc documentation is available.
•	A normal banking question follows the expected safety → intent → retrieval → LLM → evaluation → audit path.
•	Current HDFC-specific queries can trigger official-web retrieval when required.
•	Unsafe/prompt-injection-like inputs are handled by safety logic.
•	PII-sensitive inputs are detected and handled according to project guardrails.
•	EMI calculation remains deterministic and separate from the LLM response path.
•	Audit information is recorded for important workflow events.
19. Limitations
•	It is a local academic prototype.
•	It does not use real customer information.
•	It does not perform actual loan underwriting.
•	It does not approve or reject real loans.
•	It does not connect to production banking systems.
•	It is not an official HDFC Bank deployment.
•	It uses synthetic banking data for internal knowledge.
•	It uses external HDFC website retrieval for current public information.
•	It does not currently implement production-grade LoRA/QLoRA fine-tuning.
•	It does not currently provide production private model-serving infrastructure.
•	It does not provide production-grade deployment approval or rollback.
•	It does not claim production-level compliance certification.
20. Future Enhancements
 
Figure 5. Planned Custom LLM lifecycle described in the project materials.
•	Data de-identification and immutable dataset versioning.
•	Dataset lineage and quality reporting.
•	LoRA / QLoRA fine-tuning with reproducible runs.
•	Experiment tracking and GPU training orchestration.
•	Checkpoint management and candidate-vs-base evaluation.
•	Advanced banking, safety and adversarial evaluation suites.
•	Model cards, data cards and artifact checksums/signatures.
•	Formal release gates and human approval workflow.
•	Private vLLM/TGI serving and a model gateway.
•	Canary deployment, traffic shifting and rollback.
•	Advanced monitoring, model/data drift detection and production observability.
21. Submission Readiness Checklist
Check	Status to confirm before submission
GitHub repository	Repository is accessible to authorized reviewers and contains code, configs and tests.
README / Documentation	Project overview, business problem, architecture, workflow, technologies, setup, evaluation and limitations are included.
Live demo	The working product loads successfully and demonstrates the core workflow end to end.
Demo video	Video is accessible with the required sharing permission and shows the complete workflow.
Secrets	No real API keys or credentials are committed to the repository.
Architecture	Architecture diagram and workflow are consistent with the implemented project.
Data	Synthetic datasets / schemas and retrieval sources are documented.
Evaluation	Evaluation cases/results and safety checks are documented.
Team contribution	Contribution and ownership are clearly stated.

Recommended presentation wording
When presenting the project, use “academic prototype” for the current system and “planned Custom LLM lifecycle” for fine-tuning, formal model registry, private serving, canary rollout and advanced observability unless those features are demonstrably implemented.

22. Disclaimer
This project is an academic prototype created for learning, demonstration and evaluation purposes. It is not an official HDFC Bank product or deployment and should not be used for real financial decisions, loan approval, underwriting or customer servicing.
Appendix A - Source Basis
Source	How it was used
File 1 - Current project README / implementation notes	Primary source for implemented features, current architecture, workflow, technology stack, project structure, run commands, limitations and current prototype lifecycle.
File 2 - Reference project README	Used as a structural reference for presentation depth, architecture documentation, governance framing and technical README organization. Claims not present in the current implementation were not presented as implemented.
File 3 - Applied GenAI project brief / requirements	Used for business framing, expected workflow, extended lifecycle, documentation expectations, deliverables and submission checklist.

Prepared as an original project documentation draft based on the uploaded materials.
