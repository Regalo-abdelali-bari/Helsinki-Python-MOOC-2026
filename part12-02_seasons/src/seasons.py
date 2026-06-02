# Write your solution here:
def sort_by_seasons(items: list):

    def sort_order(item : dict):
        return item["seasons"]

    return sorted(items , key= sort_order)

