mapping = {
    "A#": "I",
    "C#": "J",
    "D#": "K",
    "F#": "L",
    "G#": "M",
    "B#": "X",
}
def replace_sharp(s):
    for k, v in mapping.items():
        s = s.replace(k, v)
    return s

def str_to_time(s):
    hh, mm = s.split(':')
    return int(hh) * 60 + int(mm)

def cmp(m, melody, time):
    l1, l2 = len(m), len(melody)
    temp = melody * (time // l2) + melody[:(time % l2)]
    return m in temp

def solution(m, musicinfos):
    m = replace_sharp(m)
    
    answer = [0, '']
    for each in musicinfos:
        start, end, title, melody = each.split(',')
        melody = replace_sharp(melody)
        diff = str_to_time(end) - str_to_time(start)
        if not diff:
            continue
            
        melody = melody[:diff]
        if m in melody or cmp(m, melody, diff):
            if answer[0] < diff:
                answer[0], answer[1] = diff, title
    
    if answer[1] == '':
        return "(None)"
    return answer[1]