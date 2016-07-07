.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/ar5008_phy.c

.. _`ar5008_hw_phy_modify_rx_buffer`:

ar5008_hw_phy_modify_rx_buffer
==============================

.. c:function:: void ar5008_hw_phy_modify_rx_buffer(u32 *rfBuf, u32 reg32, u32 numBits, u32 firstBit, u32 column)

    perform analog swizzling of parameters

    :param u32 \*rfBuf:
        *undescribed*

    :param u32 reg32:
        *undescribed*

    :param u32 numBits:
        *undescribed*

    :param u32 firstBit:
        *undescribed*

    :param u32 column:
        *undescribed*

.. _`ar5008_hw_phy_modify_rx_buffer.description`:

Description
-----------

Performs analog "swizzling" of parameters into their location.
Used on external AR2133/AR5133 radios.

.. _`ar5008_hw_set_channel`:

ar5008_hw_set_channel
=====================

.. c:function:: int ar5008_hw_set_channel(struct ath_hw *ah, struct ath9k_channel *chan)

    tune to a channel on the external AR2133/AR5133 radios

    :param struct ath_hw \*ah:
        atheros hardware structure

    :param struct ath9k_channel \*chan:
        *undescribed*

.. _`ar5008_hw_set_channel.description`:

Description
-----------

For the external AR2133/AR5133 radios, takes the MHz channel value and set
the channel value. Assumes writes enabled to analog bus and bank6 register
cache in ah->analogBank6Data.

.. _`ar5008_hw_spur_mitigate`:

ar5008_hw_spur_mitigate
=======================

.. c:function:: void ar5008_hw_spur_mitigate(struct ath_hw *ah, struct ath9k_channel *chan)

    convert baseband spur frequency for external radios

    :param struct ath_hw \*ah:
        atheros hardware structure

    :param struct ath9k_channel \*chan:
        *undescribed*

.. _`ar5008_hw_spur_mitigate.description`:

Description
-----------

For non single-chip solutions. Converts to baseband spur frequency given the
input channel frequency and compute register settings below.

.. _`ar5008_hw_rf_alloc_ext_banks`:

ar5008_hw_rf_alloc_ext_banks
============================

.. c:function:: int ar5008_hw_rf_alloc_ext_banks(struct ath_hw *ah)

    allocates banks for external radio programming

    :param struct ath_hw \*ah:
        atheros hardware structure

.. _`ar5008_hw_rf_alloc_ext_banks.description`:

Description
-----------

Only required for older devices with external AR2133/AR5133 radios.

.. This file was automatic generated / don't edit.

