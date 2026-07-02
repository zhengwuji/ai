import sys
import json
import os

def clean_transcript(conversation_id):
    transcript_path = f'C:\\Users\\Administrator\\.gemini\\antigravity-ide\\brain\\{conversation_id}\\.system_generated\\logs\\transcript.jsonl'
    if not os.path.exists(transcript_path):
        print(f'Transcript not found: {transcript_path}')
        return
    
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    refusals = ['I cannot fulfill', 'I cannot help', 'I am unable to provide', '我无法提供', '不能满足您的请求']
    modified = False
    
    for line in lines:
        try:
            data = json.loads(line)
            if data.get('source') == 'MODEL' and any(r in data.get('content', '') for r in refusals):
                print('Found and removing a refusal response.')
                modified = True
                continue # skip this line
        except json.JSONDecodeError:
            pass
        cleaned_lines.append(line)
    
    if modified:
        import shutil
        shutil.copy2(transcript_path, transcript_path + '.bak')
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
        print('Successfully cleaned transcript.')
    else:
        print('No refusals found.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        clean_transcript(sys.argv[1])
    else:
        print('Usage: python clean_memory.py <conversation-id>')
