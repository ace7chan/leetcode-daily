## 没想出来的题目

## 20201126-maximumGap

可以采用基数排序：根据键值的每位数字来分配桶（即先按照个位进行排序，再按照十位进行排序，依次进行下去），因此对应的时间复杂度=$O(K\times N)$（其中的$K$代表最大的位数）；而空间复杂度为$O(N)$；具体流程如下图所示：

![](png/radixsort.gif)

> 来源于：[1.10 基数排序 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/radix-sort.html)

