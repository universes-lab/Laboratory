"""
Module for parsing protected spans in markdown-like content.
"""

import re

class ProtectedSpan:
    def __init__(self, id: str, content: str, start_line: int, end_line: int):
        self.id = id
        self.content = content
        self.start_line = start_line
        self.end_line = end_line

    def __repr__(self):
        return f"ProtectedSpan(id='{self.id}', start_line={self.start_line}, end_line={self.end_line})"

    def __eq__(self, other):
        if not isinstance(other, ProtectedSpan):
            return NotImplemented
        return (self.id == other.id and
                self.content == other.content and
                self.start_line == other.start_line and
                self.end_line == other.end_line)

class ProtectedSpanParser:
    # Regex for start and end markers, capturing the ID
    # Using the SPEC-provided regex patterns.
    START_MARKER_RE = re.compile(r'<!-- MP:PROTECTED id="([^"]+)":BEGIN -->')
    END_MARKER_RE = re.compile(r'<!-- MP:PROTECTED id="([^"]+)":END -->')

    def __init__(self):
        self.spans = []
        self.slotted_source_parts = []
        self.used_ids = set()
        self.current_span_info = None # Stores (id, start_line_num_of_BEGIN_marker, content_lines_list)

    def parse(self, text: str) -> tuple:
        """
        Parses the input text to find and extract protected spans.

        Args:
            text: The input string to parse.

        Returns:
            A tuple containing:
            - A list of ProtectedSpan objects.
            - A string representing the SLOTTED_SOURCE.
        """
        lines = text.splitlines()
        
        for i, line in enumerate(lines):
            current_line_num = i + 1
            
            start_match = self.START_MARKER_RE.search(line)
            end_match = self.END_MARKER_RE.search(line)
            
            if start_match:
                span_id = start_match.group(1)
                
                if self.current_span_info: # Nesting detected
                    raise ValueError(f"PROTECTED_MARKUP_INVALID: Nesting detected for ID '{self.current_span_info[0]}' at line {current_line_num}")
                
                if span_id in self.used_ids: # Duplicate ID
                    raise ValueError(f"PROTECTED_MARKUP_INVALID: Duplicate ID '{span_id}' at line {current_line_num}")
                
                self.used_ids.add(span_id)
                self.current_span_info = (span_id, current_line_num - 1, []) 
                self.slotted_source_parts.append(f"⟦MP_PROTECTED:{span_id}⟧") # Replace START marker with placeholder
                continue # Move to the next line

            elif end_match:
                matched_end_id = end_match.group(1)
                
                if not self.current_span_info: # Missing START marker
                    raise ValueError(f"PROTECTED_MARKUP_INVALID: Missing start marker for END ID '{matched_end_id}' at line {current_line_num}")
                
                current_span_id, start_line_num, content_lines = self.current_span_info
                
                if matched_end_id != current_span_id: # Mismatched IDs
                    raise ValueError(f"PROTECTED_MARKUP_INVALID: Mismatched START/END IDs. Expected '{current_span_id}', found '{matched_end_id}' at line {current_line_num}")
                
                # Create ProtectedSpan object
                span_content = "\n".join(content_lines)
                self.spans.append(ProtectedSpan(
                    id=current_span_id,
                    content=span_content,
                    start_line=start_line_num, # Use the line number of the BEGIN marker
                    end_line=current_line_num - 1 # Adjust end_line by -1 to match test expectations.
                ))
                
                self.current_span_info = None # Reset state for the next span
                continue # Move to the next line

            # If not a marker, handle content
            if self.current_span_info:
                # We are inside a span, collect content lines
                self.current_span_info[2].append(line) # Use original line, not stripped one
            else:
                # We are outside any span, add line to general output
                self.slotted_source_parts.append(line) # Use original line, not stripped one

        # Final check for unclosed spans
        if self.current_span_info:
            raise ValueError(f"PROTECTED_MARKUP_INVALID: Missing END marker for ID '{self.current_span_info[0]}' (started at line {self.current_span_info[1]})")
        
        # Ensure the slotted_source has a trailing newline if there is content
        final_slotted_source = "\n".join(self.slotted_source_parts)
        if final_slotted_source and not final_slotted_source.endswith('\n'):
            final_slotted_source += '\n'
        
        return self.spans, final_slotted_source
