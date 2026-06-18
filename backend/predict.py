from torchvision import transforms
import torch

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def predict_image(image, model, classes):

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        confidence, predicted = torch.max(
            probabilities,
            1
        )

    prediction = classes[predicted.item()]
    confidence = round(confidence.item() * 100, 2)

    print(f"Prediction: {prediction}")
    print(f"Confidence: {confidence}%")

    return {
        "prediction": prediction,
        "confidence": confidence
    }