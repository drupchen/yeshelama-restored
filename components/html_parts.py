from textwrap import dedent

head = dedent("""\
<!-- Last updated for Version 2.1 -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>བཀའ་ཁྲིད་ཐོས་ཀློག་སྦྲགས་མ།</title>
    <link rel="stylesheet" href="../css/hyperaudio-lite-player.css">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
    <style>
      :root {
        --primary-color: #4f6fa7; /* Softer blue */
        --secondary-color: #475569;
        --accent-color: #d48b4e; /* Soft amber/gold */
        --background-color: #f7fafc;
        --text-color: #23272f;
        --light-gray: #f5f6fa;
        --border-color: #e2e8f0;
        --hover-color: #e3e7ee;
        --timecode-bg: #f9f5e7;
        --timecode-text: #d48b4e;
        --active-bg: #f7f3e7;
        --active-highlight: #d4a94e;
        --card-shadow: 0 4px 16px rgba(79, 111, 167, 0.07), 0 1.5px 4px rgba(0, 0, 0, 0.06);
      }

      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }

      body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 0;
        margin: 0;
        min-height: 100vh;
        font-size: 1.07rem;
        letter-spacing: 0.01em;
      }

      .container {
        width: 100%;
        max-width: 1024px;
        margin: 0 auto;
        padding: 2rem 1rem;
      }

      @media (max-width: 768px) {
        .container {
          padding: 1.5rem 1rem;
        }
      }

      header {
        margin-bottom: 3rem;
        text-align: center;
        padding: 1.5rem 0;
      }

      h1 {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 1.1rem;
        color: var(--secondary-color);
        letter-spacing: -0.025em;
        text-shadow: 0 2px 8px rgba(79, 111, 167, 0.05);
      }

      h2 {
        font-size: 2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.2rem;
        color: var(--secondary-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.6rem;
        letter-spacing: -0.012em;
      }

      h3 {
        font-size: 1.35rem;
        font-weight: 500;
        margin: 1.75rem 0 0.75rem;
        color: var(--secondary-color);
        letter-spacing: -0.01em;
      }

      audio {
        width: 100%;
        margin: 1rem 0 0;
        border-radius: 21px;
        box-shadow: var(--card-shadow);
        height: 40px;
        transition: all 0.3s ease;
      }

      audio:focus,
      audio:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.05), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
      }

      /* Audio player styling */

      /* Session links styling */
      /* Table of contents styling */

      .toc-section {
        background-color: #fff;
        border-radius: 18px;
        padding: 1.5rem 1.25rem;
        margin: 2rem 0;
        box-shadow: var(--card-shadow);
        border: 1.5px solid var(--border-color);
        transition: box-shadow 0.2s, border-color 0.2s;
      }

      .toc-section:last-child {
        margin-bottom: 0;
      }

      .toc-section-title {
        font-size: 1.22rem;
        font-weight: 700;
        color: var(--secondary-color);
        margin-bottom: 1.3rem;
        padding-bottom: 0.35rem;
        border-bottom: 1.5px solid var(--border-color);
        letter-spacing: 0.01em;
      }
      .toc-section-title .tibetan {
        font-size: 1.5em;
        line-height: 1.3em;
      }

      .toc-section-subtitle {
        font-size: 0.9rem;
        opacity: 0.6;
      }

      /* Session links styling */
      .session-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.35rem;
        padding: 1rem 0;
        border-bottom: 1px solid var(--light-gray);
      }
      .session-links:first-child {
        padding-top: 0;
      }
      .session-links:last-child {
        border-bottom: 0;
        padding-bottom: 0;
      }

      /* Section dividers */
      .section-divider {
        margin: 8rem 0;
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, transparent, var(--border-color), transparent);
      }

      .session-links a {
        text-decoration: none;
        color: var(--primary-color);
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.3rem 0.7rem 0.3rem 1rem;
        border-radius: 9999px;
        background-color: var(--light-gray);
        transition: all 0.18s;
        display: inline-flex;
        align-items: center;
        box-shadow: 0 1.5px 5px rgba(79, 111, 167, 0.08);
        width: fit-content;
        gap: 0.7rem;
      }

      .session-links a:hover {
        background-color: var(--hover-color);
        box-shadow: 0 4px 12px rgba(212, 169, 78, 0.11);
      }

      .timecode {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: var(--timecode-bg);
        color: var(--timecode-text);
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-left: 0.5rem;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.02em;
      }
      
      .session {
        font-size: 0.875rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
      }
      
      .session-links .tibetan {
        font-size: 15pt;
        color: #1d458c;
        display: block;
        text-align: center;
        margin-bottom: 0.1em;
        white-space: nowrap;
      }
      .session-links .english {
        font-family: 'Inter', sans-serif;
        display: block;
        text-align: center;
        margin-bottom: 0.05em;
      }

      .session-links .human-time {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--accent-color);
        background-color: var(--timecode-bg);
        padding: 0.22rem 0.7rem;
        border-radius: 9999px;
        min-width: 3.3rem;
        text-align: center;
        display: inline-block;
        letter-spacing: 0.01em;
        box-shadow: 0 1.5px 4px rgba(212, 169, 78, 0.07);
      }

      .tibetan {
        font-family: Jomolhari, serif;
        font-weight: normal;
      }

      h2 {
        margin-top: 2em;
      }

      h2 span.tibetan {
        font-size: 1em;
        display: block;
        line-height: 1.3em;
      }

      /* Improve spacing for timecodes in transcript */
      .hyperaudio-transcript .timecode {
        position: relative;
        top: 10px;
        display: inline-flex;
        justify-content: center;
        min-width: 3.5rem;
        margin: 0 5px;
        padding: 0 !important;
        vertical-align: top;
      }

      /* Transcript styling */
      .hyperaudio-transcript {
        resize: vertical;
        overflow-y: auto;
        max-height: 500px;
        width: 100%;
        scrollbar-gutter: stable;
        position: relative;
        border: 1.5px solid var(--border-color);
        border-radius: 6px;
        padding: 2.1rem 1.2rem;
        background-color: #fff;
        margin: 1.3rem 0 2.7rem;
        font-family: Jomolhari, serif;
        font-size: 1.6rem;
        line-height: 1.85;
        box-shadow: var(--card-shadow);
        transition: box-shadow 0.3s, border-color 0.2s;
      }

      .hyperaudio-transcript a {
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s;
      }
      .hyperaudio-transcript a:hover {
        background: var(--hover-color);
        border-color: var(--primary-color);
      }
      .hyperaudio-transcript a.active {
        background-color: #d9f3fc !important;
        border-color: #d9f3fc !important;
      }

      /* Custom scrollbar for modern look */
      .hyperaudio-transcript::-webkit-scrollbar {
        width: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-track {
        background: var(--light-gray);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb {
        background-color: var(--border-color);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb:hover {
        background-color: var(--secondary-color);
      }

      .hyperaudio-transcript p > .active {
        background-color: rgba(59, 130, 246, 0.2);
        text-decoration: var(--active-highlight) underline;
        text-decoration-thickness: 2px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      }

      .hyperaudio-transcript p > .unread:not(.active) {
        opacity: 0.7;
      }

      #clipboard-text {
        font-family: Jomolhari, monospace;
        padding: 0.75rem;
        background-color: var(--light-gray);
        border-radius: 4px;
        margin: 0.5rem 0;
      }

      #clipboard-confirm {
        font-size: 0.875rem;
        color: var(--accent-color);
        margin-top: 0.5rem;
      }

      /* Tibetan text styling - preserving original fonts */
      [lang='bo'] {
        font-family: Jomolhari, serif;
      }
    </style>

  </head>""")

