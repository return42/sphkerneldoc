.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpio/dpio.h

.. _`dpio_channel_mode`:

enum dpio_channel_mode
======================

.. c:type:: enum dpio_channel_mode

    DPIO notification channel mode

.. _`dpio_channel_mode.definition`:

Definition
----------

.. code-block:: c

    enum dpio_channel_mode {
        DPIO_NO_CHANNEL,
        DPIO_LOCAL_CHANNEL
    };

.. _`dpio_channel_mode.constants`:

Constants
---------

DPIO_NO_CHANNEL
    No support for notification channel

DPIO_LOCAL_CHANNEL
    Notifications on data availability can be received by a
    dedicated channel in the DPIO; user should point the queue's
    destination in the relevant interface to this DPIO

.. _`dpio_cfg`:

struct dpio_cfg
===============

.. c:type:: struct dpio_cfg

    Structure representing DPIO configuration

.. _`dpio_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpio_cfg {
        enum dpio_channel_mode channel_mode;
        u8 num_priorities;
    }

.. _`dpio_cfg.members`:

Members
-------

channel_mode
    Notification channel mode

num_priorities
    Number of priorities for the notification channel (1-8);
    relevant only if 'channel_mode = DPIO_LOCAL_CHANNEL'

.. _`dpio_attr`:

struct dpio_attr
================

.. c:type:: struct dpio_attr

    Structure representing DPIO attributes

.. _`dpio_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpio_attr {
        int id;
        u64 qbman_portal_ce_offset;
        u64 qbman_portal_ci_offset;
        u16 qbman_portal_id;
        enum dpio_channel_mode channel_mode;
        u8 num_priorities;
        u32 qbman_version;
    }

.. _`dpio_attr.members`:

Members
-------

id
    DPIO object ID

qbman_portal_ce_offset
    offset of the software portal cache-enabled area

qbman_portal_ci_offset
    offset of the software portal cache-inhibited area

qbman_portal_id
    Software portal ID

channel_mode
    Notification channel mode

num_priorities
    Number of priorities for the notification channel (1-8);
    relevant only if 'channel_mode = DPIO_LOCAL_CHANNEL'

qbman_version
    QBMAN version

.. This file was automatic generated / don't edit.

