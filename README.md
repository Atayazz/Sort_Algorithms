# README

## Sorting Algoritm Nedir?

Sıralama algoritması, bir dizi veya liste içindeki öğeleri belirli bir kurala göre düzenleme işlemidir. Bu algoritma, öğeleri artan veya azalan bir sıraya göre sıralar ve veri setinin organize edilmesi, arama veya  analiz gibi birçok uygulamada önemli bir adımdır.

## Sort Algoritm Türleri Nelerdir?

1. Bubble Sort: Bu algoritma, komşu öğeleri karşılaştırarak sıralama yapar. Her adımda, bir öğe diğerinden daha büyükse yer değiştirilir. Küçük öğeler yavaş yavaş "yüzeye çıkar" ve doğru konumlarına yerleşir. Ancak bu algoritma, büyük veri setleri için etkili değildir çünkü yavaş çalışır.
2. Insertion Sort: Bu algoritma, veri setindeki her öğeyi sırasıyla alır ve doğru konumuna yerleştirir. Her adımda, bir öğe, sıralı bölgedeki uygun konuma yerleştirilir. İnsanların kartları sıralarken kullandıkları yönteme benzer. İnsertion Sort, küçük veri setleri için etkilidir, ancak büyük veri setleri için zaman açısından maliyetli olabilir.
3. Selection Sort: Bu algoritma, veri setindeki en küçük (veya en büyük) öğeyi bulur ve ilk (veya son) pozisyona yerleştirir. Daha sonra, sıralanmış bölgedeki bir sonraki en küçük (veya en büyük) öğeyi bulur ve ikinci pozisyona yerleştirir. Bu adımlar, tüm veri seti sıralanana kadar tekrarlanır. Selection Sort, küçük veri setleri için etkilidir, ancak büyük veri setleri için yavaş çalışabilir.
4. Merge Sort: Bu algoritma, sıralanmış alt listeler oluşturarak veri setini sürekli olarak ikiye böler. Daha sonra, alt listeler birleştirilirken sıralanır. Bu aşama, alt listelerin birleştirilmesi sırasında karşılaştırmalar yaparak gerçekleştirilir. Merge Sort, büyük veri setleri için etkilidir ve istikrarlı bir algoritmadır.
5. Quick Sort: Bu algoritma, bir "pivot" öğe seçerek veri setini ikiye böler. Daha sonra, pivot öğenin solunda küçük, sağında ise büyük öğeler yer alacak şekilde sıralama yapılır. Bu adımlar, alt listelerin sıralanması tamamlanana kadar tekrarlanır. Quick Sort, genellikle hızlı bir sıralama algoritması olarak kabul edilir ve büyük veri setleri için etkilidir.

Nasıl Çalıştırılır ?

Projenin çalıştırılması için aşağıdaki adımları takip edebilirsiniz: 

1. Projenin Klonlanması
   - Terminali veya komut istemcisini açın
   - Projenin klonlanmasını istediğiniz dizine gidin:  
         cd dizin_adi
     
   - İstenen dizine gittikten sonra 'git clone' komutunu kullanarak github reposunun url'sini yazın: git clone 
         https://github.com/Atayazz/Sort_Algorithms.git
     
   - Komutu çalıştırdıktan sonra git depoyu klonlamaya başlayacaktır. Klonlama işlemi tamamlandığında işlemin gerçekleştiriğini bildiren bir mesaj göreceksiniz.
   - Proje dosyanıza yine cd komutunu kullanarak gidebilirsiniz.
         cd proje_dosyasi_adi
     
2. Projeyi çalıştırmak için Python 3'ün bilgisayarınıza yüklü olduğundan emin olun. 
3.  Sonraki adımda projenin kök dizinine gidin. 4. Aşağıdaki komutu kullanarak gerekli bağımlılıkları yükleyin: 
       pip install pygame //Bu komut, pygame kütüphanesini yükleyecektir. Bu kütüphane, görsel arayüz ve animasyonlar için kullanılacaktır. 
4. Ardından aşağıdaki komutu kullanarak uygulamayı başlatın:
       python main.py //Program, her bir sıralama algoritması için bir dizi oluşturacak ve sıralama sonuçlarını ekrana yazdıracaktır.
   
