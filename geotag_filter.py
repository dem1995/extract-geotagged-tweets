"""
Program for extracting the geotagged tweets from those in a general JSONL-formatted collection.
Outputs the extracted Tweets in JSONL format
"""
import json

def is_geotagged(tweet_json: str, bounding_box_is_fine: bool=True) -> bool:
    """
    Takes in a tweets JSON string and outputs whether the underlying tweet is geotagged.
    Arguments:
        tweet-json: str - the json string whose tweet is to be tested
    Returns:
        True if the underlying tweet in the provided string is geotagged (has a bounding box
                or coordinates field); false, otherwise.
    """
    tweet_dict = json.loads(tweet_json)
    if bounding_box_is_fine:
        is_geotagged_result = (
                                tweet_dict.has_key('bounding_box') and tweet_dict['bounding_box'] is not None 
                                or tweet_dict.has_key('coordinates') and tweet_dict['coordinates'] is not None
                              )
    else:
        is_geotagged_result = tweet_dict.has_key('coordinates') and tweet_dict['coordinates'] is not None
    return is_geotagged_result


if __name__ == "__main__":
    #Parse the arguments
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', metavar='I',
        help="The JSONL tweets file whence to extract geotagged tweets")
    parser.add_argument('-s', '--strict', action='store_true',
        help="Whether to only allow tweets that have a non-null coordinates field (by default tweets with a bounding_box field are also allowed through")
    args = parser.parse_args()

    with open(args.input) as tweet_jsons:
        #Extract only the tweets that have a coordinate location associated to them
        for tweet_json in tweet_jsons:
            try:
                if is_geotagged(tweet_json):
                    print(tweet_json, end="") #Newlines already conclude tweet strings themselves
            except ValueError:
                pass
