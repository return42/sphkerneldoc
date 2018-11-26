.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci.c

.. _`pci_bus_max_busnr`:

pci_bus_max_busnr
=================

.. c:function:: unsigned char pci_bus_max_busnr(struct pci_bus *bus)

    returns maximum PCI bus number of given bus' children

    :param bus:
        pointer to PCI bus structure to search
    :type bus: struct pci_bus \*

.. _`pci_bus_max_busnr.description`:

Description
-----------

Given a PCI bus, returns the highest PCI bus number present in the set
including the given PCI bus and its list of child PCI buses.

.. _`pci_dev_str_match_path`:

pci_dev_str_match_path
======================

.. c:function:: int pci_dev_str_match_path(struct pci_dev *dev, const char *path, const char **endptr)

    test if a path string matches a device

    :param dev:
        the PCI device to test
    :type dev: struct pci_dev \*

    :param path:
        string to match the device against
    :type path: const char \*

    :param endptr:
        pointer to the string after the match
    :type endptr: const char \*\*

.. _`pci_dev_str_match_path.description`:

Description
-----------

Test if a string (typically from a kernel parameter) formatted as a
path of device/function addresses matches a PCI device. The string must

.. _`pci_dev_str_match_path.be-of-the-form`:

be of the form
--------------


  [<domain>:]<bus>:<device>.<func>[/<device>.<func>]*

A path for a device can be obtained using 'lspci -t'.  Using a path
is more robust against bus renumbering than using only a single bus,
device and function address.

Returns 1 if the string matches the device, 0 if it does not and
a negative error code if it fails to parse the string.

.. _`pci_dev_str_match`:

pci_dev_str_match
=================

.. c:function:: int pci_dev_str_match(struct pci_dev *dev, const char *p, const char **endptr)

    test if a string matches a device

    :param dev:
        the PCI device to test
    :type dev: struct pci_dev \*

    :param p:
        string to match the device against
    :type p: const char \*

    :param endptr:
        pointer to the string after the match
    :type endptr: const char \*\*

.. _`pci_dev_str_match.description`:

Description
-----------

Test if a string (typically from a kernel parameter) matches a specified
PCI device. The string may be of one of the following formats:

  [<domain>:]<bus>:<device>.<func>[/<device>.<func>]*
  pci:<vendor>:<device>[:<subvendor>:<subdevice>]

The first format specifies a PCI bus/device/function address which
may change if new hardware is inserted, if motherboard firmware changes,
or due to changes caused in kernel parameters. If the domain is
left unspecified, it is taken to be 0.  In order to be robust against
bus renumbering issues, a path of PCI device/function numbers may be used
to address the specific device.  The path for a device can be determined
through the use of 'lspci -t'.

The second format matches devices using IDs in the configuration
space which may match multiple devices in the system. A value of 0
for any field will match all devices. (Note: this differs from
in-kernel code that uses PCI_ANY_ID which is ~0; this is for
legacy reasons and convenience so users don't have to specify
FFFFFFFFs on the command line.)

Returns 1 if the string matches the device, 0 if it does not and
a negative error code if the string cannot be parsed.

.. _`pci_find_capability`:

pci_find_capability
===================

.. c:function:: int pci_find_capability(struct pci_dev *dev, int cap)

    query for devices' capabilities

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param cap:
        capability code
    :type cap: int

.. _`pci_find_capability.description`:

Description
-----------

Tell if a device supports a given PCI capability.
Returns the address of the requested capability structure within the
device's PCI configuration space or 0 in case the device does not
support it.  Possible values for \ ``cap``\ :

 \ ``PCI_CAP_ID_PM``\            Power Management
 \ ``PCI_CAP_ID_AGP``\           Accelerated Graphics Port
 \ ``PCI_CAP_ID_VPD``\           Vital Product Data
 \ ``PCI_CAP_ID_SLOTID``\        Slot Identification
 \ ``PCI_CAP_ID_MSI``\           Message Signalled Interrupts
 \ ``PCI_CAP_ID_CHSWP``\         CompactPCI HotSwap
 \ ``PCI_CAP_ID_PCIX``\          PCI-X
 \ ``PCI_CAP_ID_EXP``\           PCI Express

.. _`pci_bus_find_capability`:

pci_bus_find_capability
=======================

.. c:function:: int pci_bus_find_capability(struct pci_bus *bus, unsigned int devfn, int cap)

    query for devices' capabilities

    :param bus:
        the PCI bus to query
    :type bus: struct pci_bus \*

    :param devfn:
        PCI device to query
    :type devfn: unsigned int

    :param cap:
        capability code
    :type cap: int

.. _`pci_bus_find_capability.description`:

Description
-----------

Like \ :c:func:`pci_find_capability`\  but works for pci devices that do not have a
pci_dev structure set up yet.

Returns the address of the requested capability structure within the
device's PCI configuration space or 0 in case the device does not
support it.

.. _`pci_find_next_ext_capability`:

pci_find_next_ext_capability
============================

.. c:function:: int pci_find_next_ext_capability(struct pci_dev *dev, int start, int cap)

    Find an extended capability

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param start:
        address at which to start looking (0 to start at beginning of list)
    :type start: int

    :param cap:
        capability code
    :type cap: int

.. _`pci_find_next_ext_capability.description`:

Description
-----------

Returns the address of the next matching extended capability structure
within the device's PCI configuration space or 0 if the device does
not support it.  Some capabilities can occur several times, e.g., the
vendor-specific capability, and this provides a way to find them all.

.. _`pci_find_ext_capability`:

pci_find_ext_capability
=======================

.. c:function:: int pci_find_ext_capability(struct pci_dev *dev, int cap)

    Find an extended capability

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param cap:
        capability code
    :type cap: int

.. _`pci_find_ext_capability.description`:

Description
-----------

Returns the address of the requested extended capability structure
within the device's PCI configuration space or 0 if the device does
not support it.  Possible values for \ ``cap``\ :

 \ ``PCI_EXT_CAP_ID_ERR``\          Advanced Error Reporting
 \ ``PCI_EXT_CAP_ID_VC``\           Virtual Channel
 \ ``PCI_EXT_CAP_ID_DSN``\          Device Serial Number
 \ ``PCI_EXT_CAP_ID_PWR``\          Power Budgeting

.. _`pci_find_next_ht_capability`:

pci_find_next_ht_capability
===========================

.. c:function:: int pci_find_next_ht_capability(struct pci_dev *dev, int pos, int ht_cap)

    query a device's Hypertransport capabilities

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param pos:
        Position from which to continue searching
    :type pos: int

    :param ht_cap:
        Hypertransport capability code
    :type ht_cap: int

.. _`pci_find_next_ht_capability.description`:

Description
-----------

To be used in conjunction with \ :c:func:`pci_find_ht_capability`\  to search for
all capabilities matching \ ``ht_cap``\ . \ ``pos``\  should always be a value returned
from \ :c:func:`pci_find_ht_capability`\ .

NB. To be 100% safe against broken PCI devices, the caller should take
steps to avoid an infinite loop.

.. _`pci_find_ht_capability`:

pci_find_ht_capability
======================

.. c:function:: int pci_find_ht_capability(struct pci_dev *dev, int ht_cap)

    query a device's Hypertransport capabilities

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param ht_cap:
        Hypertransport capability code
    :type ht_cap: int

.. _`pci_find_ht_capability.description`:

Description
-----------

Tell if a device supports a given Hypertransport capability.
Returns an address within the device's PCI configuration space
or 0 in case the device does not support the request capability.
The address points to the PCI capability, of type PCI_CAP_ID_HT,
which has a Hypertransport capability matching \ ``ht_cap``\ .

.. _`pci_find_parent_resource`:

pci_find_parent_resource
========================

.. c:function:: struct resource *pci_find_parent_resource(const struct pci_dev *dev, struct resource *res)

    return resource region of parent bus of given region

    :param dev:
        PCI device structure contains resources to be searched
    :type dev: const struct pci_dev \*

    :param res:
        child resource record for which parent is sought
    :type res: struct resource \*

.. _`pci_find_parent_resource.description`:

Description
-----------

 For given resource region of given device, return the resource
 region of parent bus the given region is contained in.

.. _`pci_find_resource`:

pci_find_resource
=================

.. c:function:: struct resource *pci_find_resource(struct pci_dev *dev, struct resource *res)

    Return matching PCI device resource

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param res:
        Resource to look for
    :type res: struct resource \*

.. _`pci_find_resource.description`:

Description
-----------

Goes over standard PCI resources (BARs) and checks if the given resource
is partially or fully contained in any of them. In that case the
matching resource is returned, \ ``NULL``\  otherwise.

.. _`pci_find_pcie_root_port`:

pci_find_pcie_root_port
=======================

