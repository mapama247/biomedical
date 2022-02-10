"""
Text Pairs Schema
"""
import datasets


features = datasets.Features(
    {
        "id": datasets.Value("int32"),
        "document_id": datasets.Value("string"),
        "text_1": datasets.Value("string"),
        "text_2": datasets.Value("string"),
        "label": datasets.Value("string"),
    }
)
