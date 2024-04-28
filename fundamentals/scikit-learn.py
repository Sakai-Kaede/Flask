import sklearn

from sklearn.datasets import load_breast_cancer
brest_cancer = load_breast_cancer()
type(brest_cancer)

x = brest_cancer['data']
t = brest_cancer['target']

type(x), x.shape

x[:3]

t[:3]
# 実行結果
# array([0, 0, 0])

len(t[t == 0]), len(t[t == 1])

# 議論の対象としたいカテゴリーを1にする
import numpy as np
t = np.where(t==0,1,0)
t[:3]

# パラメータのチューニングを行う

# モデルを保存する