.. c:function:: struct pci_dev *pci_find_pcie_root_port(struct pci_dev *dev)

    return PCIe Root Port

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pci_find_pcie_root_port.description`:

Description
-----------

Traverse up the parent chain and return the PCIe Root Port PCI Device
for a given PCI Device.

.. _`pci_wait_for_pending`:

pci_wait_for_pending
====================

.. c:function:: int pci_wait_for_pending(struct pci_dev *dev, int pos, u16 mask)

    wait for \ ``mask``\  bit(s) to clear in status word \ ``pos``\ 

    :param dev:
        the PCI device to operate on
    :type dev: struct pci_dev \*

    :param pos:
        config space offset of status word
    :type pos: int

    :param mask:
        mask of bit(s) to care about in status word
    :type mask: u16

.. _`pci_wait_for_pending.description`:

Description
-----------

Return 1 when mask bit(s) in status word clear, 0 otherwise.

.. _`pci_restore_bars`:

pci_restore_bars
================

.. c:function:: void pci_restore_bars(struct pci_dev *dev)

    restore a device's BAR values (e.g. after wake-up)

    :param dev:
        PCI device to have its BARs restored
    :type dev: struct pci_dev \*

.. _`pci_restore_bars.description`:

Description
-----------

Restore the BAR values for a given device, so as to make it
accessible by its driver.

.. _`pci_raw_set_power_state`:

pci_raw_set_power_state
=======================

.. c:function:: int pci_raw_set_power_state(struct pci_dev *dev, pci_power_t state)

    Use PCI PM registers to set the power state of given PCI device

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        PCI power state (D0, D1, D2, D3hot) to put the device into.
    :type state: pci_power_t

.. _`pci_raw_set_power_state.return-value`:

RETURN VALUE
------------

-EINVAL if the requested state is invalid.
-EIO if device does not support PCI PM or its PM capabilities register has a
wrong version, or device doesn't support the requested state.
0 if device already is in the requested state.
0 if device's power state has been successfully changed.

.. _`pci_update_current_state`:

pci_update_current_state
========================

.. c:function:: void pci_update_current_state(struct pci_dev *dev, pci_power_t state)

    Read power state of given device and cache it

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        State to cache in case the device doesn't have the PM capability
    :type state: pci_power_t

.. _`pci_update_current_state.description`:

Description
-----------

The power state is read from the PMCSR register, which however is
inaccessible in D3cold.  The platform firmware is therefore queried first
to detect accessibility of the register.  In case the platform firmware
reports an incorrect state or the device isn't power manageable by the
platform at all, we try to detect D3cold by testing accessibility of the
vendor ID in config space.

.. _`pci_power_up`:

pci_power_up
============

.. c:function:: void pci_power_up(struct pci_dev *dev)

    Put the given device into D0 forcibly

    :param dev:
        PCI device to power up
    :type dev: struct pci_dev \*

.. _`pci_platform_power_transition`:

pci_platform_power_transition
=============================

.. c:function:: int pci_platform_power_transition(struct pci_dev *dev, pci_power_t state)

    Use platform to change device power state

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        State to put the device into.
    :type state: pci_power_t

.. _`pci_wakeup`:

pci_wakeup
==========

.. c:function:: int pci_wakeup(struct pci_dev *pci_dev, void *ign)

    Wake up a PCI device

    :param pci_dev:
        Device to handle.
    :type pci_dev: struct pci_dev \*

    :param ign:
        ignored parameter
    :type ign: void \*

.. _`pci_wakeup_bus`:

pci_wakeup_bus
==============

.. c:function:: void pci_wakeup_bus(struct pci_bus *bus)

    Walk given bus and wake up devices on it

    :param bus:
        Top bus of the subtree to walk.
    :type bus: struct pci_bus \*

.. _`__pci_start_power_transition`:

__pci_start_power_transition
============================

.. c:function:: void __pci_start_power_transition(struct pci_dev *dev, pci_power_t state)

    Start power transition of a PCI device

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        State to put the device into.
    :type state: pci_power_t

.. _`__pci_dev_set_current_state`:

__pci_dev_set_current_state
===========================

.. c:function:: int __pci_dev_set_current_state(struct pci_dev *dev, void *data)

    Set current state of a PCI device

    :param dev:
        Device to handle
    :type dev: struct pci_dev \*

    :param data:
        pointer to state to be set
    :type data: void \*

.. _`pci_bus_set_current_state`:

pci_bus_set_current_state
=========================

.. c:function:: void pci_bus_set_current_state(struct pci_bus *bus, pci_power_t state)

    Walk given bus and set current state of devices

    :param bus:
        Top bus of the subtree to walk.
    :type bus: struct pci_bus \*

    :param state:
        state to be set
    :type state: pci_power_t

.. _`__pci_complete_power_transition`:

__pci_complete_power_transition
===============================

.. c:function:: int __pci_complete_power_transition(struct pci_dev *dev, pci_power_t state)

    Complete power transition of a PCI device

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        State to put the device into.
    :type state: pci_power_t

.. _`__pci_complete_power_transition.description`:

Description
-----------

This function should not be called directly by device drivers.

.. _`pci_set_power_state`:

pci_set_power_state
===================

.. c:function:: int pci_set_power_state(struct pci_dev *dev, pci_power_t state)

    Set the power state of a PCI device

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        PCI power state (D0, D1, D2, D3hot) to put the device into.
    :type state: pci_power_t

.. _`pci_set_power_state.description`:

Description
-----------

Transition a device to a new power state, using the platform firmware and/or
the device's PCI PM registers.

.. _`pci_set_power_state.return-value`:

RETURN VALUE
------------

-EINVAL if the requested state is invalid.
-EIO if device does not support PCI PM or its PM capabilities register has a
wrong version, or device doesn't support the requested state.
0 if the transition is to D1 or D2 but D1 and D2 are not supported.
0 if device already is in the requested state.
0 if the transition is to D3 but D3 is not supported.
0 if device's power state has been successfully changed.

.. _`pci_choose_state`:

pci_choose_state
================

.. c:function:: pci_power_t pci_choose_state(struct pci_dev *dev, pm_message_t state)

    Choose the power state of a PCI device

    :param dev:
        PCI device to be suspended
    :type dev: struct pci_dev \*

    :param state:
        target sleep state for the whole system. This is the value
        that is passed to \ :c:func:`suspend`\  function.
    :type state: pm_message_t

.. _`pci_choose_state.description`:

Description
-----------

Returns PCI power state suitable for given device and given system
message.

.. _`pci_save_state`:

pci_save_state
==============

.. c:function:: int pci_save_state(struct pci_dev *dev)

    save the PCI configuration space of a device before suspending

    :param dev:
        - PCI device that we're dealing with
    :type dev: struct pci_dev \*

.. _`pci_restore_state`:

pci_restore_state
=================

.. c:function:: void pci_restore_state(struct pci_dev *dev)

    Restore the saved state of a PCI device

    :param dev:
        - PCI device that we're dealing with
    :type dev: struct pci_dev \*

.. _`pci_store_saved_state`:

pci_store_saved_state
=====================

.. c:function:: struct pci_saved_state *pci_store_saved_state(struct pci_dev *dev)

    Allocate and return an opaque struct containing the device saved state.

    :param dev:
        PCI device that we're dealing with
    :type dev: struct pci_dev \*

.. _`pci_store_saved_state.description`:

Description
-----------

Return NULL if no state or error.

.. _`pci_load_saved_state`:

pci_load_saved_state
====================

.. c:function:: int pci_load_saved_state(struct pci_dev *dev, struct pci_saved_state *state)

    Reload the provided save state into struct pci_dev.

    :param dev:
        PCI device that we're dealing with
    :type dev: struct pci_dev \*

    :param state:
        Saved state returned from \ :c:func:`pci_store_saved_state`\ 
    :type state: struct pci_saved_state \*

.. _`pci_load_and_free_saved_state`:

pci_load_and_free_saved_state
=============================

.. c:function:: int pci_load_and_free_saved_state(struct pci_dev *dev, struct pci_saved_state **state)

    Reload the save state pointed to by state, and free the memory allocated for it.

    :param dev:
        PCI device that we're dealing with
    :type dev: struct pci_dev \*

    :param state:
        Pointer to saved state returned from \ :c:func:`pci_store_saved_state`\ 
    :type state: struct pci_saved_state \*\*

.. _`pci_reenable_device`:

pci_reenable_device
===================

.. c:function:: int pci_reenable_device(struct pci_dev *dev)

    Resume abandoned device

    :param dev:
        PCI device to be resumed
    :type dev: struct pci_dev \*

.. _`pci_reenable_device.description`:

Description
-----------

 Note this function is a backend of pci_default_resume and is not supposed
 to be called by normal code, write proper resume handler and use it instead.

.. _`pci_enable_device_io`:

pci_enable_device_io
====================

.. c:function:: int pci_enable_device_io(struct pci_dev *dev)

    Initialize a device for use with IO space

    :param dev:
        PCI device to be initialized
    :type dev: struct pci_dev \*

.. _`pci_enable_device_io.description`:

Description
-----------

 Initialize device before it's used by a driver. Ask low-level code
 to enable I/O resources. Wake up the device if it was suspended.
 Beware, this function can fail.

.. _`pci_enable_device_mem`:

pci_enable_device_mem
=====================

.. c:function:: int pci_enable_device_mem(struct pci_dev *dev)

    Initialize a device for use with Memory space

    :param dev:
        PCI device to be initialized
    :type dev: struct pci_dev \*

.. _`pci_enable_device_mem.description`:

Description
-----------

 Initialize device before it's used by a driver. Ask low-level code
 to enable Memory resources. Wake up the device if it was suspended.
 Beware, this function can fail.

.. _`pci_enable_device`:

pci_enable_device
=================

.. c:function:: int pci_enable_device(struct pci_dev *dev)

    Initialize device before it's used by a driver.

    :param dev:
        PCI device to be initialized
    :type dev: struct pci_dev \*

.. _`pci_enable_device.description`:

Description
-----------

 Initialize device before it's used by a driver. Ask low-level code
 to enable I/O and memory. Wake up the device if it was suspended.
 Beware, this function can fail.

 Note we don't actually enable the device many times if we call
 this function repeatedly (we just increment the count).

.. _`pcim_enable_device`:

pcim_enable_device
==================

.. c:function:: int pcim_enable_device(struct pci_dev *pdev)

    Managed \ :c:func:`pci_enable_device`\ 

    :param pdev:
        PCI device to be initialized
    :type pdev: struct pci_dev \*

.. _`pcim_enable_device.description`:

Description
-----------

Managed \ :c:func:`pci_enable_device`\ .

.. _`pcim_pin_device`:

pcim_pin_device
===============

.. c:function:: void pcim_pin_device(struct pci_dev *pdev)

    Pin managed PCI device

    :param pdev:
        PCI device to pin
    :type pdev: struct pci_dev \*

.. _`pcim_pin_device.description`:

Description
-----------

Pin managed PCI device \ ``pdev``\ .  Pinned device won't be disabled on
driver detach.  \ ``pdev``\  must have been enabled with
\ :c:func:`pcim_enable_device`\ .

.. _`pcibios_release_device`:

pcibios_release_device
======================

.. c:function:: void pcibios_release_device(struct pci_dev *dev)

    provide arch specific hooks when releasing device dev

    :param dev:
        the PCI device being released
    :type dev: struct pci_dev \*

.. _`pcibios_release_device.description`:

Description
-----------

Permits the platform to provide architecture specific functionality when
devices are released. This is the default implementation. Architecture
implementations can override this.

.. _`pcibios_disable_device`:

pcibios_disable_device
======================

.. c:function:: void pcibios_disable_device(struct pci_dev *dev)

    disable arch specific PCI resources for device dev

    :param dev:
        the PCI device to disable
    :type dev: struct pci_dev \*

.. _`pcibios_disable_device.description`:

Description
-----------

Disables architecture specific PCI resources for the device. This
is the default implementation. Architecture implementations can
override this.

.. _`pcibios_penalize_isa_irq`:

pcibios_penalize_isa_irq
========================

.. c:function:: void pcibios_penalize_isa_irq(int irq, int active)

    penalize an ISA IRQ

    :param irq:
        ISA IRQ to penalize
    :type irq: int

    :param active:
        IRQ active or not
    :type active: int

.. _`pcibios_penalize_isa_irq.description`:

Description
-----------

Permits the platform to provide architecture-specific functionality when
penalizing ISA IRQs. This is the default implementation. Architecture
implementations can override this.

.. _`pci_disable_enabled_device`:

pci_disable_enabled_device
==========================

.. c:function:: void pci_disable_enabled_device(struct pci_dev *dev)

    Disable device without updating enable_cnt

    :param dev:
        PCI device to disable
    :type dev: struct pci_dev \*

.. _`pci_disable_enabled_device.note`:

NOTE
----

This function is a backend of PCI power management routines and is
not supposed to be called drivers.

.. _`pci_disable_device`:

pci_disable_device
==================

.. c:function:: void pci_disable_device(struct pci_dev *dev)

    Disable PCI device after use

    :param dev:
        PCI device to be disabled
    :type dev: struct pci_dev \*

.. _`pci_disable_device.description`:

Description
-----------

Signal to the system that the PCI device is not in use by the system
anymore.  This only involves disabling PCI bus-mastering, if active.

Note we don't actually disable the device until all callers of
\ :c:func:`pci_enable_device`\  have called \ :c:func:`pci_disable_device`\ .

.. _`pcibios_set_pcie_reset_state`:

pcibios_set_pcie_reset_state
============================

.. c:function:: int pcibios_set_pcie_reset_state(struct pci_dev *dev, enum pcie_reset_state state)

    set reset state for device dev

    :param dev:
        the PCIe device reset
    :type dev: struct pci_dev \*

    :param state:
        Reset state to enter into
    :type state: enum pcie_reset_state

.. _`pcibios_set_pcie_reset_state.description`:

Description
-----------


Sets the PCIe reset state for the device. This is the default
implementation. Architecture implementations can override this.

.. _`pci_set_pcie_reset_state`:

pci_set_pcie_reset_state
========================

.. c:function:: int pci_set_pcie_reset_state(struct pci_dev *dev, enum pcie_reset_state state)

    set reset state for device dev

    :param dev:
        the PCIe device reset
    :type dev: struct pci_dev \*

    :param state:
        Reset state to enter into
    :type state: enum pcie_reset_state

.. _`pci_set_pcie_reset_state.description`:

Description
-----------


Sets the PCI reset state for the device.

.. _`pcie_clear_root_pme_status`:

pcie_clear_root_pme_status
==========================

.. c:function:: void pcie_clear_root_pme_status(struct pci_dev *dev)

    Clear root port PME interrupt status.

    :param dev:
        PCIe root port or event collector.
    :type dev: struct pci_dev \*

.. _`pci_check_pme_status`:

pci_check_pme_status
====================

.. c:function:: bool pci_check_pme_status(struct pci_dev *dev)

    Check if given device has generated PME.

    :param dev:
        Device to check.
    :type dev: struct pci_dev \*

.. _`pci_check_pme_status.description`:

Description
-----------

Check the PME status of the device and if set, clear it and clear PME enable
(if set).  Return 'true' if PME status and PME enable were both set or
'false' otherwise.

.. _`pci_pme_wakeup`:

pci_pme_wakeup
==============

.. c:function:: int pci_pme_wakeup(struct pci_dev *dev, void *pme_poll_reset)

    Wake up a PCI device if its PME Status bit is set.

    :param dev:
        Device to handle.
    :type dev: struct pci_dev \*

    :param pme_poll_reset:
        Whether or not to reset the device's pme_poll flag.
    :type pme_poll_reset: void \*

.. _`pci_pme_wakeup.description`:

Description
-----------

Check if \ ``dev``\  has generated PME and queue a resume request for it in that
case.

.. _`pci_pme_wakeup_bus`:

pci_pme_wakeup_bus
==================

.. c:function:: void pci_pme_wakeup_bus(struct pci_bus *bus)

    Walk given bus and wake up devices on it, if necessary.

    :param bus:
        Top bus of the subtree to walk.
    :type bus: struct pci_bus \*

.. _`pci_pme_capable`:

pci_pme_capable
===============

.. c:function:: bool pci_pme_capable(struct pci_dev *dev, pci_power_t state)

    check the capability of PCI device to generate PME#

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param state:
        PCI state from which device will issue PME#.
    :type state: pci_power_t

.. _`pci_pme_restore`:

pci_pme_restore
===============

.. c:function:: void pci_pme_restore(struct pci_dev *dev)

    Restore PME configuration after config space restore.

    :param dev:
        PCI device to update.
    :type dev: struct pci_dev \*

.. _`pci_pme_active`:

pci_pme_active
==============

.. c:function:: void pci_pme_active(struct pci_dev *dev, bool enable)

    enable or disable PCI device's PME# function

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param enable:
        'true' to enable PME# generation; 'false' to disable it.
    :type enable: bool

.. _`pci_pme_active.description`:

Description
-----------

The caller must verify that the device is capable of generating PME# before
calling this function with \ ``enable``\  equal to 'true'.

.. _`__pci_enable_wake`:

__pci_enable_wake
=================

.. c:function:: int __pci_enable_wake(struct pci_dev *dev, pci_power_t state, bool enable)

    enable PCI device as wakeup event source

    :param dev:
        PCI device affected
    :type dev: struct pci_dev \*

    :param state:
        PCI state from which device will issue wakeup events
    :type state: pci_power_t

    :param enable:
        True to enable event generation; false to disable
    :type enable: bool

.. _`__pci_enable_wake.description`:

Description
-----------

This enables the device as a wakeup event source, or disables it.
When such events involves platform-specific hooks, those hooks are
called automatically by this routine.

Devices with legacy power management (no standard PCI PM capabilities)
always require such platform hooks.

.. _`__pci_enable_wake.return-value`:

RETURN VALUE
------------

0 is returned on success
-EINVAL is returned if device is not supposed to wake up the system
Error code depending on the platform is returned if both the platform and
the native mechanism fail to enable the generation of wake-up events

.. _`pci_enable_wake`:

pci_enable_wake
===============

.. c:function:: int pci_enable_wake(struct pci_dev *pci_dev, pci_power_t state, bool enable)

    change wakeup settings for a PCI device

    :param pci_dev:
        Target device
    :type pci_dev: struct pci_dev \*

    :param state:
        PCI state from which device will issue wakeup events
    :type state: pci_power_t

    :param enable:
        Whether or not to enable event generation
    :type enable: bool

.. _`pci_enable_wake.description`:

Description
-----------

If \ ``enable``\  is set, check \ :c:func:`device_may_wakeup`\  for the device before calling
\ :c:func:`__pci_enable_wake`\  for it.

.. _`pci_wake_from_d3`:

pci_wake_from_d3
================

.. c:function:: int pci_wake_from_d3(struct pci_dev *dev, bool enable)

    enable/disable device to wake up from D3_hot or D3_cold

    :param dev:
        PCI device to prepare
    :type dev: struct pci_dev \*

    :param enable:
        True to enable wake-up event generation; false to disable
    :type enable: bool

.. _`pci_wake_from_d3.description`:

Description
-----------

Many drivers want the device to wake up the system from D3_hot or D3_cold
and this function allows them to set that up cleanly - \ :c:func:`pci_enable_wake`\ 
should not be called twice in a row to enable wake-up due to PCI PM vs ACPI
ordering constraints.

This function only returns error code if the device is not allowed to wake
up the system from sleep or it is not capable of generating PME# from both
D3_hot and D3_cold and the platform is unable to enable wake-up power for it.

.. _`pci_target_state`:

pci_target_state
================

.. c:function:: pci_power_t pci_target_state(struct pci_dev *dev, bool wakeup)

    find an appropriate low power state for a given PCI dev

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param wakeup:
        Whether or not wakeup functionality will be enabled for the device.
    :type wakeup: bool

.. _`pci_target_state.description`:

Description
-----------

Use underlying platform code to find a supported low power state for \ ``dev``\ .
If the platform can't manage \ ``dev``\ , return the deepest state from which it
can generate wake events, based on any available PME info.

.. _`pci_prepare_to_sleep`:

pci_prepare_to_sleep
====================

.. c:function:: int pci_prepare_to_sleep(struct pci_dev *dev)

    prepare PCI device for system-wide transition into a sleep state

    :param dev:
        Device to handle.
    :type dev: struct pci_dev \*

.. _`pci_prepare_to_sleep.description`:

Description
-----------

Choose the power state appropriate for the device depending on whether
it can wake up the system and/or is power manageable by the platform
(PCI_D3hot is the default) and put the device into that state.

.. _`pci_back_from_sleep`:

pci_back_from_sleep
===================

.. c:function:: int pci_back_from_sleep(struct pci_dev *dev)

    turn PCI device on during system-wide transition into working state

    :param dev:
        Device to handle.
    :type dev: struct pci_dev \*

.. _`pci_back_from_sleep.description`:

Description
-----------

Disable device's system wake-up capability and put it into D0.

.. _`pci_finish_runtime_suspend`:

pci_finish_runtime_suspend
==========================

.. c:function:: int pci_finish_runtime_suspend(struct pci_dev *dev)

    Carry out PCI-specific part of runtime suspend.

    :param dev:
        PCI device being suspended.
    :type dev: struct pci_dev \*

.. _`pci_finish_runtime_suspend.description`:

Description
-----------

Prepare \ ``dev``\  to generate wake-up events at run time and put it into a low
power state.

.. _`pci_dev_run_wake`:

pci_dev_run_wake
================

.. c:function:: bool pci_dev_run_wake(struct pci_dev *dev)

    Check if device can generate run-time wake-up events.

    :param dev:
        Device to check.
    :type dev: struct pci_dev \*

.. _`pci_dev_run_wake.description`:

Description
-----------

Return true if the device itself is capable of generating wake-up events
(through the platform or using the native PCIe PME) or if the device supports
PME and one of its upstream bridges can generate wake-up events.

.. _`pci_dev_keep_suspended`:

pci_dev_keep_suspended
======================

.. c:function:: bool pci_dev_keep_suspended(struct pci_dev *pci_dev)

    Check if the device can stay in the suspended state.

    :param pci_dev:
        Device to check.
    :type pci_dev: struct pci_dev \*

.. _`pci_dev_keep_suspended.description`:

Description
-----------

Return 'true' if the device is runtime-suspended, it doesn't have to be
reconfigured due to wakeup settings difference between system and runtime
suspend and the current power state of it is suitable for the upcoming
(system) transition.

If the device is not configured for system wakeup, disable PME for it before
returning 'true' to prevent it from waking up the system unnecessarily.

.. _`pci_dev_complete_resume`:

pci_dev_complete_resume
=======================

.. c:function:: void pci_dev_complete_resume(struct pci_dev *pci_dev)

    Finalize resume from system sleep for a device.

    :param pci_dev:
        Device to handle.
    :type pci_dev: struct pci_dev \*

.. _`pci_dev_complete_resume.description`:

Description
-----------

If the device is runtime suspended and wakeup-capable, enable PME for it as
it might have been disabled during the prepare phase of system suspend if
the device was not configured for system wakeup.

.. _`pci_bridge_d3_possible`:

pci_bridge_d3_possible
======================

.. c:function:: bool pci_bridge_d3_possible(struct pci_dev *bridge)

    Is it possible to put the bridge into D3

    :param bridge:
        Bridge to check
    :type bridge: struct pci_dev \*

.. _`pci_bridge_d3_possible.description`:

Description
-----------

This function checks if it is possible to move the bridge to D3.
Currently we only allow D3 for recent enough PCIe ports and Thunderbolt.

.. _`pci_d3cold_enable`:

pci_d3cold_enable
=================

.. c:function:: void pci_d3cold_enable(struct pci_dev *dev)

    Enable D3cold for device

    :param dev:
        PCI device to handle
    :type dev: struct pci_dev \*

.. _`pci_d3cold_enable.description`:

Description
-----------

This function can be used in drivers to enable D3cold from the device
they handle.  It also updates upstream PCI bridge PM capabilities
accordingly.

.. _`pci_d3cold_disable`:

pci_d3cold_disable
==================

.. c:function:: void pci_d3cold_disable(struct pci_dev *dev)

    Disable D3cold for device

    :param dev:
        PCI device to handle
    :type dev: struct pci_dev \*

.. _`pci_d3cold_disable.description`:

Description
-----------

This function can be used in drivers to disable D3cold from the device
they handle.  It also updates upstream PCI bridge PM capabilities
accordingly.

.. _`pci_pm_init`:

pci_pm_init
===========

.. c:function:: void pci_pm_init(struct pci_dev *dev)

    Initialize PM functions of given PCI device

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

.. _`_pci_add_cap_save_buffer`:

_pci_add_cap_save_buffer
========================

.. c:function:: int _pci_add_cap_save_buffer(struct pci_dev *dev, u16 cap, bool extended, unsigned int size)

    allocate buffer for saving given capability registers

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param cap:
        the capability to allocate the buffer for
    :type cap: u16

    :param extended:
        Standard or Extended capability ID
    :type extended: bool

    :param size:
        requested size of the buffer
    :type size: unsigned int

.. _`pci_allocate_cap_save_buffers`:

pci_allocate_cap_save_buffers
=============================

.. c:function:: void pci_allocate_cap_save_buffers(struct pci_dev *dev)

    allocate buffers for saving capabilities

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_configure_ari`:

