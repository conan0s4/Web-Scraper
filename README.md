<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Surface x Dark Web Scraper</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #0d1117;
      color: #c9d1d9;
      margin: 0;
      padding: 0;
    }

    .container {
      width: 80%;
      margin: auto;
      padding: 40px 0;
    }

    .header {
      text-align: center;
      padding: 20px;
      border-bottom: 1px solid #30363d;
    }

    .title {
      font-size: 30px;
      font-weight: bold;
    }

    .subtitle {
      color: #8b949e;
      margin-top: 8px;
    }

    .badge {
      display: inline-block;
      background: #238636;
      padding: 4px 10px;
      border-radius: 5px;
      margin-top: 10px;
      font-size: 12px;
    }

    h2 {
      border-bottom: 1px solid #30363d;
      padding-bottom: 6px;
      margin-top: 30px;
    }

    pre {
      background: #161b22;
      padding: 12px;
      border-radius: 6px;
      overflow-x: auto;
    }

    code {
      background: #161b22;
      padding: 2px 5px;
      border-radius: 4px;
    }

    .warning {
      background: #2a1a1a;
      border-left: 4px solid #f85149;
      padding: 10px;
      margin-top: 15px;
    }

    ul, ol {
      line-height: 1.6;
    }
  </style>
</head>

<body>

<div class="container">

  <!-- HEADER -->
  <div class="header">
    <div class="title">Surface x Dark Web Scraper</div>
    <div class="subtitle">OSINT Recon Tool for Surface and Dark Web Intelligence Gathering</div>
    <div class="badge">Python • BeautifulSoup • Requests • Tor Support</div>
  </div>

  <!-- ABOUT -->
  <h2>About</h2>
  <p>
    A lightweight reconnaissance tool designed for extracting structured intelligence from web pages.
    It supports both standard HTTP requests and Tor routing for .onion domain analysis when configured.
  </p>

  <!-- WARNING -->
  <div class="warning">
    This tool is intended for educational and authorized security testing only. Unauthorized use is strictly prohibited.
  </div>

  <!-- FEATURES -->
  <h2>Features</h2>
  <ul>
    <li>Standard and Tor-based HTTP requests</li>
    <li>Extraction of usernames, emails, IP addresses, and domains</li>
    <li>Detection of subdomains and phone numbers</li>
    <li>Link and onion URL parsing</li>
    <li>HTML metadata extraction (titles, headings, comments)</li>
    <li>Regex-based OSINT data gathering</li>
  </ul>

  <!-- INSTALLATION -->
  <h2>Installation</h2>
  <pre>
pip install requests beautifulsoup4
  </pre>

  <p>Optional requirements for Tor support:</p>
  <ul>
    <li>Tor service running locally</li>
    <li>Socks proxy enabled on 127.0.0.1:9050</li>
  </ul>

  <!-- USAGE -->
  <h2>Usage</h2>
  <pre>
python scraper.py
  </pre>

  <p>Input example:</p>
  <pre>
Target web >> https://example.com
Use Tor? [y/n] >> y
input timeout >> 10
  </pre>

  <!-- OUTPUT -->
  <h2>Output Example</h2>
  <pre>
[+] Usernames found:
@admin

[+] Emails found:
test@example.com

[+] Links found:
https://example.com/page

[+] IPs found:
192.168.1.1
  </pre>

  <!-- HOW IT WORKS -->
  <h2>How It Works</h2>
  <ol>
    <li>User inputs target URL</li>
    <li>HTTP request is sent (Tor optional)</li>
    <li>BeautifulSoup parses HTML content</li>
    <li>Regex extracts OSINT indicators</li>
    <li>Results are grouped and displayed</li>
  </ol>

  <!-- TECH STACK -->
  <h2>Tech Stack</h2>
  <ul>
    <li>Python 3</li>
    <li>Requests</li>
    <li>BeautifulSoup4</li>
    <li>Regex</li>
  </ul>

  <!-- STRUCTURE -->
  <h2>Repository Structure</h2>
  <pre>
recon-tool/
├── scraper.py
├── extractor.py
├── requirements.txt
├── README.html
  </pre>

  <!-- FUTURE -->
  <h2>Future Improvements</h2>
  <ul>
    <li>Recursive crawling system</li>
    <li>Export results to JSON and CSV</li>
    <li>Async scraping performance upgrade</li>
    <li>Deduplication layer for results</li>
    <li>Stealth request headers and rate limiting</li>
  </ul>

  <!-- DISCLAIMER -->
  <div class="warning">
    Legal Notice: Use only on systems you own or have explicit authorization to test.
  </div>

</div>

</body>
</html>
