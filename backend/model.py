import torch
import torch.nn as nn
from torchvision import models


NUM_CLASSES = 15

def load_model():

    model = models.vgg16(weights=None)

    layers = []
    in_features = 25088

    for _ in range(3):
        layers.extend([
            nn.Linear(in_features, 256),
            nn.ReLU(),
            nn.BatchNorm1d(256),
            nn.Dropout(0.5)
        ])

        in_features = 256

    layers.append(
        nn.Linear(256, NUM_CLASSES)
    )

    model.classifier = nn.Sequential(*layers)

    model.load_state_dict(
        torch.load(
            "vgg16_plant_diseasefinal.pth",
            map_location="cpu"
        )
    )

    model.eval()

    return model