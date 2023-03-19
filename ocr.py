from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
print()

def do_ocr(img_path):
    result = ocr.ocr(img_path, cls=True)
    text = []
    for res in result:
        text.append(res[1][0])

    return text


# Test
if __name__ == "__main__":
    res = do_ocr('./captured_images/stage_static.png')
    print(res)