import streamlit as st

def main():
    st.set_page_config(layout="wide")
    # Add custom CSS
    custom_css = '''
    <style>
        /* Your CSS styles here */
    
    body{
    background-color: #121223;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: whitesmoke;
    font-size: 16px;
}

header {
    background-color: #0f0369;
    padding: 17px;
    color: whitesmoke;
}
p {
    font-size: 24px;
    font-weight: 400;
    padding: 5px;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 26px;
    font-weight: bold;
}

.navbar-links {
    list-style: none;
    margin: 0;
    padding: 0;
}

.navbar-links li {
    display: inline-block;
    margin-left: 20px;
}

.navbar-links li a {
    text-decoration: none;
    color: #fff;
}

main {
    padding: 20px;
}

.hero {
    text-align: center;
    padding: 50px 60px;
    background-color: #121223;
    color: #fff;
}

.hero h1 {
    font-size: 56px;
    margin-bottom: 20px;
}

.file-upload-section,
.pdf-selector-section,
.view-report-section {
    background-color: #121223;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.1);
}

.file-upload-section h2,
.pdf-selector-section h2,
.view-report-section h2 {
    font-size: 30px;
    margin-bottom: 10px;
}

.btn {
    background-color: #e41520;
    color: #fff;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #911f1f;
}

.view-report-btn {
    background-color: #2ea231;
}
.view-report-btn:hover {
    background-color: #1e6822;
}


footer {
    background-color: #202020;
    color: #fff;
    text-align: center;
    padding: 1px;
}

    </style>
    '''
    st.markdown(custom_css, unsafe_allow_html=True)

    # Add custom HTML
    custom_html = '''
    <header>
        <nav>
            <div class="logo">Flipkart</div>
            <ul class="navbar-links">
                <li><a href="#">Dashboard</a></li>
                <li><a href="#">Report</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Help</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="hero">
            <h1>Monitoring Complaince </h1>
            <p>Guarding Your Privacy</p>
        </section>

    <section class="file-upload-section">
            <h2>Upload Your Log Files</h2>
            <p>Select files in TXT, CSV and PDF format:</p>
            <form>
                <input type="file" id="textFile" name="textFile" accept=".txt">
                <input type="file" id="csvFile" name="csvFile" accept=".csv">
                <input type="file" id="pdfFile" name="pdfFile" accept=".pdf">
                <button type="submit" class="btn">Submit</button>
            </form>
        </section>

    <section class="pdf-selector-section">
            <h2>Select Your Ruleset  File</h2>
            <form>
                <input type="file" id="pdfSelector" name="pdfSelector" accept=".pdf">
                <button type="submit" class="btn">Submit</button>
            </form>
        </section>

    <section class="view-report-section">
            <h2>Click Here to View Report</h2>
            <button class="btn view-report-btn">View Report</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Service Website. All rights reserved.</p>
    </footer>
    '''
    st.markdown(custom_html, unsafe_allow_html=True)

    # Add custom JavaScript
    custom_js = '''
    <script>
        function myFunction() {
            alert("Button clicked!");
        }
    </script>
    '''
    st.markdown(custom_js, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
