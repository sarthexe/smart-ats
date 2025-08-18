# Smart ATS Score for Resume

## Overview
The **Smart ATS Score** project is an intelligent web application designed to evaluate resumes by generating an Applicant Tracking System (ATS) compatibility score. Built with **Streamlit**, it provides an intuitive user interface for job seekers and recruiters to upload resumes and job descriptions, analyze content, and receive actionable feedback. The tool leverages advanced natural language processing (NLP) to assess resume content against job requirements, helping candidates optimize their resumes for better ATS performance.

This project is ideal for job seekers, recruiters, and career coaches aiming to improve resume effectiveness in automated hiring systems.

## Tech Stack
- **Streamlit**: Powers the interactive web interface for easy resume and job description uploads and result visualization.
- **LangChain**: Used for building the NLP pipeline, enabling efficient text processing and interaction with large language models.
- **PyPDF2**: Utilizes for extracting text from PDF resumes, ensuring accurate parsing of resume content.
- **OpenAI**: Drives the NLP model to analyze and score resumes based on semantic similarity and keyword matching with job descriptions.

## Features
- **Resume Parsing**: Extracts text from uploaded PDF resumes with high accuracy.
- **ATS Score Calculation**: Generates a score (0-100) based on keyword relevance, content structure, and ATS compatibility.
- **Job Description Matching**: Compares resume content with job descriptions to identify gaps and suggest improvements.
- **Interactive UI**: Streamlit-based interface for seamless file uploads and real-time score visualization.
- **Actionable Feedback**: Provides a clear report with the ATS score and optimization tips.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/smart-ats-score.git
   cd smart-ats-score
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up OpenAI API Key**:
   - Obtain an API key from [OpenAI](https://platform.openai.com/account/api-keys).
   - Create a `.env` file in the project root and add:
     ```
     OPENAI_API_KEY=your-api-key
     ```

## Usage
1. Ensure all dependencies are installed and the `.env` file is configured.
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open your browser to `http://localhost:8501` (or the provided URL).
4. Upload a resume (PDF) and a job description (text or PDF) via the Streamlit interface.
5. View the ATS score and optimization suggestions displayed on the web app.

## Example
After running `streamlit run app.py`, the interface allows you to:
- Upload a resume (e.g., `john_doe.pdf`).
- Upload or paste a job description (e.g., `data_scientist.txt`).
- Receive output like:
  ```
  ATS Score: 92/100
  Suggestions:
  - Add keywords: "machine learning," "data visualization"
  - Use bullet points for better ATS readability
  ```

## Project Structure
```
smart-ats-score/
│
├── app.py                 # Main Streamlit application script
├── requirements.txt       # List of dependencies
├── resumes/               # Folder for storing uploaded resume PDFs
├── job_descriptions/      # Folder for storing job description files
├── utils/                 # Utility scripts for text extraction and processing
└── README.md              # Project documentation
```

## Requirements
Ensure the following are included in `requirements.txt`:
```
streamlit
langchain
PyPDF2
openai
python-dotenv
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, reach out to [your-email@example.com](mailto:your-email@example.com) or open an issue on GitHub.