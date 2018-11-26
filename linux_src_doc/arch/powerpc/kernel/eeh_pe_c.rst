.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_pe.c

.. _`eeh_set_pe_aux_size`:

eeh_set_pe_aux_size
===================

.. c:function:: void eeh_set_pe_aux_size(int size)

    Set PE auxillary data size

    :param size:
        PE auxillary data size
    :type size: int

.. _`eeh_set_pe_aux_size.description`:

Description
-----------

Set PE auxillary data size

.. _`eeh_pe_alloc`:

eeh_pe_alloc
============

.. c:function:: struct eeh_pe *eeh_pe_alloc(struct pci_controller *phb, int type)

    Allocate PE

    :param phb:
        PCI controller
    :type phb: struct pci_controller \*

    :param type:
        PE type
    :type type: int

.. _`eeh_pe_alloc.description`:

Description
-----------

Allocate PE instance dynamically.

.. _`eeh_phb_pe_create`:

eeh_phb_pe_create
=================

.. c:function:: int eeh_phb_pe_create(struct pci_controller *phb)

    Create PHB PE

    :param phb:
        PCI controller
    :type phb: struct pci_controller \*

.. _`eeh_phb_pe_create.description`:

Description
-----------

The function should be called while the PHB is detected during
system boot or PCI hotplug in order to create PHB PE.

.. _`eeh_wait_state`:

eeh_wait_state
==============

.. c:function:: int eeh_wait_state(struct eeh_pe *pe, int max_wait)

    Wait for PE state

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param max_wait:
        maximal period in millisecond
    :type max_wait: int

.. _`eeh_wait_state.description`:

Description
-----------

Wait for the state of associated PE. It might take some time
to retrieve the PE's state.

.. _`eeh_phb_pe_get`:

eeh_phb_pe_get
==============

.. c:function:: struct eeh_pe *eeh_phb_pe_get(struct pci_controller *phb)

    Retrieve PHB PE based on the given PHB

    :param phb:
        PCI controller
    :type phb: struct pci_controller \*

.. _`eeh_phb_pe_get.description`:

Description
-----------

The overall PEs form hierarchy tree. The first layer of the
hierarchy tree is composed of PHB PEs. The function is used
to retrieve the corresponding PHB PE according to the given PHB.

.. _`eeh_pe_next`:

eeh_pe_next
===========

.. c:function:: struct eeh_pe *eeh_pe_next(struct eeh_pe *pe, struct eeh_pe *root)

    Retrieve the next PE in the tree

    :param pe:
        current PE
    :type pe: struct eeh_pe \*

    :param root:
        root PE
    :type root: struct eeh_pe \*

.. _`eeh_pe_next.description`:

Description
-----------

The function is used to retrieve the next PE in the
hierarchy PE tree.

.. _`eeh_pe_traverse`:

eeh_pe_traverse
===============

.. c:function:: void *eeh_pe_traverse(struct eeh_pe *root, eeh_pe_traverse_func fn, void *flag)

    Traverse PEs in the specified PHB

    :param root:
        root PE
    :type root: struct eeh_pe \*

    :param fn:
        callback
    :type fn: eeh_pe_traverse_func

    :param flag:
        extra parameter to callback
    :type flag: void \*

.. _`eeh_pe_traverse.description`:

Description
-----------

The function is used to traverse the specified PE and its
child PEs. The traversing is to be terminated once the
callback returns something other than NULL, or no more PEs
to be traversed.

.. _`eeh_pe_dev_traverse`:

eeh_pe_dev_traverse
===================

.. c:function:: void *eeh_pe_dev_traverse(struct eeh_pe *root, eeh_edev_traverse_func fn, void *flag)

    Traverse the devices from the PE

    :param root:
        EEH PE
    :type root: struct eeh_pe \*

    :param fn:
        function callback
    :type fn: eeh_edev_traverse_func

    :param flag:
        extra parameter to callback
    :type flag: void \*

.. _`eeh_pe_dev_traverse.description`:

Description
-----------

The function is used to traverse the devices of the specified
PE and its child PEs.

.. _`eeh_pe_get`:

eeh_pe_get
==========

.. c:function:: struct eeh_pe *eeh_pe_get(struct pci_controller *phb, int pe_no, int config_addr)

    Search PE based on the given address

    :param phb:
        PCI controller
    :type phb: struct pci_controller \*

    :param pe_no:
        PE number
    :type pe_no: int

    :param config_addr:
        Config address
    :type config_addr: int

.. _`eeh_pe_get.description`:

Description
-----------

Search the corresponding PE based on the specified address which
is included in the eeh device. The function is used to check if
the associated PE has been created against the PE address. It's

.. _`eeh_pe_get.notable-that-the-pe-address-has-2-format`:

notable that the PE address has 2 format
----------------------------------------

traditional PE address
which is composed of PCI bus/device/function number, or unified
PE address.

.. _`eeh_pe_get_parent`:

eeh_pe_get_parent
=================

.. c:function:: struct eeh_pe *eeh_pe_get_parent(struct eeh_dev *edev)

    Retrieve the parent PE

    :param edev:
        EEH device
    :type edev: struct eeh_dev \*

.. _`eeh_pe_get_parent.description`:

Description
-----------

The whole PEs existing in the system are organized as hierarchy
tree. The function is used to retrieve the parent PE according
to the parent EEH device.

.. _`eeh_add_to_parent_pe`:

eeh_add_to_parent_pe
====================

.. c:function:: int eeh_add_to_parent_pe(struct eeh_dev *edev)

    Add EEH device to parent PE

    :param edev:
        EEH device
    :type edev: struct eeh_dev \*

.. _`eeh_add_to_parent_pe.description`:

Description
-----------

