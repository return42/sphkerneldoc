.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/appletouch.c

.. _`atp_status_bits`:

enum atp_status_bits
====================

.. c:type:: enum atp_status_bits

    status bit meanings

.. _`atp_status_bits.definition`:

Definition
----------

.. code-block:: c

    enum atp_status_bits {
        ATP_STATUS_BUTTON,
        ATP_STATUS_BASE_UPDATE,
        ATP_STATUS_FROM_RESET
    };

.. _`atp_status_bits.constants`:

Constants
---------

ATP_STATUS_BUTTON
    The button was pressed

ATP_STATUS_BASE_UPDATE
    Update of the base values (untouched pad)

ATP_STATUS_FROM_RESET
    Reset previously performed

.. _`atp_status_bits.description`:

Description
-----------

These constants represent the meaning of the status bits.
(only Geyser 3/4)

.. This file was automatic generated / don't edit.

