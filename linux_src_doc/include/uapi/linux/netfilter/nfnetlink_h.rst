.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/netfilter/nfnetlink.h

.. _`nfnl_batch_attributes`:

enum nfnl_batch_attributes
==========================

.. c:type:: enum nfnl_batch_attributes

    nfnetlink batch netlink attributes

.. _`nfnl_batch_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nfnl_batch_attributes {
        NFNL_BATCH_UNSPEC,
        NFNL_BATCH_GENID,
        __NFNL_BATCH_MAX
    };

.. _`nfnl_batch_attributes.constants`:

Constants
---------

NFNL_BATCH_UNSPEC
    *undescribed*

NFNL_BATCH_GENID
    generation ID for this changeset (NLA_U32)

__NFNL_BATCH_MAX
    *undescribed*

.. This file was automatic generated / don't edit.

