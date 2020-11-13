# TP1 DataMining

## 1-File Formart

### 2-

```text
14 exemples
```

### 3-

```text
outlook : sunny|overcast|rainy
temperature : hot|midl|cool
humidity : high|normal
windy : FALSE|TRUE
play : no|yes
```

### 4-

```text
Jitter pour mieux visualiser les points en ajoutant du bruit
PointSize pour régler la taille du point.
```

### 5-

```text
La largeur et la longeur des pétales sont discriminant dans le choix du type de fleur.
```

### 6-

```text
@attribute outlook {sunny, overcast, rainy}
@attribute temperature {hot, mild, cool}
@attribute humidity {high, normal}
@attribute windy {TRUE, FALSE}
@attribute play {yes, no}
```

## 2-Decision Trees

### 2.d-

```text
1737               78.9187 %
```

### 2.e-

```text
La matrice de confusion nous indique 20 faux positif pour Survied=yes.
```

### 2.f-

```text
On a 441 faux négatif.
```

### 2.g-

```text
Precision Survived = no : 1470/(444+1470) = 0.768

```

### 2.h-

```text
Rappel Survived = no : 1470/(1470+20) = 0.9865
```

## 2.2-Evaluation Methods

### 2.2.a-

```text
La méthode par défault est le Cross validation 10 fois
```

### 2.2.b-

```text
Base apprentissage et base test :
on met la meme chose = optimist *training set*
*percentage split* 1/3 pour apprendre et 2/3 pour tester (param pourcentage = apprentissage)
*Supplied test* on a deja une base de test
*Validation coisé* on va faire plusieurs validation et on regroupe ensuite les résultats (param combien de fois on répète le test)
```

## 3 k-Nearest Neighbours

```text
What do the parameters stand for?
- KNN: The number of neighbours to use
- batchSize: the preferred number of instances to process if batch prediction is being performed
- crossValidate
- debug
- distanceWeighting
- doNotCheckCapabilities
- meanSquare: Whetherer the mean squared error is used rather than mean absolute error when doing  cross-validation for regression problem
- nearestNeighbourSearchAlgorithm : default algorithm used
- numDecimalPlaces : The number of decimal places to be used for the output of numbers in the model
-  windowSize : Get the maximum number of instances allowed in the training pool
```

### 3.1 Value of k

#### 3.1.c-

```text
Pondération sur la distance en prenant la classe majoritaire
Plus on prend de voisin moins les voisins pris sont proches donc il faut équilibrer en prenant en compte la distance des voisins
```

#### 3.1.d-

```text
le résultat est équivalent aux arbres de décisions, en mettant
le percantage split a 66% les deux algorithmes obtienne les même matrice de confusion avec un léger avantage pour la méthode des k-voisins.
Et en mettant le cross-validation les deux algorithmes se trompe un peu plus que sans ce qui est étrange mais pas tant que ça
```

#### 3.1.e-

```text
Par défaut c'est la classe majoritaire qui est prise en compte.
Si on fait grandir le nb de voisins (KNN) il faut prendre en compte la distance (distanceWeithing).
```

### 3.2 Normalization

```text
La normalisation est un processus qui est utilisée pour éliminer les données
redondantes et elle garantit la bonne qualité des clusters.
==> améliore l'efficacité des algorithmes de clustering
```

## 4 Clustering

### 4.a-

```text
Cluster 0  : (1857.0) adult  male no
Cluster 1  : (344.0) adult  female yes

(x) = nombres d'éléments dans le cluster.
```

### 4.b-

```text
On peut visualiser les assignments des exemples
```

### 4.c-

```text
nb de fois ou l'algo a recalculer les cluster est et les distances (réajustement des centre et réaffectation des données)
Nombre d'itération c'est le nombre de fois ou on va affiner le centre de cluster
pour approcher la réalité le plus possible
```

## 5 Association

### 5.a-

```text
Generated via weka tool :
 1. biscuits=t frozen foods=t fruit=t total=high 788 ==> bread and cake=t
 2. baking needs=t biscuits=t fruit=t total=high 760 ==> bread and cake=t
 3. baking needs=t frozen foods=t fruit=t total=high 770 ==> bread and cake=t
 4. biscuits=t fruit=t vegetables=t total=high 815 ==> bread and cake=t
 5. party snack foods=t fruit=t total=high 854 ==> bread and cake=t
 6. biscuits=t frozen foods=t vegetables=t total=high 797 ==> bread and cake=t
 7. baking needs=t biscuits=t vegetables=t total=high 772 ==> bread and cake=t
 8. biscuits=t fruit=t total=high 954 ==> bread and cake=t
 9. frozen foods=t fruit=t vegetables=t total=high 834 ==> bread and cake=t
10. frozen foods=t fruit=t total=high 969 ==> bread and cake=t
```

### 5.b-

```text
Les paramètres de la règle d'associations sont :
car : Boolean, if true association rules are determined with the data instead of general association rules

classIndex : index of the class attribute

delta : iteratively decrease support by this factor

doNotCheckCapabilities : Boolean association capabilities checked before associator is built

lowerBoundMinSupport : integer for te lower bound minimum support

metricType : metric type to rank the rules, can be confidence,
lift leverage or conviction

minMetric : minimum metric score

numRules : number of rules to find

outputItemSet : boolean, if set the itemset are output aswell

removeAllMissingCols : noolean, remove all column with missing values

significanceLevel : integer

treatZeroAsMissing : boolean, treat zero as a missing value

upperBoundMinSupport : Boolean

verbose : boolean, enable the verbose mode
```

### 5.c-

```text
rule 10: if "frozen foods" and "fruit" equals "t" and "total" equals "height 969" then "bread" and "cake = t"

support : 877
confidence : 0.91
```
