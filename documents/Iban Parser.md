# Iban Parser Özelliği Nedir Ne İşe Yarar?


IBAN Para transferi için kullanılan küresel bir sistemdir bu nedenle bu sistem içerisinde belirlir tanımlayıcı unsurlar bulunmaktadır. Iban parser modülü de bu tanımlayıcı bilgileri Iban içerisinden çıkartarak insanların anlayabileceği bir formata getirmektedir.


IBAN içerisinde gelen bazı bilgiler:

- Ülke Kodu 
- Sepa Desteği
- Hesap Kontrolü Desteği
- Şube Kontrolü 
- Banka Kodu 
- Hesap Numarası
- Şube Kodu
- Müşteri Numarası
- Hesap Ek Numrası


Bu bilgilerden bazıları yetkili makamlar hariç bizim işimize yaramasada banka adı ,şube kodu, Müşteri numarası işimize yarar farklı ibanların aynı müşterinin mi olduğuna, şube kodu ile kişinin yaşadığı tahmini bölge tespit edilebilmektedir. Bu nedenle dolandırıcılık vs gibi olaylarda bu modülden yararlanmak zamandan kazandırır.