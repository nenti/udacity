import datetime

class Cache(dict):
    def __setitem__(self, key, value, *args, **kwargs):
        cur_time = datetime.datetime.now()
        new_value = {
                     "time": cur_time,
                     "value": value
                    }
        super(Cache,self).__setitem__(key, new_value, *args, **kwargs)
        
    def __getitem__(self, key, *args, **kwargs):
        item = super(Cache,self).__getitem__(key, *args, **kwargs)
        return item['value']
    
    def getDelta(self, key):
        item = super(Cache,self).__getitem__(key)
        cur_time = datetime.datetime.now()
        return int(abs((cur_time - item["time"]).total_seconds()))