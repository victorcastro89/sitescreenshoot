import json

import os
import requests
import base64

api_key = ""


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

prompt = """
Your task is to carefully analyze this website image and categorize the website into a structured format capturing key information about what the website is about.

First, write your initial thoughts, analysis and reasoning about how to categorize this website based on its content.

Then, output your final categorization of the website in JSON format with the following fields:
- category: The overall category or industry of the website 
- subcategory: A more specific subcategory within the overall category, if applicable
- products: An array of specific products the website sells or offers, if any in case it is an e-commerce website
- services: An array of specific services the website provides, if any in case it is a professional services website
- features: An array of specific features or functionalities of the website, if any
- target_audience: Who the intended audience or customers of this website are likely to be

Provide your final JSON categorization as the example bellow:

{
  "reasoning":"Your analysis and reasoning here",
  "category": "category here",
  "subcategory": "subcategory here",
  "products": ["product1", "product2"],
  "services": ["service1", "service2"],
  "target_audience": "target audience here"
}


"""


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Directory containing the images
image_directory = "./img/lv"

# List all image files in the directory
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

# Constructing the messages with image URLs
messages_content = [
    {
        "type": "text",
        "text": prompt
    }
]

for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    base64_image = encode_image(image_path)
    messages_content.append({
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
        }
    })

payload = {
    "model": "gpt-4o",
    "response_format": {"type": "json_object"},
    "messages": [
        {
            "role": "user",
            "content": messages_content
        }
    ],

}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

json_data = json.loads(response.json()['choices'][0]['message']['content'])
pretty_json = json.dumps(json_data, indent=4, ensure_ascii=False)
print(pretty_json)
