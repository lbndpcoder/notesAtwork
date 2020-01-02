

# beta

1. 伯努利实验：

   - 每一次实验是否成功的概率假设为 $P_n$ ，这个概率的数值可以认为是一个先验的概率，在具体的例子当中可以理解为每一次出现一个广告点击的概率为 $P$ ；但是在一个不太了解的或者数据很小的情况下出现的一个类型的广告，我们根据小量的样本得到的点击的频率作为先验并不是很好的选择，如果只有三次的实验数据，而三次都进行了点击，并不能将先验信息即点击的概率定为 100 %；
   - 所以此时的目标是要找到一个合理的分布去拟合每一次点击的概率的大小 $P$ 的分布；

2. beta 分布：可以大概的理解为每一次点击的概率 $P$ 的概率分布。

   - 在一次进行点击 n 次的实验中，假设其中点击的次数为 $x$ 次，那么n次展示 点击 $x$ 次的概率可以表示为：

   - $$
     p(x)=C_n^{x}q^{x}(1-q)^{n-x}
     $$

   - 如果在实验次数和点击次数固定的情况下，那么这个概率可以认为是关于 q 的一个函数；

   - $$
     f(q) = kq^{a}(1-q)^{b}
     $$

   - 也就是说 q 的大小决定了 f 的大小，可以将这个 f 的数值映射到一个固定的（0-1）区间上，并且使得 q 这个变量的每一个取值得到的概率相加为1：

   - $$
     \int_{0}^{1}f(q)dq=\int kq^{a}(1-q)^{b}dq=1
     $$

   - 通过设置 k 的数值就可以得到 q 的概率分布：

   - $$
     k = \frac{1}{\int q^{a}(1-q)^{b}dq}
     $$

   - 所以此时的 $f(q)$ 代表了 q 的概率分布：

   - $$
     B(a+1,b+1) = \int q^{a}(1-q)^{b}dq
     $$

   - 所以得到了beta分布如下：

   - $$
     f(x;\alpha,\beta)=\frac{1}{B(\alpha,\beta)}x^{\alpha-1}(1-x)^{\beta-1}
     $$

3. gamma 函数：

   - 首先要理解beta分布的具体含义，在上面虽然推导了 beta 分布但是并不是很清晰：

   - （1）：假设在一个长度为 1 的桌子上抛一个红色的球，那么这个红色的球落在每一个点上的概率分布可以认为是一个均匀分布服从 $U \sim [0,1]$ 在这个 x 固定为某一个数值的条件下，扔 n 次的白球，其中假设落在红球的左侧的个数 K 为一个随机变量，那么当 $K = k$ 的时候可以得到此时的概率为：

   - $$
     p(K=k|x)=C_{n}^{k}x^{k}(1-x)^{n-k}
     $$

   - 在每一个 x 取值的情况下得到关于 $K=k$ 时候的概率为：

   - $$
     p(K=k)=C_{n}^{k}\int_{0}^{1}x^{k}(1-x)^{n-k}dx
     $$

   - （2）：上面（1）中的抛球过程最终在桌子上上存在着 n+1 个球，如果先将 n+1 个球抛到桌子上，然后选择任意一个作为红球那么 K 这个随机变量的也是一个均匀分布并且每一个值的概率都为 $1/(n+1)$ 。两个实验描述的是同一个事情那么可以知道积分为：

   - $$
     \int_{0}^{1}x^{k}(1-x)^{n-k}dx=\frac{k!(n-k)!}{(n+1)!}
     $$

   - $k = \alpha-1,n-k=\beta-1,\Tau(a)=(a-1)!$  所以得到：

   - $$
     \frac{k!(n-k)!}{(n+1)!} = \frac{(\alpha-1)!(\beta-1)!}{(\alpha+\beta-1)!}
     $$

   - $$
     B(\alpha,\beta)=\int x^{\alpha-1}(1-x)^{\beta-1}dx=\frac{(\alpha-1)!(\beta-1)!}{(\alpha+\beta-1)!}=\frac{\Tau(\alpha)\Tau(\beta)}{\Tau(\alpha+\beta)}
     $$

   - 所以分布也可以为：

   - $$
     f(x;\alpha,\beta)=\frac{\Tau(\alpha+\beta)}{\Tau(\alpha)\Tau(\beta)}x^{\alpha-1}(1-x)^{\beta-1}
     $$

   - 调整不同的 $\alpha,\beta$ 的数值可以调整整个分布；

4. beta 分布与二项分布，beta分布描述的是二项分布中的每一个动作成功的概率：在假设每一次成功的概率为 beta 分布的同时，如果出现 k 次的实验成功那么每一次后验概率分布为：

   - $$
     Beta(\alpha+k, \beta+n-k)
     $$

   - 下面就要证明这个关系：在一次实验中，假设打球的次数为 n 次，其中一共击中的次数为 k 次，假设这个事件为 y ，并且运动员在每一次的击球击中的概率分布为 beta 分布：

   - $$
     p(\theta|\alpha,\beta)\sim Beta(\alpha,\beta)
     $$

   - 那么事件 $y$ 和 概率 $\theta$ 的联合概率分布：

   - $$
     \begin{aligned}
     f(\theta,y|\alpha,\beta) &= f(\theta|\alpha,\beta)p(y|\theta) \\
     &= \frac{1}{B(\alpha,\beta)}\theta^{\alpha-1}(1-\theta)^{\beta-1}C_{n}^{k}\theta^{k}(1-\theta)^{n-k} \\
     &= \frac{1}{B(\alpha,\beta)}C_{n}^{k}\theta^{\alpha+k-1}(1-\theta)^{\beta+n-k-1} \\
     &= \frac{B(\alpha+k,\beta+n-k)}{B(\alpha,\beta)}C_{n}^{k}\frac{1}{B(\alpha+k,\beta+n-k)}\theta^{\alpha+k-1}(1-\theta)^{\beta+n-k-1}
     \end{aligned}
     $$

   - 现在得到的是 y 和 $\theta$ 的联合概率分布函数，现在需要求得是在确定 y 的情况下 能成功击球的概率值，也就是说在知道一定的先验概率分布 $Beta(\alpha,\beta)$ 在确定的一些信息下比如 y 下对击球概率进行更新；

   - $$
     f(\theta,y|\alpha,\beta)=f(\theta|y,\alpha,\beta)f(y|\alpha,\beta)
     $$

   - 可以知道等式左侧的公式，可以知道等式右侧第二个公式就是 y 的边缘概率分布，可以得到：

   - $$
     f(\theta|y,\alpha,\beta)=\frac{1}{B(\alpha+k,\beta+n-k)}\theta^{\alpha+k-1}(1-\theta)^{\beta+n-k-1}
     $$

   - 就是 $B(\alpha+k,\beta+n-k)$ ，那么可以知道在知道事件 y 的条件下，是如何由 $B(\alpha,\beta)$ 到 $B(\alpha+k,\beta+n-k)$ 更新的；