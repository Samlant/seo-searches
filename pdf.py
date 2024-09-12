from pathlib import Path
from fpdf import FPDF

# Function to create a PDF file of all screenshots with two screenshots next to each other per page
def create_pdf(screenshot_dir):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Search Results Screenshots', 0, 1, 'C')

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    pdf = PDF(orientation='L', unit='pt', format=(2400, 1800))
    pdf.set_auto_page_break(auto=True, margin=15)

    screenshots = list(screenshot_dir.glob("*_search_results.png"))

    for i in range(0, len(screenshots), 2):
        pdf.add_page()
        
        # Add title for the first screenshot
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 20, screenshots[i].stem, 0, 1, 'C')
        
        pdf.image(str(screenshots[i]), x=10, y=40, w=1180)
        
        if i + 1 < len(screenshots):
            # Add title for the second screenshot
            pdf.set_y(20)  # Adjust y position for the second title
            pdf.cell(0, 20, screenshots[i + 1].stem, 0, 1, 'C')
            
            pdf.image(str(screenshots[i + 1]), x=1210, y=40, w=1180)

    # Save the final PDF in the "result" directory
    result_dir = Path("result")
    result_dir.mkdir(exist_ok=True)
    pdf.output(result_dir / "search_results.pdf")

    print("PDF of all screenshots saved as result/search_results.pdf")
