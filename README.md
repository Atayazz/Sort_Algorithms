# README

## Sorting Algorithm Nedir?

Sıralama algoritması, bir dizi veya liste içindeki öğeleri belirli bir kurala göre düzenleme işlemidir. Bu algoritma, öğeleri artan veya azalan bir sıraya göre sıralar ve veri setinin organize edilmesi, arama veya  analiz gibi birçok uygulamada önemli bir adımdır.

## Sorting Algorithm Türleri Nelerdir?

1. Bubble Sort: Komşu öğeleri karşılaştırarak sıralama yapar. Yavaş çalışır, büyük veri setleri için etkili değildir.
2. Insertion Sort: Her öğeyi sırasıyla alarak doğru konumuna yerleştirir. Küçük veri setleri için etkilidir, büyük veri setleri için zaman açısından maliyetli olabilir.
3. Selection Sort: En küçük (veya en büyük) öğeyi bulur ve ilk (veya son) pozisyona yerleştirir. Küçük veri setleri için etkilidir, büyük veri setleri için yavaş çalışabilir.
4. Merge Sort: Veri setini sürekli olarak ikiye böler ve alt listeleri birleştirirken sıralar. Büyük veri setleri için etkilidir ve istikrarlı bir algoritmadır.
5. Quick Sort: Pivot öğe seçerek veri setini ikiye böler ve alt listeleri sıralar. Hızlı bir sıralama algoritması olarak kabul edilir ve büyük veri setleri için etkilidir.

## Geliştirme Ortamı

Bu proje, Python programlama dilinde geliştirilmiştir ve aşağıdaki bileşenler kullanılmıştır:

- Python 3.7 veya daha üstü sürümü
- Pygame kütüphanesi (görsel arayüz ve animasyonlar için)

## Nasıl Çalıştırılır ?

Projenin çalıştırılması için aşağıdaki adımları takip edebilirsiniz: 

1. Projenin Klonlanması

   - Terminali veya komut istemcisini açın

   - Projenin klonlanmasını istediğiniz dizine gidin:  

     ```bash
     cd dizin_adi
     ```

     

   - İstenen dizine gittikten sonra 'git clone' komutunu kullanarak github reposunun url'sini yazın: git clone 

     ```
     https://github.com/Atayazz/Sort_Algorithms.git
     ```

     

   - Komutu çalıştırdıktan sonra git depoyu klonlamaya başlayacaktır. Klonlama işlemi tamamlandığında işlemin gerçekleştiriğini bildiren bir mesaj göreceksiniz.

   - Proje dosyanıza yine cd komutunu kullanarak gidebilirsiniz.

     ```
     cd proje_dosyasi_adi
     ```

     

2. Projeyi çalıştırmak için Python 3'ün bilgisayarınıza yüklü olduğundan emin olun. 

3.  Sonraki adımda projenin kök dizinine gidin. 4. Aşağıdaki komutu kullanarak gerekli bağımlılıkları yükleyin: 

   ```bash
   pip install pygame //Bu komut, pygame kütüphanesini yükleyecektir. Bu kütüphane, görsel arayüz ve animasyonlar için kullanılacaktır. 
   ```

4. Ardından aşağıdaki komutu kullanarak uygulamayı başlatın:

   ```bash
   python main.py //Program, her bir sıralama algoritması için bir dizi oluşturacak ve sıralama sonuçlarını ekrana yazdıracaktır.
   ```

   


   
