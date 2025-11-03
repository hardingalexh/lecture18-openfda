import requests

BASE_URL = "https://api.fda.gov/drug/event.json?"
print(BASE_URL)
# request_url = "https://api.fda.gov/drug/event.json?count=patient.drug.drugindication.exact&limit=50"

# response = requests.get(request_url)
# data = response.json()
# breakpoint()


def print_results(results):
    for result in results:
        print(result)


def make_string(params):
    search_list = [f"{k}:{v}" for k, v in params.items()]
    search_str = "+".join(search_list)
    return search_str


## query parameters
## indication of arrythmia
## medication of metoprolol
## reaction of bradycardia

search_params = {
    "patient.drug.drugindication": "arrythmia",
    "patient.drug.activesubstance.activesubstancename.exact": "metoprolol",
    "patient.reaction.reactionmeddrapt.exact": "bradycardia",
}


final_output = []
total_results = 0
# skip = 0
limit = 1000

while len(final_output) <= total_results:
    req_url = f"{BASE_URL}search={make_string(search_params)}&skip={len(final_output)}&limit={limit}"
    ## sanity check
    print(f"Loop ran with skip:{len(final_output)} limit:{limit}")
    print("sending query to", req_url)
    response = requests.get(req_url)
    data = response.json()
    ## set our total
    total = data.get("meta").get("results").get("total")
    total_results = total

    ##
    print("Total is now", total)

    results = data.get("results")
    print(f"Received {len(results)} results")
    final_output = final_output + results

print("All done!")
