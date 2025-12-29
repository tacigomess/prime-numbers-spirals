# prime-numbers-spirals


This repository corresponds to **Article 0** of a broader research project on geometric representations of prime numbers.

The focus here is the **historical and geometric construction of a polar spiral embedding of prime numbers**, prior to the introduction of halo-based density analysis.


Paper: Geometric Regularity in the Distribution of Prime Numbers on Polar Spirals

[Document](https://docs.google.com/document/d/11sa36fFxUokgMzjVDVdVdCFUfjkujBwkSI9eKV9YrwQ/edit?tab=t.0)

## How to Run

0. (1 time only): Create your env
```bash
   python3 -m venv names_env
```

1. Activate your env
```bash
   source names_env/bin/activate
```

2. git clone
```bash
git clone git@github.com:tacigomess/prime-numbers-spirals.git
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Code
   
1. [Only visual to generate graphics]
- `spiral_all_numbers.py`: Shows the spiral with all natural numbers up to [n = 1000] with the prime numbers highlighted in red.
![Image generated](Spiral_Natural_Numbers_with_Primes.png)

- `prime_spiral.py`: Shows the spiral with only prime numbers up to [n = 1000].
![Image generated](Prime_spiral.png)

- `prime_spiral_with_parallel_arc_connections.py`: Shows the spiral with parallel Arcs - prime numbers up to [n = 1000].
![Image generated](Prime_parallel_arcs.png)

2. [Distance Calculation]
- `prime_spiral_generate_csv.py`: Generate a dataset with distances from 10.000 numbers
- `prime_spiral_distances_columns.csv`: Dataset (.csv) with distances from 10.000 numbers
- `prime_spiral_calculate_metrics_from_csv.py`: Calculate the metrics with all distances
 

3. [Random Forest Classifier] - [Classifier and Dataset]
- Generated Dataset to Random Forest Classifier
- `features_names.txt`: Names/description of all features in the database for the Random Forest Classifier
- `prime_spiral_features_dataset.csv`: Dataset with 10.000 numbers

- code: `dataset_generator_csv_random_forest.py` to generate: `prime_spiral_features_dataset.csv`

This dataset included geometric and local context features for each number from 2 to 10,000.
-  Features used for classification:
-  n,x,y,r,theta,is_prime,prime_density,avg_prime_dist
-  x, y: Cartesian coordinates in the spiral
-  r, θ: Polar coordinates (radius and angle)
-  Prime density: Number of primes within a 10-unit radius
-  Average distance to nearby primes
-  Target variable: Whether the number is prime (1) or not (0)
  
Training the classifier: `train_and_analyze_random_forest.py`
![Confusion Matrix](confusion_matrix.png)
    
## Author
- TAGC - tacigomess@me.com