body_beginning = dedent("""\
    <body>
      <div id="popover"><a id="popover-btn">Copy to clipboard<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="-130 -110 600 600"><path d="m161,152.9h190c0.1,0 0.1,0 0.2,0 10.8,0 19.6-7.1 19.6-16 0-1.5-14.1-82.7-14.1-82.7-1.3-7.9-9.6-13.8-19.4-13.8l-61.7,.1v-13.5c0-8.8-8.8-16-19.6-16-10.8,0-19.6,7.1-19.6,16v13.6l-61.8,.1c-9.8,0-18,5.9-19.4,13.8l-13.7,80.3c-1.2,14.3 13.5,18.1 19.5,18.1z" fill="currentcolor"/><path d="m427.5,78.9h-26.8c0,0 9.3,53.5 9.3,58 0,30.4-26.4,55.2-58.8,55.2h-190.2c-19.6,0.4-63.3-14.7-58.1-63.9l8.4-49.2h-26.8c-10.8,0-19.6,8.8-19.6,19.6v382.9c0,10.8 8.8,19.6 19.6,19.6h343c10.8,0 19.6-8.8 19.6-19.6v-383c0-10.8-8.8-19.6-19.6-19.6zm-76.5,320.1h-190c-10.8,0-19.6-8.8-19.6-19.6 0-10.8 8.8-19.6 19.6-19.6h190c10.8,0 19.6,8.8 19.6,19.6 0,10.8-8.7,19.6-19.6,19.6zm0-110.3h-190c-10.8,0-19.6-8.8-19.6-19.6 0-10.8 8.8-19.6 19.6-19.6h190c10.8,0 19.6,8.8 19.6,19.6 0,10.8-8.7,19.6-19.6,19.6z" fill="currentcolor"/></svg></a></div>

<dialog id="clipboard-dialog">
    <h3>The following text has been copied to the clipboard</h3>
    <p id=clipboard-text></p>
    <div style="text-align: right;">
      <button id="clipboard-confirm">ok</button>
    </div>
</dialog>
          """)

