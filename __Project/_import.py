import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load


# Load the latest version
from kagglehub import dataset_load, KaggleDatasetAdapter

df = dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "thedevastator/properties-of-stars-in-our-galaxy",
  "total_stars.csv"
)



print("First 5 records:", df.head())