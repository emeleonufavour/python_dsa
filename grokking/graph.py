from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_mango_seller(name: str) -> bool:
    """Check for if a name is Mango seller"""
    if (name[-1] == "m"):
        return True
    else:
        return False


def find_mango_seller() -> bool:
    search_queue = deque()
    search_queue += graph["you"]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


result = find_mango_seller()
print(result)
