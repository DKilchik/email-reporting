import json 
import os
from datetime import datetime


class By:
    NAME = "name"
    START_TIMESTAMP = "start_timestamp"
    ID = "id"
    FEATURE = "feature"


class CucumberReport:

    __results = []

    def __init__(self, dir) -> None:
        self.dir = dir
        
        self.data = self.__read()

    def __get_files(self):
        files =  os.listdir(self.dir)
        return [f for f in files if f.endswith(".json")]


    def __read(self):
        reports = self.__get_files()
        for report in reports:
            with open(os.path.join(self.dir, report), "r") as f:
                text = f.read()
            features = json.loads(text)
            for feature in features:
                feature_name = feature["name"]
                for scenario in feature["elements"]:
                    is_failed = False
                    failed_step = None
                    error_message = None
                    test = {"name":scenario["name"], "start_timestamp":self.__to_timestap(scenario["start_timestamp"]),"id":scenario["id"],"feature":feature_name}
                    # getting status of the test and failed step name
                    # handle before
                    for step in scenario["before"]:
                        if step["result"]["status"] == "failed":
                            is_failed = True
                            failed_step = step["name"]
                            error_message = step["result"]["error_message"]
                    # handle after
                    for step in scenario["after"]:
                        if step["result"]["status"] == "failed":
                            is_failed = True
                            failed_step = step["name"]
                            error_message = step["result"]["error_message"]
                    # handle scenario steps
                    for step in scenario["steps"]:
                        if step["result"]["status"] == "failed":
                            is_failed = True
                            failed_step = step["name"]
                            error_message = step["result"]["error_message"]
                    test["is_failed"] = is_failed
                    test["failed_step"] = failed_step
                    test["error_essage"] = error_message
                    self.__results.append(test)
            
    def __to_timestap(self, time: str) -> int:
        dt = datetime.strptime(time.replace("Z", ""), '%Y-%m-%dT%H:%M:%S.%f')
        return int(round(dt.timestamp()))

    def merge(self):
        history = []
        output = []
        for i in range(0, len(self.__results)):
            id = self.__results[i]["id"]
            
            if id in history:
                continue
            
            duplicates = []
            history.append(id)

            for j in range(i, len(self.__results)):
                if self.__results[j]["id"] == id:
                    duplicates.append(self.__results[j])


            output.append(sorted(duplicates, key=lambda d: d['start_timestamp'])[0])
            
        self.__results = output 

    def sort(self,key):
        tmp = sorted(self.__results, key=lambda d: d[key])
        self.results = tmp



    @property
    def get_results(self):
        return self.__results
    
    @property
    def get_total(self):
        return len(self.__results)
    
    @property
    def get_total_features(self):
        features = []
        for test in self.__results:
            if test["feature"] not in features:
                features.append(test["feature"])
        return len(features)


    @property
    def get_failed(self):
        failed = 0
        for test in self.__results:
            if test["is_failed"]:
                failed += 1
        return failed
    

    
