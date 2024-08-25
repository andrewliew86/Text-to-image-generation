# Deploying an open source text-to-image model as a serverless endpoint on RunPod via Docker
## Overview
This weekend project demonstrates the basic deployment of Stable Diffusion 2, a powerful open source image generation model, as a serverless endpoint on RunPod via a Docker image. Stable Diffusion 2 enables the generation of high-quality images from text prompts, making it ideal for applications in creative content generation.

## Features include: 
- Serverless Deployment: Deploy Stable Diffusion 2 as a serverless endpoint on RunPod, minimizing infrastructure management.
- Scalable: Automatically scales to handle varying workloads, ensuring optimal performance.
- Cost-Effective: Leverage RunPod's pricing model to minimize costs, paying only for what you use.
- Flexible Integration: Easily integrate the deployed endpoint into various applications and workflows.

## Results
The model was deployed on RunPod via a Docker image created using a RunPod worker template. The model performs well, generating high-quality images based on text prompts such as 'Photograph of colorful coral reefs', 'An old photo of cowboys' and 'Watercolor image of a forest'. Inferencing time averages around 7-8 seconds per request, depending on the complexity of the prompt and the RunPod instance used.

## Notes
- **Python Libraries/Tools**: diffusers, transformers, RunPod SDK
- **Cloud Computing Resources**: RunPod instance with at least 24 GB VRAM (e.g., 1x NVIDIA GeForce RTX 4090 pod instance)
- **Limitations**: Model does not always render humans and animals accurately
- Code was modified from here: https://blog.dreamrunnerlabs.com/deploying-your-preferred-model-on-runpod-serverless-490981fc5b6f



![Stable Diffusion 2-generated images](https://github.com/andrewliew86/Text-to-image-generation/blob/main/photo-collage-wide.png)
**Figure: Photo collage of images generated using Stable Diffusion 2 using text prompts**
