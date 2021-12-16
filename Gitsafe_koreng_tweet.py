import json
import random
import tweepy

def lambda_handler(event,context): #lambda handler for AWS-Lambda


    consumer_key = "CONSUMER KEY" ##Get from your own Twitter Developer portal
    consumer_secret ="CONSUMER SECRET KEY" ##Get from your own Twitter Developer portal
    access_token="ACCESS TOKEN" ##Get from your own Twitter Developer portal
    access_token_secret="SECRET ACCESS TOKEN" ##Get from your own Twitter Developer portal


    def get_koreng():
        with open('final_dictionary.json') as f: #dictionary file created using webscraping / cleaned - read READ.ME file for more information/ refer to other py files in project
            koreng_json =json.load(f)
            return koreng_json #load json file with dictionary

    def get_random_koreng():
        koreng = get_koreng()
        random_koreng=random.choice(koreng)
        return random_koreng #select random korean-english-pronunciation pairs 

    def create_tweet():
        koreng=get_random_koreng()
        tweet = """
                {} | {} | {}
                """.format("An-nyung! This is the word/phrase of the day: "+ koreng['English'],koreng['Pronunciation'], koreng['Korean']+ " (: TTYL (Najoong-eh Ddo Bwah! )")
        return tweet #tweet the random pair

    def tweet_koreng():

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret) #read Tweepy documentation for more information on getting started with Tweepy re: authentication

        api = tweepy.API(auth)

        test_tweet=create_tweet()
        api.update_status(test_tweet) #create twitter


    def lambda_handler(event, context):
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('it works!')
        }


    if __name__ == "__main__":
        tweet_koreng()


    return {
        'statusCode':200,
        'body':json.dumps('It Worked!!')
     } #Amazon Lambda return if works