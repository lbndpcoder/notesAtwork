[TOC]

# git

## 本地操作

git中有三个区：

- 工作区 W ；
- 缓存区 C ；
- 本地仓库 R ；

我们平时的代码都存储在工作区，通过：

```shell
git add fileName
```

将文件的更改放在缓存区，然后利用 

```shell
git commit -m "change message"
```

将文件的更改放在 R 中，这样可以将 R 的文件直接传到 远程仓库当中；

## 远程库

可以在github上建立自己的远程库，然后通过：

```shell
git remote add origin git@github.com:michaelliao/learngit.git
```

将本地的仓库 R 和远程的仓库相关联起来；然后可以将本地的master内容以及master分支上的内容都直接push到远程仓库中去：

```shell
git push -u origin master
```

第一次的时候可能需要这个push，但是之后只需要：

```shell
$ git push origin master
```

上面讲的是将本地库push到远程，我们也可以在远程创建一个库，然后再：

```shell
git clone git@github.com:michaelliao/gitskills.git
```

将远程库的内容直接clone到本地，然后就可以在本地创建了一个和远程库一样的本地文件用于开发了。远程仓库的对应的名字是origin，可以利用查看远程的名字：

```shell
git remote 
origin
```

一般的时候远程的非 master 分支并不能被 clone 到本地，所以需要单独的将远程的分支比如 dev 分支弄到本地：

```shell
git checkout -b dev origin/dev
```

如果你要更改的分支已经被更改了，需要将该分支最新的代码 git pull 到本地，但是可能会出问题，因为没有关联到本地的dev分支和远程的 origin/dev 分支，所以将本地的和远程的关联在一起：

```shell
git branch --set-upstream-to=origin/dev dev
```

1. 首先，可以试图用`git push origin <branch_name>`推送自己的修改；
2. 如果没法推送，说明本地的这个 branch 比较旧需要重新的`git pull`;
3. `git pull` 也失败并出现no tracking information ❌ 说明需要将本地与远程的分支创建链接；
4. 再`git pull ` 然后再放在一起；

## 分支

在本地创建分支可以和本地的master合并，也可以在本地创建分支然后在远程也同样创建对应的分支。当本地的分支并不存在于远程的时候需要在远程保持一个相同的分支。本地创建分支如下：

```shell
git checkout -b dev
```

相当于

```shell
git branch dev
git checkout dev
```



