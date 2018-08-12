.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/omap_dmm_tiler.c

.. _`dmm_txn_init`:

dmm_txn_init
============

.. c:function:: struct dmm_txn *dmm_txn_init(struct dmm *dmm, struct tcm *tcm)

    :param struct dmm \*dmm:
        *undescribed*

    :param struct tcm \*tcm:
        *undescribed*

.. _`dmm_txn_append`:

dmm_txn_append
==============

.. c:function:: void dmm_txn_append(struct dmm_txn *txn, struct pat_area *area, struct page **pages, u32 npages, u32 roll)

    corresponding slot is cleared (ie. dummy_pa is programmed)

    :param struct dmm_txn \*txn:
        *undescribed*

    :param struct pat_area \*area:
        *undescribed*

    :param struct page \*\*pages:
        *undescribed*

    :param u32 npages:
        *undescribed*

    :param u32 roll:
        *undescribed*

.. _`dmm_txn_commit`:

dmm_txn_commit
==============

.. c:function:: int dmm_txn_commit(struct dmm_txn *txn, bool wait)

    :param struct dmm_txn \*txn:
        *undescribed*

    :param bool wait:
        *undescribed*

.. This file was automatic generated / don't edit.

