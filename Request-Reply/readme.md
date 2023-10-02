#### Server
python server.py 5556
python server.py 5546

#### Client
python client.py 5546 5556

#### Notes
Pada demo ini akan terdapat dua sever dengan port 5556 dan 5546, dan sebuah client yang terhubung kepada kedua server ini. Client nantinya akan mengirimkan request menggunakan zmq, yang kemudian akan dialihkan oleh load balancer ke salah satu diantara server yang terhubung pada client. Pada kasus ini, requestnya akan dibalas oleh masing-masing sever dengan port 5556 dan 5546 secara bergantian.

ketika server dimatikan, client akan diam, akan tetapi tidka crash, namun client akan menunggu hingga servver kembali menyala
Ketika server sudah hidup kembali, client akan lanjut mendapatkan reply dari server