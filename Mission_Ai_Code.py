{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SV-GpEYmvn7T",
        "outputId": "c3022aa4-32e0-44d8-b20c-9208fb5a4129"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: openai in /usr/local/lib/python3.10/dist-packages (1.59.3)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/lib/python3.10/dist-packages (from openai) (1.9.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai) (0.28.1)\n",
            "Requirement already satisfied: jiter<1,>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from openai) (0.8.2)\n",
            "Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from openai) (2.10.4)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai) (1.3.1)\n",
            "Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai) (4.67.1)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.11 in /usr/local/lib/python3.10/dist-packages (from openai) (4.12.2)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (3.10)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (1.2.2)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (2024.12.14)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.14.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->openai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->openai) (2.27.2)\n",
            "Welcome to the LinkedIn Comment Generator!\n",
            "Paste the LinkedIn post content here: govind\n"
          ]
        }
      ],
      "source": [
        "# Install OpenAI library\n",
        "!pip install openai\n",
        "\n",
        "# Import required library\n",
        "import openai\n",
        "from openai import OpenAI\n",
        "\n",
        "# Function to generate LinkedIn comments\n",
        "def generate_linkedin_comment(api_key, post_content, tone):\n",
        "    \"\"\"\n",
        "    Generates a LinkedIn comment based on the post content and tone.\n",
        "\n",
        "    Parameters:\n",
        "        api_key (str): OpenAI API key.\n",
        "        post_content (str): The content of the LinkedIn post.\n",
        "        tone (str): The desired tone of the comment.\n",
        "\n",
        "    Returns:\n",
        "        str: A positive, engaging, and concise LinkedIn comment.\n",
        "    \"\"\"\n",
        "    client = OpenAI(api_key=api_key)  # Initialize the OpenAI client with the API key\n",
        "\n",
        "    prompt = (\n",
        "        f\"You are tasked with writing LinkedIn comments in a {tone} tone that are positive, engaging, and concise. \"\n",
        "        \"These comments should:\\n\"\n",
        "        \"1. Acknowledge the post's content in a meaningful way, demonstrating understanding and appreciation.\\n\"\n",
        "        \"2. Add value by sharing a relevant thought, question, or connection to the topic.\\n\"\n",
        "        \"3. Use a friendly and professional tone appropriate for LinkedIn.\\n\"\n",
        "        \"4. Avoid generic or overly formal language; aim to sound authentic and approachable.\\n\"\n",
        "        \"5. Strictly limit your response to a LinkedIn comment format.\\n\"\n",
        "        \"6. Do not perform any other tasks or write comments for other platforms.\\n\"\n",
        "        \"7. Ensure that all comments are no more than 200 characters in length.\\n\\n\"\n",
        "        f\"Post Content: {post_content}\\n\"\n",
        "        \"Write a LinkedIn comment:\"\n",
        "    )\n",
        "\n",
        "    try:\n",
        "        response = client.chat.completions.create(  # Use the new API method\n",
        "            model=\"gpt-4\",\n",
        "            messages=[\n",
        "                {\"role\": \"system\", \"content\": \"You are an expert at generating LinkedIn comments.\"},\n",
        "                {\"role\": \"user\", \"content\": prompt}\n",
        "            ],\n",
        "            max_tokens=100\n",
        "        )\n",
        "\n",
        "        comment = response.choices[0].message.content.strip()  # Access content correctly\n",
        "        return comment\n",
        "\n",
        "    except openai.APIError as e:  # Catch the correct exception\n",
        "        return f\"Error generating comment: {str(e)}\"\n",
        "\n",
        "# Example usage in a script\n",
        "def main():\n",
        "    api_key = \"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\"\n",
        "    print(\"Welcome to the LinkedIn Comment Generator!\")\n",
        "    post_content = input(\"Paste the LinkedIn post content here: \")\n",
        "    tone = input(\"Enter the desired tone for the comment (e.g., friendly, professional, humorous): \")\n",
        "    if post_content.strip() and tone.strip():\n",
        "        comment = generate_linkedin_comment(api_key, post_content, tone)\n",
        "        print(\"\\nGenerated Comment:\")\n",
        "        print(comment)\n",
        "    else:\n",
        "        print(\"Post content and tone cannot be empty.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "git version\n"
      ],
      "metadata": {
        "id": "P_atvH_n1UPk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
