# Error 모음 (MAC)

E. 장고 실행시키려는데 파일은 생성되는데, 터미널창에 갑자기 잘되다가 이런 에러가 보임

###### 에러코드

>  Error processing line 1 of /miniconda3/lib/python3.7/site-packages/protobuf-3.6.1-py3.7-nspkg.pth:
>
>   Traceback (most recent call last):
>     File "/miniconda3/lib/python3.7/site.py", line 168, in addpackage
>       exec(line)
>     File "<string>", line 1, in <module>
>     File "<frozen importlib._bootstrap>", line 580, in module_from_spec
>   AttributeError: 'NoneType' object has no attribute 'loader'



해결 1

```shell
conda update   --name base  conda
conda list    --name base  conda
conda update --all
conda install anaconda
```

