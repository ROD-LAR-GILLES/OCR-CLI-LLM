"""Document processing adapters."""
from .pymupdf_adapter import PyMuPDFAdapter
from .table_detector import TableDetector

__all__ = ['PyMuPDFAdapter', 'TableDetector']
