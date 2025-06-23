import get_yt_transcript_TEST
import  gemTest
api_key = "AIzaSyAsp5Aa8AYC3VyKNeTW450WlYZkxZ2QTCo" 
def test_gemini ():
    text = get_yt_transcript_TEST.transcript_without_title
    summarized_text = gemTest.summarize_text_with_gemini(api_key,text)
    print("Summarized text: \n")
    print("==============================================\n")
    print(summarized_text)
    print("==============================================\n")
    print("Test passed")

test_gemini()