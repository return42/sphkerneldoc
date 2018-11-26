.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/omap_dmm_tiler.c

.. _`dmm_txn_init`:

dmm_txn_init
============

.. c:function:: struct dmm_txn *dmm_txn_init(struct dmm *dmm, struct tcm *tcm)

    :param dmm:
        *undescribed*
    :type dmm: struct dmm \*

    :param tcm:
        *undescribed*
    :type tcm: struct tcm \*

.. _`dmm_txn_append`:

dmm_txn_append
==============

.. c:function:: void dmm_txn_append(struct dmm_txn *txn, struct pat_area *area, struct page **pages, u32 npages, u32 roll)

    corresponding slot is cleared (ie. dummy_pa is programmed)

    :param txn:
        *undescribed*
    :type txn: struct dmm_txn \*

    :param area:
        *undescribed*
    :type area: struct pat_area \*

    :param pages:
        *undescribed*
    :type pages: struct page \*\*

    :param npages:
        *undescribed*
    :type npages: u32

    :param roll:
        *undescribed*
    :type roll: u32

.. _`dmm_txn_commit`:

dmm_txn_commit
==============

.. c:function:: int dmm_txn_commit(struct dmm_txn *txn, bool wait)

    :param txn:
        *undescribed*
    :type txn: struct dmm_txn \*

    :param wait:
        *undescribed*
    :type wait: bool

.. This file was automatic generated / don't edit.

