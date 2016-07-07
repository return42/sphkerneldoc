.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/ocb.c

.. _`ocb_deferred_task_flags`:

enum ocb_deferred_task_flags
============================

.. c:type:: enum ocb_deferred_task_flags

    mac80211 OCB deferred tasks

.. _`ocb_deferred_task_flags.definition`:

Definition
----------

.. code-block:: c

    enum ocb_deferred_task_flags {
        OCB_WORK_HOUSEKEEPING
    };

.. _`ocb_deferred_task_flags.constants`:

Constants
---------

OCB_WORK_HOUSEKEEPING
    run the periodic OCB housekeeping tasks

.. _`ocb_deferred_task_flags.description`:

Description
-----------

These flags are used in \ ``wrkq_flags``\  field of \ :c:type:`struct ieee80211_if_ocb <ieee80211_if_ocb>`\ 

.. This file was automatic generated / don't edit.

