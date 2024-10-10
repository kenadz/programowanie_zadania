class Zadanie:
    def __init__(self, sasiedzi):
        self.koneksje = [[] for _ in range(sasiedzi + 1)]

    def dodaj_koneksje(self, a, b):
        self.koneksje[a].append(b)
        self.koneksje[b].append(a)

    def sprawdz_koneksje(self, s1, s2):
        return s2 in self.koneksje[s1]

def main():
    sasiedzi, koneksje = map(int, input().split())
    zadanie = Zadanie(sasiedzi)

    for _ in range(koneksje):
        a, b = map(int, input().split())
        zadanie.dodaj_koneksje(a, b)

    zapytania = int(input())

    odpowiedzi = []

    for _ in range(zapytania):
        s1, s2 = map(int, input().split())
        if zadanie.sprawdz_koneksje(s1, s2):
            odpowiedzi.append("TAK")
        else:
            odpowiedzi.append("NIE")

    print("\n".join(odpowiedzi))

if __name__ == "__main__":
    main()
