# koreng

| What is this project? |

KorEng_Bot is a KORean to ENGglish Twitter bot to aid your Korean learning. A fun fact: Ko-re means whale in Korean ///🐋🐋🐋 
This individual project started with the PFCH Course at Pratt Institute. Techniques include web scraping, dictionary cleaning, Tweepy, Twitter API, and Amazon AWS Lambda. With a surprising lack of beginner-friendly, non-grammar-centered resources for Korean-English vocabulary and phrase learning, I decided to center my project around creating a bot that would Tweet a random Korean phrase/word once a week. 

You can see the bot on Twitter: https://twitter.com/KorEng_Bot

| Project Components |

The repository consists of four files:

1) korword.py: This python file uses BeautifulSoup to web scape wp-block-table elements and store into Python dictionary from first source

2) ling.py: This python file uses Beautiful Soup to web scrape wp-block-table elements and store into Python dictionary from second source

3) finaldic.py: This python file combines the webscraped dictionaries (.json files) into ONE dataset and cleans up the data for anomalies such as repeated lines, removing scraping of word 'play' from the second source, and inconsistent headers

4) Gitsafe_koreng_tweet.py (***REMINDER HERE THAT FOR AWS LAMBDA USE, YOU WOULD NEED TO SAVE THIS FILE AS `lambda_function.py` before zipping it***): This python file uses Tweepy to create random lines of tweets from the .json file from 3) using Twitter API and wrapped in lambda_handler to be uploaded into Amazon AWS - Lambda, so that the bot does not have to run locally

For AWS Lambda Usage:
  Zip the .json file, Tweepy package, and lambda_function.py file and upload into Amazon Lambda. Test run to see if it works. Once confirmed, Set the interval that you want for the bot. 

| Contact |

Any questions or concerns about the contents of the repository or the bot itself can be directed to me via github OR via https://jiheeyoonprojects.squarespace.com/

|Major Credit*** IMPORTANT MESSAGING|

As I mention in the comment lines in the scraping py files, ALL credits in terms of content of the bot and the research done to create these Korean-English translation and pronunication goes to the websites I am mentioning in my comments and in my project. Please visit their website for more information. 

url="https://koreanly.com/most-common-korean-words/" #this is the first url to the website where I'm collecting Korean words with English definitions and romanticized pronunciation

url="https://ling-app.com/ko/basic-words-and-phrases-in-korean/" #this is the second url to the website where I'm collecting Korean words with English definitions and romanticized pronunciation


