from movie import Movie
import fresh_tomatoes


# The main method that will be executed
def main():
    # creation of each Movie object with each individual property
    # The Boss Baby movie: movie title, storyline, poster image and movie
    # trailer
    the_boss_baby = Movie("The Boss Baby",
                          "A new baby's arrival impacts a family, told from "
                          "the point of view of a delightfully unreliable "
                          "narrator -- a wildly imaginative 7-year-old named "
                          "Tim",
                          "http://www.impawards.com/2017/posters/boss_baby_xlg.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=r8kE7rSzfQs")  # NOQA
    # War for the Planet of the Apes movie: movie title, storyline, poster
    # image and movie trailer
    war_for_the_planet_of_the_apes = Movie("War for the Planet of the Apes",
                                           "Caesar (Andy Serkis) and his apes "
                                           "are forced into a deadly conflict "
                                           "with an army of humans led by a "
                                           "ruthless colonel (Harrelson)",
                                           "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/war-for-the-planet-of-the-apes-poster.jpg",  # NOQA
                                           "https://www.youtube.com/watch?v=IjK_h57ixPw")  # NOQA
    # Cars 3 movie: movie title, storyline, poster image and movie trailer
    cars_3 = Movie("Cars 3",
                   "Blindsided by a new generation of blazing-fast cars, the "
                   "legendary Lighting McQueen finds himself pushed out of the"
                   " sport that he loves",
                   "http://www.impawards.com/2017/posters/cars_three_ver3_xlg.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=E4K7JgPJ8-s")  # NOQA
    # The LEGO Batman Movie movie: movie title, storyline, poster image and
    # movie trailer
    the_lego_batman_movie = Movie("The LEGO Batman Movie",
                                  "There are big changes brewing in Gotham, "
                                  "but if Batman (Will Arnett) wants to save "
                                  "the city from the Joker's (Zach "
                                  "Galifianakis) hostile takeover, he may have"
                                  " to drop the lone vigilante thing, try to "
                                  "work with others and maybe, just maybe, "
                                  "learn to lighten up",
                                  "http://www.impawards.com/2017/posters/lego_batman_movie_ver4.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=LHgQSwgKygk")  # NOQA
    # Logan movie: movie title, storyline, poster image and movie trailer
    logan = Movie("Logan",
                  "In the near future, a weary Logan (Hugh Jackman) cares for "
                  "an ailing Professor X (Patrick Stewart) at a remote outpost"
                  "on the Mexican border",
                  "http://www.joblo.com/timthumb.php?src=/posters/images/full/logan-poster-3.jpg&h=600&q=100",  # NOQA
                  "https://www.youtube.com/watch?v=Div0iP65aZo")  # NOQA
    # The Handmaiden movie: movie title, storyline, poster image and movie
    # trailer
    the_handmaiden = Movie("The Handmaiden",
                           "With help from an orphaned pickpocket "
                           "(Kim Tae-ri), a Korean con man (Ha Jung-woo) "
                           "devises an elaborate plot to seduce and bilk a "
                           "Japanese woman (Kim Min-hee) out of her "
                           "inheritance",
                           "http://i.boxasian.com/poster/521/the-handmaiden-korean-japan-2016-0m1b09l4.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=whldChqCsYk")  # NOQA
    # Voyage of Time movie: movie title, storyline, poster image and movie
    # trailer
    voyage_of_time = Movie("Voyage of Time",
                           "Filmmaker Terrence Malick examines the origins of "
                           "the universe, the birth of stars and galaxies, the"
                           "beginning of life on Earth and the evolution of "
                           "diverse species",
                           "http://www.indiewire.com/wp-content/uploads/2016/06/image11.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=uTmZYcCjj9Q")  # NOQA
    # The Greasy Strangler movie: movie title, storyline, poster image and
    # movie trailer
    the_greasy_strangler = Movie("The Greasy Strangler",
                                 "Ronnie (Michael St. Michaels) runs a disco "
                                 "walking tour along with his browbeaten son, "
                                 "Brayden (Sky Elobar). When a sexy, alluring "
                                 "woman named Janet (Elizabeth De Razzo) comes"
                                 " to take the tour, it begins a competition "
                                 "between father and son for her attentions.",
                                 "http://www.impawards.com/2016/posters/greasy_strangler.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=VPl1vcb4hao")  # NOQA
    # Always Shine movie: movie title, storyline, poster image and movie
    # trailer
    always_shine = Movie("Always Shine",
                         "Two women, both actresses with differing degrees of "
                         "success, travel north from Los Angeles to Big Sur "
                         "for a weekend vacation",
                         "http://www.impawards.com/2016/posters/always_shine_xlg.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=wp4blJoV9h4")  # NOQA
    # Shin Godzilla movie: movie title, storyline, poster image and movie
    # trailer
    shin_godzilla = Movie("Shin Godzilla",
                          "Shin Godzilla is a 2016 Japanese monster film "
                          "featuring Godzilla, produced by Toho and Cine "
                          "Bazar and distributed by Toho",
                          "https://images-na.ssl-images-amazon.com/images/I/81T3SbIwHUL._SY550_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=zgyq6YKeIms")  # NOQA
    # Kubo and the Two Strings movie: movie title, storyline, poster image
    # and movie trailer
    kubo_and_the_two_strings = Movie("Kubo and the Two Strings",
                                     "Young Kubo's (Art Parkinson) peaceful "
                                     "existence comes crashing down when he "
                                     "accidentally summons a vengeful spirit "
                                     "from the past",
                                     "http://www.impawards.com/2016/posters/kubo_and_the_two_strings_ver14_xlg.jpg",  # NOQA
                                     "https://www.youtube.com/watch?v=p4-6qJzeb3A")  # NOQA
    # The Alchemist Cookbook movie: movie title, storyline, poster image and
    # movie trailer
    the_alchemist_cookbook = Movie("The Alchemist Cookbook",
                                   "An isolated man (Ty Hickson) lands in hot "
                                   "water when he summons an ancient demon in "
                                   "the backwoods of Grand Rapids, Mich",
                                   "http://www.impawards.com/2016/posters/alchemist_cookbook.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=q42qZ1oKnfw")  # NOQA
    # Rogue One: A Star Wars Story movie: movie title, storyline, poster image
    #  and movie trailer
    rogue_one_a_star_wars_story = Movie("Rogue One: A Star Wars Story",
                                        "Former scientist Galen Erso lives on "
                                        "a farm with his wife and young "
                                        "daughter, Jyn. His peaceful existence"
                                        " comes crashing down when the evil "
                                        "Orson Krennic takes him away from his"
                                        " beloved family",
                                        "http://www.impawards.com/2016/posters/rogue_one_a_star_wars_story_ver17.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=sC9abcLLQpI")  # NOQA
    # Moonlight movie: movie title, storyline, poster image and movie trailer
    moonlight = Movie("Moonlight",
                      "A look at three defining chapters in the life of "
                      "Chiron, a young black man growing up in Miami. His epic"
                      " journey to manhood is guided by the kindness, support "
                      "and love of the community that helps raise him.",
                      "http://film-reviews-and-news.com/sites/default/files/field/image/moonlight-ab-.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=9NJj12tJzqc")  # NOQA
    # 10 Cloverfield Lane movie: movie title, storyline, poster image and
    # movie trailer
    cloverfield_lane = Movie("10 Cloverfield Lane",
                             "After surviving a car accident, Michelle (Mary "
                             "Elizabeth Winstead) wakes up to find herself in "
                             "an underground bunker with two men",
                             "http://www.impawards.com/2016/posters/ten_cloverfield_lane_xlg.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=saHzng8fxL")  # NOQA
    # Wonder Woman movie: movie title, storyline, poster image and movie
    # trailer
    wonder_woman = Movie("Wonder Woman",
                         "Before she was Wonder Woman (Gal Gadot), she was "
                         "Diana, princess of the Amazons, trained to be an "
                         "unconquerable warrior",
                         "http://www.impawards.com/2017/posters/wonder_woman_ver5_xlg.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=5lGoQhFb4NM")  # NOQA

    # add all the objects to an array to be sent to the fresh_tomatoes function
    collection = [the_boss_baby, war_for_the_planet_of_the_apes, cars_3,
                  the_lego_batman_movie, logan, the_handmaiden, voyage_of_time,
                  the_greasy_strangler, always_shine, shin_godzilla,
                  kubo_and_the_two_strings, the_alchemist_cookbook,
                  rogue_one_a_star_wars_story, moonlight, cloverfield_lane,
                  wonder_woman]

    # open the HTML file in the browser with the list of movies created before
    fresh_tomatoes.open_movies_page(collection)


# standard script initialization
if __name__ == '__main__':
    main()
