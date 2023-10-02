#### Server
python server.py 5556

#### Client
python client.py 5556 10001
python client.py 5556 10002

#### Notes
pada demo ini akan terdapat satu publisher dengan port 5556 yang akan terus mengirimkan pesan. Pesan yang disampaikan terdiri atas dua hal, yaitu topic dan message. kemudian terdapat 2 subscriber yang akan subscribe kepada publisher. Subscriber ini dapat menentukan topic mana yang akan diambil oleh masing-masing subscriber. Subscriber hanya akan menerima pesan yang topicnya sesuai dengan yang dia minta.

Disini si subscriber akan mengambil 5 data kemudian akan mengambil average dari data yang diambil