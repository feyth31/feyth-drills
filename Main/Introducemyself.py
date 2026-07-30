def get_profile():
    profile = {
        "pet": "🐶 🐶 🐶",
        "name": "Angel Faith P. Tuante",
        "nickname": "Gel, Peyt",
        "birthday": "01/31/2005",
        "address": "Napnapan Sur, Tigbauan, Iloilo",
        "favorite_song": "Your Song - Parokya ni Edgar",
        "motivation": "My family, my lover, and my dreams motivate me to keep studying and push myself to do my best.",
        "support": "Understanding teacher, clear instructions, and enough time to complete activities would make this semester more comfortable."
    }
    return profile


def display_profile(profile):
    print(profile["pet"])
    print()
    print(f"Name       : {profile['name']} ({profile['nickname']})")
    print(f"Birthday   : {profile['birthday']}")
    print(f"Address    : {profile['address']}")
    print(f"Fav Song   : {profile['favorite_song']}")
    print(f"Motivation : {profile['motivation']}")
    print(f"Support    : {profile['support']}")


profile = get_profile()
display_profile(profile)