from re import search
import wikipedia
import json
class Wikipedia_info(object):
    def __init__(self,keyword,n):
        self.keyword=keyword
        self.n=n
        self.search_results=wikipedia.search(keyword,results=self.n+5) # extra seach incase of disambiguation or pages not available)
        for x in self.search_results:
            if "(disambiguation)" in x:
                self.search_results.remove(x)


    def output_builder(self):
        self.json_object=[]
        count=0
        for x in self.search_results:
            
            try:
                url=wikipedia.page(x).url
                paragraph=wikipedia.summary(x,sentences=3).strip()
                self.json_object.append({"url":url,"paragraph":paragraph})
            except:
                continue
            if count==self.n-1:
                break
        return json.dumps(self.json_object,indent=2)