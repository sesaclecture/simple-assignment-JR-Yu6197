anime = ["Naruto", "One Piece", "Attack on Titan", "My Hero Academia", "Demon Slayer"]

print(anime)

target_anime = input("Enter the name of the anime you want to find: ")
index = anime.index(target_anime)

print(f"{anime[index]} is at index {index}")

new_anime = input("Enter the name of a new anime to insert:")
insert_pos = int(input("At which index to insert it? "))
anime.insert(insert_pos, new_anime)

remove_anime = input("Enter a anime to remove: ")
anime.remove(remove_anime)

print(anime)