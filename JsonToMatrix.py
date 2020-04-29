import json
import numpy as np

class JsonToMatrix():
    
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
        self.urls = []
    
    def getMatrix(self):
        with open(self.jsonPath) as f:
            data = json.load(f)                             
            adjMatrix = np.zeros((len(data), len(data)))            # Square matrix of 0s matching number of urls scraped
            for page in data:
                self.urls.append(page['url'])                       # Fill list with scraped urls
            for i in range(0, len(self.urls)):                      # Iterate over scraped urls
                for toUrl in data[i]['forward_links']:              # Iterate over forward links for each url
                    try:                                            
                        adjMatrix[self.urls.index(toUrl)][i] = 1    # Place 1 in column to which a scraped url links
                    except ValueError:                              # Try:{} except skips parsed but not scraped urls. No all 0 columns
                        pass
            return adjMatrix
    
    def getUrls(self):
        return self.urls

def main():
    converter = JsonToMatrix("./backlinkscraper/adjacency.py")
    matrix = converter.getMatrix()
    print(matrix)
                
if __name__ == "__main__":
    # execute only if run as a script
    main()