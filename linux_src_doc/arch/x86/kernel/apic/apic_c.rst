.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/apic/apic.c

.. _`get_physical_broadcast`:

get_physical_broadcast
======================

.. c:function:: int get_physical_broadcast( void)

    Get number of physical broadcast IDs

    :param void:
        no arguments
    :type void: 

.. _`lapic_get_maxlvt`:

lapic_get_maxlvt
================

.. c:function:: int lapic_get_maxlvt( void)

    get the maximum number of local vector table entries

    :param void:
        no arguments
    :type void: 

.. _`clear_local_apic`:

clear_local_APIC
================

.. c:function:: void clear_local_APIC( void)

    shutdown the local APIC

    :param void:
        no arguments
    :type void: 

.. _`clear_local_apic.description`:

Description
-----------

This is called, when a CPU is disabled and before rebooting, so the state of
the local APIC has no dangling leftovers. Also used to cleanout any BIOS
leftovers during boot.

.. _`disable_local_apic`:

disable_local_APIC
==================

.. c:function:: void disable_local_APIC( void)

    clear and disable the local APIC

    :param void:
        no arguments
    :type void: 

.. _`sync_arb_ids`:

sync_Arb_IDs
============

.. c:function:: void sync_Arb_IDs( void)

    synchronize APIC bus arbitration IDs

    :param void:
        no arguments
    :type void: 

.. _`setup_local_apic`:

setup_local_APIC
================

.. c:function:: void setup_local_APIC( void)

    setup the local APIC

    :param void:
        no arguments
    :type void: 

.. _`setup_local_apic.description`:

Description
-----------

Used to setup local APIC while initializing BSP or bringing up APs.
Always called with preemption disabled.

.. _`init_apic_mappings`:

init_apic_mappings
==================

.. c:function:: void init_apic_mappings( void)

    initialize APIC mappings

    :param void:
        no arguments
    :type void: 

.. _`connect_bsp_apic`:

connect_bsp_APIC
================

.. c:function:: void connect_bsp_APIC( void)

    attach the APIC to the interrupt system

    :param void:
        no arguments
    :type void: 

.. _`disconnect_bsp_apic`:

disconnect_bsp_APIC
===================

.. c:function:: void disconnect_bsp_APIC(int virt_wire_setup)

    detach the APIC from the interrupt system

    :param virt_wire_setup:
        indicates, whether virtual wire mode is selected
    :type virt_wire_setup: int

.. _`disconnect_bsp_apic.description`:

Description
-----------

Virtual wire mode is necessary to deliver legacy interrupts even when the
APIC is disabled.

.. _`apic_id_is_primary_thread`:

apic_id_is_primary_thread
=========================

.. c:function:: bool apic_id_is_primary_thread(unsigned int apicid)

    Check whether APIC ID belongs to a primary thread

    :param apicid:
        *undescribed*
    :type apicid: unsigned int

.. _`apic_bsp_setup`:

apic_bsp_setup
==============

.. c:function:: void apic_bsp_setup(bool upmode)

    Setup function for local apic and io-apic

    :param upmode:
        Force UP mode (for APIC_init_uniprocessor)
    :type upmode: bool

.. _`apic_bsp_setup.return`:

Return
------

apic_id of BSP APIC

.. This file was automatic generated / don't edit.

