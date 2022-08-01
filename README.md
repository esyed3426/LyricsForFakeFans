# Lyrics for Fake Fans

## What this monstrosity of a repo is

This is a repo for a project that allows a user to enter an album name and then the app will send all of the lyrics 
for every song on the album straight to your phone number via SMS so you can secretly have the lyrics out during 
concerts without people noticing hehe. Just run the main file and enter an album name before you leave, and when you
get to the concert you have everything you need to stay undercover in your pocket.

## Why did I made it

I'm going to a Post Malone concert for his Twelve Carat Toothache (what even is that) tour and I don't know most of the songs.
But best believe ya boi gonna be singing like his life depends on it for the vibes. I'm not willing to memorize these songs (some of them are really bad)
so I have to have lyrics on me. To stay undercover, I can't use Spotify or Genius to read the lyrics because then I'll be ousted and 
hanged for the crime of being a fake fan. (Also Im poor and dont have the data to spend searching up lyrics) 

### I am actually going to be using this, once the concert's over Ill send a picture

## How I made it (idk really)

I used python to get albums from Spotify based on user input, then I stored all the tracks in the album into an array of custom 
abstract objects, and when adding them in, I got the lyrics for them using the Genius API and did some error handling there in the case
of None responses. I then parsed the lyrics for each song into segments of max 1550 to get around that max SMS character count of 1600. 
After that, I sent each songs lyrics to my phone number using the Twilio API. Bing bada boom mr worldwide as i step in the room, dale
