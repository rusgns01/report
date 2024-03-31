
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()  # 이미지를 화면에 출력

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)

# 테스트 데이터로 예측해본다. 
y_pred = knn.predict(X_test)

# 정확도를 계산한다. 
scores = metrics.accuracy_score(y_test, y_pred)
print(scores)

# 이미지를 출력하기 위하여 평탄화된 이미지를 다시 8×8 형상으로 만든다. 
plt.imshow(X_test[10].reshape(8,8), cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()  # 이미지를 화면에 출력
y_pred = knn.predict([X_test[10]]) 	# 입력은 항상 2차원 행렬이어야 한다. 
print(y_pred)
