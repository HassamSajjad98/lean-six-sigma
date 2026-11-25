# Lean Six Sigma | Precision shaft machining
Independent simulated DMAIC case study. No employer data or real achieved savings. 500 consecutive synthetic measurements per phase (100 subgroups of five), plus independent ten-shift operating samples per phase. Seed 42; generation assumptions in generate_data.py.

## Define
CTQ: diameter 25 ± 0.05 mm, surface finish and burr-free edges. Scope: incoming blanks through CNC machining, inspection and release. Sponsor: operations manager; owner: manufacturing engineer. Targets: defects <2%, OEE >80%, Cpk ≥1.33, downtime reduction ≥30%, quality cost reduction ≥50%.

SIPOC: steel supplier → blanks, drawings, tools → setup, turn, deburr, inspect → accepted shafts → motor assembly customer.

## Measure
Measurements.csv records mutually exclusive first-failure categories; diameter outside limits takes precedence. Production.csv is a separate operating sample; its quality rate need not equal the inspection sample. Ideal cycle 0.6 min/unit; 480 planned minutes/shift. In practice validate gauge R&R, calibration, sampling and defect definitions before capability analysis.

## Analyse
Baseline: 45/500 defective, 31 oversize, 8 surface finish, 6 burr. Hypothesised causes (not experimentally established): worn inserts, offset errors, clamping variation, coolant and deburring. Five Whys hypothesis: oversize → tool offset drift → wear compensation not updated → no standard check → absent ownership in control plan. Test with tool-life logs, offset trials and measurement-system validation.

Cp=(USL−LSL)/(6 sigma), Cpk=min(USL−mean,mean−LSL)/(3 sigma); sigma=mean subgroup range/2.326. Ppk uses overall sample standard deviation. X-bar limits = grand mean ±0.577 mean range; R limits=0 and 2.114 mean range. Limits fitted separately for each phase; points outside limits require investigation; no complete run-rule or normality validation performed.

OEE = availability × performance × quality; availability=run/planned time; performance=ideal cycle×total/run time; quality=good/total. Aggregate shift counts and times before computing ratios.

## Improve
Modelled intervention: centre tool offsets, standardise setup, replace inserts at validated wear thresholds, preventive maintenance, deburr checks. Synthetic improved distribution was deliberately generated with lower variation and closer centring; this is a scenario, not causal evidence. Proposed validation: pilot across operators and shifts, compare defect proportions and downtime, confirm repeatability and customer approval.

## Control
| Control | Frequency | Owner | Reaction |
|---|---|---|---|
| Diameter X-bar/R | 5 sequential pieces hourly | Quality technician | Hold affected lot, verify gauge, investigate and adjust only after cause confirmed |
| Tool wear | Each setup / validated tool life | CNC operator | Replace insert, verify first piece |
| OEE and downtime | Every shift | Production lead | Escalate repeat losses and assign action |
| Defect Pareto | Weekly | Quality engineer | Review corrective actions |
| Capability | Monthly after stability review | Process engineer | Investigate if Cpk <1.33 |

## Results and economics
Defects 9.0% → 0.8%; OEE 57.35% → 81.75%; Cpk 0.538 → 1.745; downtime 1206 → 610 minutes. At 100,000 units/year and €18 average avoidable cost per defective unit, annual gross savings €147,600; assumed one-time investment €12,000; simple payback 0.98 months. No recurring cost, tax, throughput revenue or downtime savings included. Validate costs and extrapolation before business use.

## Run
Open index.html directly or deploy with GitHub Pages. No server or external dependencies. Run `python analysis.py` for reproducible metrics from CSV; `python generate_data.py` regenerates the synthetic inputs and embedded dashboard metrics (then rebuild dashboard via build_dashboard.py). Dashboard is a snapshot with interactive phase selection and financial assumptions; CSV edits require rebuilding. 
