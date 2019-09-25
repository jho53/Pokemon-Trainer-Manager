from blank_stats import BlankStats


class blankManager:
    def __init__(self):
        self._blanktitties = []

    def add(self, blank):
        pass

    def get(self, id):
        pass

    def get_all(self):
        return self._blanktitties

    def get_all_by_type(self, type):
        return self._blanktitties

    def update(self, blank):
        pass

    def delete(self, id):
        pass

    def get_stats(self):
        BlankStats()
