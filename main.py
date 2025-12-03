import gradio as gr
import requests

def scan_vulnerabilities(target):
    """
    Very simple example:
    - Tries to send an HTTP request to the target on port 80.
    - Shows whether the host has an HTTP service responding.

    Use only on systems you are authorized to test.
    """
    url = f"http://{target}"

    try:
        response = requests.get(url, timeout=5)

        if response.ok:
            return (
                f"Reached {url}\n"
                f"HTTP status: {response.status_code}\n"
                "This host has an HTTP service responding."
            )
        else:
            return (
                f"Reached {url}, but got HTTP status {response.status_code}.\n"
                "The host is up, but returned a non-200 response."
            )

    except requests.exceptions.RequestException as e:
        return f"Could not reach {url}.\nError: {e}"

demo = gr.Interface(
    fn=scan_vulnerabilities,
    inputs=gr.Textbox(
        label="Enter target IP or host",
        placeholder="e.g., 192.168.1.1"
    ),
    outputs=gr.Code(
        label="Scan result",
        lines=10
    ),
    title="Personal Ethical Hacking Tool",
    description=(
        "Simple demo scanner that checks for an HTTP service. "
        "For educational use only on authorized targets."
    )
)

if __name__ == "__main__":
    demo.launch()
