.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath9k/ath9k.h

.. _`buffer_type`:

enum buffer_type
================

.. c:type:: enum buffer_type

    Buffer type flags

.. _`buffer_type.definition`:

Definition
----------

.. code-block:: c

    enum buffer_type {
        BUF_AMPDU,
        BUF_AGGR
    };

.. _`buffer_type.constants`:

Constants
---------

BUF_AMPDU
    This buffer is an ampdu, as part of an aggregate (during TX)

BUF_AGGR
    Indicates whether the buffer can be aggregated
    (used in aggregation scheduling)

.. This file was automatic generated / don't edit.

