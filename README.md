# Lock Center

Programa para simular exclusão mútua distribuída baseado em um algoritmo com coordenador (centralizado).


#### Requisitos
* Python3.6+

#### Execução
**Coordenador**
```sh
$ python3 -m coordinator <porta> 
```

**Recurso**
```sh
$ python3 -m resource <porta>
```

**Nodo**
```sh
$ python3 -m node <endereco_coordenador> <endereco_recurso>
```

#### Exemplo

```sh
$ python3 -m coordinator 5666
```
```sh
$ python3 -m resource 5777
```
```sh
$ python3 -m node http://localhost:5666 http://localhost:5777
```

*O recurso compartilhado é o arquivo resource/resource.txt*
