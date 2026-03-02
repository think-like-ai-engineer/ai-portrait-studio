"""Streamlit interface for AI Portrait Studio.

This layer is intentionally thin.
It handles user interaction only.
All processing logic lives in the pipeline.
"""

import streamlit as st
from PIL import Image

from src.pipeline import PortraitPipeline


st.set_page_config(page_title="AI Portrait Studio", layout="centered")

st.title("AI Portrait Studio")
st.write(
    "Upload a portrait to remove the background and optionally apply a style transformation."
)

uploaded_file = st.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"]
)

apply_style = st.checkbox("Apply artistic style")

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)

        pipeline = PortraitPipeline(apply_style_filter=apply_style)

        with st.spinner("Processing portrait..."):
            result = pipeline.process(image)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original")
            st.image(image, width="stretch")

        with col2:
            st.subheader("Processed")
            st.image(result, width="stretch")

        st.markdown("---")
        st.caption("Built with a modular AI inference pipeline.")

    except Exception as exc:
        st.error(f"Processing failed: {exc}")