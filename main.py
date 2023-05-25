import math
import pygame
import random
size = int(input("Liste boyutunu giriniz: "))
pygame.init()

class DrawInformation:
    GREEN = 0, 255, 0
    BLACK = 0, 0, 0
    BEJ = 255,228,196
    BLUE = 0,128,128
    RED = 128,0,0
    arkaplan_rengi = BEJ

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('aeria', 30)
    büyük_punto = pygame.font.SysFont('aeria', 40)

    kenar_bosluk = 100
    yukarı_bosluk = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sıralama Algoritmaları Uygulaması")
        self.liste_olustur(lst)
        self.animasyon_hizi = 1
        self.hamle_sayisi = 0

    def animasyon_hizi_olustur(self, hiz):
        self.animasyon_hizi = max(1, min(hiz, 10))
    def liste_olustur(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.kenar_bosluk) / len(lst))
        self.block_height = math.floor((self.height - self.yukarı_bosluk) / (self.max_val - self.min_val))
        self.start_x = self.kenar_bosluk // 2
    def increment_hamle_sayisi(self):
        self.hamle_sayisi += 1
def draw(cizim_bilgisi, algoirtma_isimi, artan):
    cizim_bilgisi.window.fill(cizim_bilgisi.arkaplan_rengi)

    title = cizim_bilgisi.büyük_punto.render(f"{algoirtma_isimi} - {'Artan' if artan else 'Azalan'}", 1, cizim_bilgisi.BLUE)
    baslik_konumu = title.get_rect(center=(cizim_bilgisi.width/2, 20))
    cizim_bilgisi.window.blit(title, baslik_konumu)

    menü = cizim_bilgisi.FONT.render("R - Sıfırlama | SPACE - Start Sorting | A - Artan | D - Azalan", 1, cizim_bilgisi.RED)
    menü_konumu = menü.get_rect(center=(cizim_bilgisi.width/4, 60))
    cizim_bilgisi.window.blit(menü, menü_konumu)

    sorting = cizim_bilgisi.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort | M - Merge Sort | Q - Quick Sort", 1, cizim_bilgisi.RED)
    sıralama_menüsü_konumu = sorting.get_rect(center=(cizim_bilgisi.width/3.35, 90))
    cizim_bilgisi.window.blit(sorting, sıralama_menüsü_konumu)

    liste_cizdirme(cizim_bilgisi)
    hamle_metni = cizim_bilgisi.FONT.render(f"Hamle Sayısı: {cizim_bilgisi.hamle_sayisi}", 1, cizim_bilgisi.RED)
    hamle_metni_konum = hamle_metni.get_rect(center=(cizim_bilgisi.width / 1.15, 60))
    cizim_bilgisi.window.blit(hamle_metni, hamle_metni_konum)
    pygame.display.update()

    animasyon_hizi = cizim_bilgisi.FONT.render(f"Animasyon Hızı: {cizim_bilgisi.animasyon_hizi}x", 1, cizim_bilgisi.RED)
    animasyon_hizi_rect = animasyon_hizi.get_rect(center=(cizim_bilgisi.width / 1.15, 90))
    cizim_bilgisi.window.blit(animasyon_hizi, animasyon_hizi_rect)

    wait_time = max(5, round(50 / cizim_bilgisi.animasyon_hizi))
    pygame.time.wait(wait_time)

