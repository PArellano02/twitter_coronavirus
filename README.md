# The spread of Coronavirus on Twitter

## What?

This project uses a input data all geotagged tweets from the year 2020 to determine the frequency of different hashtags across different languages, countries, and times during the first year of the pandemic. 


## How?
To do this this I ran the command

```
python3 ./src/map.py --input_path=/data/Twitter\ dataset/geoTwitter20-01-01.zip
```

to run the [map.py](/src/map.py) file. This file goes through a day's worth of geotagged tweets and obtains the creates a couple of files for the given day [geoTwitter20-01-01.zip.lang](/outputs/geoTwitter20-001-01.zip.lang) and [geoTwitter20-01-01.zip.country](/outputs/geoTwitter20-001-01.zip.country). These two files contain the use of the hashtags in each country and language in that particular day.


To get this for all days of the year and not just January 1st, I created the [runmaps.sh](runmamps.sh) file that runs the [maps.py](src/map.py) file on every the zip files corresponding to every day of the year. To run this file I used the command

```
nohup sh runmaps.sh &
```

After running this command I closed my computer, went to sleep and let the program run in the background.


After obtaining all the files for each day.  The commands

```
python3 ./src/reduce.py --input_paths outputs/geoTwitter20-*.lang --output_path=reduced.lang
```
and 

```
python3 ./src/reduce.py --input_paths outputs/geoTwitter20-*.country --output_path=reduced.country
```
consolidated the information from the outputs folder into two files  [reduced.lang](reduced.lang)  [reduced.country](reduced.country). The  [visualize.py](src/visualize.py) file uses matplotlibs to graph the distribution of the use of a given hashtag across the top 10 most frequent countries or languages depending on the input file. 


Bellow are the graphs and their corresponding commands

## Graphs

```
python3 ./src/visualize.py --input_path=reduced.lang --key='#coronavirus'
```

![#coronavirus across languages](https://raw.githubusercontent.com/PArellano02/twitter_coronavirus/master/%23coronavirus_lang.png)

```
python3 ./src/visualize.py --input_path=reduced.country --key='#coronavirus'
```
![#coronavirus across countries](https://raw.githubusercontent.com/PArellano02/twitter_coronavirus/master/%23coronavirus_country.png)

```
python3 ./src/visualize.py --input_path=reduced.lang --key='##코로나바이러스'
```

![#코로나바이러스 across lamnguages](https://raw.githubusercontent.com/PArellano02/twitter_coronavirus/master/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_lang.png)

```
python3 ./src/visualize.py --input_path=reduced.country --key='##코로나바이러스'
```

![#코로나바이러스 across countries](https://raw.githubusercontent.com/PArellano02/twitter_coronavirus/master/%23%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_country.png)


## Altermnative_reduce.py 

Finally, I created another file which takes as input a list of hashtags, loops over each file on the outputs folder a graph containing the use of those particular hashtags across all of 2020.

Below are the graphs and their corresponding commands

```
python3 ./alternative_reduce.py --input_hashtags '#covid19' '#virus'
```

![#covid19 #virus](https://raw.githubusercontent.com/PArellano02/twitter_coronavirus/master/%5B'%23covid19'%2C%20'%23virus'%5D_.png)

```
python3 ./alternative_reduce.py --input_hashtags '#hospital' '#doctor'
```

![#hospital #doctor](https://raw.githubusercontent.com/PArellano02/twitter_coronavirus/master/%5B'%23hospital'%2C%20'%23doctor'%5D_.png)
