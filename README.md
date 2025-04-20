# Azure-AI-Projects

---

# 🤖 ITI109 AI-Powered Application Development Project

This project is part of the **Specialist Diploma in Applied Artificial Intelligence** coursework for the **ITI109: Application Development Using AI Services** module. It showcases the use of Microsoft Azure AI services to solve real-world business problems using **computer vision** and **natural language processing (NLP)**.

## 📚 Project Overview

The assignment is divided into **two main sections**:

1. **Section A: Computer Vision for Automated Fruit Classification**
2. **Section B: NLP-Based Multilingual Chatbot Development**

Both sections use Microsoft’s AI tools such as **Azure Custom Vision**, **Azure AI Language Studio**, and **Azure Translator** to build intelligent solutions.

---

## 🧠 Section A: Automated Fruit Classification Using Computer Vision

### 🏢 Business Context

Company ABC seeks to reduce labor costs and increase efficiency by automating the classification of fruits using AI, given challenges such as variations in color, shape, and lighting.

### ✅ Solution Features

- Built using **Azure Vision Studio**, **Custom Vision**, and **Azure Machine Learning AutoML**
- Used labeled images to train a **Custom Vision model**
- Exported model in **COCO (Common Objects in Context)** format
- Integrated the model into a Python app for inference

### 🧩 Technologies Used

- **Azure Custom Vision** – For building and training custom image classification models.
- **Azure ML AutoML** – For automating model selection and evaluation.
- **COCO format annotations** – For structured labeling of image data.
- **Python** – For model integration and testing.

### 📷 Sample Results

- **High accuracy** on standard fruits (apples, bananas, etc.)
- **Decreased confidence** on unseen or hybrid fruits (e.g., cucumber-pear hybrids)
- Model deployment via **REST API** for real-time inference

---

## 💬 Section B: Multilingual Chatbot for Customer Service

### 🏢 Business Context

An online food company targeting the **Asian market** wants to automate customer service using a multilingual chatbot to reduce manpower costs and increase customer engagement.

### ✅ Solution Features

- Developed a chatbot using **Azure Language Studio** and **Azure AI Services**
- Created a **knowledge base** using Excel QnA pairs
- Published and tested the chatbot with English queries
- Extended to support a second **Asian language (e.g., Chinese, Malay, etc.)**
- Integrated **speech-to-text** and **text-to-speech** features for enhanced UX

### 🧩 Technologies Used

- **Azure Language Studio** – To build, train, and test QnA-style chatbots
- **Azure AI Language Service** – For NLU, NER, sentiment analysis
- **Azure Translator** – For real-time multilingual capabilities
- **Azure OpenAI** – For generative responses and conversation handling
- **Python (Bot Framework)** – For testing and extending chatbot capabilities

### 🔄 Key Functionalities

- Handles **FAQ-style queries** (shipping, refunds, product info, etc.)
- Responds to users in **English + 1 Asian language**
- Uses Azure AI Translator for **on-the-fly translation**
- Supports **voice input/output** via Azure Speech Services

---

## 🌏 Benefits of a Multilingual Chatbot

- **Expanded Market Reach**: Serve customers across Asia more effectively.
- **Enhanced Brand Image**: Showcase global readiness and inclusivity.
- **Cultural Adaptability**: Tailor experiences to diverse cultural preferences.

---

## 📃 License

This project is for educational purposes under the Specialist Diploma in Applied AI and is shared under the MIT License.