pci_configure_ari
=================

.. c:function:: void pci_configure_ari(struct pci_dev *dev)

    enable or disable ARI forwarding

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_configure_ari.description`:

Description
-----------

If \ ``dev``\  and its upstream bridge both support ARI, enable ARI in the
bridge.  Otherwise, disable ARI in the bridge.

.. _`pci_request_acs`:

pci_request_acs
===============

.. c:function:: void pci_request_acs( void)

    ask for ACS to be enabled if supported

    :param void:
        no arguments
    :type void: 

.. _`pci_disable_acs_redir`:

pci_disable_acs_redir
=====================

.. c:function:: void pci_disable_acs_redir(struct pci_dev *dev)

    disable ACS redirect capabilities

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_disable_acs_redir.description`:

Description
-----------

For only devices specified in the disable_acs_redir parameter.

.. _`pci_std_enable_acs`:

pci_std_enable_acs
==================

.. c:function:: void pci_std_enable_acs(struct pci_dev *dev)

    enable ACS on devices using standard ACS capabilites

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_enable_acs`:

pci_enable_acs
==============

.. c:function:: void pci_enable_acs(struct pci_dev *dev)

    enable ACS if hardware support it

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_acs_enabled`:

pci_acs_enabled
===============

.. c:function:: bool pci_acs_enabled(struct pci_dev *pdev, u16 acs_flags)

    test ACS against required flags for a given device

    :param pdev:
        device to test
    :type pdev: struct pci_dev \*

    :param acs_flags:
        required PCI ACS flags
    :type acs_flags: u16

