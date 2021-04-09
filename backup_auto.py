from swift_upload import upload_file
import glob
# if we've crashed, we need to upload all the files
if __name__ == '__main__':
    for filename in glob.glob("*.txt"): 
        if filename in ['broke_email.txt', 'started_email.txt', 'saving.txt']:
            continue
        
        print("Uploading file ",  filename)
        upload_file("alberta_twitter_data", filename, filename)