Add EEH device to the parent PE. If the parent PE already
exists, the PE type will be changed to EEH_PE_BUS. Otherwise,
we have to create new PE to hold the EEH device and the new
PE will be linked to its parent PE as well.

.. _`eeh_rmv_from_parent_pe`:

eeh_rmv_from_parent_pe
======================

.. c:function:: int eeh_rmv_from_parent_pe(struct eeh_dev *edev)

    Remove one EEH device from the associated PE

    :param edev:
        EEH device
    :type edev: struct eeh_dev \*

.. _`eeh_rmv_from_parent_pe.description`:

Description
-----------

The PE hierarchy tree might be changed when doing PCI hotplug.
Also, the PCI devices or buses could be removed from the system
during EEH recovery. So we have to call the function remove the
corresponding PE accordingly if necessary.

.. _`eeh_pe_update_time_stamp`:

eeh_pe_update_time_stamp
========================

.. c:function:: void eeh_pe_update_time_stamp(struct eeh_pe *pe)

    Update PE's frozen time stamp

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`eeh_pe_update_time_stamp.description`:

Description
-----------

We have time stamp for each PE to trace its time of getting
frozen in last hour. The function should be called to update
the time stamp on first error of the specific PE. On the other
handle, we needn't account for errors happened in last hour.

.. _`eeh_pe_state_mark`:

eeh_pe_state_mark
=================

.. c:function:: void eeh_pe_state_mark(struct eeh_pe *root, int state)

    Mark specified state for PE and its associated device

    :param root:
        *undescribed*
    :type root: struct eeh_pe \*

    :param state:
        *undescribed*
    :type state: int

.. _`eeh_pe_state_mark.description`:

Description
-----------

EEH error affects the current PE and its child PEs. The function
is used to mark appropriate state for the affected PEs and the
associated devices.

.. _`eeh_pe_mark_isolated`:

eeh_pe_mark_isolated
====================

.. c:function:: void eeh_pe_mark_isolated(struct eeh_pe *root)

    :param root:
        *undescribed*
    :type root: struct eeh_pe \*

.. _`eeh_pe_mark_isolated.description`:

Description
-----------

Record that a PE has been isolated by marking the PE and it's children as
EEH_PE_ISOLATED (and EEH_PE_CFG_BLOCKED, if required) and their PCI devices
as pci_channel_io_frozen.

.. _`eeh_pe_dev_mode_mark`:

eeh_pe_dev_mode_mark
====================

.. c:function:: void eeh_pe_dev_mode_mark(struct eeh_pe *pe, int mode)

    Mark state for all device under the PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param mode:
        *undescribed*
    :type mode: int

.. _`eeh_pe_dev_mode_mark.description`:

Description
-----------

Mark specific state for all child devices of the PE.

.. _`__eeh_pe_state_clear`:

\__eeh_pe_state_clear
=====================

.. c:function:: void *__eeh_pe_state_clear(struct eeh_pe *pe, void *flag)

    Clear state for the PE

    :param pe:
        *undescribed*
    :type pe: struct eeh_pe \*

    :param flag:
        state
    :type flag: void \*

.. _`__eeh_pe_state_clear.description`:

Description
-----------

The function is used to clear the indicated state from the
given PE. Besides, we also clear the check count of the PE
as well.

.. _`eeh_pe_state_clear`:

eeh_pe_state_clear
==================

.. c:function:: void eeh_pe_state_clear(struct eeh_pe *pe, int state)

    Clear state for the PE and its children

    :param pe:
        PE
    :type pe: struct eeh_pe \*

    :param state:
        state to be cleared
    :type state: int

.. _`eeh_pe_state_clear.description`:

Description
-----------

When the PE and its children has been recovered from error,
we need clear the error state for that. The function is used
for the purpose.

.. _`eeh_restore_one_device_bars`:

eeh_restore_one_device_bars
===========================

.. c:function:: void *eeh_restore_one_device_bars(struct eeh_dev *edev, void *flag)

    Restore the Base Address Registers for one device

    :param edev:
        *undescribed*
    :type edev: struct eeh_dev \*

    :param flag:
        Unused
    :type flag: void \*

.. _`eeh_restore_one_device_bars.description`:

Description
-----------

Loads the PCI configuration space base address registers,
the expansion ROM base address, the latency timer, and etc.
from the saved values in the device node.

.. _`eeh_pe_restore_bars`:

eeh_pe_restore_bars
===================

.. c:function:: void eeh_pe_restore_bars(struct eeh_pe *pe)

    Restore the PCI config space info

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`eeh_pe_restore_bars.description`:

Description
-----------

This routine performs a recursive walk to the children
of this device as well.

.. _`eeh_pe_loc_get`:

eeh_pe_loc_get
==============

.. c:function:: const char *eeh_pe_loc_get(struct eeh_pe *pe)

    Retrieve location code binding to the given PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`eeh_pe_loc_get.description`:

Description
-----------

Retrieve the location code of the given PE. If the primary PE bus
is root bus, we will grab location code from PHB device tree node
or root port. Otherwise, the upstream bridge's device tree node
of the primary PE bus will be checked for the location code.

.. _`eeh_pe_bus_get`:

eeh_pe_bus_get
==============

.. c:function:: struct pci_bus *eeh_pe_bus_get(struct eeh_pe *pe)

    Retrieve PCI bus according to the given PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`eeh_pe_bus_get.description`:

Description
-----------

Retrieve the PCI bus according to the given PE. Basically,
there're 3 types of PEs: PHB/Bus/Device. For PHB PE, the
primary PCI bus will be retrieved. The parent bus will be
returned for BUS PE. However, we don't have associated PCI
bus for DEVICE PE.

.. This file was automatic generated / don't edit.

