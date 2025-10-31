import gradio as gr


def log_viewer_ui():
    gr.Markdown(
        """
    # Log viewer
    
    This is a template extension. Replace this content with your extension's functionality.
    
    To use it, simply modify this UI and add your custom logic.
    """
    )
    
    # Add your UI components here
    # Example:
    # with gr.Row():
    #     with gr.Column():
    #         input_text = gr.Textbox(label="Input")
    #         button = gr.Button("Process")
    #     with gr.Column():
    #         output_text = gr.Textbox(label="Output")
    # 
    # button.click(
    #     fn=your_processing_function,
    #     inputs=[input_text],
    #     outputs=[output_text],
    #     api_name="log_viewer",
    # )


def extension__tts_generation_webui():
    log_viewer_ui()
    
    return {
        "package_name": "tts_webui_extension.log_viewer",
        "name": "Log viewer",
        "requirements": "git+https://github.com/username_missing/tts_webui_extension.log_viewer@main",
        "description": "A template extension for TTS Generation WebUI",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "Your Name",
        "extension_author": "username_missing",
        "license": "MIT",
        "website": "https://github.com/username_missing/tts_webui_extension.log_viewer",
        "extension_website": "https://github.com/username_missing/tts_webui_extension.log_viewer",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        with gr.Tab("Log viewer", id="log_viewer"):
            log_viewer_ui()

    demo.launch(
        server_port=7772,  # Change this port if needed
    )
