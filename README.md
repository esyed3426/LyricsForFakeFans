# Lyrics for Fake Fans

## What this monstrosity of a repo is:

This is a repo for a project that allows a user to enter an album name and then the app will send all of the lyrics 
for every song on the album straight to your phone number via SMS so you can secretly have the lyrics out during 
concerts without people noticing hehe.

## Why did I make this: 

I'm going to a Post Malone concert for his Twelve Carat Toothache (what even is that) tour and I don't know most of the songs.
But best believe ya boi gonna be singing like his life depends on it for the vibes. I'm not willing to memorize these songs (some of them are really bad)
so I have to have lyrics on me. To stay undercover, I can't use Spotify or Genius to read the lyrics because then I'll be ousted and 
hanged for the crime of being a fake fan. (Also Im poor and dont have the data to spend searching up lyrics)

## How did I make this: (idk really)

I used python to get into Spotify with its oAuth, then I parsed all that data into an array of custom Track objects 
with numPy, and from there, got around the max SMS character count by splitting the data into separate messages. 