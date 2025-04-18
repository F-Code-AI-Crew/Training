import numpy as np
from numpy import typing as npt


# Simulate an image
image: npt.NDArray[np.float64] = np.random.rand(1000, 1000)
print("Raw:\n", image)


# Z-score normalization
mean: float = np.mean(image)
std: float = np.std(image)
normalized_image: npt.NDArray[np.float64] = (image - mean) / std
print("Normalized:\n", normalized_image)


print("Mean after normalization:", np.mean(normalized_image))
print("Std after normalization:", np.std(normalized_image))