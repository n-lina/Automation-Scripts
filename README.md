## Automation Scripts

delete.py: <br/><br/>
I have a large backup of photos on my computer. I wanted to move my photos to the cloud without exceeding the free cloud storage limit. To save space, I wrote this script to isolate the duplicate images. I consider an image to be a duplicate if it has the same modification time and date and size as another image. As a precautionary measure, I first tested my algorithm on only 200 images and verified that the isolated files were indeed duplicates before processing all 7000+ photos.
