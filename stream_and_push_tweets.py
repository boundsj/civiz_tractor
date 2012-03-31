from publisher import Publisher
from tweetstreamwrapper.tweetils import Tweetils  
from user_info import user_info

pub = Publisher()
app = Tweetils(None, pub, user_info) 
app.start_stream();