player_start = '<audio id="hyperplayer1" style="position:relative; width:97%" src="'

audio_links = {
    "A1": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406750768-44100-2-ff6a3a96df743.m4a",
    "A2": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406750846-44100-2-f1050d86eb8b1.m4a",
    "A3": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406750897-44100-2-86e832e55a743.m4a",
    "A4": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406750947-44100-2-fbf2caa90d12c.m4a",
    "A5": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406750980-44100-2-0172976f5d259.m4a",
    "A6": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751039-44100-2-f9cef3a63ccac.m4a",
    "A7": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751081-44100-2-87880d6714865.m4a",
    "A8": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751264-44100-2-8cbd3fd0f252f.m4a",
    "A9": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751608-44100-2-5794841b49d04.m4a",
    "A10": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751668-44100-2-6d48b12279faf.m4a",
    "A11": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751729-44100-2-ee01c3f5cda4d.m4a",
    "A12": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751847-44100-2-9ba111eb56aef.m4a",
    "A13": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751906-44100-2-8dfe045d9cee8.m4a",
    "A14": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406751972-44100-2-7e041048df32d.m4a",
    "A15": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406752035-44100-2-a57c7a4057e6d.m4a",
    "A16": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406752097-44100-2-c4a20f36d2602.m4a",
    "A17": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406752136-44100-2-b7f256631d3ba.m4a",
    "A18": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-2/406752176-44100-2-396e1198702db.m4a",
    "A19": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/c88d7a19-f566-f947-bce4-0e6c5840ab57.mp3",
    "A20": 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407476680-44100-2-a4069a95c2eb.m4a',
    'A21': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477037-44100-2-752a5763c05a1.m4a',
    'A22': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477086-44100-2-ee7a5d609a98d.m4a',
    'A23': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/785780d8-f075-f534-6934-8444eea046a5.mp3',
    'A24': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477202-44100-2-0c54f7f1cf603.m4a',
    'B1': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/5281b183-f2f2-dfb4-d5bc-94fd932c8f36.mp3',
    'B2': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477569-44100-2-148a60dcea3ab.m4a',
    'B3': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/1a374a1b-0e62-7918-4d77-ed0a74e1025a.mp3',
    'B4': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477666-44100-2-a6baebd2e9388.m4a',
    'B5': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477728-44100-2-de080971cab53.m4a',
    'B6': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477760-44100-2-6305bf5d1f314.m4a',
    'B7': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477786-44100-2-8c39b9a1be2d9.m4a',
    'B8': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/63393717-8c19-06bc-046f-8fd54b83612d.mp3',
    'B9': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407477901-44100-2-ac40249f90f75.m4a',
    'B10': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/eaf4f22e-7279-463a-6eb8-af5b73cfebc5.mp3',
    'B11': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/3af59b8e-a950-e29f-0f13-8feb58c077bf.mp3',
    'B12': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478039-44100-2-3e0c83f1fc536.m4a',
    'B13': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/2eaa9b34-9750-8372-cbd4-f1586cafe4e0.mp3',
    'B14': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/73ceda60-73cd-14c1-f8f4-df0922034553.mp3',
    'B15': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/284b9b18-ba98-e5e1-28e1-86790466d64c.mp3',
    'B16': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/4c34e6bb-c8c3-7ed3-0567-5e2ae084aa89.mp3',
    'B17': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478318-44100-2-1130bfe59a43e.m4a',
    'B18': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/08441aa1-1595-1803-ae52-2002e1928f6d.mp3',
    'B19': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/5e74c720-0623-b3f9-4fe1-177d8dd21020.mp3',
    'B20': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/fd6a3bbb-cb43-ad4d-a45f-aabee52eb9c3.mp3',
    'B21': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478513-44100-2-3b2299c2e470d.m4a',
    'B22': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/41a5e6a0-294f-c888-031b-41de75545a55.mp3',
    'B23': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/8e15a105-fb19-bcaf-7868-45c6ba73bb7a.mp3',
    'B24': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478716-44100-2-c18bbac318785.m4a',
    'B25': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/d1bca234-4ed1-0192-53f8-a833814a075e.mp3',
    'B26': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/33595bdb-1c67-a71e-6b6c-c52f36f5eade.mp3',
    "C1": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478868-44100-2-cfd97f363a6b9.m4a",
    'C2': "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478936-44100-2-caf8924237591.m4a",
    "C3": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407478977-44100-2-e87cc79695003.m4a",
    "C4": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407479036-44100-2-3f913eae4beb1.m4a",
    'C5': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407479096-44100-2-025fbe491e134.m4a',
    'C6': 'https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407479144-44100-2-f0e9db6fd18d3.m4a',
    "C7": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407479195-44100-2-56ee56fc5b4c6.m4a",
    "C8": "https://d3ctxlq1ktw2nl.cloudfront.net/staging/2025-8-14/407479336-44100-2-1cce2934b2ac3.m4a",
}
player_middle = '" type="audio/'
player_end = '" controlsList="nodownload" controls></audio>'

