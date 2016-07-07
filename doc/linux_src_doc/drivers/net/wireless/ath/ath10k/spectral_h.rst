.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath10k/spectral.h

.. _`ath10k_spec_scan`:

struct ath10k_spec_scan
=======================

.. c:type:: struct ath10k_spec_scan

    parameters for Atheros spectral scan

.. _`ath10k_spec_scan.definition`:

Definition
----------

.. code-block:: c

    struct ath10k_spec_scan {
        u8 count;
        u8 fft_size;
    }

.. _`ath10k_spec_scan.members`:

Members
-------

count
    number of scan results requested for manual mode

fft_size
    number of bins to be requested = 2^(fft_size - bin_scale)

.. This file was automatic generated / don't edit.

