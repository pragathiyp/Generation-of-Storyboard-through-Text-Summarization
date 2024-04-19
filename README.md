# Generation-of-Storyboard-through-Text-Summarization
## Installation

To use this template, your computer needs:

- [Python 2 or 3](https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)

### Running the app

```bash
python app.py
```
# Storyboard-Generation-NLP
## Introduction
Our NLP-based PowerPoint Generator revolutionizes the process of creating presentations and
storyboards from lengthy PDF documents. By leveraging Natural Language Processing (NLP)
techniques, this innovative system drastically reduces the time and effort required for these tasks.
The generator extracts key information from the PDFs, ensuring accurate comprehension of
concepts and data points. It then generates a comprehensive storyboard as the foundation for
visually appealing PowerPoint slides. Our solution streamlines the creation process, saving
valuable time and effort. The presentations and storyboards maintain consistency and clarity
throughout, delivering impactful results.
In summary, our NLP-based PowerPoint Generator offers an efficient approach to transform PDF
documents into compelling presentations. With automated information extraction and voice over
capabilities, users can create engaging slides with ease.


## Scope of the Project
The scope of this project encompasses the development of an advanced NLP-based PowerPoint
Generator with a focus on providing a user-friendly interface and efficient generation of visually
appealing presentations. The system will be capable of effectively processing both long and short
documents to produce high-quality PowerPoint slides.
The core functionalities of the PowerPoint Generator include automated extraction and
summarization of key information which will also provide a seamless and intuitive user interface,
ensuring ease of use for individuals with varying levels of technical expertise.
As a future enhancement, the project aims to incorporate interactive storyboards, enabling features
such as quizzing and integration of videos, to enhance audience engagement and interactivity. This
expansion will further elevate the overall user experience and create a more dynamic and
immersive presentation environment.
The development process has been organized and structured, encompassing essential stages such
as requirement analysis, sequence diagram creation, state diagram design, and high-level system
design. This systematic approach ensures a well-defined and organized development path,
facilitating efficient implementation and robust system performance.
The project emphasizes delivering a visually appealing user interface and efficient performance,
ensuring the generated PowerPoint presentations are of high quality. By incorporating user
feedback and iterative development practices, the system will undergo continuous improvement to
meet user requirements and enhance user satisfaction.

## Problem statement
The manual process of converting lengthy PDF documents into PowerPoint presentations is timeconsuming and inefficient, lacking automated extraction and synthesis of key information. This
results in presentations that often fail to engage the audience effectively. To overcome these
challenges, our project aims to develop an NLP-based PPT generator that can analyze PDF
documents, extract essential points, and generate visually captivating slides with relevant images.
By optimizing the extraction algorithm, improving the user interface, and conducting
comprehensive testing, our goal is to significantly reduce the time and effort required to create
compelling presentations, empowering users with a powerful tool to enhance communication and
productivity in various fields.

## Literature Survey