.. _`pci_acs_enabled.description`:

Description
-----------

Return true if the device supports the provided flags.  Automatically
filters out flags that are not implemented on multifunction devices.

Note that this interface checks the effective ACS capabilities of the
device rather than the actual capabilities.  For instance, most single
function endpoints are not required to support ACS because they have no
opportunity for peer-to-peer access.  We therefore return 'true'
regardless of whether the device exposes an ACS capability.  This makes
it much easier for callers of this function to ignore the actual type
or topology of the device when testing ACS support.

.. _`pci_acs_path_enabled`:

pci_acs_path_enabled
====================

.. c:function:: bool pci_acs_path_enabled(struct pci_dev *start, struct pci_dev *end, u16 acs_flags)

    test ACS flags from start to end in a hierarchy

    :param start:
        starting downstream device
    :type start: struct pci_dev \*

    :param end:
        ending upstream device or NULL to search to the root bus
    :type end: struct pci_dev \*

    :param acs_flags:
        required flags
    :type acs_flags: u16

.. _`pci_acs_path_enabled.description`:

Description
-----------

Walk up a device tree from start to end testing PCI ACS support.  If
any step along the way does not support the required flags, return false.

.. _`pci_rebar_find_pos`:

pci_rebar_find_pos
==================

.. c:function:: int pci_rebar_find_pos(struct pci_dev *pdev, int bar)

    find position of resize ctrl reg for BAR

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to find
    :type bar: int

.. _`pci_rebar_find_pos.description`:

Description
-----------

