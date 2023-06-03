from image_preprocess import *
from extract_infos import *
from check_grammar import *

def convert_to_text(temp_result):#email, title, info부분 각각 매개변수로 따로 받기
    #processed_img=image_preprocess(img)#이부분 없애기
    #extracted_img=extract_infos(processed_img)#이부분 없애기

    #ocr
    #email
    reader_en = easyocr.Reader(['en'])
    raw_email = reader_en.readtext(temp_result[0], detail=0, height_ths=1, width_ths=100)
    
    email = "".join(raw_email).replace(" ", "")#띄어쓰기 없애기
    #@뒤는 한정짓기
    #####
    print(email)

    #title
    reader_ko = easyocr.Reader(['ko'])
    raw_title = reader_ko.readtext(temp_result[1], detail=0, height_ths=1, width_ths=100)
    
    #check grammar of title
    title=check_grammar(raw_title)
    title="".join(title)
    print(title)

    #info
    info = reader_ko.readtext(temp_result[2], detail=0, height_ths=1, width_ths=100)
    print(info)
    #check grammar of each sentence in info
    refined_text=check_grammar(info)

    #insert newline
    text='\n'.join(refined_text)

    # return (email, title, text) -->tuple!!
    return (email, title, text)

#print(convert_to_text("processed.png"))