![Screenshot 2024-04-19 205107](https://github.com/pragathiyp/Generation-of-Storyboard-through-Text-Summarization/assets/90029094/f586590d-20ad-4ca7-b2b4-2647a3ab3277)

![Screenshot 2024-04-19 205133](https://github.com/pragathiyp/Generation-of-Storyboard-through-Text-Summarization/assets/90029094/1620851f-a417-4b6d-b5d2-e7d9443da8dc)

![Screenshot 2024-04-19 205150](https://github.com/pragathiyp/Generation-of-Storyboard-through-Text-Summarization/assets/90029094/9632e6d9-698e-4d19-8215-1c011eaac9fc)




## Design
### High Level Design
The high-level design of the application involves a structured workflow that includes document
input, text preprocessing, extraction of text in JSON format for seamless pipelining into
PowerPoint slides, classification of text into headings, subheadings, and summary points ensuring
a well-organized content structure, text summarization, and generation of the PowerPoint
presentation. Users upload documents as input, followed by text preprocessing for optimization.
The extracted text is transformed into JSON format to facilitate smooth data handling. The
summarized text is generated using advanced techniques, condensing it into concise key points.
Finally, the application generates visually appealing PowerPoint slides. This high-level design
guarantees a systematic and efficient approach to create compelling presentations with structured
content hierarchy.

![image](https://github.com/pragathi23/Storyboard-Genearation-NLP/assets/102874384/5432bf6d-3f1d-4dac-af84-362262d5482f)


## Detailed Design
The user will login through the interactive user interface after which they can upload the pdf to be
summarized, which is then taken for summarization. The output is then pipelined for PPT generation
which is visually appealing.

## Sequence Diagram
As shown in the diagram user is an actor interacting with the system. As shown in the design After
opening the webpage, user has to login. After successful login, the user uploads the document , the
model is used to summarize the text which gives the output in JSON to generate the PPT which is
then returned to the user.

![image](https://github.com/pragathi23/Storyboard-Genearation-NLP/assets/102874384/4a572713-0f6b-4bde-8c8e-cae6db53329f)

## Use Case Diagram
As shown above there are two actors interacting with the system, one is the user and the other one
is the System. The user has use-cases like authentication, login and logout. The user and system is
responsible for the document management. The system will process the input document by
preprocessing, ppt generation, and summarization which can be accessed by the user.

![image](https://github.com/pragathi23/Storyboard-Genearation-NLP/assets/102874384/2c1e9047-99be-4ae4-aecb-7a2904eda06c)


## Implementation
### Proposed methodology
The project uses a combination of methodologies and techniques for text summarization. The original text in the input document undergoes several preprocessing steps, including tokenization, stop word removal, and other text cleaning techniques. Once pre-processed, the text is classified into headings, subheadings, and content.
Techniques used in the project:
1. Tokenization: The original text is divided into individual tokens, usually words or subwords, to facilitate further processing and analysis.
2. Stop Word Removal: Commonly used words with little semantic meaning, such as "the," "is," and "and," are removed to reduce noise in the text and improve the quality of the summary.
3. Text Cleaning: Various techniques are employed to clean the text, including removing punctuation, converting text to lowercase, and handling special characters or symbols.
4. Headings and Subheadings Extraction: The document is analysed to identify headings and subheadings based on formatting, such as font size, style, or indentation.
5. Sentence Importance Scoring: Techniques like TF-IDF (Term Frequency-Inverse Document Frequency) or LDA (Latent Dirichlet Allocation) are used to assign importance scores to sentences based on their relevance to the main topics or themes in the document.
6. Postprocessing: The obtained summary content is further processed to refine its readability and coherence. This may include capitalizing the first letter of each sentence, adding appropriate punctuation, and ensuring proper formatting.
7. JSON Format: The final summarized content is structured in JSON (JavaScript Object Notation) format, which is a lightweight data interchange format widely used for data representation and communication.
8. PPT Pipeline: The summarized content in JSON format is then pipelined into a PowerPoint (PPT) presentation, where it can be used to generate slides or populate existing slide templates with the summarized information.

## Algorithm used for implementation

Various Methodologies have been implemented such as : 
Extractive Summarization: the extractive approach selects the most important phrases and lines from the documents. It then combines all the important lines to create the summary. So, in this case, every line and word of the summary actually belongs to the original document which is summarized.

Abstractive Summarization: The abstractive approach uses new phrases and terms that are different from the original document, keeping the meaning the same, just like how humans do in summarization. So, it is much harder than the extractive approach.

1. LSA (Latent Semantic Analysis) is a mathematical technique used for text analysis and
   information retrieval. It aims to capture the underlying semantic structure of a document
   collection by analyzing the relationships between words and documents. LSA represents text in a
   lower-dimensional space, allowing for efficient processing and summarization. Here is a detailed
   explanation of LSA:
   1. Building the Term-Document Matrix: 
   ● The first step in LSA is to construct a term-document matrix that represents the
   frequency of terms in the document collection.
   ● The matrix has rows corresponding to terms and columns corresponding to
   documents.
   ● Each entry in the matrix represents the frequency or weight of a term in a
   document.
   ● Various weighting schemes can be used, such as term frequency (TF), inverse
   document frequency (IDF), or TF-IDF.
   2. Singular Value Decomposition (SVD):
   ● After constructing the term-document matrix, LSA applies Singular Value
   Decomposition (SVD) to factorize the matrix.
   ● SVD breaks down the matrix into three separate matrices: U, Σ, and V^T.
   ● U represents the left singular vectors, which capture the relationships between
   terms.
   ● Σ is a diagonal matrix containing singular values, which indicate the importance
   of each dimension.
   ● V^T represents the right singular vectors, which capture the relationships between
   documents.
   3. Dimensionality Reduction:
   ● The dimensionality of the term-document matrix is typically very high, which
   makes processing and analysis computationally expensive.
   ● To reduce the dimensionality, LSA truncates the singular values and
   corresponding singular vectors.
   ● By keeping only the top k singular values and their associated vectors, the matrix
   is transformed into a lower-dimensional representation.
   ● The choice of k determines the level of dimensionality reduction and the amount
   of information retained.
   4. Sentence/Document Similarity Calculation:
   ● Once the dimensionality is reduced, LSA calculates the similarity between
   sentences or documents based on their vector representations.
   ● The similarity between two vectors can be computed using various metrics, such
   as cosine similarity.
   ● Cosine similarity measures the cosine of the angle between two vectors, providing
   a value between -1 and 1. Higher values indicate greater similarity.
   5. Sentence Importance Scoring:
   ● LSA assigns importance scores to sentences based on their similarity to the main
   topics or themes in the document collection.
   ● One common approach is to calculate the sentence importance score as the sum of
   the similarities between the sentence vector and the main topic vectors.
   ● The main topic vectors can be obtained by averaging the vectors of the top-k
   documents that are most representative of each topic.
   6. Sentence Selection for Summarization:
   ● After scoring the sentences, LSA selects the most important sentences to form the
   summary.
   ● The number of sentences selected depends on the desired length of the summary.
   ● The selected sentences should capture the main ideas and themes of the document
   while maintaining coherence and readability.

![image](https://github.com/pragathi23/Storyboard-Genearation-NLP/assets/102874384/4838bfa1-364f-4bb7-b3bd-23f47a302b8e)

2. PEGASUS MODEL:

PEGASUS, which stands for Pre-training with Extracted Gap-Sentences for Abstractive Summarization developed by Google AI in 2020. They propose pre-training large Transformer-based encoder-decoder models on massive text corpora with a new self-supervised objective.

In PEGASUS, several complete sentences are [MASK] from a document. PEGASUS is trained to predict these sentences. An input is a document with missing sentences, PEGASUS will recover them then the output consists of missing sentences concatenated together. This task is Gap Sentence Generation (GSG).
Although the main contribution of PEGASUS is Gap Sentence Generation, its base architecture includes an encoder and a decoder. So, PEGASUS uses a pre-trained encoder as a masked language model.

In the encoder module, we take random mask words from the sequences and use other words from the sequence to predict these masked words.
In PEGASUS, encoder (MLM) and decoder (GSG) train simultaneously.

Originally there were three sentences. One sentence is masked with [MASK1] and used as target generation text (GSG). The other two sentences remain in the input, but some words are randomly masked by [MASK2] (MLM).

![image](https://github.com/shubpotadar/slidewizard/assets/90029094/d2103b2e-9e09-4239-965c-d1fd5fcc89f0)


   
4. BART MODEL:
   
BART ( Bidirectional and Auto-Regressive) from transformers is a sequence-to-sequence model trained as a denoising autoencoder. This means that a fine-tuned BART model can take a text sequence (for example, English) as input and produce a different text sequence at the output (for example, French). This type of model is relevant for machine translation (translating text from one language to another), question-answering (producing answers for a given question on a specific corpus), text summarization (giving a summary of or paraphrasing a long text document), or sequence classification (categorizing input text sentences or tokens). Another task is sentence entailment which, given two or more sentences, evaluates whether the sentences are logical extensions or are logically related to a given statement.

BART was trained as a denoising autoencoder, so the training data includes “corrupted” or “noisy” text, which would be mapped to clean or original text. So what exactly counts as “noisy” for text data. The authors of BART settle on using some existing and some new noising techniques for pretraining. The noising schemes they use are Token Masking, Token Deletion, Text Infilling, Sentence Permutation, and Document Rotation. However, not all transformations are employed in training the final BART model. Based on a comparative study of pre-training objectives, the authors use only text infilling and sentence permutation transformations, with about 30% of tokens being masked and all sentences permuted.

![image](https://github.com/shubpotadar/slidewizard/assets/90029094/78d80032-6b47-4257-ba23-f6320cfb8499)

5. WizardLM

Implemented the WizardCoder with modifications to control the length of the summaries obtained as well as fine-tuning.

## Document Analysis

Deepdoctection is a Python library that orchestrates document extraction and document layout analysis tasks using deep learning models. It does not implement models but enables you to build pipelines using highly acknowledged libraries for object detection, OCR and selected NLP tasks and provides an integrated framework for fine-tuning, evaluating and running models. For more specific text processing tasks use one of the many other great NLP libraries.

Deepdoctection focuses on applications and is made for those who want to solve real world problems related to document extraction from PDFs or scans in various image formats.


<img src="https://github.com/shubpotadar/slidewizard/assets/90029094/84c65d07-0716-4d79-a742-f21d6660465a" width="400" height="600">




