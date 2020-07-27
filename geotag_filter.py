"""
Program for extracting the geotagged tweets from those in a general JSONL-formatted collection.
Outputs the extracted Tweets in JSONL format
"""
import json

def is_geotagged(tweet_json: str) -> bool:
    tweet_dict = json.loads(tweet_json)
    return tweet_json['coordinates'] is not None


if __name__ == "__main__":
    #Parse the arguments
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', metavar='I',
        description="The JSONL tweets file to extract geotagged tweets from")
    args = parser.parse_args()

    with open(args.input) as tweet_jsons:
        #Extract only the tweets that have a coordinate location associated to them
        for tweet_json in tweet_jsons:
            if is_geotagged(tweet_json):
                print(tweet_json)
