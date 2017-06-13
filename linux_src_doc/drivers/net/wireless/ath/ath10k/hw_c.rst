.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath10k/hw.c

.. _`ath10k_hw_qca6174_enable_pll_clock`:

ath10k_hw_qca6174_enable_pll_clock
==================================

.. c:function:: int ath10k_hw_qca6174_enable_pll_clock(struct ath10k *ar)

    enable the qca6174 hw pll clock

    :param struct ath10k \*ar:
        the ath10k blob

.. _`ath10k_hw_qca6174_enable_pll_clock.description`:

Description
-----------

This function is very hardware specific, the clock initialization
steps is very sensitive and could lead to unknown crash, so they
should be done in sequence.

\*\*\* Be aware if you planned to refactor them. \*\*\*

.. _`ath10k_hw_qca6174_enable_pll_clock.return`:

Return
------

0 if successfully enable the pll, otherwise EINVAL

.. This file was automatic generated / don't edit.

