_TOMB = object()

class HashTable:
    def __init__(self, capacity: int = 8) -> None:
        assert capacity > 0
        self.capacity = capacity
        self.slots = [None] * capacity
        self.size = 0
        self.tombs = 0
        self.exceed_lvl = 0.7

    def _h(self, key: str) -> int:
        h = 0
        B = 31
        for elem in key:
            h = h * B + ord(elem)
        return h % self.capacity

    def put(self, key: str, value: int) -> None:
        first_tomb = None
        base = self._h(key)
        for j in range(self.capacity):
            i = (base + j) % self.capacity
            cell = self.slots[i]

            if cell is None:
                dest = first_tomb if first_tomb is not None else i
                self.slots[dest] = (key, value)
                self.size += 1
                if (self.size + self.tombs) / self.capacity > self.exceed_lvl:
                    self.rebuild_hash_table()
                return

            if cell is _TOMB:
                if first_tomb is None:
                    first_tomb = i
                continue

            k, _ = cell
            if k == key:
                self.slots[i] = (key, value)
                if (self.size + self.tombs) / self.capacity > self.exceed_lvl:
                    self.rebuild_hash_table()
                return

        if first_tomb is not None:
            self.slots[first_tomb] = (key, value)
            self.size += 1
            if self.size / self.capacity > self.exceed_lvl:
                self.rebuild_hash_table()

    def get(self, key: str) -> int | None:
        base = self._h(key)
        for j in range(self.capacity):
            i = (base + j) % self.capacity
            cell = self.slots[i]

            if cell is None:
                return None
            if cell is _TOMB:
                continue

            k, v = cell
            if k == key:
                return v
        return None

    def delete(self, key: str) -> None:
        base = self._h(key)
        for j in range(self.capacity):
            i = (base + j) % self.capacity
            cell = self.slots[i]

            if cell is None:
                return False
            if cell is _TOMB:
                continue

            k, v = cell
            if k == key:
                self.slots[i] = _TOMB
                self.tombs += 1
                self.size -= 1
                return True
        return False

    def rebuild_hash_table(self):
        old_slots = self.slots
        self.capacity *= 2
        self.tombs = 0
        self.slots = [None] * self.capacity
        self.size = 0
        for cell in old_slots:
            if cell is None or cell is _TOMB:
                continue
            k, v = cell
            self.put(k, v)


def main():
    table = HashTable()
    q = int(input())
    out = []
    for _ in range(q):
        parts = input().split()
        cmd = parts[0]
        if cmd == "put":
            table.put(parts[1], int(parts[2]))
        elif cmd == "get":
            v = table.get(parts[1])
            out.append("Error" if v is None else str(v))
        elif cmd == "del":
            v = table.get(parts[1])
            if v is None:
                out.append("Error")
            else:
                table.delete(parts[1])
                out.append(str(v))
        elif cmd == "size":
            out.append(str(table.size))
    print("\n".join(out))


if __name__ == "__main__":
    main()