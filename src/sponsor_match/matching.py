from dataclasses import dataclass
import re
from typing import Iterable


@dataclass(frozen=True)
class Sponsor:
    name: str
    industries: frozenset[str]
    target_audiences: frozenset[str]
    regions: frozenset[str]
    budget: int


@dataclass(frozen=True)
class Event:
    name: str
    industries: frozenset[str]
    audiences: frozenset[str]
    regions: frozenset[str]
    sponsorship_minimum: int


@dataclass(frozen=True)
class Match:
    event: Event
    score: float
    confidence: str
    reasons: tuple[str, ...]


def normalize(value: str) -> str:
    """Normalize a label for deterministic comparisons."""
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _overlap(left: Iterable[str], right: Iterable[str]) -> set[str]:
    return {normalize(x) for x in left} & {normalize(x) for x in right}


def score_pair(sponsor: Sponsor, event: Event) -> tuple[float, tuple[str, ...]]:
    reasons: list[str] = []
    score = 0.0
    industries = _overlap(sponsor.industries, event.industries)
    audiences = _overlap(sponsor.target_audiences, event.audiences)
    regions = _overlap(sponsor.regions, event.regions)

    if industries:
        score += 0.35
        reasons.append(f"industry overlap: {', '.join(sorted(industries))}")
    if audiences:
        score += 0.35
        reasons.append(f"audience overlap: {', '.join(sorted(audiences))}")
    if regions:
        score += 0.20
        reasons.append(f"regional overlap: {', '.join(sorted(regions))}")
    if sponsor.budget >= event.sponsorship_minimum:
        score += 0.10
        reasons.append("budget meets sponsorship minimum")
    else:
        reasons.append("budget below sponsorship minimum")

    return round(score, 3), tuple(reasons)


def rank_events(sponsor: Sponsor, events: Iterable[Event]) -> list[Match]:
    """Return deterministic, explainable recommendations from highest score."""
    matches = []
    for event in events:
        score, reasons = score_pair(sponsor, event)
        confidence = "high" if score >= 0.8 else "medium" if score >= 0.5 else "low"
        matches.append(Match(event, score, confidence, reasons))
    return sorted(matches, key=lambda m: (-m.score, normalize(m.event.name)))
