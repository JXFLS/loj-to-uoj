# LOJ to UOJ

**暂时只支持 `Linux` 系统**。需要系统支持 `zip` 和 `unzip` 命令（有的发行版可能不自带）。

## 用途

下载 [LOJ](https://loj.ac) 的题面及数据并自动转化为 [UOJ](http://uoj.ac) 格式。

同样适用于所有基于 [UOJ](http://uoj.ac) 搭建的OJ，如 [JXOJ](https://www.jxoj.net)

## 方法

```
python3 main.py {pid} {pid} {pid} ...
```

`{pid}` 代表题号，可一次处理任意道题目。

如需处理 [#1. A + B Problem](https://loj.ac/problem/1) 和 [#2. Hello, World!](https://loj.ac/problem/2) ：

```
python3 main.py 1 2
```

完成后会在 `resource/{pid}` 目录生成 `problem.md` 和 `uoj.zip` ，分别为题面和可以直接上传到 [UOJ](http://uoj.ac) 的数据包。

## TODO

- [ ] 自动上传
- [ ] 支持 `Windows` 系统

## License

MIT