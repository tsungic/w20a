import dbcreds
import mariadb





def getOption():
    print("Select your option")
    print("1) write a new post")
    print("2) See all posts")
    print("3) Enter any other key to exit")
    option = input("Enter your option: ")
    return option





# For option 2 (SELECT query):
# The user should simply be shown all of the posts
# in the DB in some way (printing)



# 1)Open connetion

def showposts():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(
            user=dbcreds.user,
            password=dbcreds.password, 
            host=dbcreds.host,
            port=dbcreds.port, 
            database=dbcreds.database
        )
        # 2) Create cursor
        cursor = conn.cursor()
        # 3) Execute statement
        cursor.execute("SELECT * FROM blog_post")
        # 5) Collect results if needed
        blog_posts = cursor.fetchall()
        print("Total blog post number is: " + str(cursor.rowcount))
        for post in blog_posts:
            print(post)
        # 6) Close cursor
    except Exception as e:
        print(e)     
    finally:
        if(cursor != None): 
            cursor.close()
        if(conn != None):
            # 7) Close connection
            conn.close()







# For option 1 (INSERT query):
# The user should be prompted to enter in their blog post.
# Once they hit enter, it should go and insert their blog 
# post into the DB


def addPost():
    conn = None
    cursor = None
#  1)Open connetion
    try:
        conn = mariadb.connect(
            user=dbcreds.user,
            password=dbcreds.password, 
            host=dbcreds.host,
            port=dbcreds.port, 
            database=dbcreds.database
        )
        # 2) Create cursor
        cursor = conn.cursor()
        blogContent = input("Enter the blog content: ")
        username = input("Enter username: ")
        # 3) Execute statement
        cursor.execute("INSERT INTO blog_post (username, content)VALUES(?, ?)",[username, blogContent])
        # 4) Commit 
        conn.commit()
        if(cursor.rowcount == 1):
            print("Post created!")
        else:
            print("Something went wrong, post not created")
        # 6) Close cursor
    except Exception as e:
        print(e)     
    finally:
        if(cursor != None): 
            cursor.close()
        if(conn != None):
            # 7) Close connection
            conn.close()

option=getOption()
while True:
    if(option =="2"):
        showposts()
    elif(option =="1"):
        addPost()
    else:
        print("Invalid input")
        break
    option=getOption()









