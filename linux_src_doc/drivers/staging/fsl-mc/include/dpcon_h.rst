.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dpcon.h

.. _`dpcon_invalid_dpio_id`:

DPCON_INVALID_DPIO_ID
=====================

.. c:function::  DPCON_INVALID_DPIO_ID()

.. _`dpcon_attr`:

struct dpcon_attr
=================

.. c:type:: struct dpcon_attr

    Structure representing DPCON attributes

.. _`dpcon_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpcon_attr {
        int id;
        u16 qbman_ch_id;
        u8 num_priorities;
    }

.. _`dpcon_attr.members`:

Members
-------

id
    DPCON object ID

qbman_ch_id
    Channel ID to be used by dequeue operation

num_priorities
    Number of priorities for the DPCON channel (1-8)

.. _`dpcon_notification_cfg`:

struct dpcon_notification_cfg
=============================

.. c:type:: struct dpcon_notification_cfg

    Structure representing notification params

.. _`dpcon_notification_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpcon_notification_cfg {
        int dpio_id;
        u8 priority;
        u64 user_ctx;
    }

.. _`dpcon_notification_cfg.members`:

Members
-------

dpio_id
    DPIO object ID; must be configured with a notification channel;
    to disable notifications set it to 'DPCON_INVALID_DPIO_ID';

priority
    Priority selection within the DPIO channel; valid values
    are 0-7, depending on the number of priorities in that channel

user_ctx
    User context value provided with each CDAN message

.. This file was automatic generated / don't edit.