Helper to find the position of the ctrl register for a BAR.
Returns -ENOTSUPP if resizable BARs are not supported at all.
Returns -ENOENT if no ctrl register for the BAR could be found.

.. _`pci_rebar_get_possible_sizes`:

pci_rebar_get_possible_sizes
============================

.. c:function:: u32 pci_rebar_get_possible_sizes(struct pci_dev *pdev, int bar)

    get possible sizes for BAR

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to query
    :type bar: int

.. _`pci_rebar_get_possible_sizes.description`:

Description
-----------

Get the possible sizes of a resizable BAR as bitmask defined in the spec
(bit 0=1MB, bit 19=512GB). Returns 0 if BAR isn't resizable.

.. _`pci_rebar_get_current_size`:

pci_rebar_get_current_size
==========================

.. c:function:: int pci_rebar_get_current_size(struct pci_dev *pdev, int bar)

    get the current size of a BAR

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to set size to
    :type bar: int

.. _`pci_rebar_get_current_size.description`:

Description
-----------

Read the size of a BAR from the resizable BAR config.
Returns size if found or negative error code.

.. _`pci_rebar_set_size`:

pci_rebar_set_size
==================

.. c:function:: int pci_rebar_set_size(struct pci_dev *pdev, int bar, int size)

    set a new size for a BAR

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to set size to
    :type bar: int

    :param size:
        new size as defined in the spec (0=1MB, 19=512GB)
    :type size: int

.. _`pci_rebar_set_size.description`:

Description
-----------

Set the new size of a BAR as defined in the spec.
Returns zero if resizing was successful, error code otherwise.

.. _`pci_enable_atomic_ops_to_root`:

pci_enable_atomic_ops_to_root
=============================

.. c:function:: int pci_enable_atomic_ops_to_root(struct pci_dev *dev, u32 cap_mask)

    enable AtomicOp requests to root port

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param cap_mask:
        mask of desired AtomicOp sizes, including one or more of:
        PCI_EXP_DEVCAP2_ATOMIC_COMP32
        PCI_EXP_DEVCAP2_ATOMIC_COMP64
        PCI_EXP_DEVCAP2_ATOMIC_COMP128
    :type cap_mask: u32

.. _`pci_enable_atomic_ops_to_root.description`:

Description
-----------

Return 0 if all upstream bridges support AtomicOp routing, egress
blocking is disabled on all upstream ports, and the root port supports
the requested completion capabilities (32-bit, 64-bit and/or 128-bit
AtomicOp completion), or negative otherwise.

.. _`pci_swizzle_interrupt_pin`:

pci_swizzle_interrupt_pin
=========================

.. c:function:: u8 pci_swizzle_interrupt_pin(const struct pci_dev *dev, u8 pin)

    swizzle INTx for device behind bridge

    :param dev:
        the PCI device
    :type dev: const struct pci_dev \*

    :param pin:
        the INTx pin (1=INTA, 2=INTB, 3=INTC, 4=INTD)
    :type pin: u8

.. _`pci_swizzle_interrupt_pin.description`:

Description
-----------

Perform INTx swizzling for a device behind one level of bridge.  This is
required by section 9.1 of the PCI-to-PCI bridge specification for devices
behind bridges on add-in cards.  For devices with ARI enabled, the slot
number is always 0 (see the Implementation Note in section 2.2.8.1 of
the PCI Express Base Specification, Revision 2.1)

.. _`pci_common_swizzle`:

pci_common_swizzle
==================

.. c:function:: u8 pci_common_swizzle(struct pci_dev *dev, u8 *pinp)

    swizzle INTx all the way to root bridge

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param pinp:
        pointer to the INTx pin value (1=INTA, 2=INTB, 3=INTD, 4=INTD)
    :type pinp: u8 \*

.. _`pci_common_swizzle.description`:

Description
-----------

Perform INTx swizzling for a device.  This traverses through all PCI-to-PCI
bridges all the way up to a PCI root bus.

.. _`pci_release_region`:

pci_release_region
==================

.. c:function:: void pci_release_region(struct pci_dev *pdev, int bar)

    Release a PCI bar

    :param pdev:
        PCI device whose resources were previously reserved by pci_request_region
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to release
    :type bar: int

.. _`pci_release_region.description`:

Description
-----------

     Releases the PCI I/O and memory resources previously reserved by a
     successful call to pci_request_region.  Call this function only
     after all use of the PCI regions has ceased.

.. _`__pci_request_region`:

__pci_request_region
====================

.. c:function:: int __pci_request_region(struct pci_dev *pdev, int bar, const char *res_name, int exclusive)

    Reserved PCI I/O and memory resource

    :param pdev:
        PCI device whose resources are to be reserved
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to be reserved
    :type bar: int

    :param res_name:
        Name to be associated with resource.
    :type res_name: const char \*

    :param exclusive:
        whether the region access is exclusive or not
    :type exclusive: int

.. _`__pci_request_region.description`:

Description
-----------

     Mark the PCI region associated with PCI device \ ``pdev``\  BR \ ``bar``\  as
     being reserved by owner \ ``res_name``\ .  Do not access any
     address inside the PCI regions unless this call returns
     successfully.

     If \ ``exclusive``\  is set, then the region is marked so that userspace
     is explicitly not allowed to map the resource via /dev/mem or
     sysfs MMIO access.

     Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
     message is also printed on failure.

.. _`pci_request_region`:

pci_request_region
==================

.. c:function:: int pci_request_region(struct pci_dev *pdev, int bar, const char *res_name)

    Reserve PCI I/O and memory resource

    :param pdev:
        PCI device whose resources are to be reserved
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to be reserved
    :type bar: int

    :param res_name:
        Name to be associated with resource
    :type res_name: const char \*

.. _`pci_request_region.description`:

Description
-----------

     Mark the PCI region associated with PCI device \ ``pdev``\  BAR \ ``bar``\  as
     being reserved by owner \ ``res_name``\ .  Do not access any
     address inside the PCI regions unless this call returns
     successfully.

     Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
     message is also printed on failure.

.. _`pci_request_region_exclusive`:

pci_request_region_exclusive
============================

.. c:function:: int pci_request_region_exclusive(struct pci_dev *pdev, int bar, const char *res_name)

    Reserved PCI I/O and memory resource

    :param pdev:
        PCI device whose resources are to be reserved
    :type pdev: struct pci_dev \*

    :param bar:
        BAR to be reserved
    :type bar: int

    :param res_name:
        Name to be associated with resource.
    :type res_name: const char \*

.. _`pci_request_region_exclusive.description`:

Description
-----------

     Mark the PCI region associated with PCI device \ ``pdev``\  BR \ ``bar``\  as
     being reserved by owner \ ``res_name``\ .  Do not access any
     address inside the PCI regions unless this call returns
     successfully.

     Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
     message is also printed on failure.

     The key difference that _exclusive makes it that userspace is
     explicitly not allowed to map the resource via /dev/mem or
     sysfs.

.. _`pci_release_selected_regions`:

pci_release_selected_regions
============================

.. c:function:: void pci_release_selected_regions(struct pci_dev *pdev, int bars)

    Release selected PCI I/O and memory resources

    :param pdev:
        PCI device whose resources were previously reserved
    :type pdev: struct pci_dev \*

    :param bars:
        Bitmask of BARs to be released
    :type bars: int

.. _`pci_release_selected_regions.description`:

Description
-----------

Release selected PCI I/O and memory resources previously reserved.
Call this function only after all use of the PCI regions has ceased.

.. _`pci_request_selected_regions`:

pci_request_selected_regions
============================

.. c:function:: int pci_request_selected_regions(struct pci_dev *pdev, int bars, const char *res_name)

    Reserve selected PCI I/O and memory resources

    :param pdev:
        PCI device whose resources are to be reserved
    :type pdev: struct pci_dev \*

    :param bars:
        Bitmask of BARs to be requested
    :type bars: int

    :param res_name:
        Name to be associated with resource
    :type res_name: const char \*

.. _`pci_release_regions`:

pci_release_regions
===================

.. c:function:: void pci_release_regions(struct pci_dev *pdev)

    Release reserved PCI I/O and memory resources

    :param pdev:
        PCI device whose resources were previously reserved by pci_request_regions
    :type pdev: struct pci_dev \*

.. _`pci_release_regions.description`:

Description
-----------

     Releases all PCI I/O and memory resources previously reserved by a
     successful call to pci_request_regions.  Call this function only
     after all use of the PCI regions has ceased.

.. _`pci_request_regions`:

pci_request_regions
===================

.. c:function:: int pci_request_regions(struct pci_dev *pdev, const char *res_name)

    Reserved PCI I/O and memory resources

    :param pdev:
        PCI device whose resources are to be reserved
    :type pdev: struct pci_dev \*

    :param res_name:
        Name to be associated with resource.
    :type res_name: const char \*

.. _`pci_request_regions.description`:

Description
-----------

     Mark all PCI regions associated with PCI device \ ``pdev``\  as
     being reserved by owner \ ``res_name``\ .  Do not access any
     address inside the PCI regions unless this call returns
     successfully.

     Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
     message is also printed on failure.

.. _`pci_request_regions_exclusive`:

pci_request_regions_exclusive
=============================

.. c:function:: int pci_request_regions_exclusive(struct pci_dev *pdev, const char *res_name)

    Reserved PCI I/O and memory resources

    :param pdev:
        PCI device whose resources are to be reserved
    :type pdev: struct pci_dev \*

    :param res_name:
        Name to be associated with resource.
    :type res_name: const char \*

