def get_text_between_tags(string, start_tag, end_tag=None):
    if end_tag is None:
        end_tag = start_tag
    start_tag = "<" + start_tag + ">"
    end_tag = "</" + end_tag + ">"
    content = []
    start_index = 0
    while True:
        start_loc = string.find(start_tag, start_index)
        if start_loc == -1:
            break
        end_loc = string.find(end_tag, start_loc + len(start_tag))
        if end_loc == -1:
            break
        content.append(string[start_loc + len(start_tag):end_loc])
        start_index = end_loc + len(end_tag)
    return content