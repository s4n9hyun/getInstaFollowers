import instaloader

L = instaloader.Instaloader()

USER = "dawara0058@gmail.com"
PROFILE = "hufs_dsm"

L.interactive_login(USER) 
profile = instaloader.Profile.from_username(L.context, PROFILE)

followers = set(profile.get_followers())

print("Storing followers into file.")
with open("followers.txt", 'w') as f:
    for follower in followers:
        s = 'www.instagram.com/' + follower.username
        print(s, file=f)