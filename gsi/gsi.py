import requests

#  longitude , latitude 
def get_max_depth(LON, LAT, key=None):
    url = f"https://suiboumap.gsi.go.jp/shinsuimap/Api/Public/GetMaxDepth?lon={LON}&lat={LAT}"
    response = requests.get(url)
    jsonData = response.json()
    if key:
        if jsonData:
            return jsonData[key]
        else :
            return  None
    
    return jsonData

""" debug """
def get_max_depth_keys():
    return ["Depth", "OfficeCode", "RiverCode", "SubRiverCode",  "CSVScale"]