.. _`pci_request_regions_exclusive.description`:

Description
-----------

     Mark all PCI regions associated with PCI device \ ``pdev``\  as
     being reserved by owner \ ``res_name``\ .  Do not access any
     address inside the PCI regions unless this call returns
     successfully.

     \ :c:func:`pci_request_regions_exclusive`\  will mark the region so that
     /dev/mem and the sysfs MMIO access will not be allowed.

     Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
     message is also printed on failure.

.. _`pci_remap_iospace`:

pci_remap_iospace
=================

.. c:function:: int pci_remap_iospace(const struct resource *res, phys_addr_t phys_addr)

    Remap the memory mapped I/O space

    :param res:
        Resource describing the I/O space
    :type res: const struct resource \*

    :param phys_addr:
        physical address of range to be mapped
    :type phys_addr: phys_addr_t

.. _`pci_remap_iospace.description`:

Description
-----------

     Remap the memory mapped I/O space described by the \ ``res``\ 
     and the CPU physical address \ ``phys_addr``\  into virtual address space.
     Only architectures that have memory mapped IO functions defined
     (and the PCI_IOBASE value defined) should call this function.

.. _`pci_unmap_iospace`:

pci_unmap_iospace
=================

.. c:function:: void pci_unmap_iospace(struct resource *res)

    Unmap the memory mapped I/O space

    :param res:
        resource to be unmapped
    :type res: struct resource \*

.. _`pci_unmap_iospace.description`:

Description
-----------

     Unmap the CPU virtual address \ ``res``\  from virtual address space.
     Only architectures that have memory mapped IO functions defined
     (and the PCI_IOBASE value defined) should call this function.

.. _`devm_pci_remap_iospace`:

devm_pci_remap_iospace
======================

.. c:function:: int devm_pci_remap_iospace(struct device *dev, const struct resource *res, phys_addr_t phys_addr)

    Managed \ :c:func:`pci_remap_iospace`\ 

    :param dev:
        Generic device to remap IO address for
    :type dev: struct device \*

    :param res:
        Resource describing the I/O space
    :type res: const struct resource \*

    :param phys_addr:
        physical address of range to be mapped
    :type phys_addr: phys_addr_t

.. _`devm_pci_remap_iospace.description`:

Description
-----------

Managed \ :c:func:`pci_remap_iospace`\ .  Map is automatically unmapped on driver
detach.

.. _`devm_pci_remap_cfgspace`:

devm_pci_remap_cfgspace
=======================

.. c:function:: void __iomem *devm_pci_remap_cfgspace(struct device *dev, resource_size_t offset, resource_size_t size)

    Managed \ :c:func:`pci_remap_cfgspace`\ 

    :param dev:
        Generic device to remap IO address for
    :type dev: struct device \*

    :param offset:
        Resource address to map
    :type offset: resource_size_t

    :param size:
        Size of map
    :type size: resource_size_t

.. _`devm_pci_remap_cfgspace.description`:

Description
-----------

Managed \ :c:func:`pci_remap_cfgspace`\ .  Map is automatically unmapped on driver
detach.

.. _`devm_pci_remap_cfg_resource`:

devm_pci_remap_cfg_resource
===========================

.. c:function:: void __iomem *devm_pci_remap_cfg_resource(struct device *dev, struct resource *res)

    check, request region and ioremap cfg resource

    :param dev:
        generic device to handle the resource for
    :type dev: struct device \*

    :param res:
        configuration space resource to be handled
    :type res: struct resource \*

.. _`devm_pci_remap_cfg_resource.description`:

Description
-----------

Checks that a resource is a valid memory region, requests the memory
region and ioremaps with \ :c:func:`pci_remap_cfgspace`\  API that ensures the
proper PCI configuration space memory attributes are guaranteed.

All operations are managed and will be undone on driver detach.

Returns a pointer to the remapped memory or an \ :c:func:`ERR_PTR`\  encoded error code
on failure. Usage example::

     res = platform_get_resource(pdev, IORESOURCE_MEM, 0);
     base = devm_pci_remap_cfg_resource(&pdev->dev, res);
     if (IS_ERR(base))
             return PTR_ERR(base);

.. _`pcibios_setup`:

pcibios_setup
=============

.. c:function:: char *pcibios_setup(char *str)

    process "pci=" kernel boot arguments

    :param str:
        string used to pass in "pci=" kernel boot arguments
    :type str: char \*

.. _`pcibios_setup.description`:

Description
-----------

Process kernel boot arguments.  This is the default implementation.
Architecture specific implementations can override this as necessary.

.. _`pcibios_set_master`:

pcibios_set_master
==================

.. c:function:: void pcibios_set_master(struct pci_dev *dev)

    enable PCI bus-mastering for device dev

    :param dev:
        the PCI device to enable
    :type dev: struct pci_dev \*

.. _`pcibios_set_master.description`:

Description
-----------

Enables PCI bus-mastering for the device.  This is the default
implementation.  Architecture specific implementations can override
this if necessary.

.. _`pci_set_master`:

pci_set_master
==============

.. c:function:: void pci_set_master(struct pci_dev *dev)

    enables bus-mastering for device dev

    :param dev:
        the PCI device to enable
    :type dev: struct pci_dev \*

.. _`pci_set_master.description`:

Description
-----------

Enables bus-mastering on the device and calls \ :c:func:`pcibios_set_master`\ 
to do the needed arch specific settings.

.. _`pci_clear_master`:

pci_clear_master
================

.. c:function:: void pci_clear_master(struct pci_dev *dev)

    disables bus-mastering for device dev

    :param dev:
        the PCI device to disable
    :type dev: struct pci_dev \*

.. _`pci_set_cacheline_size`:

pci_set_cacheline_size
======================

.. c:function:: int pci_set_cacheline_size(struct pci_dev *dev)

    ensure the CACHE_LINE_SIZE register is programmed

    :param dev:
        the PCI device for which MWI is to be enabled
    :type dev: struct pci_dev \*

.. _`pci_set_cacheline_size.description`:

Description
-----------

Helper function for pci_set_mwi.
Originally copied from drivers/net/acenic.c.
Copyright 1998-2001 by Jes Sorensen, <jes@trained-monkey.org>.

.. _`pci_set_cacheline_size.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`pci_set_mwi`:

pci_set_mwi
===========

.. c:function:: int pci_set_mwi(struct pci_dev *dev)

    enables memory-write-invalidate PCI transaction

    :param dev:
        the PCI device for which MWI is enabled
    :type dev: struct pci_dev \*

.. _`pci_set_mwi.description`:

Description
-----------

Enables the Memory-Write-Invalidate transaction in \ ``PCI_COMMAND``\ .

.. _`pci_set_mwi.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`pcim_set_mwi`:

pcim_set_mwi
============

.. c:function:: int pcim_set_mwi(struct pci_dev *dev)

    a device-managed \ :c:func:`pci_set_mwi`\ 

    :param dev:
        the PCI device for which MWI is enabled
    :type dev: struct pci_dev \*

.. _`pcim_set_mwi.description`:

Description
-----------

Managed \ :c:func:`pci_set_mwi`\ .

.. _`pcim_set_mwi.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`pci_try_set_mwi`:

pci_try_set_mwi
===============

.. c:function:: int pci_try_set_mwi(struct pci_dev *dev)

    enables memory-write-invalidate PCI transaction

    :param dev:
        the PCI device for which MWI is enabled
    :type dev: struct pci_dev \*

.. _`pci_try_set_mwi.description`:

Description
-----------

Enables the Memory-Write-Invalidate transaction in \ ``PCI_COMMAND``\ .
Callers are not required to check the return value.

.. _`pci_try_set_mwi.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`pci_clear_mwi`:

pci_clear_mwi
=============

.. c:function:: void pci_clear_mwi(struct pci_dev *dev)

    disables Memory-Write-Invalidate for device dev

    :param dev:
        the PCI device to disable
    :type dev: struct pci_dev \*

.. _`pci_clear_mwi.description`:

Description
-----------

Disables PCI Memory-Write-Invalidate transaction on the device

.. _`pci_intx`:

pci_intx
========

.. c:function:: void pci_intx(struct pci_dev *pdev, int enable)

    enables/disables PCI INTx for device dev

    :param pdev:
        the PCI device to operate on
    :type pdev: struct pci_dev \*

    :param enable:
        boolean: whether to enable or disable PCI INTx
    :type enable: int

.. _`pci_intx.description`:

Description
-----------

Enables/disables PCI INTx for device dev

.. _`pci_check_and_mask_intx`:

pci_check_and_mask_intx
=======================

.. c:function:: bool pci_check_and_mask_intx(struct pci_dev *dev)

    mask INTx on pending interrupt

    :param dev:
        the PCI device to operate on
    :type dev: struct pci_dev \*

.. _`pci_check_and_mask_intx.description`:

Description
-----------

Check if the device dev has its INTx line asserted, mask it and
return true in that case. False is returned if no interrupt was
pending.

.. _`pci_check_and_unmask_intx`:

pci_check_and_unmask_intx
=========================

.. c:function:: bool pci_check_and_unmask_intx(struct pci_dev *dev)

    unmask INTx if no interrupt is pending

    :param dev:
        the PCI device to operate on
    :type dev: struct pci_dev \*

.. _`pci_check_and_unmask_intx.description`:

