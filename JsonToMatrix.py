import json
import numpy as np

class JsonToMatrix():
    
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
    
    def getMatrix(self):
        urls=[]
        with open(self.jsonPath) as f:
            data = json.load(f)
            adjMatrix = np.zeros((len(data), len(data)))
            for page in data:
                urls.append(page['url'])
            for i in range(0, len(urls)):
                for toUrl in data[i]['forward_links']:
                    adjMatrix[urls.index(toUrl)][i] = 1
            return adjMatrix
        

def main():
    converter = JsonToMatrix("./backlinkscraper/"+argv[1])
    matrix = converter.getMatrix()
    print(matrix)
                
if __name__ == "__main__":
    # execute only if run as a script
    main()