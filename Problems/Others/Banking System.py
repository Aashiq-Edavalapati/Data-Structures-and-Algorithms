class Transaction:
    class Node:
        def __init__(self,source,dest,amt,time_stamp) -> None:
            self.source = source
            self.destination = dest
            self.amount = amt
            self.time_stamp = time_stamp
    
    def __init__(self) -> None:
        self.head = None
        self.transactionsCount = 0


class User:
    class Node:
        def __init__(self,id,kind) -> None:
            self.id = id
            self.kind = kind
    
    def __init__(self) -> None:
        self.firstUser = None
        self.usersCount = 0