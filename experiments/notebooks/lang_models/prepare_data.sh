wget https://dumps.wikimedia.org/tewiki/20180401/tewiki-20180401-pages-articles-multistream.xml.bz2
wget https://github.com/attardi/wikiextractor/raw/master/WikiExtractor.py
bzip2 -d tewiki-20180401-pages-articles-multistream.xml.bz2

python WikiExtractor.py -o data/ tewiki-20180401-pages-articles-multistream.xml -s --json
