.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_base.c

.. _`module_author`:

MODULE_AUTHOR
=============

.. c:function::  MODULE_AUTHOR("Frank Haverkamp <haver@linux.vnet.ibm.com>")

.. _`module_author.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`module_author.author`:

Author
------

Frank Haverkamp <haver@linux.vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt@de.ibm.com>

Michael Jung <mijung@gmx.net>

Michael Ruettger <michael@ibmra.de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 2 only)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`genwqe_dev_alloc`:

genwqe_dev_alloc
================

.. c:function:: struct genwqe_dev *genwqe_dev_alloc( void)

    Create and prepare a new card descriptor

    :param void:
        no arguments
    :type void: 

.. _`genwqe_dev_alloc.return`:

Return
------

Pointer to card descriptor, or ERR_PTR(err) on error

.. _`genwqe_bus_reset`:

genwqe_bus_reset
================

.. c:function:: int genwqe_bus_reset(struct genwqe_dev *cd)

    Card recovery

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_bus_reset.description`:

Description
-----------

\ :c:func:`pci_reset_function`\  will recover the device and ensure that the
registers are accessible again when it completes with success. If
not, the card will stay dead and registers will be unaccessible
still.

.. _`genwqe_recovery_on_fatal_gfir_required`:

genwqe_recovery_on_fatal_gfir_required
======================================

.. c:function:: int genwqe_recovery_on_fatal_gfir_required(struct genwqe_dev *cd)

    Version depended actions

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_recovery_on_fatal_gfir_required.description`:

Description
-----------

Bitstreams older than 2013-02-17 have a bug where fatal GFIRs must
be ignored. This is e.g. true for the bitstream we gave to the card
manufacturer, but also for some old bitstreams we released to our
test-lab.

.. _`genwqe_t_psec`:

genwqe_T_psec
=============

.. c:function:: int genwqe_T_psec(struct genwqe_dev *cd)

    Calculate PF/VF timeout register content

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_t_psec.note`:

Note
----

From a design perspective it turned out to be a bad idea to
use codes here to specifiy the frequency/speed values. An old
driver cannot understand new codes and is therefore always a
problem. Better is to measure out the value or put the
speed/frequency directly into a register which is always a valid
value for old as well as for new software.

.. _`genwqe_setup_pf_jtimer`:

genwqe_setup_pf_jtimer
======================

.. c:function:: bool genwqe_setup_pf_jtimer(struct genwqe_dev *cd)

    Setup PF hardware timeouts for DDCB execution

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_setup_pf_jtimer.description`:

Description
-----------

Do this \_after\_ \ :c:func:`card_reset`\  is called. Otherwise the values will
vanish. The settings need to be done when the queues are inactive.

The max. timeout value is 2^(10+x) \* T (6ns for 166MHz) \* 15/16.
The min. timeout value is 2^(10+x) \* T (6ns for 166MHz) \* 14/16.

.. _`genwqe_setup_vf_jtimer`:

genwqe_setup_vf_jtimer
======================

.. c:function:: bool genwqe_setup_vf_jtimer(struct genwqe_dev *cd)

    Setup VF hardware timeouts for DDCB execution

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_stop`:

genwqe_stop
===========

.. c:function:: int genwqe_stop(struct genwqe_dev *cd)

    Stop card operation

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_stop.recovery-notes`:

Recovery notes
--------------

As long as genwqe_thread runs we might access registers during
error data capture. Same is with the genwqe_health_thread.
When \ :c:func:`genwqe_bus_reset`\  fails this function might called two times:
first by the \ :c:func:`genwqe_health_thread`\  and later by \ :c:func:`genwqe_remove`\  to
unbind the device. We must be able to survive that.

This function must be robust enough to be called twice.

.. _`genwqe_recover_card`:

genwqe_recover_card
===================

.. c:function:: int genwqe_recover_card(struct genwqe_dev *cd, int fatal_err)

    Try to recover the card if it is possible

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

    :param fatal_err:
        *undescribed*
    :type fatal_err: int

.. _`genwqe_recover_card.description`:

Description
-----------

If fatal_err is set no register access is possible anymore. It is
likely that genwqe_start fails in that situation. Proper error
handling is required in this case.

\ :c:func:`genwqe_bus_reset`\  will cause the pci code to call \ :c:func:`genwqe_remove`\ 
and later \ :c:func:`genwqe_probe`\  for all virtual functions.

.. _`genwqe_fir_checking`:

genwqe_fir_checking
===================

.. c:function:: u64 genwqe_fir_checking(struct genwqe_dev *cd)

    Check the fault isolation registers of the card

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_fir_checking.description`:

Description
-----------

If this code works ok, can be tried out with help of the genwqe_poke tool:
sudo ./tools/genwqe_poke 0x8 0xfefefefefef

Now the relevant FIRs/sFIRs should be printed out and the driver should
invoke recovery (devices are removed and readded).

.. _`genwqe_pci_fundamental_reset`:

genwqe_pci_fundamental_reset
============================

.. c:function:: int genwqe_pci_fundamental_reset(struct pci_dev *pci_dev)

    trigger a PCIe fundamental reset on the slot

    :param pci_dev:
        *undescribed*
    :type pci_dev: struct pci_dev \*

.. _`genwqe_pci_fundamental_reset.note`:

Note
----

\ :c:func:`pci_set_pcie_reset_state`\  is not implemented on all archs, so this
reset method will not work in all cases.

.. _`genwqe_pci_fundamental_reset.return`:

Return
------

0 on success or error code from \ :c:func:`pci_set_pcie_reset_state`\ 

.. _`genwqe_health_thread`:

genwqe_health_thread
====================

.. c:function:: int genwqe_health_thread(void *data)

    Health checking thread

    :param data:
        *undescribed*
    :type data: void \*

.. _`genwqe_health_thread.description`:

Description
-----------

This thread is only started for the PF of the card.

This thread monitors the health of the card. A critical situation
is when we read registers which contain -1 (IO_ILLEGAL_VALUE). In
this case we need to be recovered from outside. Writing to
registers will very likely not work either.

This thread must only exit if \ :c:func:`kthread_should_stop`\  becomes true.

Condition for the health-thread to trigger:
a) when a \ :c:func:`kthread_stop`\  request comes in or
b) a critical GFIR occured

Informational GFIRs are checked and potentially printed in
GENWQE_HEALTH_CHECK_INTERVAL seconds.

.. _`genwqe_pci_setup`:

genwqe_pci_setup
================

.. c:function:: int genwqe_pci_setup(struct genwqe_dev *cd)

    Allocate PCIe related resources for our card

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_pci_remove`:

genwqe_pci_remove
=================

.. c:function:: void genwqe_pci_remove(struct genwqe_dev *cd)

    Free PCIe related resources for our card

    :param cd:
        *undescribed*
    :type cd: struct genwqe_dev \*

.. _`genwqe_probe`:

genwqe_probe
============

.. c:function:: int genwqe_probe(struct pci_dev *pci_dev, const struct pci_device_id *id)

    Device initialization

    :param pci_dev:
        *undescribed*
    :type pci_dev: struct pci_dev \*

    :param id:
        *undescribed*
    :type id: const struct pci_device_id \*

.. _`genwqe_probe.description`:

Description
-----------

Callable for multiple cards. This function is called on bind.

.. _`genwqe_probe.return`:

Return
------

0 if succeeded, < 0 when failed

.. _`genwqe_remove`:

genwqe_remove
=============

.. c:function:: void genwqe_remove(struct pci_dev *pci_dev)

    Called when device is removed (hot-plugable)

    :param pci_dev:
        *undescribed*
    :type pci_dev: struct pci_dev \*

.. _`genwqe_remove.description`:

Description
-----------

Or when driver is unloaded respecitively when unbind is done.

.. _`genwqe_devnode`:

genwqe_devnode
==============

.. c:function:: char *genwqe_devnode(struct device *dev, umode_t *mode)

    Set default access mode for genwqe devices.

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param mode:
        *undescribed*
    :type mode: umode_t \*

.. _`genwqe_devnode.description`:

Description
-----------

Default mode should be rw for everybody. Do not change default
device name.

.. _`genwqe_init_module`:

genwqe_init_module
==================

.. c:function:: int genwqe_init_module( void)

    Driver registration and initialization

    :param void:
        no arguments
    :type void: 

.. _`genwqe_exit_module`:

genwqe_exit_module
==================

.. c:function:: void __exit genwqe_exit_module( void)

    Driver exit

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

