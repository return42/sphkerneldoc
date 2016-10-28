.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/ar9002_phy.c

.. _`ar9002_hw_set_channel`:

ar9002_hw_set_channel
=====================

.. c:function:: int ar9002_hw_set_channel(struct ath_hw *ah, struct ath9k_channel *chan)

    set channel on single-chip device

    :param struct ath_hw \*ah:
        atheros hardware structure

    :param struct ath9k_channel \*chan:
        *undescribed*

.. _`ar9002_hw_set_channel.description`:

Description
-----------

This is the function to change channel on single-chip devices, that is
all devices after ar9280.

This function takes the channel value in MHz and sets
hardware channel value. Assumes writes have been enabled to analog bus.

Actual Expression,

For 2GHz channel,
Channel Frequency = (3/4) \* freq_ref \* (chansel[8:0] + chanfrac[16:0]/2^17)
(freq_ref = 40MHz)

For 5GHz channel,
Channel Frequency = (3/2) \* freq_ref \* (chansel[8:0] + chanfrac[16:0]/2^10)
(freq_ref = 40MHz/(24>>amodeRefSel))

.. _`ar9002_hw_spur_mitigate`:

ar9002_hw_spur_mitigate
=======================

.. c:function:: void ar9002_hw_spur_mitigate(struct ath_hw *ah, struct ath9k_channel *chan)

    convert baseband spur frequency

    :param struct ath_hw \*ah:
        atheros hardware structure

    :param struct ath9k_channel \*chan:
        *undescribed*

.. _`ar9002_hw_spur_mitigate.description`:

Description
-----------

For single-chip solutions. Converts to baseband spur frequency given the
input channel frequency and compute register settings below.

.. This file was automatic generated / don't edit.

