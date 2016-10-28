.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/cosm/cosm_main.h

.. _`cosm_msg_id`:

enum cosm_msg_id
================

.. c:type:: enum cosm_msg_id


.. _`cosm_msg_id.definition`:

Definition
----------

.. code-block:: c

    enum cosm_msg_id {
        COSM_MSG_SHUTDOWN,
        COSM_MSG_SYNC_TIME,
        COSM_MSG_HEARTBEAT,
        COSM_MSG_SHUTDOWN_STATUS
    };

.. _`cosm_msg_id.constants`:

Constants
---------

COSM_MSG_SHUTDOWN
    host->card trigger shutdown

COSM_MSG_SYNC_TIME
    host->card send host time to card to sync time

COSM_MSG_HEARTBEAT
    card->host heartbeat

COSM_MSG_SHUTDOWN_STATUS
    card->host with shutdown status as payload

.. This file was automatic generated / don't edit.

