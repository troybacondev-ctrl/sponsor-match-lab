from .matching import Event, Sponsor, rank_events


def main() -> None:
    sponsor = Sponsor(
        "Northstar Audio",
        frozenset({"music", "technology"}),
        frozenset({"creators", "students"}),
        frozenset({"southeast"}),
        25000,
    )
    events = [
        Event("Southeast Creator Summit", frozenset({"music", "technology"}), frozenset({"creators"}), frozenset({"southeast"}), 20000),
        Event("National Health Data Forum", frozenset({"healthcare"}), frozenset({"clinicians"}), frozenset({"northeast"}), 15000),
        Event("Student Arts Weekend", frozenset({"arts"}), frozenset({"students"}), frozenset({"southeast"}), 30000),
    ]
    for match in rank_events(sponsor, events):
        print(f"{match.event.name}: {match.score:.3f} ({match.confidence})")
        for reason in match.reasons:
            print(f"  - {reason}")


if __name__ == "__main__":
    main()
