from pathlib import Path

# Function to create an HTML webpage with accompanying CSS
def create_html(screenshot_dir):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Search Results</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .screenshot {
                display: flex;
                justify-content: space-between;
                margin-bottom: 40px;
            }
            .screenshot img {
                width: 48%;
                border: 1px solid #ddd;
                border-radius: 4px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            }
            .title {
                text-align: center;
                font-size: 18px;
                margin-bottom: 10px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Search Results Screenshots</h1>
    """

    screenshots = list(screenshot_dir.glob("*_search_results.png"))

    for i in range(0, len(screenshots), 2):
        html_content += '<div class="screenshot">\n'
        html_content += f'    <div class="title">{screenshots[i].stem}</div>\n'
        html_content += f'    <img src="../{screenshots[i]}" alt="{screenshots[i].stem}">\n'
        if i + 1 < len(screenshots):
            html_content += f'    <div class="title">{screenshots[i + 1].stem}</div>\n'
            html_content += f'    <img src="../{screenshots[i + 1]}" alt="{screenshots[i + 1].stem}">\n'
        html_content += '</div>\n'

    html_content += """
        </div>
    </body>
    </html>
    """

    # Save the HTML file in the "result" directory
    result_dir = Path("result")
    result_dir.mkdir(exist_ok=True)
    html_file = result_dir / "search_results.html"
    with open(html_file, "w") as file:
        file.write(html_content)

    print("HTML webpage of all screenshots saved as result/search_results.html")
