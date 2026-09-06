import re
from typing import List, Optional, Any

# We import ProtectedSpan only for type hinting if needed, but we use Duck Typing 
# to avoid hard dependency on Step 1 if not strictly necessary, 
# though for this project it's fine to import it.
try:
    from src.parser.protected_span_parser import ProtectedSpan
except ImportError:
    # Fallback for environments where it's not yet available or in different path
    class ProtectedSpan:
        def __init__(self, id: str, content: str, start_line: int, end_line: int):
            self.id = id
            self.content = content
            self.start_line = start_line
            self.end_line = end_line

class ATXHeading:
    """Represents an extracted ATX heading with its metadata."""
    def __init__(self, level: int, heading_text: str, raw_heading: str, marker_id: Optional[str], start_offset: int, end_offset: int):
        self.level = level
        self.heading_text = heading_text
        self.raw_heading = raw_heading
        self.marker_id = marker_id
        self.start_offset = start_offset
        self.end_offset = end_offset

    def __repr__(self):
        return (f"ATXHeading(level={self.level}, heading_text='{self.heading_text}', marker_id='{self.marker_id}', "
                f"offsets=({self.start_offset}, {self.end_offset}))")

    def __eq__(self, other):
        if not isinstance(other, ATXHeading):
            return NotImplemented
        return (self.level == other.level and
                self.heading_text == other.heading_text and
                self.raw_heading == other.raw_heading and
                self.marker_id == other.marker_id and
                self.start_offset == other.start_offset and
                self.end_offset == other.end_offset)

class ATXHeadingExtractor:
    """
    Extracts Markdown ATX headings from slotted source content,
    associating them with production markers and exact source positions.
    """
    # ATX Heading: 1-6 '#' followed by separation whitespace
    ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
    # Production Marker: <!-- MP:(\d{4}) --> as established by Step 2
    PRODUCTION_MARKER_RE = re.compile(r"<!-- MP:(\d{4}) -->")

    def __init__(self, slotted_source: str, protected_spans: List[Any] = None, initial_marker_id: Optional[str] = None):
        """
        Initialize the extractor.
        
        Args:
            slotted_source: The source text (usually SLOTTED_SOURCE).
            protected_spans: Optional list of ProtectedSpan objects.
            initial_marker_id: Optional initial marker context (e.g. "MP:0001").
        """
        self.slotted_source = slotted_source
        self.protected_spans = protected_spans if protected_spans is not None else []
        self.initial_marker_id = initial_marker_id
        self.headings: List[ATXHeading] = []

    def _is_within_protected_span(self, line_index: int) -> bool:
        """
        Checks if the 0-based line index falls within any protected span.
        """
        for span in self.protected_spans:
            # ProtectedSpanParser uses 0-based start_line/end_line
            if span.start_line <= line_index <= span.end_line:
                return True
        return False

    def extract(self) -> List[ATXHeading]:
        """
        Performs the extraction of ATX headings from the provided source.
        Returns a list of ATXHeading objects.
        """
        # keepends=True is vital for accurate character offsets
        lines = self.slotted_source.splitlines(keepends=True)
        current_marker_id = self.initial_marker_id
        current_offset = 0

        for i, line in enumerate(lines):
            # 1. Update marker context from the current line
            marker_matches = self.PRODUCTION_MARKER_RE.findall(line)
            if marker_matches:
                # Per SourceParser convention: marker_id = f"MP:{digits}"
                current_marker_id = f"MP:{marker_matches[-1]}"

            # 2. Extract heading if it's a heading and not protected
            if not self._is_within_protected_span(i):
                heading_match = self.ATX_HEADING_RE.match(line)
                if heading_match:
                    level = len(heading_match.group(1))
                    
                    # Exact matched heading line text, excluding line terminator
                    # rstrip('\r\n') removes the terminator for raw_heading
                    raw_heading = line.rstrip('\r\n')
                    heading_text = heading_match.group(2).rstrip('\r\n')
                    
                    start_offset = current_offset
                    end_offset = current_offset + len(raw_heading)
                    
                    self.headings.append(ATXHeading(
                        level=level,
                        heading_text=heading_text,
                        raw_heading=raw_heading,
                        marker_id=current_marker_id,
                        start_offset=start_offset,
                        end_offset=end_offset
                    ))

            current_offset += len(line)

        return self.headings
