.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/can/platform/ti_hecc.h

.. _`ti_hecc_platform_data`:

struct ti_hecc_platform_data
============================

.. c:type:: struct ti_hecc_platform_data

    HECC Platform Data

.. _`ti_hecc_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_hecc_platform_data {
        u32 scc_hecc_offset;
        u32 scc_ram_offset;
        u32 hecc_ram_offset;
        u32 mbx_offset;
        u32 int_line;
        u32 version;
        void (*transceiver_switch)(int);
    }

.. _`ti_hecc_platform_data.members`:

Members
-------

scc_hecc_offset
    mostly 0 - should really never change

scc_ram_offset
    SCC RAM offset

hecc_ram_offset
    HECC RAM offset

mbx_offset
    Mailbox RAM offset

int_line
    Interrupt line to use - 0 or 1

version
    version for future use

transceiver_switch
    platform specific callback fn for transceiver control

.. _`ti_hecc_platform_data.description`:

Description
-----------

Platform data structure to get all platform specific settings.
this structure also accounts the fact that the IP may have different
RAM and mailbox offsets for different SOC's

.. This file was automatic generated / don't edit.

