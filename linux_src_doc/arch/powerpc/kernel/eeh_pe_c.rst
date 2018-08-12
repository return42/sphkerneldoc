.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_pe.c

.. _`eeh_set_pe_aux_size`:

eeh_set_pe_aux_size
===================

.. c:function:: void eeh_set_pe_aux_size(int size)

    Set PE auxillary data size

    :param int size:
        PE auxillary data size

.. _`eeh_set_pe_aux_size.description`:

Description
-----------

Set PE auxillary data size

.. _`eeh_pe_alloc`:

eeh_pe_alloc
============

.. c:function:: struct eeh_pe *eeh_pe_alloc(struct pci_controller *phb, int type)

    Allocate PE

    :param struct pci_controller \*phb:
        PCI controller

    :param int type:
        PE type

.. _`eeh_pe_alloc.description`:

Description
-----------

Allocate PE instance dynamically.

.. _`eeh_phb_pe_create`:

eeh_phb_pe_create
=================

.. c:function:: int eeh_phb_pe_create(struct pci_controller *phb)

    Create PHB PE

    :param struct pci_controller \*phb:
        PCI controller

.. _`eeh_phb_pe_create.description`:

Description
-----------

The function should be called while the PHB is detected during
system boot or PCI hotplug in order to create PHB PE.

.. _`eeh_phb_pe_get`:

eeh_phb_pe_get
==============

.. c:function:: struct eeh_pe *eeh_phb_pe_get(struct pci_controller *phb)

    Retrieve PHB PE based on the given PHB

    :param struct pci_controller \*phb:
        PCI controller

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

    :param struct eeh_pe \*pe:
        current PE

    :param struct eeh_pe \*root:
        root PE

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

    :param struct eeh_pe \*root:
        root PE

    :param eeh_pe_traverse_func fn:
        callback

    :param void \*flag:
        extra parameter to callback

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

    :param struct eeh_pe \*root:
        EEH PE

    :param eeh_edev_traverse_func fn:
        function callback

    :param void \*flag:
        extra parameter to callback

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

    :param struct pci_controller \*phb:
        PCI controller

    :param int pe_no:
        PE number

    :param int config_addr:
        Config address

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

    :param struct eeh_dev \*edev:
        EEH device

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

    :param struct eeh_dev \*edev:
        EEH device

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

    :param struct eeh_dev \*edev:
        EEH device

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

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_pe_update_time_stamp.description`:

Description
-----------

We have time stamp for each PE to trace its time of getting
frozen in last hour. The function should be called to update
the time stamp on first error of the specific PE. On the other
handle, we needn't account for errors happened in last hour.

.. _`__eeh_pe_state_mark`:

\__eeh_pe_state_mark
====================

.. c:function:: void *__eeh_pe_state_mark(struct eeh_pe *pe, void *flag)

    Mark the state for the PE

    :param struct eeh_pe \*pe:
        *undescribed*

    :param void \*flag:
        state

.. _`__eeh_pe_state_mark.description`:

Description
-----------

The function is used to mark the indicated state for the given
PE. Also, the associated PCI devices will be put into IO frozen
state as well.

.. _`eeh_pe_state_mark`:

eeh_pe_state_mark
=================

.. c:function:: void eeh_pe_state_mark(struct eeh_pe *pe, int state)

    Mark specified state for PE and its associated device

    :param struct eeh_pe \*pe:
        EEH PE

    :param int state:
        *undescribed*

.. _`eeh_pe_state_mark.description`:

Description
-----------

EEH error affects the current PE and its child PEs. The function
is used to mark appropriate state for the affected PEs and the
associated devices.

.. _`eeh_pe_dev_mode_mark`:

eeh_pe_dev_mode_mark
====================

.. c:function:: void eeh_pe_dev_mode_mark(struct eeh_pe *pe, int mode)

    Mark state for all device under the PE

    :param struct eeh_pe \*pe:
        EEH PE

    :param int mode:
        *undescribed*

.. _`eeh_pe_dev_mode_mark.description`:

Description
-----------

Mark specific state for all child devices of the PE.

.. _`__eeh_pe_state_clear`:

\__eeh_pe_state_clear
=====================

.. c:function:: void *__eeh_pe_state_clear(struct eeh_pe *pe, void *flag)

    Clear state for the PE

    :param struct eeh_pe \*pe:
        *undescribed*

    :param void \*flag:
        state

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

    :param struct eeh_pe \*pe:
        PE

    :param int state:
        state to be cleared

.. _`eeh_pe_state_clear.description`:

Description
-----------

When the PE and its children has been recovered from error,
we need clear the error state for that. The function is used
for the purpose.

.. _`eeh_pe_state_mark_with_cfg`:

eeh_pe_state_mark_with_cfg
==========================

.. c:function:: void eeh_pe_state_mark_with_cfg(struct eeh_pe *pe, int state)

    Mark PE state with unblocked config space

    :param struct eeh_pe \*pe:
        PE

    :param int state:
        PE state to be set

.. _`eeh_pe_state_mark_with_cfg.description`:

Description
-----------

Set specified flag to PE and its child PEs. The PCI config space
of some PEs is blocked automatically when EEH_PE_ISOLATED is set,
which isn't needed in some situations. The function allows to set
the specified flag to indicated PEs without blocking their PCI
config space.

.. _`eeh_restore_one_device_bars`:

eeh_restore_one_device_bars
===========================

.. c:function:: void *eeh_restore_one_device_bars(struct eeh_dev *edev, void *flag)

    Restore the Base Address Registers for one device

    :param struct eeh_dev \*edev:
        *undescribed*

    :param void \*flag:
        Unused

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

    :param struct eeh_pe \*pe:
        EEH PE

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

    :param struct eeh_pe \*pe:
        EEH PE

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

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_pe_bus_get.description`:

Description
-----------

Retrieve the PCI bus according to the given PE. Basically,
there're 3 types of PEs: PHB/Bus/Device. For PHB PE, the
primary PCI bus will be retrieved. The parent bus will be
returned for BUS PE. However, we don't have associated PCI
bus for DEVICE PE.

.. This file was automatic generated / don't edit.

