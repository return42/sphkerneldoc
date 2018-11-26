.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qualcomm/emac/emac.c

.. _`emac_update_hw_stats`:

emac_update_hw_stats
====================

.. c:function:: void emac_update_hw_stats(struct emac_adapter *adpt)

    read the EMAC stat registers

    :param adpt:
        *undescribed*
    :type adpt: struct emac_adapter \*

.. _`emac_update_hw_stats.description`:

Description
-----------

Reads the stats registers and write the values to adpt->stats.

adpt->stats.lock must be held while calling this function,
and while reading from adpt->stats.

.. This file was automatic generated / don't edit.

