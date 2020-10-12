import os, time
directory =  'C:\Users\Lina\Desktop\MSBackup\Extra Found Files\JPEG Digital Camera'
dup_dir = 'C:\Users\Lina\Desktop\MSBackup\duplicates'
i = 0
duplicate = set([])

# print("last modified: %s" % time.ctime(mtime))
for filename in os.listdir(directory):
    # if i < 200: 
    curr = os.path.join(directory, filename)
    date = time.ctime(os.path.getmtime(curr))
    size = os.path.getsize(curr)
    if (date, size) in duplicate:
        new_location = os.path.join(dup_dir, filename)
        os.rename(curr, new_location)
        continue
    else:
        duplicate.add((date, size)) 
    # i += 1 
    
    # print("time: %s" % time.ctime(os.path.getmtime(curr)))
    # print("size: %s" % os.path.getsize(curr))
