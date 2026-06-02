# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):

    def sort_order(item : dict):
        return item["rating"]

    return sorted(items , key= sort_order , reverse = True)

