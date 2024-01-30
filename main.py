
import numpy as np



#normalde iki listeyiçarpabilmek için dışarda boş bir liste ve iki for döngüsü ile bu iki listeni
#bütün elemanlarını gezmek, ardından çarpıp diğer listeye eklemek gerekiyor
#yapıyor olmamız gerekir

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range (0, len(a)):
    ab.append(a[i]*b[i])

###################################
# NUMPY Array'i Oluşturmak
###################################


np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4 , 5]))   #numpy.ndarray çıktısını verir

#0lardan oluşan array
np.zeros(10, dtype=int)   #array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

#rastegele değerlerden array oluşturmak
np.random.randint(0, 10, size=10)   #array([0, 3, 5, 1, 2, 4, 1, 3, 1, 7])

#normal dağılımlı kitlenin ortalaması, argüman, boyut bilgisi girilerek oluşturulur
np.random.normal(10, 4, (3, 4))

#array([[13.16912897,  8.07385602,  5.05595623, 15.11582862],
#       [ 5.50790861,  2.89781314, 10.93371209, 10.76014025],
#       [11.21244241,  4.7640476 ,  5.42851649,  6.48491856]])

#Birçok farklı tipte array oluşturma yöntemi araştırılarak edinilebilir
#Veri bilimi alanında yaygın kullanımda sıfırdan bir array oluşturularak üzerinde çalışılmaz
#Veriler dönüştürülerek arrayler elde edilir ve bunların üzerinde işlemler yapılır.


###################################
# NUMPY Array Özellikleri
###################################

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi


#buraya hiçbir ifade girilmediğinde randint başlangıcını 0 olarak kabul eder
#aralık belirtmek için başladığı ve bittiği noktayı bildirmek gerekir
a = np.random.randint(10, size = 5)
a.ndim   #1
a.shape  #(5,)
a.size   #5
a.dtype  #dtype('int32')



###################################
# Yeniden Şekillendirme (Reshaping)
###################################

#elimizdeki bir numpy array2nin boyutunu değiştirmek istediğimizde  reshape metodunu kullanırız

ar = np.random.randint(1, 10, size=9)
ar.reshape(3,3)

#array([[1, 8, 2],
#       [6, 4, 9],
#      [1, 1, 4]])

ar = np.random.randint(1, 10, size = 10)
ar.reshape(3,3)
#yukarıdaki kısım çalıştırıldığında hata alınır, 10 adet eleman 3X3lük bir matrise çevrilemez



###################################
# Index İşlemleri
###################################

a = np.random.randint(10, size = 10)
a[0] #9
a[0:5] #dilimleme işlemi 5.index dahil edilmez
a[0] = 999 #a[0]'a atama yapıldı

m = np.random.randint(10, size=(3,5))
#array([[5, 6, 1, 2, 1],
#       [7, 6, 7, 7, 0],
#       [7, 8, 6, 2, 7]])


m[0, 0]  #m[satır, sutun] #array ve listeler 0. index ile başlangıç yapar
m[2, 3] = 3.9   #2. satır 3.sütundaki değer 2.9'a eşitlendi
#array([[5, 6, 1, 2, 1],
#       [7, 6, 7, 7, 0],
#       [7, 8, 6, 3, 7]])

#3.9 atanan değerin matriste 3 olduğu görülüyor
#python bize derki; ben tek tipte veri saklarım, diğer indexlerdeki değerleri tipi ne ise
#bana verilen değişkenide ilgili tipe çeviririm

#Python'ın hızlı çalışma prensibinin ilk kuralı

m[:, 0]     #bütün satırları seç, 0. sutunu seç
m[1, :]     #1. satır bütün sutunları seç
m[0:2,0:3]  #satırlardan 0'dan 2'ye kadar git, sutunlardan 0'dan 3'e kadar git



###################################
# Fancy Index
###################################

v = np.arange(0, 30, 3)   #0'dan 30'a kadar 3'er 3'er artacak şekilde array oluştur
#array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27])
v[1]
v[4]

#elimizde binlerce index olduğu durumda fancy index devreye girer

#Fancy index eldeki numpy array'ne bir liste girildiğinde kolay bir şekilde seçim yapmayı sağlar

catch = [1, 2, 3]  #elimizde birden fazla yakalanması gereken indexlerin listesi var

v[catch]          #bu liste matriste yerine koyulduğunda o indexlere karşılık gelen değerleri döndürecektir
                  #array([3, 6, 9])
                  #v numpy array'i, catch ise yakalanması gereken indexlerdir



###################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
###################################

v = np.array([1, 2, 3, 4, 5])
#AMAÇ : array içerisindeki 3'ten küçük olan değerlere erişmek


###################################
# Klasik Döngü ile Çözümü
###################################

ab = []

for i in v:
    if i < 3 :
        ab.append(i)

# ab --> [1, 2]

###################################
# Numpy ile
###################################

#matris içerisinde true false ifadelerinden oluşan bir array'de gönderilebilir

v < 3

#3'ten küçük olan değerleri True, büyük olan değerleri False döndürür
# array([ True,  True, False, False, False])
#***NumPy yüksek Seviyeli İşlemler yapar***

v[v < 3 ]    #array([1, 2])
v[v > 3 ]    #array([4, 5])
v[v != 3 ]   #array([1, 2, 4, 5])
v[v == 3 ]   #array([3])
v[v >= 3 ]   #array([3, 4, 5])

#NumPy üzerinde koşullu eleman işlemleri oldukça kolaydır
#yapılması gereken şey ilgili array'in içerisine koşul ifadesinin girilmesidir
#Arka planda çalışan şey Fancy kavramıdır, True False ifadesi gönderilse bile çalışır


###################################
# Matematiksel İşlemler
###################################


#NumPy'da bun yapmak vektörel işlemler kadar kolaydır

v = np.array([1, 2, 3, 4, 5])
v / 5    #tüm elemanları gezer, 5'e böler ve numPy formunda geri döndürür
#array([0.2, 0.4, 0.6, 0.8, 1. ])

#arka arkaya matematiksel işlemlerde yapılır

v * 5 / 10  #array([0.5, 1. , 1.5, 2. , 2.5])
v ** 2      #array([ 1,  4,  9, 16, 25], dtype=int32)
v - 1       #array([0, 1, 2, 3, 4])

#bu işlemleri methodlar aracılığıylada yapabiliriz

np.subtract(v, 1)    #array([0, 1, 2, 3, 4])
np.add(v, 1)         #array([2, 3, 4, 5, 6])
np.mean(v)           #3.0
np.sum(v)            #15
np.min(v)            #1
np.max(v)            #5
np.var(v)            #2.0


###################################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
###################################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

#Numpy  değişkenlerin katsayılarını belirli bir yapıda gönderirsen bunları çözebilirim der

a = np.array([5,1], [1,3])    #ilk denklemde (birinci değişkenin katsayısı, ikinci değişkenin katsayısı), ikinci denklenmde (birinci değğişkenin katsayısı, ikinci değişkenin katsayısı)
b = np.array([12,10])         #sonuçlar

np.linalg.solve(a,b)


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
#[5 6]
