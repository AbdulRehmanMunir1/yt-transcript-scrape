from playwright.sync_api import sync_playwright
import pyperclip

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=800)
    page = browser.new_page()
    page.goto("https://www.youtube.com/watch?v=FGfIoyO7v5M")

    try:
        expand_button = page.locator('tp-yt-paper-button#expand').first
        expand_button.click(timeout=5000)
        page.wait_for_timeout(1000)
        show_transcript_button = page.get_by_role("button", name="Show transcript")

        show_transcript_button.click()

        # Refined locator to target the correct transcript element
        transcript = page.locator('ytd-engagement-panel-section-list-renderer ytd-transcript-segment-list-renderer').first

        

        transcript.highlight()
        transcript_text = transcript.inner_text()
        
        transcript_without_title = ""       
        index = transcript_text.find("0:00")  # Find the index of "0:00"
        if index != -1:
            title_text = transcript_text[:index].strip()
        
       

        parts = transcript_text.split("0:00", 1)  # Split at "0:00", keeping only the second part
        if len(parts) > 1:
            transcript_without_title  =  "0:00" + parts[1] 
        

        print("============Start=================")
        print(title_text)
        print("--------------------------")
        print(transcript_without_title)

        pyperclip.copy(transcript_text)
        print("============End=================")

        page.wait_for_timeout(5000)
    except Exception as e:
        print(f"An error occurred: {e}")

    
    page.wait_for_timeout(5000)

    browser.close()