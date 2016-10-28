.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hbm.h

.. _`mei_hbm_state`:

enum mei_hbm_state
==================

.. c:type:: enum mei_hbm_state

    host bus message protocol state

.. _`mei_hbm_state.definition`:

Definition
----------

.. code-block:: c

    enum mei_hbm_state {
        MEI_HBM_IDLE,
        MEI_HBM_STARTING,
        MEI_HBM_ENUM_CLIENTS,
        MEI_HBM_CLIENT_PROPERTIES,
        MEI_HBM_STARTED,
        MEI_HBM_STOPPED
    };

.. _`mei_hbm_state.constants`:

Constants
---------

MEI_HBM_IDLE
    protocol not started

MEI_HBM_STARTING
    start request message was sent

MEI_HBM_ENUM_CLIENTS
    enumeration request was sent

MEI_HBM_CLIENT_PROPERTIES
    acquiring clients properties

MEI_HBM_STARTED
    enumeration was completed

MEI_HBM_STOPPED
    stopping exchange

.. This file was automatic generated / don't edit.

