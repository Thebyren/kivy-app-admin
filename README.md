# presentacion

[![Video de YouTube](https://img.youtube.com/vi/edcPNME7d5s/0.jpg)](https://youtu.be/edcPNME7d5s)

## requerimientos

sistema macOS, linux o windows con Python >= 3.7

### instalacion de modulos necesarios

```sh
pip install -r requirements.txt
```

### uso

```sh
python3 main.py
```

#### apk instalable para telefonos de arquitectura arm64-v8a, armeabi-v7a

[Descarga el instalable aqui](./bin/totalControl-0.2-arm64-v8a_armeabi-v7a-debug.apk?download=true)

## instalacion android manual

 se requiere buildozer instalado, tambien un sistema tipo unix. ademas editar buildozer.spec y editar la arquitectura para el dispositivo requerido

```sh
git clone https://github.com/Thebyren/kivy-app-admin

pip install buildozer cython git cmake
buildozer -v android debug
```
