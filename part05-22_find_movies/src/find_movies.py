def find_movies(database: list, search_term: str):
    d = []
    for items in database :
        
        if search_term.lower() in items["name"].lower():
            d.append(items)
        
    return d