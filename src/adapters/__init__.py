"""
Adapters module.
Organized by functional categories: OCR, LLM, and Document processing.
"""
from .ocr import OCRAdapter, ParallelOCRProcessor
from .llm import LLMRefiner, LanguageDetector, OpenAIProvider, GeminiProvider
from .document import PyMuPDFAdapter, TableDetector

__all__ = [
    # OCR
    'OCRAdapter',
    'ParallelOCRProcessor',
    # LLM
    'LLMRefiner',
    'LanguageDetector', 
    'OpenAIProvider',
    'GeminiProvider',
    # Document
    'PyMuPDFAdapter',
    'TableDetector'
]