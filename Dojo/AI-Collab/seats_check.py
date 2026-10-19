# seats_check.py
import json
import sys
import os

def check_seats_registry():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seats.json")

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"SEATS: FAIL — seats.json not found at {file_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"SEATS: FAIL — seats.json is not valid JSON", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"SEATS: FAIL — Error reading seats.json: {e}", file=sys.stderr)
        sys.exit(1)

    seats = data.get("seats")

    if not isinstance(seats, list):
        print(f"SEATS: FAIL — 'seats' key is not a list in seats.json", file=sys.stderr)
        sys.exit(1)

    # Check for exactly 2 seats
    if len(seats) != 2:
        print(f"SEATS: FAIL — Expected 2 seats, found {len(seats)}", file=sys.stderr)
        sys.exit(1)

    seat_ids = set()
    conv_ids = set()
    seat_id_not_in_url = True
    conv_id_not_in_url = True
    profile_id_valid = True

    for i, seat in enumerate(seats):
        # Print seat info
        seat_id = seat.get("seat_id")
        conv_id = seat.get("conv_id")
        url = seat.get("url")
        profile_id = seat.get("profile_id")

        if not seat_id or not conv_id or not url or not profile_id:
            print(f"SEATS: FAIL — Seat {i+1} is missing required fields (seat_id, conv_id, url, profile_id)", file=sys.stderr)
            sys.exit(1)

        print(f"seat_id={seat_id} conv_id={conv_id}")

        # Check for duplicate seat_ids
        if seat_id in seat_ids:
            print(f"SEATS: FAIL — Duplicate seat_id found: {seat_id}", file=sys.stderr)
            sys.exit(1)
        seat_ids.add(seat_id)

        # Check for duplicate conv_ids
        if conv_id in conv_ids:
            print(f"SEATS: FAIL — Duplicate conv_id found: {conv_id}", file=sys.stderr)
            sys.exit(1)
        conv_ids.add(conv_id)

        # Check if conv_id is in URL
        if conv_id in url:
            conv_id_not_in_url = False
            print(f"SEATS: FAIL — conv_id '{conv_id}' is present in url '{url}'", file=sys.stderr)
            # Do not exit immediately, allow other checks to run and report all failures

        # Check if seat_id is in URL
        if seat_id in url:
            seat_id_not_in_url = False
            print(f"SEATS: FAIL — seat_id '{seat_id}' is present in url '{url}'", file=sys.stderr)
            # Do not exit immediately

        # Check profile_id validity
        if not isinstance(profile_id, str) or not profile_id:
            profile_id_valid = False
            print(f"SEATS: FAIL — Invalid or empty profile_id for seat '{seat_id}'", file=sys.stderr)
            # Do not exit immediately

    # Final check for seat_id not derived from URL and conv_id not derived from URL
    if not seat_id_not_in_url:
        sys.exit(1)
    if not conv_id_not_in_url:
        sys.exit(1)
    if not profile_id_valid:
        sys.exit(1)

    # If all checks passed without exiting
    print("SEATS: PASS")
    sys.exit(0)

if __name__ == "__main__":
    check_seats_registry()
