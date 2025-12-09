# Intro to Sort
# Author: Coco Woo
# 4 December

import helper_spotify

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort
    Params:
        l - list of numbers to sort
        ascending - True if sorting in ascending order
    Returns:
        a sorted list
    """
    num_items = len(l)

    # starting at the beginning of the list
    for i in range(num_items):
        lowest_num = l[i]
        lowest_index = i

        # check the rest of the list
        for j in range(i + 1, num_items):
            if l[j] < lowest_num:
                lowest_num = l[j]
                lowest_index = j

        # swap the current number with the number at the
        # lowest index
        l[i], l[lowest_index] = l[lowest_index], l[i]

    return l


def sort_songs(songs: list[list[str]], col: int, ascending=False) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""

    # Use Selection Sort to sort songs
    num_songs = len(songs)

    # starting at the begining of the list songs
    for i in range(num_songs):
        # This value is the candidate
        candidate_val = helper_spotify.string_to_num(
            songs[i][col]
        )  # the col the reseacher wanna find and change string to integer
        # This index is the candidate
        candidate_idx = i
        # check the rest of the list
        for j in range(i + 1, num_songs):
            this_songs_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                this_songs_val = helper_spotify.string_to_num(songs[j][col])
                # if ascending
                # is this value lower than candidate

                if this_songs_val < candidate_idx:
                    # mark num as the candidate
                    # mark this index as candidate Loc
                    candidate_val = this_songs_val
                    candidate_idx = j
            # if descending
            else:
                # is this value higher than the candidate
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            # mark this num as the candidate
            # mark thsi index as the candidate
            # swap the candidate with the current index
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


# if __name__ == "__main__":
#     # artist -> col 11
#     taylors_songs = helper_spotify.songs_by_artist(
#         "data/spotify2024.csv", "Taylor Swift"
#     )
#     sorted_ytviews_songs = sort_songs(taylors_songs, 11, ascending=False)

#     for song in sorted_ytviews_songs:
#         print("Taylor's Songs")
#         print("--------------------")
#         print(song[0], "\t", song[11])
# sorted_list = selection_sort([1, 43, 55, -11, 100, 34])

# print(sorted_list)

# Task 1 and task 2
# if __name__ == "__main__":
#     # artist -> col 11
#     sheeran_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
#     sorted_ytviews_songs = sort_songs(sheeran_songs, 11, ascending=False)

#     for song in sorted_ytviews_songs:
#         print("Ed Sheeran")
#         print("--------------------")
#         print(song[0], "\t", song[11])

if __name__ == "__main__":
    # artist -> col 11
    sheeran_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    sorted_ytviews_songs = sort_songs(sheeran_songs, 15, ascending=False)

    for song in sorted_ytviews_songs:
        print("Ed Sheeran")
        print("--------------------")
        print(song[0], "\t", song[15])