transcript_start = """\
          
          <div id="hypertranscript1" class="hyperaudio-transcript" style="resize: vertical; overflow-y:scroll; height:800px; width: 97%; scrollbar-gutter: stable; position:relative; border-style:dashed; border-width: 1px; border-color:#999; padding: 8px">
          <article><section>"""

transcript_end = dedent("""\
          </section></article>
          </div>""")

body_end = dedent("""\
      <script src="https://w.soundcloud.com/player/api.js"></script>
      <script src="../js/hyperaudio-lite.js"></script>
      <script src="../js/hyperaudio-lite-extension.js"></script>
      <script>
      // minimizedMode is still experimental - it aims to show the current words in the title, which can be seen on the browser tab.
      let minimizedMode = false;
      let autoScroll = true;
      let doubleClick = false;
      let webMonetization = false;

      new HyperaudioLite("hypertranscript1", "hyperplayer1", minimizedMode, autoScroll, doubleClick, webMonetization);
      </script>
      <script>
        var coll = document.getElementsByClassName("collapsible");
        var i;

        for (i = 0; i < coll.length; i++) {
          coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
              content.style.display = "none";
            } else {
              content.style.display = "block";
            }
          });
        }
      </script>
  </body>
</html>""")

index_head = dedent("""\
<!-- Last updated for Version 2.1 -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ཡེ་ཤེས་བླ་མ།</title>
    <link rel="stylesheet" href="css/hyperaudio-lite-player.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jomolhari" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.5.0/velocity.js"></script>
    <style>
      :root {
        --primary-color: #4f6fa7; /* Softer blue */
        --secondary-color: #475569;
        --accent-color: #d48b4e; /* Soft amber/gold */
        --background-color: #f7fafc;
        --text-color: #23272f;
        --light-gray: #f5f6fa;
        --border-color: #e2e8f0;
        --hover-color: #e3e7ee;
        --timecode-bg: #f9f5e7;
        --timecode-text: #d48b4e;
        --active-bg: #f7f3e7;
        --active-highlight: #d4a94e;
        --card-shadow: 0 4px 16px rgba(79, 111, 167, 0.07), 0 1.5px 4px rgba(0, 0, 0, 0.06);
      }

      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }

      body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background-color: var(--background-color);
        padding: 0;
        margin: 0;
        min-height: 100vh;
        font-size: 1.07rem;
        letter-spacing: 0.01em;
      }

      .container {
        width: 100%;
        max-width: 1024px;
        margin: 0 auto;
        padding: 2rem 1rem;
      }

      @media (max-width: 768px) {
        .container {
          padding: 1.5rem 1rem;
        }
      }

      header {
        margin-bottom: 3rem;
        text-align: center;
        padding: 1.5rem 0;
      }

      h1 {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 1.1rem;
        color: var(--secondary-color);
        letter-spacing: -0.025em;
        text-shadow: 0 2px 8px rgba(79, 111, 167, 0.05);
      }

      h2 {
        font-size: 2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.2rem;
        color: var(--secondary-color);
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.6rem;
        letter-spacing: -0.012em;
      }

      h3 {
        font-size: 1.35rem;
        font-weight: 500;
        margin: 1.75rem 0 0.75rem;
        color: var(--secondary-color);
        letter-spacing: -0.01em;
      }

      audio {
        width: 100%;
        margin: 1rem 0 0;
        border-radius: 21px;
        box-shadow: var(--card-shadow);
        height: 40px;
        transition: all 0.3s ease;
      }

      audio:focus,
      audio:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.05), 0 3px 6px rgba(0, 0, 0, 0.08);
        transform: translateY(-1px);
      }

      /* Audio player styling */

      /* Session links styling */
      /* Table of contents styling */

      .toc-section {
        background-color: #fff;
        border-radius: 18px;
        padding: 1.5rem 1.25rem;
        margin: 2rem 0;
        box-shadow: var(--card-shadow);
        border: 1.5px solid var(--border-color);
        transition: box-shadow 0.2s, border-color 0.2s;
      }

      .toc-section:last-child {
        margin-bottom: 0;
      }

      .toc-section-title {
        font-size: 1.22rem;
        font-weight: 700;
        color: var(--secondary-color);
        margin-bottom: 1.3rem;
        padding-bottom: 0.35rem;
        border-bottom: 1.5px solid var(--border-color);
        letter-spacing: 0.01em;
      }
      .toc-section-title .tibetan {
        font-size: 1.5em;
        line-height: 1.3em;
      }

      .toc-section-subtitle {
        font-size: 0.9rem;
        opacity: 0.6;
      }

      /* Session links styling */
      .session-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.35rem;
        padding: 1rem 0;
        border-bottom: 1px solid var(--light-gray);
      }
      .session-links:first-child {
        padding-top: 0;
      }
      .session-links:last-child {
        border-bottom: 0;
        padding-bottom: 0;
      }

      /* Section dividers */
      .section-divider {
        margin: 8rem 0;
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, transparent, var(--border-color), transparent);
      }

      .session-links a {
        text-decoration: none;
        color: var(--primary-color);
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.3rem 0.7rem 0.3rem 1rem;
        border-radius: 9999px;
        background-color: var(--light-gray);
        transition: all 0.18s;
        display: inline-flex;
        align-items: center;
        box-shadow: 0 1.5px 5px rgba(79, 111, 167, 0.08);
        width: fit-content;
        gap: 0.7rem;
      }

      .session-links a:hover {
        background-color: var(--hover-color);
        box-shadow: 0 4px 12px rgba(212, 169, 78, 0.11);
      }

      .timecode {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: var(--timecode-bg);
        color: var(--timecode-text);
        font-size: 0.875rem;
        font-weight: 500;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        margin-left: 0.5rem;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.02em;
      }
      
      .session {
        font-size: 0.875rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
      }
      
      .session-links .tibetan {
        font-size: 15pt;
        color: #1d458c;
        display: block;
        text-align: center;
        margin-bottom: 0.1em;
        white-space: nowrap;
      }
      .session-links .english {
        font-family: 'Inter', sans-serif;
        display: block;
        text-align: center;
        margin-bottom: 0.05em;
      }

      .session-links .human-time {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--accent-color);
        background-color: var(--timecode-bg);
        padding: 0.22rem 0.7rem;
        border-radius: 9999px;
        min-width: 3.3rem;
        text-align: center;
        display: inline-block;
        letter-spacing: 0.01em;
        box-shadow: 0 1.5px 4px rgba(212, 169, 78, 0.07);
      }

      .tibetan {
        font-family: Jomolhari, serif;
        font-weight: normal;
      }

      h2 {
        margin-top: 2em;
      }

      h2 span.tibetan {
        font-size: 1em;
        display: block;
        line-height: 1.3em;
      }

      /* Improve spacing for timecodes in transcript */
      .hyperaudio-transcript .timecode {
        position: relative;
        top: 10px;
        display: inline-flex;
        justify-content: center;
        min-width: 3.5rem;
        margin: 0 5px;
        padding: 0 !important;
        vertical-align: top;
      }

      /* Transcript styling */
      .hyperaudio-transcript {
        resize: vertical;
        overflow-y: auto;
        max-height: 500px;
        width: 100%;
        scrollbar-gutter: stable;
        position: relative;
        border: 1.5px solid var(--border-color);
        border-radius: 6px;
        padding: 2.1rem 1.2rem;
        background-color: #fff;
        margin: 1.3rem 0 2.7rem;
        font-family: Jomolhari, serif;
        font-size: 1.6rem;
        line-height: 1.85;
        box-shadow: var(--card-shadow);
        transition: box-shadow 0.3s, border-color 0.2s;
      }

      .hyperaudio-transcript a {
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s;
      }
      .hyperaudio-transcript a:hover {
        background: var(--hover-color);
        border-color: var(--primary-color);
      }
      .hyperaudio-transcript a.active {
        background-color: #d9f3fc !important;
        border-color: #d9f3fc !important;
      }

      /* Custom scrollbar for modern look */
      .hyperaudio-transcript::-webkit-scrollbar {
        width: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-track {
        background: var(--light-gray);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb {
        background-color: var(--border-color);
        border-radius: 8px;
      }

      .hyperaudio-transcript::-webkit-scrollbar-thumb:hover {
        background-color: var(--secondary-color);
      }

      .hyperaudio-transcript p > .active {
        background-color: rgba(59, 130, 246, 0.2);
        text-decoration: var(--active-highlight) underline;
        text-decoration-thickness: 2px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      }

      .hyperaudio-transcript p > .unread:not(.active) {
        opacity: 0.7;
      }

      #clipboard-text {
        font-family: Jomolhari, monospace;
        padding: 0.75rem;
        background-color: var(--light-gray);
        border-radius: 4px;
        margin: 0.5rem 0;
      }

      #clipboard-confirm {
        font-size: 0.875rem;
        color: var(--accent-color);
        margin-top: 0.5rem;
      }

      /* Tibetan text styling - preserving original fonts */
      [lang='bo'] {
        font-family: Jomolhari, serif;
      }
    </style>
  </head>""")

index_body = dedent("""\
  <body>
    <div class="toc-section">""")

index_link_start = '\n<a href="sessions/transcript_'
index_link_start2 = '.html#hypertranscript1='
index_link_middle1a = '"><span class="session-a"><span class="session">'
index_link_middle1b = '"><span class="session-b"><span class="session">'
index_link_middle1c = '"><span class="session-c"><span class="session">'
index_link_middle2 = ' </span><span class="tibetan">'
index_link_end = '</span></span></a>'

index_end = dedent("""\
    </div>
  </body>
</html>
""")