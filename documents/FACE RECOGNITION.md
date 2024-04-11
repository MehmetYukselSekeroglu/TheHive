# TheHive / Yüz Tanımlama ( Recognition )


## Kullanılan kütüphaneler ve sistemler:
    - InsightFace   : Yüz tespiti için kullanılan kütüphane
    - numpy         : Benzerlik hesaplamaları için
    - PostgreSQL    : Yüksek hacimli veriyi saklamak için


Yüz tanıma sisteminin temelini [InsightFace](https://github.com/deepinsight/insightface) açık kaynaklı kütüphanesi oluşturur. Gerek güncel olması gerek ön tanımlı kullanmış olduğu modellerin doğruluğu sayesinde diğer sistemlerden daha verimli çalışmaktadır kanaatimizce.



## Nasıl çalışır:
InsightFace kütüpahnesi ile resimdeki yüzleri tespit ederek yüzler için önemli olan noktaları PostgreSQL üzerinde BLOB (Binary Large Object ) olarak saklıyoruz bu sayede numpy dizilerinin bozulması engelleniyor veritabanı içerisinde Resmin kendisi, 2d olarak yüzün yer işaretleri, gömme bilgileri ( hesaplama için kullanılan vektörler) ve eklenme tarihleri saklanır. Sistem üzerinde bir arama yapılacağı zaman kaynak resimdeki vektörler alınarak veritabanında saklanan TÜM vektörler ile tek tek numpy ile karşılaştırılır karşılaştırma sonucunda `kosinüs` benzerliği oranları elde edilir bu oranlardan güncel olarak en yüksek 10 adeti resmin id'si ile bir python sözlüğü içerisinde saklanır ve tüm veritabanı araması bittiği zaman sözlük içerisindeki en yüksek benzerlik değeri veritabanından seçilerek ekrana getirilir. Sistem eşik değerin üstündeki ilk sonucu değil en yüksek oranı getirecek şekilde ayarlıdır bu nedenle yüksek oranda doğruluk sağlamaktadır. Şuanki veritabanı yapısı ve arama modeli nedeniyle çok geniş bir veritabanına sahipseniz canlı tanıma için kullanmaya elverişli değildir (100.000+ resim örneğin).


## Benzerlik hesaplaması:
Benzerliğin hesaplanması için yüz vektörlerinin direk olarak numpy üzerinden kosinüs benzerliği hesaplanır, benzerlik hesaplamasında herhangi bir model kullanılmaz bu nedenle aynı kişinin 2 resmi üzerinde bile bazen %100 vermez ama farklı kişiler içinde bi okadar hassaslık sağlar. 



Örnek olarak ( Doğrulama sisteminden bir ekran görüntüsü ):


<img src="./../img/FaceVerificationFarkliKisiler.png"/>



## Yeni veritabanları ve servisler oluşturulabilirmi?

Şuan için grafiksel arayüz üzerinden ayrı ayrı veritabanları oluşturma ve kullanma desteği eklenmemiştir. Yakın zamanda bu destek eklenecektir.









<br>
<br>
<br>
Son Düzenleme: 19.02.2024