Description
-----------

Check if the device dev has its INTx line asserted, unmask it if not
and return true. False is returned and the mask remains active if
there was still an interrupt pending.

.. _`pci_wait_for_pending_transaction`:

pci_wait_for_pending_transaction
================================

.. c:function:: int pci_wait_for_pending_transaction(struct pci_dev *dev)

    waits for pending transaction

    :param dev:
        the PCI device to operate on
    :type dev: struct pci_dev \*

.. _`pci_wait_for_pending_transaction.description`:

Description
-----------

Return 0 if transaction is pending 1 otherwise.

.. _`pcie_has_flr`:

pcie_has_flr
============

.. c:function:: bool pcie_has_flr(struct pci_dev *dev)

    check if a device supports function level resets

    :param dev:
        device to check
    :type dev: struct pci_dev \*

.. _`pcie_has_flr.description`:

Description
-----------

Returns true if the device advertises support for PCIe function level
resets.

.. _`pcie_flr`:

pcie_flr
========

.. c:function:: int pcie_flr(struct pci_dev *dev)

    initiate a PCIe function level reset

    :param dev:
        device to reset
    :type dev: struct pci_dev \*

.. _`pcie_flr.description`:

Description
-----------

Initiate a function level reset on \ ``dev``\ .  The caller should ensure the
device supports FLR before calling this function, e.g. by using the
\ :c:func:`pcie_has_flr`\  helper.

.. _`pci_pm_reset`:

pci_pm_reset
============

.. c:function:: int pci_pm_reset(struct pci_dev *dev, int probe)

    Put device into PCI_D3 and back into PCI_D0.

    :param dev:
        Device to reset.
    :type dev: struct pci_dev \*

    :param probe:
        If set, only check if the device can be reset this way.
    :type probe: int

.. _`pci_pm_reset.description`:

Description
-----------

If \ ``dev``\  supports native PCI PM and its PCI_PM_CTRL_NO_SOFT_RESET flag is
unset, it will be reinitialized internally when going from PCI_D3hot to
PCI_D0.  If that's the case and the device is not in a low-power state
already, force it into PCI_D3hot and back to PCI_D0, causing it to be reset.

.. _`pci_pm_reset.note`:

NOTE
----

