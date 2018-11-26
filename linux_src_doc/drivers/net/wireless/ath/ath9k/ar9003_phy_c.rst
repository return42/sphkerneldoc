.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/ar9003_phy.c

.. _`ar9003_hw_set_channel`:

ar9003_hw_set_channel
=====================

.. c:function:: int ar9003_hw_set_channel(struct ath_hw *ah, struct ath9k_channel *chan)

    set channel on single-chip device

    :param ah:
        atheros hardware structure
    :type ah: struct ath_hw \*

    :param chan:
        *undescribed*
    :type chan: struct ath9k_channel \*

.. _`ar9003_hw_set_channel.description`:

Description
-----------

This is the function to change channel on single-chip devices, that is
for AR9300 family of chipsets.

This function takes the channel value in MHz and sets
hardware channel value. Assumes writes have been enabled to analog bus.

Actual Expression,

For 2GHz channel,
Channel Frequency = (3/4) \* freq_ref \* (chansel[8:0] + chanfrac[16:0]/2^17)
(freq_ref = 40MHz)

For 5GHz channel,
Channel Frequency = (3/2) \* freq_ref \* (chansel[8:0] + chanfrac[16:0]/2^10)
(freq_ref = 40MHz/(24>>amodeRefSel))

For 5GHz channels which are 5MHz spaced,
Channel Frequency = (3/2) \* freq_ref \* (chansel[8:0] + chanfrac[16:0]/2^17)
(freq_ref = 40MHz)

.. _`ar9003_hw_spur_mitigate_mrc_cck`:

ar9003_hw_spur_mitigate_mrc_cck
===============================

.. c:function:: void ar9003_hw_spur_mitigate_mrc_cck(struct ath_hw *ah, struct ath9k_channel *chan)

    convert baseband spur frequency

    :param ah:
        atheros hardware structure
    :type ah: struct ath_hw \*

    :param chan:
        *undescribed*
    :type chan: struct ath9k_channel \*

.. _`ar9003_hw_spur_mitigate_mrc_cck.description`:

Description
-----------

For single-chip solutions. Converts to baseband spur frequency given the
input channel frequency and compute register settings below.

Spur mitigation for MRC CCK

.. This file was automatic generated / don't edit.

