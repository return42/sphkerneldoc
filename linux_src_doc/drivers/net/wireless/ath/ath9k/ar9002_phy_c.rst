.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/ar9002_phy.c

.. _`programming-atheros-802.11n-analog-front-end-radios`:

Programming Atheros 802.11n analog front end radios
===================================================

AR5416 MAC based PCI devices and AR518 MAC based PCI-Express
devices have either an external AR2133 analog front end radio for single
band 2.4 GHz communication or an AR5133 analog front end radio for dual
band 2.4 GHz / 5 GHz communication.

All devices after the AR5416 and AR5418 family starting with the AR9280
have their analog front radios, MAC/BB and host PCIe/USB interface embedded
into a single-chip and require less programming.

The following single-chips exist with a respective embedded radio:

AR9280 - 11n dual-band 2x2 MIMO for PCIe
AR9281 - 11n single-band 1x2 MIMO for PCIe
AR9285 - 11n single-band 1x1 for PCIe
AR9287 - 11n single-band 2x2 MIMO for PCIe

AR9220 - 11n dual-band 2x2 MIMO for PCI
AR9223 - 11n single-band 2x2 MIMO for PCI

AR9287 - 11n single-band 1x1 MIMO for USB

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

