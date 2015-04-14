from tornado_fetcher import Fetcher

# create a fetcher
fetcher=Fetcher(
  user_agent='phantomjs', # user agent
  phantomjs_proxy='http://localhost:12306', # phantomjs url
  pool_size=10, # max httpclient num
  async=False
  )
# fetch html after rendering javascript from url
res = fetcher.phantomjs_fetch('http://www.2tu.cc/Html/GP233.html')
# or execute additional javascript after rendering end, which must be a function
##fetcher.fetch(url, js_script='setTimeout("function(){window.scrollTo(0,100000)}", 1000)')
