from pathlib import Path
import re
from decimal import Decimal
import datetime

import srt

from components.html_parts import *


def parse_srt(in_file):
    """
    :param in_file: .srt utf-8 file
    :return: [{'start': <start-time-in-milliseconds>, 'end': <end-time-in-milliseconds>, 'content': <string>}, ...]
    """
    def to_milli(time):
        return int(time.total_seconds()*1000)

    raw = Path(in_file).read_text()
    sub_raw = list(srt.parse(raw))

    parsed = []
    for sub in sub_raw:
        start = to_milli(sub.start)
        end = to_milli(sub.end)
        content = sub.content
        content = normalize_punct(content)
        s = {'start': start, 'end': end, 'content': content}
        parsed.append(s)
    return parsed


def normalize_punct(string):
    string = string.strip().replace('་ ', '་')
    if string.endswith(' །'):
        pass
    elif string.endswith('།') or string.endswith('ཿ') or string.endswith('༔'):
        string += ' '
    return string


def gen_ha_page(in_file):
    # A. parse and prepare chunks
    parsed = parse_srt(in_file)
    chunks = []
    chunks_for_links = []
    cur = []
    slide_num = []
    for p in parsed:
        if p['content'].startswith('{'):
            # add to chunks
            if cur:
                num = []
                if slide_num:
                    num = slide_num
                chunks.append((num, cur))
                cur = []
                slide_num = []

            # start new chunk
            text = p['content']
            while '}' in text:
                s_num, text = text.split('}', 1)
                slide_num.append(int(s_num[1:]))
            p['content'] = text
            cur.append(p)
        else:
            cur.append(p)
    # trailing chunk
    if cur:
        chunks.append((slide_num, cur))

    # B. format and add ha html code
    ha_trans = []
    for s_num, chunk in chunks:
        # add slide to html
        if s_num:
            for n, s in enumerate(s_num):
                img = f'\n<img src="components/slides/slide_{s}.jpg" alt="slide {s}">\n'
                if len(s_num) > 1 and n < len(s_num)-1:
                    img += '<br>'
                ha_trans.append(img)
        # add text
        ha_trans.append('<p>')
        for p in chunk:
            start = p['start']
            duration = p['end'] - p['start']
            content = p['content']
            # further process content here ########################################
            if (content.endswith('།') and not content.endswith(' །')) or content.endswith('༔'):
                content += ' '

            # unsure
            content = content.replace('༺', '<span class="unsure">')
            content = content.replace('༻', '</span>')

            # hesitation
            content = content.replace('༼', '<span class="hesit">(')
            content = content.replace('༽', ')</span>')

            # changed syllables
            idxs = [m.start() for m in re.finditer('࿏', content)]
            if idxs:
                raw = [content[:idxs[0]]]
                raw.extend([content[i:j] for i,j in zip(idxs, idxs[1:]+[None])])
                parts = []
                for r in raw:
                    if r.startswith('࿏'):
                        parts.append(r[:2])
                        if r[2:]:
                            parts.append(r[2:])
                    else:
                        parts.append(r)

                for i in range(len(parts)):
                    if i > 0 and parts[i].startswith('࿏'):
                        while True:
                            if not parts[i-1]:
                                break
                            c = parts[i-1][-1]
                            if c == '་':
                                break
                            parts[i] = c + parts[i]
                            parts[i-1] = parts[i-1][:-1]

                for i in range(len(parts)):
                    if '࿏' in parts[i]:
                        if '/span>' in parts[i]:
                            a, b = parts[i].split('/span>')
                            a += '/span>'
                            b = f'<span class="changed">{b}</span>'
                            new = a+b
                            parts[i] = new.replace('࿏', '')
                        else:
                            parts[i] = f'<span class="changed">{parts[i].replace('࿏', '')}</span>'
                content = ''.join(parts)
            # #######################################################################

            # add units while ignoring empty segments
            if content.strip():
                # human readable duration
                m, s = divmod(duration/1000, 60)
                m = str(m).split('.')[0]
                s = str(s).split('.')[0]

                if m != '0':
                    dur = f'{m}m{s}s'
                else:
                    dur = f'{s}s'

                trans = f'\n<a data-m="{start}" data-d="{duration}">{content}<span class="timecode">{dur}</span></a>'
                ha_trans.append(trans)

                ### create duration for link
                start_for_link = str(Decimal(start/1000).quantize(Decimal('0.01')))
                end_for_link = str(Decimal((start+duration)/1000).quantize(Decimal('0.01')))
                for_link = f'{start_for_link},{end_for_link}'
                chunks_for_links.append((content,for_link))

        ha_trans.append('</p>')

    return ''.join(ha_trans), chunks, chunks_for_links

def format_text(chunks):
    out = []
    for _, chunk in chunks:
        c = ''.join([c['content'] for c in chunk])
        out.append(c)
    return '\n\n'.join(out)

files = []
for f in Path('components').glob('*.srt'):
    file_num = f.stem.split('_', 1)[0]
    file_num = int(file_num)
    files.append((file_num, f))
files = sorted(files)

total_text = []
for file_num, in_file in files:
    l = audio_links[str(file_num)]
    ext = l.split('.')[-1]
    player = f'{player_start}{l}{player_middle}{ext}{player_end}'

    transcription, chunks, for_links = gen_ha_page(in_file)
    transcription = f'\n{transcript_start}\n{transcription}\n{transcript_end}\n\n'

    html_page = '\n'.join([head, body_beginning, player, transcription, body_end])
    Path(f'sessions/transcript_{file_num}.html').write_text(html_page)

    for a, b in for_links:
        total_text.append((a, b, file_num))

index = [index_head, index_body]
body = []
for text, idx, f_num in total_text:
    link = f'{index_link_start}{f_num}{index_link_start2}{idx}{index_link_middle}{text}{index_link_end}'
    body.append(link)
body = ''.join(body)
index.append(body)
index.append(index_end)
Path('index_staging.html').write_text('\n'.join(index))

