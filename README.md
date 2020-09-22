# extract-geotagged-tweets
Program to extract only the geotagged tweets from those contained in a JSONL file

## Program description
```
Program for extracting the geotagged tweets from those in a general JSONL-formatted
collection. Outputs the extracted Tweets in JSONL format

positional arguments:
  I             The JSONL tweets file whence to extract geotagged tweets

optional arguments:
  -h, --help    show this help message and exit
  -s, --strict  Whether to only allow tweets that have a non-null coordinates field (by
                default tweets with a bounding_box field are also allowed through
```

## Program usage
`python geotag_filter.py input.jsonl > output.jsonl`
