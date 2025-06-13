# MSCardio Seismocardiography Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15657893.svg)](https://doi.org/10.5281/zenodo.15657893)

## Overview

The **MSCardio Seismocardiography Dataset** is an open-access dataset collected as part of the Mississippi State Remote Cardiovascular Monitoring (MSCardio) study. This dataset includes seismocardiogram (SCG) signals recorded from participants using smartphone sensors, enabling scalable, real-world cardiovascular monitoring without requiring specialized equipment. The dataset aims to support research in SCG signal processing, machine learning applications in health monitoring, and cardiovascular assessment.

## Background

Cardiovascular diseases remain the leading cause of morbidity and mortality worldwide. SCG is a non-invasive technique that captures chest vibrations induced by cardiac activity and respiration, providing valuable insights into cardiac function. However, the scarcity of open-access SCG datasets has been a significant limitation for research in this field. The **MSCardio dataset** addresses this gap by providing real-world SCG signals collected via smartphone sensors from a diverse population.

## Data Description

### Study Population

- **Total participants enrolled**: 123
- **Participants who uploaded data**: 108 (46 males, 61 females, 1 unspecified)
- **Age range**: 18 to 62 years
- **Total recordings uploaded**: 515
- **Unique recordings after duplicate removal**: 502
- **Platforms used**: iOS and Android smartphones

### Signal Data

- Axial vibrations in three directions (SCG) recorded using smartphone sensors
- Sampling frequency varies depending on the device capabilities
- Data synchronization is ensured for temporal accuracy
- Missing SCG data identified in certain recordings, addressed through preprocessing

### Metadata

Each recording includes:

- **Device model** (e.g., iPhone Pro Max)
- **Recording time** (UTC) and time zone
- **Platform** (iOS or Android)
- **General demographic details** (gender, race, age, height, weight)

### File Structure

The dataset is organized as follows:

```
MSCardio_SCG_Dataset/
│── info/
│   └── all_subject_data.csv             # Consolidated metadata for all subjects
│── MSCardio/
│   ├── Subject_XXXX/                    # Subject-specific folder
│   │   ├── general_metadata.json        # Demographic and device information
│   │   ├── Recording_XXX/               # Individual recordings
│   │   │   ├── scg.csv                  # SCG signal
│   │   │   ├── uncalibrated_scg.csv     # Raw SCG signal
│   │   │   ├── recording_metadata.json  # Timestamp and device details
```

## Data Collection Protocol

- Participants placed their smartphone on their chest while lying in a supine position.
- The app recorded SCG signals for approximately two minutes.
- Self-reported demographic data were collected.
- Data were uploaded to the study's cloud storage.

## Usage and Applications

This dataset is intended for research in:

- SCG signal processing and feature extraction
- Machine learning applications in cardiovascular monitoring
- Investigating inter- and intra-subject variability in SCG signals
- Remote cardiovascular health assessment
- The `Data_visualization.py` script is provided for data visualization

## Citation

If you use this dataset in your research, please cite:

```
@article{rahman2025MSCardio,
  author    = {Taebi, Amirtah{\`a} and Rahman, Mohammad Muntasir},
  title     = {MSCardio: Initial insights from remote monitoring of cardiovascular-induced chest vibrations via smartphones},
  journal   = {Data in Brief},
  year      = {2025},
  publisher = {Elsevier}
}
```

## Contact

For any questions regarding the dataset, please contact:

- Amirtahà Taebi and Mohammad Muntasir Rahman
- **E-mail**: ataebi@abe.msstate.edu, mmr510@msstate.edu
- Biomedical Engineering Program, Mississippi State University

---

This dataset is provided under an open-access license. Please ensure ethical and responsible use when utilizing this dataset for research.

