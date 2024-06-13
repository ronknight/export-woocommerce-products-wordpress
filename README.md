<h1 align="center"><a href="https://github.com/ronknight/export-woocommerce-products-wordpress">Export WooCommerce Products from WordPress</a></h1>
<h4 align="center">This Python script, along with a batch file, automates the process of exporting WooCommerce products from a WordPress website using Selenium and the Chrome browser.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/export-woocommerce-products-wordpress/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/export-woocommerce-products-wordpress/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#acknowledgment">Acknowledgment</a> •
  <a href="#diagrams">Diagrams</a> •
</p>

---

## Prerequisites

- Python 3.7.1
- Selenium 1.22
- ChromeDriver 2.24.1
- Google Chrome

## Installation

1. Clone or download the repository.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Download the appropriate version of ChromeDriver for your Chrome browser and operating system from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Extract the ChromeDriver executable and place it in a directory that is included in your system's `PATH` environment variable.

## Usage

1. Open the `export-woocommerce-products-wordpress.py` file and update the following lines with your WordPress website credentials and admin URL:

```python
driver.get('https://yourwordpresssite.com/wp-admin')
id_box.send_keys('your-user-name')
pass_box.send_keys('your-password')
```

2. Save the changes to the Python file.
3. Double-click the Run.bat file or run it from the command prompt to execute the script.

The script will open the Chrome browser, navigate to your WordPress admin dashboard, log in using the provided credentials, navigate to the WooCommerce products page, and initiate the export process. The exported CSV file will be downloaded to your default downloads folder.

## Acknowledgments

Selenium - The web automation tool used in this project.
ChromeDriver - The WebDriver used to automate the Chrome browser.