# Sponsor Match Lab

A small, original reference implementation of explainable sponsor-to-event matching using synthetic data.

This project demonstrates portfolio-safe patterns relevant to event platforms and data products: normalization, weighted feature scoring, deterministic ranking, confidence bands, and testable Python APIs. It is not copied from or connected to any employer system, production dataset, or private SponsorOS implementation.

## What it does

- Normalizes sponsor and event attributes such as industry, audience, geography, and budget.
- Scores candidate pairs with transparent weighted rules rather than opaque rankings.
- Returns a ranked list with feature-level reasons that explain each recommendation.
- Includes deterministic tests and a tiny synthetic dataset so the example is reproducible.

## Quick start

```bash
python -m unittest discover -s tests -v
python -m src.sponsor_match.cli
```

Example output includes the recommended event, score, confidence band, and matched features.

## Design notes

The scoring model is intentionally simple. It is suitable for a technical portfolio demonstration, not for making real commercial, employment, healthcare, or financial decisions. A production system would add data validation, privacy controls, calibration against labeled outcomes, monitoring, and human review.

## Repository provenance

This repository is original work created for a portfolio demonstration. It uses synthetic records and does not claim affiliation with any employer, client, or third-party project. The design is informed by common entity-resolution and recommendation patterns in public engineering literature and open-source systems, but the code here was written independently.

## License

MIT. See [LICENSE](LICENSE).
