import streamlit as st
from src.chains import generate_smart_response

# UI Configuration
st.set_page_config(
    page_title=" Sensei AI Assistant",
    layout="centered"
)

def main():
    # Header Section
    st.title("Sensei AI Assistant")
    st.subheader("Automated Customer Response System")
    st.write("Paste an incoming customer email below to generate a drafted response based on our internal documentation.")

    # Main Input Area
    with st.container():
        user_email = st.text_area(
            "Customer Email Content:",
            placeholder="Type or paste the email here, example: Hi, I can't log into my account and I also want to know if I can get a refund for my last payment.",
            height=200
        )

        # Action Button
        if st.button("Generate AI Response", type="primary"):
            if user_email.strip():
                with st.spinner("Processing email and consulting knowledge base..."):
                    # Call the RAG chain logic from src/chains.py
                    response = generate_smart_response(user_email)
                    if response.startswith("Error processing request"):
                        st.error(response)
                    else:
                        st.divider()
                        st.success("Draft Generated!")
                        st.subheader("Suggested Response:")
                        st.info(response)
                        st.button("Copy to Clipboard", on_click=lambda: st.toast("Copied! (Simulation)"))
            else:
                st.warning("Please enter some email content first.")

    # Sidebar Information
    with st.sidebar:
        st.title("System Info")
        st.write("**Model:** Llama 3.1 8B (Ollama)")
        st.write("**Technique:** RAG with ChromaDB")
        st.write("**Stack:** LangChain + Streamlit")
        st.divider()
        st.markdown("""
        ### How it works:
        1. **Vectorization:** Converts email to embeddings.
        2. **Retrieval:** Finds related docs in `.chroma_db`.
        3. **Generation:** Ollama drafts the final reply.
        """)

if __name__ == "__main__":
    main()