def liste_cizdirme(cizim_bilgisi, renk_durumu={}, clear_bg=False):
    lst = cizim_bilgisi.lst

    if clear_bg:
        clear_react = (
            cizim_bilgisi.kenar_bosluk // 2,
            cizim_bilgisi.yukarı_bosluk,
            cizim_bilgisi.width - cizim_bilgisi.kenar_bosluk,
            cizim_bilgisi.height - cizim_bilgisi.yukarı_bosluk,
        )
        pygame.draw.rect(cizim_bilgisi.window, cizim_bilgisi.arkaplan_rengi, clear_react)

    for i, val in enumerate(lst):
        x = cizim_bilgisi.start_x + i * cizim_bilgisi.block_width
        y = cizim_bilgisi.height - (val - cizim_bilgisi.min_val) * cizim_bilgisi.block_height

        color = cizim_bilgisi.GRADIENTS[i % 3]

        if i in renk_durumu:
            color = renk_durumu[i]

        pygame.draw.rect(cizim_bilgisi.window, color, (x, y, cizim_bilgisi.block_width, cizim_bilgisi.height))

        text = cizim_bilgisi.FONT.render(str(val), 1, cizim_bilgisi.BLACK, cizim_bilgisi.arkaplan_rengi)
        kucuk_metin = pygame.font.SysFont('aeria', 20)
        small_text = kucuk_metin.render(str(val), 1, cizim_bilgisi.BLACK)
        text_rect = small_text.get_rect(center=(x + cizim_bilgisi.block_width // 2, cizim_bilgisi.height - 10))
        cizim_bilgisi.window.blit(small_text, text_rect)

    if clear_bg:
        pygame.display.update()


def bastan_liste_olusturma(n, min_val, max_val):
    lst = []

    for _ in range (n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def bubble_sort(cizim_bilgisi, artan=True):
    lst = cizim_bilgisi.lst
    cizim_bilgisi.hamle_sayisi = 0

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and artan) or (num1 < num2 and not artan):
                cizim_bilgisi.hamle_sayisi += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                liste_cizdirme(cizim_bilgisi, {j: cizim_bilgisi.GREEN, j+1: cizim_bilgisi.RED}, True)
                yield True
                wait_time = max(5, round(10 / cizim_bilgisi.animasyon_hizi))
                pygame.time.wait(wait_time)
    return lst


def insertion_sort(cizim_bilgisi, artan=True):
    lst = cizim_bilgisi.lst
    cizim_bilgisi.hamle_sayisi = 0

    for i in range(1, len(lst)):
        current = lst[i]
        while True:
            artan_siralama = i > 0 and lst[i - 1] > current and artan
            azalan_siralama = i > 0 and lst[i - 1] < current and not artan

            if not artan_siralama and not azalan_siralama:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            cizim_bilgisi.hamle_sayisi += 1
            liste_cizdirme(cizim_bilgisi, {i - 1: cizim_bilgisi.GREEN, i: cizim_bilgisi.RED}, True)
            yield True
            wait_time = max(5, round(10 / cizim_bilgisi.animasyon_hizi))
            pygame.time.wait(wait_time)
    return lst

def selection_sort(cizim_bilgisi, artan=True):
    lst = cizim_bilgisi.lst
    cizim_bilgisi.hamle_sayisi = 0

    for i in range(len(lst)):
        min_idx = i

        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[min_idx] and artan) or (lst[j] > lst[min_idx] and not artan):
                cizim_bilgisi.hamle_sayisi += 1
                min_idx = j

        (lst[i], lst[min_idx]) = (lst[min_idx], lst[i])
        liste_cizdirme(cizim_bilgisi, {min_idx: cizim_bilgisi.GREEN, i: cizim_bilgisi.RED}, True)
        yield True
        wait_time = max(5, round(10 / cizim_bilgisi.animasyon_hizi))
        pygame.time.wait(wait_time)
    return lst


def bölme(cizim_bilgisi,liste, düsük, yuksek, artan=True):
    i = düsük - 1
    pivot = liste[yuksek]

    for j in range(düsük, yuksek):
        cizim_bilgisi.hamle_sayisi += 1
        if (liste[j] <= pivot and artan) or (liste[j] >= pivot and not artan):
            i = i + 1
            liste[i], liste[j] = liste[j], liste[i]

    liste[i + 1], liste[yuksek] = liste[yuksek], liste[i + 1]
    return i + 1

def quick_sort(cizim_bilgisi, liste, düsük, yuksek, artan=True):
    if düsük < yuksek:
        pivot_index = bölme(cizim_bilgisi, liste, düsük, yuksek, artan)
        quick_sort(cizim_bilgisi, liste, düsük, pivot_index - 1, artan)
        quick_sort(cizim_bilgisi, liste, pivot_index + 1, yuksek, artan)
        wait_time = max(5, round(10 / cizim_bilgisi.animasyon_hizi))
        pygame.time.wait(wait_time)

def merge(cizim_bilgisi, liste, left, mid, right, artan=True):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = liste[left + i]

    for j in range(n2):
        R[j] = liste[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        cizim_bilgisi.hamle_sayisi += 1
        if (L[i] <= R[j] and artan) or (L[i] >= R[j] and not artan):
            liste[k] = L[i]
            i += 1
        else:
            liste[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        liste[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        liste[k] = R[j]
        j += 1
        k += 1

def merge_sort(cizim_bilgisi, liste, left, right, artan=True):
    if left < right:
        mid = (left + right) // 2
        merge_sort(cizim_bilgisi, liste, left, mid, artan)
        merge_sort(cizim_bilgisi, liste, mid + 1, right, artan)
        merge(cizim_bilgisi, liste, left, mid, right, artan)
        wait_time = max(5, round(10 / cizim_bilgisi.animasyon_hizi))
        pygame.time.wait(wait_time)



def main():
    run = True
    clock = pygame.time.Clock()
    n = size
    min_val = 0
    max_val = 500
    lst = bastan_liste_olusturma(n, min_val, max_val)
    cizim_bilgisi = DrawInformation(1500, 800, lst)
    sorting = False
    artan = True

    sorting_algorithm = bubble_sort
    sorting_algoirtma_isimi = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(2*cizim_bilgisi.animasyon_hizi)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(cizim_bilgisi, sorting_algoirtma_isimi, artan)
            pygame.display.update()
            clock.tick(cizim_bilgisi.animasyon_hizi)

        if pygame.time.get_ticks() % 100 == 0:
            cizim_bilgisi.hamle_sayisi = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not sorting:
                        cizim_bilgisi.animasyon_hizi += 1
                        cizim_bilgisi.animasyon_hizi_olustur(cizim_bilgisi.animasyon_hizi)
                elif event.key == pygame.K_DOWN:
                    if not sorting:
                        cizim_bilgisi.animasyon_hizi -= 1
                        cizim_bilgisi.animasyon_hizi_olustur(cizim_bilgisi.animasyon_hizi)



            if event.key == pygame.K_r:
                lst = bastan_liste_olusturma(n, min_val, max_val)
                cizim_bilgisi.liste_olustur(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(cizim_bilgisi, artan)
            elif event.key == pygame.K_a and not sorting:
                artan = True
            elif event.key == pygame.K_d and not sorting:
                artan = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algoirtma_isimi = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algoirtma_isimi = "Bubble Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algoirtma_isimi = "Selection Sort"
            elif event.key == pygame.K_m and not sorting:
                cizim_bilgisi.hamle_sayisi = 0
                sorting_algorithm = merge_sort
                sorting_algoirtma_isimi = "Merge Sort"
                lst_copy = list(cizim_bilgisi.lst)
                if artan == True:
                    merge_sort(cizim_bilgisi, lst_copy, 0, len(lst_copy) - 1, artan=True)
                else:
                    merge_sort(cizim_bilgisi, lst_copy, 0, len(lst_copy) - 1, artan=False)
                cizim_bilgisi.liste_olustur(lst_copy)
            elif event.key == pygame.K_q and not sorting:
                cizim_bilgisi.hamle_sayisi = 0
                sorting_algorithm = quick_sort
                sorting_algoirtma_isimi = "Quick Sort"
                lst_copy = list(cizim_bilgisi.lst)
                if artan == True:
                    quick_sort(cizim_bilgisi, lst_copy, 0, len(lst_copy) - 1, artan=True)
                else:
                    quick_sort(cizim_bilgisi, lst_copy, 0, len(lst_copy) - 1, artan=False)
                cizim_bilgisi.liste_olustur(lst_copy)

    pygame.quit()

if __name__ == "__main__":
    main()