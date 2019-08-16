import sys
import os

postname = sys.argv[1]
blogname = "./blog.md"


postfile = open(postname, "r")
blogfile = open(blogname, "a+")

# Create blog file
mdfilename = os.path.splitext(postname)[0] + ".md"
mdfile = open(mdfilename, "w")

istitle = True
for line in postfile:
    if istitle:
        mdfile.write("# " + line + "\n")
        istitle = False
    else:
        mdfile.write(line) 

mdfile.close() 

# Then update title page 
with open(postname, "r") as f:
    title = f.readline().rstrip()
    blogfile.write("* ["+title+"](./"+mdfilename+")\n") 

postfile.close()
blogfile.close()