This causes the caller to sleep for twice the device power transition
cooldown period, which for the D0->D3hot and D3hot->D0 transitions is 10 ms
by default (i.e. unless the \ ``dev``\ 's d3_delay field has a different value).
Moreover, only devices in D0 can be reset by this function.

.. _`pcie_wait_for_link`:

pcie_wait_for_link
==================

.. c:function:: bool pcie_wait_for_link(struct pci_dev *pdev, bool active)

    Wait until link is active or inactive

    :param pdev:
        Bridge device
    :type pdev: struct pci_dev \*

    :param active:
        waiting for active or inactive?
    :type active: bool

.. _`pcie_wait_for_link.description`:

Description
-----------

Use this to wait till link becomes active or inactive.

.. _`pci_bridge_secondary_bus_reset`:

pci_bridge_secondary_bus_reset
==============================

.. c:function:: int pci_bridge_secondary_bus_reset(struct pci_dev *dev)

    Reset the secondary bus on a PCI bridge.

    :param dev:
        Bridge device
    :type dev: struct pci_dev \*

.. _`pci_bridge_secondary_bus_reset.description`:

Description
-----------

Use the bridge control register to assert reset on the secondary bus.
Devices on the secondary bus are left in power-on state.

.. _`__pci_reset_function_locked`:

__pci_reset_function_locked
===========================

.. c:function:: int __pci_reset_function_locked(struct pci_dev *dev)

    reset a PCI device function while holding the \ ``dev``\  mutex lock.

    :param dev:
        PCI device to reset
    :type dev: struct pci_dev \*

.. _`__pci_reset_function_locked.description`:

Description
-----------

Some devices allow an individual function to be reset without affecting
other functions in the same device.  The PCI device must be responsive
to PCI config space in order to use this function.

The device function is presumed to be unused and the caller is holding
the device mutex lock when this function is called.
Resetting the device will make the contents of PCI configuration space
random, so any caller of this must be prepared to reinitialise the
device including MSI, bus mastering, BARs, decoding IO and memory spaces,
etc.

Returns 0 if the device function was successfully reset or negative if the
device doesn't support resetting a single function.

.. _`pci_probe_reset_function`:

pci_probe_reset_function
========================

.. c:function:: int pci_probe_reset_function(struct pci_dev *dev)

    check whether the device can be safely reset

    :param dev:
        PCI device to reset
    :type dev: struct pci_dev \*

.. _`pci_probe_reset_function.description`:

Description
-----------

Some devices allow an individual function to be reset without affecting
other functions in the same device.  The PCI device must be responsive
to PCI config space in order to use this function.

Returns 0 if the device function can be reset or negative if the
device doesn't support resetting a single function.

.. _`pci_reset_function`:

pci_reset_function
==================

.. c:function:: int pci_reset_function(struct pci_dev *dev)

    quiesce and reset a PCI device function

    :param dev:
        PCI device to reset
    :type dev: struct pci_dev \*

.. _`pci_reset_function.description`:

Description
-----------

Some devices allow an individual function to be reset without affecting
other functions in the same device.  The PCI device must be responsive
to PCI config space in order to use this function.

This function does not just reset the PCI portion of a device, but
clears all the state associated with the device.  This function differs
from \ :c:func:`__pci_reset_function_locked`\  in that it saves and restores device state
over the reset and takes the PCI device lock.

Returns 0 if the device function was successfully reset or negative if the
device doesn't support resetting a single function.

.. _`pci_reset_function_locked`:

pci_reset_function_locked
=========================

.. c:function:: int pci_reset_function_locked(struct pci_dev *dev)

    quiesce and reset a PCI device function

    :param dev:
        PCI device to reset
    :type dev: struct pci_dev \*

.. _`pci_reset_function_locked.description`:

Description
-----------

Some devices allow an individual function to be reset without affecting
other functions in the same device.  The PCI device must be responsive
to PCI config space in order to use this function.

This function does not just reset the PCI portion of a device, but
clears all the state associated with the device.  This function differs
from \ :c:func:`__pci_reset_function_locked`\  in that it saves and restores device state
over the reset.  It also differs from \ :c:func:`pci_reset_function`\  in that it
requires the PCI device lock to be held.

Returns 0 if the device function was successfully reset or negative if the
device doesn't support resetting a single function.

.. _`pci_try_reset_function`:

pci_try_reset_function
======================

.. c:function:: int pci_try_reset_function(struct pci_dev *dev)

    quiesce and reset a PCI device function

    :param dev:
        PCI device to reset
    :type dev: struct pci_dev \*

.. _`pci_try_reset_function.description`:

Description
-----------

Same as above, except return -EAGAIN if unable to lock device.

.. _`pci_probe_reset_slot`:

pci_probe_reset_slot
====================

.. c:function:: int pci_probe_reset_slot(struct pci_slot *slot)

    probe whether a PCI slot can be reset

    :param slot:
        PCI slot to probe
    :type slot: struct pci_slot \*

.. _`pci_probe_reset_slot.description`:

Description
-----------

Return 0 if slot can be reset, negative if a slot reset is not supported.

.. _`__pci_reset_slot`:

__pci_reset_slot
================

.. c:function:: int __pci_reset_slot(struct pci_slot *slot)

    Try to reset a PCI slot

    :param slot:
        PCI slot to reset
    :type slot: struct pci_slot \*

.. _`__pci_reset_slot.description`:

Description
-----------

A PCI bus may host multiple slots, each slot may support a reset mechanism
independent of other slots.  For instance, some slots may support slot power
control.  In the case of a 1:1 bus to slot architecture, this function may
wrap the bus reset to avoid spurious slot related events such as hotplug.
Generally a slot reset should be attempted before a bus reset.  All of the
function of the slot and any subordinate buses behind the slot are reset
through this function.  PCI config space of all devices in the slot and
behind the slot is saved before and restored after reset.

Same as above except return -EAGAIN if the slot cannot be locked

.. _`pci_bus_error_reset`:

pci_bus_error_reset
===================

.. c:function:: int pci_bus_error_reset(struct pci_dev *bridge)

    reset the bridge's subordinate bus

    :param bridge:
        The parent device that connects to the bus to reset
    :type bridge: struct pci_dev \*

.. _`pci_bus_error_reset.description`:

Description
-----------

This function will first try to reset the slots on this bus if the method is
available. If slot reset fails or is not available, this will fall back to a
secondary bus reset.

.. _`pci_probe_reset_bus`:

pci_probe_reset_bus
===================

.. c:function:: int pci_probe_reset_bus(struct pci_bus *bus)

    probe whether a PCI bus can be reset

    :param bus:
        PCI bus to probe
    :type bus: struct pci_bus \*

.. _`pci_probe_reset_bus.description`:

Description
-----------

Return 0 if bus can be reset, negative if a bus reset is not supported.

.. _`__pci_reset_bus`:

__pci_reset_bus
===============

.. c:function:: int __pci_reset_bus(struct pci_bus *bus)

    Try to reset a PCI bus

    :param bus:
        top level PCI bus to reset
    :type bus: struct pci_bus \*

.. _`__pci_reset_bus.description`:

Description
-----------

Same as above except return -EAGAIN if the bus cannot be locked

.. _`pci_reset_bus`:

pci_reset_bus
=============

.. c:function:: int pci_reset_bus(struct pci_dev *pdev)

    Try to reset a PCI bus

    :param pdev:
        top level PCI device to reset via slot/bus
    :type pdev: struct pci_dev \*

.. _`pci_reset_bus.description`:

Description
-----------

Same as above except return -EAGAIN if the bus cannot be locked

.. _`pcix_get_max_mmrbc`:

pcix_get_max_mmrbc
==================

.. c:function:: int pcix_get_max_mmrbc(struct pci_dev *dev)

    get PCI-X maximum designed memory read byte count

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcix_get_max_mmrbc.description`:

Description
-----------

Returns mmrbc: maximum designed memory read count in bytes
   or appropriate error value.

.. _`pcix_get_mmrbc`:

pcix_get_mmrbc
==============

.. c:function:: int pcix_get_mmrbc(struct pci_dev *dev)

    get PCI-X maximum memory read byte count

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcix_get_mmrbc.description`:

Description
-----------

Returns mmrbc: maximum memory read count in bytes
   or appropriate error value.

.. _`pcix_set_mmrbc`:

pcix_set_mmrbc
==============

.. c:function:: int pcix_set_mmrbc(struct pci_dev *dev, int mmrbc)

    set PCI-X maximum memory read byte count

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param mmrbc:
        maximum memory read count in bytes
        valid values are 512, 1024, 2048, 4096
    :type mmrbc: int

.. _`pcix_set_mmrbc.description`:

Description
-----------

If possible sets maximum memory read byte count, some bridges have erratas
that prevent this.

.. _`pcie_get_readrq`:

pcie_get_readrq
===============

.. c:function:: int pcie_get_readrq(struct pci_dev *dev)

    get PCI Express read request size

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcie_get_readrq.description`:

Description
-----------

Returns maximum memory read request in bytes
   or appropriate error value.

.. _`pcie_set_readrq`:

pcie_set_readrq
===============

.. c:function:: int pcie_set_readrq(struct pci_dev *dev, int rq)

    set PCI Express maximum memory read request

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param rq:
        maximum memory read count in bytes
        valid values are 128, 256, 512, 1024, 2048, 4096
    :type rq: int

.. _`pcie_set_readrq.description`:

Description
-----------

If possible sets maximum memory read request in bytes

.. _`pcie_get_mps`:

pcie_get_mps
============

.. c:function:: int pcie_get_mps(struct pci_dev *dev)

    get PCI Express maximum payload size

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcie_get_mps.description`:

Description
-----------

Returns maximum payload size in bytes

.. _`pcie_set_mps`:

pcie_set_mps
============

.. c:function:: int pcie_set_mps(struct pci_dev *dev, int mps)

    set PCI Express maximum payload size

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param mps:
        maximum payload size in bytes
        valid values are 128, 256, 512, 1024, 2048, 4096
    :type mps: int

.. _`pcie_set_mps.description`:

Description
-----------

If possible sets maximum payload size

.. _`pcie_bandwidth_available`:

pcie_bandwidth_available
========================

.. c:function:: u32 pcie_bandwidth_available(struct pci_dev *dev, struct pci_dev **limiting_dev, enum pci_bus_speed *speed, enum pcie_link_width *width)

    determine minimum link settings of a PCIe device and its bandwidth limitation

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param limiting_dev:
        storage for device causing the bandwidth limitation
    :type limiting_dev: struct pci_dev \*\*

    :param speed:
        storage for speed of limiting device
    :type speed: enum pci_bus_speed \*

    :param width:
        storage for width of limiting device
    :type width: enum pcie_link_width \*

.. _`pcie_bandwidth_available.description`:

Description
-----------

Walk up the PCI device chain and find the point where the minimum
bandwidth is available.  Return the bandwidth available there and (if
limiting_dev, speed, and width pointers are supplied) information about
that point.  The bandwidth returned is in Mb/s, i.e., megabits/second of
raw bandwidth.

.. _`pcie_get_speed_cap`:

pcie_get_speed_cap
==================

.. c:function:: enum pci_bus_speed pcie_get_speed_cap(struct pci_dev *dev)

    query for the PCI device's link speed capability

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcie_get_speed_cap.description`:

Description
-----------

Query the PCI device speed capability.  Return the maximum link speed
supported by the device.

.. _`pcie_get_width_cap`:

pcie_get_width_cap
==================

.. c:function:: enum pcie_link_width pcie_get_width_cap(struct pci_dev *dev)

    query for the PCI device's link width capability

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcie_get_width_cap.description`:

Description
-----------

Query the PCI device width capability.  Return the maximum link width
supported by the device.

.. _`pcie_bandwidth_capable`:

pcie_bandwidth_capable
======================

.. c:function:: u32 pcie_bandwidth_capable(struct pci_dev *dev, enum pci_bus_speed *speed, enum pcie_link_width *width)

    calculate a PCI device's link bandwidth capability

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param speed:
        storage for link speed
    :type speed: enum pci_bus_speed \*

    :param width:
        storage for link width
    :type width: enum pcie_link_width \*

.. _`pcie_bandwidth_capable.description`:

Description
-----------

Calculate a PCI device's link bandwidth by querying for its link speed
and width, multiplying them, and applying encoding overhead.  The result
is in Mb/s, i.e., megabits/second of raw bandwidth.

.. _`__pcie_print_link_status`:

__pcie_print_link_status
========================

.. c:function:: void __pcie_print_link_status(struct pci_dev *dev, bool verbose)

    Report the PCI device's link speed and width

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

    :param verbose:
        Print info even when enough bandwidth is available
    :type verbose: bool

.. _`__pcie_print_link_status.description`:

Description
-----------

If the available bandwidth at the device is less than the device is
capable of, report the device's maximum possible bandwidth and the
upstream link that limits its performance.  If \ ``verbose``\ , always print
the available bandwidth, even if the device isn't constrained.

.. _`pcie_print_link_status`:

pcie_print_link_status
======================

.. c:function:: void pcie_print_link_status(struct pci_dev *dev)

    Report the PCI device's link speed and width

    :param dev:
        PCI device to query
    :type dev: struct pci_dev \*

.. _`pcie_print_link_status.description`:

Description
-----------

Report the available bandwidth at the device.

.. _`pci_select_bars`:

pci_select_bars
===============

.. c:function:: int pci_select_bars(struct pci_dev *dev, unsigned long flags)

    Make BAR mask from the type of resource

    :param dev:
        the PCI device for which BAR mask is made
    :type dev: struct pci_dev \*

    :param flags:
        resource type mask to be selected
    :type flags: unsigned long

.. _`pci_select_bars.description`:

Description
-----------

This helper routine makes bar mask from the type of resource.

.. _`pci_set_vga_state`:

pci_set_vga_state
=================

.. c:function:: int pci_set_vga_state(struct pci_dev *dev, bool decode, unsigned int command_bits, u32 flags)

    set VGA decode state on device and parents if requested

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param decode:
        true = enable decoding, false = disable decoding
    :type decode: bool

    :param command_bits:
        PCI_COMMAND_IO and/or PCI_COMMAND_MEMORY
    :type command_bits: unsigned int

    :param flags:
        traverse ancestors and change bridges
        CHANGE_BRIDGE_ONLY / CHANGE_BRIDGE
    :type flags: u32

.. _`pci_add_dma_alias`:

pci_add_dma_alias
=================

.. c:function:: void pci_add_dma_alias(struct pci_dev *dev, u8 devfn)

    Add a DMA devfn alias for a device

    :param dev:
        the PCI device for which alias is added
    :type dev: struct pci_dev \*

    :param devfn:
        alias slot and function
    :type devfn: u8

.. _`pci_add_dma_alias.description`:

Description
-----------

This helper encodes an 8-bit devfn as a bit number in dma_alias_mask
which is used to program permissible bus-devfn source addresses for DMA
requests in an IOMMU.  These aliases factor into IOMMU group creation
and are useful for devices generating DMA requests beyond or different
from their logical bus-devfn.  Examples include device quirks where the
device simply uses the wrong devfn, as well as non-transparent bridges
where the alias may be a proxy for devices in another domain.

IOMMU group creation is performed during device discovery or addition,
prior to any potential DMA mapping and therefore prior to driver probing
(especially for userspace assigned devices where IOMMU group definition
cannot be left as a userspace activity).  DMA aliases should therefore
be configured via quirks, such as the PCI fixup header quirk.

.. _`pci_specified_resource_alignment`:

pci_specified_resource_alignment
================================

.. c:function:: resource_size_t pci_specified_resource_alignment(struct pci_dev *dev, bool *resize)

    get resource alignment specified by user.

    :param dev:
        the PCI device to get
    :type dev: struct pci_dev \*

    :param resize:
        whether or not to change resources' size when reassigning alignment
    :type resize: bool \*

.. _`pci_specified_resource_alignment.return`:

Return
------

Resource alignment if it is specified.
         Zero if it is not specified.

.. _`pci_ext_cfg_avail`:

pci_ext_cfg_avail
=================

.. c:function:: int pci_ext_cfg_avail( void)

    can we access extended PCI config space?

    :param void:
        no arguments
    :type void: 

.. _`pci_ext_cfg_avail.description`:

Description
-----------

Returns 1 if we can access PCI extended config space (offsets
greater than 0xff). This is the default implementation. Architecture
implementations can override this.

.. This file was automatic generated / don't edit.

