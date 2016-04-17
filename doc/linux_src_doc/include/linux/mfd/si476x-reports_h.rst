.. -*- coding: utf-8; mode: rst -*-

================
si476x-reports.h
================


.. _`si476x_rsq_status_report`:

struct si476x_rsq_status_report
===============================

.. c:type:: si476x_rsq_status_report

    structure containing received signal quality


.. _`si476x_rsq_status_report.definition`:

Definition
----------

.. code-block:: c

  struct si476x_rsq_status_report {
    __u8 multhint;
    __u8 multlint;
    __u8 snrhint;
    __u8 snrlint;
    __u8 rssihint;
    __u8 rssilint;
    __u8 bltf;
    __u8 snr_ready;
    __u8 rssiready;
    __u8 afcrl;
    __u8 valid;
    __u16 readfreq;
    __s8 freqoff;
    __s8 rssi;
    __s8 snr;
    __s8 hassi;
    __s8 mult;
    __u8 dev;
    __u16 readantcap;
    __s8 assi;
    __s8 usn;
  };


.. _`si476x_rsq_status_report.members`:

Members
-------

:``multhint``:
    Multipath Detect High.
    true  - Indicatedes that the value is below
    FM_RSQ_MULTIPATH_HIGH_THRESHOLD
    false - Indicatedes that the value is above
    FM_RSQ_MULTIPATH_HIGH_THRESHOLD

:``multlint``:
    Multipath Detect Low.
    true  - Indicatedes that the value is below
    FM_RSQ_MULTIPATH_LOW_THRESHOLD
    false - Indicatedes that the value is above
    FM_RSQ_MULTIPATH_LOW_THRESHOLD

:``snrhint``:
    SNR Detect High.
    true  - Indicatedes that the value is below
    FM_RSQ_SNR_HIGH_THRESHOLD
    false - Indicatedes that the value is above
    FM_RSQ_SNR_HIGH_THRESHOLD

:``snrlint``:
    SNR Detect Low.
    true  - Indicatedes that the value is below
    FM_RSQ_SNR_LOW_THRESHOLD
    false - Indicatedes that the value is above
    FM_RSQ_SNR_LOW_THRESHOLD

:``rssihint``:
    RSSI Detect High.
    true  - Indicatedes that the value is below
    FM_RSQ_RSSI_HIGH_THRESHOLD
    false - Indicatedes that the value is above
    FM_RSQ_RSSI_HIGH_THRESHOLD

:``rssilint``:
    RSSI Detect Low.
    true  - Indicatedes that the value is below
    FM_RSQ_RSSI_LOW_THRESHOLD
    false - Indicatedes that the value is above
    FM_RSQ_RSSI_LOW_THRESHOLD

:``bltf``:
    Band Limit.
    Set if seek command hits the band limit or wrapped to
    the original frequency.

:``snr_ready``:
    SNR measurement in progress.

:``rssiready``:
    RSSI measurement in progress.

:``afcrl``:
    Set if FREQOFF >= MAX_TUNE_ERROR

:``valid``:
    Set if the channel is valid
    rssi < FM_VALID_RSSI_THRESHOLD
    snr  < FM_VALID_SNR_THRESHOLD
    tune_error < FM_VALID_MAX_TUNE_ERROR

:``readfreq``:
    Current tuned frequency.

:``freqoff``:
    Signed frequency offset.

:``rssi``:
    Received Signal Strength Indicator(dBuV).

:``snr``:
    RF SNR Indicator(dB).

:``hassi``:
    Low/High side Adjacent(100 kHz) Channel Strength Indicator

:``mult``:
    Multipath indicator

:``dev``:
    Who knows? But values may vary.

:``readantcap``:
    Antenna tuning capacity value.

:``assi``:
    Adjacent Channel(+/- 200kHz) Strength Indicator

:``usn``:
    Ultrasonic Noise Inticator in -DBFS


