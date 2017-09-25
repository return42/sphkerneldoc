.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/host/pci-hyperv.c

.. _`hv_msi_desc`:

struct hv_msi_desc
==================

.. c:type:: struct hv_msi_desc


.. _`hv_msi_desc.definition`:

Definition
----------

.. code-block:: c

    struct hv_msi_desc {
        u8 vector;
        u8 delivery_mode;
        u16 vector_count;
        u32 reserved;
        u64 cpu_mask;
    }

.. _`hv_msi_desc.members`:

Members
-------

vector
    IDT entry

delivery_mode
    As defined in Intel's Programmer's
    Reference Manual, Volume 3, Chapter 8.

vector_count
    Number of contiguous entries in the
    Interrupt Descriptor Table that are
    occupied by this Message-Signaled
    Interrupt. For "MSI", as first defined
    in PCI 2.2, this can be between 1 and
    32. For "MSI-X," as first defined in PCI
    3.0, this must be 1, as each MSI-X table
    entry would have its own descriptor.

reserved
    Empty space

cpu_mask
    All the target virtual processors.

.. _`hv_msi_desc2`:

struct hv_msi_desc2
===================

.. c:type:: struct hv_msi_desc2

    1.2 version of hv_msi_desc

.. _`hv_msi_desc2.definition`:

Definition
----------

.. code-block:: c

    struct hv_msi_desc2 {
        u8 vector;
        u8 delivery_mode;
        u16 vector_count;
        u16 processor_count;
        u16 processor_array[32];
    }

.. _`hv_msi_desc2.members`:

Members
-------

vector
    IDT entry

delivery_mode
    As defined in Intel's Programmer's
    Reference Manual, Volume 3, Chapter 8.

vector_count
    Number of contiguous entries in the
    Interrupt Descriptor Table that are
    occupied by this Message-Signaled
    Interrupt. For "MSI", as first defined
    in PCI 2.2, this can be between 1 and
    32. For "MSI-X," as first defined in PCI
    3.0, this must be 1, as each MSI-X table
    entry would have its own descriptor.

processor_count
    number of bits enabled in array.

processor_array
    All the target virtual processors.

.. _`tran_int_desc`:

struct tran_int_desc
====================

.. c:type:: struct tran_int_desc


.. _`tran_int_desc.definition`:

Definition
----------

.. code-block:: c

    struct tran_int_desc {
        u16 reserved;
        u16 vector_count;
        u32 data;
        u64 address;
    }

.. _`tran_int_desc.members`:

Members
-------

reserved
    unused, padding

vector_count
    same as in hv_msi_desc

data
    This is the "data payload" value that is
    written by the device when it generates
    a message-signaled interrupt, either MSI
    or MSI-X.

address
    This is the address to which the data
    payload is written on interrupt
    generation.

.. _`hv_pci_generic_compl`:

hv_pci_generic_compl
====================

.. c:function:: void hv_pci_generic_compl(void *context, struct pci_response *resp, int resp_packet_size)

    Invoked for a completion packet

    :param void \*context:
        Set up by the sender of the packet.

    :param struct pci_response \*resp:
        The response packet

    :param int resp_packet_size:
        Size in bytes of the packet

.. _`hv_pci_generic_compl.description`:

Description
-----------

This function is used to trigger an event and report status
for any message for which the completion packet contains a
status and nothing else.

.. _`devfn_to_wslot`:

devfn_to_wslot
==============

.. c:function:: u32 devfn_to_wslot(int devfn)

    Convert from Linux PCI slot to Windows

    :param int devfn:
        The Linux representation of PCI slot

.. _`devfn_to_wslot.description`:

Description
-----------

Windows uses a slightly different representation of PCI slot.

.. _`devfn_to_wslot.return`:

Return
------

The Windows representation

.. _`wslot_to_devfn`:

wslot_to_devfn
==============

.. c:function:: int wslot_to_devfn(u32 wslot)

    Convert from Windows PCI slot to Linux

    :param u32 wslot:
        The Windows representation of PCI slot

.. _`wslot_to_devfn.description`:

Description
-----------

Windows uses a slightly different representation of PCI slot.

.. _`wslot_to_devfn.return`:

Return
------

The Linux representation

.. _`_hv_pcifront_read_config`:

_hv_pcifront_read_config
========================

.. c:function:: void _hv_pcifront_read_config(struct hv_pci_dev *hpdev, int where, int size, u32 *val)

    Internal PCI config read

    :param struct hv_pci_dev \*hpdev:
        The PCI driver's representation of the device

    :param int where:
        Offset within config space

    :param int size:
        Size of the transfer

    :param u32 \*val:
        Pointer to the buffer receiving the data

.. _`_hv_pcifront_write_config`:

_hv_pcifront_write_config
=========================

.. c:function:: void _hv_pcifront_write_config(struct hv_pci_dev *hpdev, int where, int size, u32 val)

    Internal PCI config write

    :param struct hv_pci_dev \*hpdev:
        The PCI driver's representation of the device

    :param int where:
        Offset within config space

    :param int size:
        Size of the transfer

    :param u32 val:
        The data being transferred

.. _`hv_pcifront_read_config`:

hv_pcifront_read_config
=======================

.. c:function:: int hv_pcifront_read_config(struct pci_bus *bus, unsigned int devfn, int where, int size, u32 *val)

    Read configuration space

    :param struct pci_bus \*bus:
        PCI Bus structure

    :param unsigned int devfn:
        Device/function

    :param int where:
        Offset from base

    :param int size:
        Byte/word/dword

    :param u32 \*val:
        Value to be read

.. _`hv_pcifront_read_config.return`:

Return
------

PCIBIOS_SUCCESSFUL on success
PCIBIOS_DEVICE_NOT_FOUND on failure

.. _`hv_pcifront_write_config`:

hv_pcifront_write_config
========================

.. c:function:: int hv_pcifront_write_config(struct pci_bus *bus, unsigned int devfn, int where, int size, u32 val)

    Write configuration space

    :param struct pci_bus \*bus:
        PCI Bus structure

    :param unsigned int devfn:
        Device/function

    :param int where:
        Offset from base

    :param int size:
        Byte/word/dword

    :param u32 val:
        Value to be written to device

.. _`hv_pcifront_write_config.return`:

Return
------

PCIBIOS_SUCCESSFUL on success
PCIBIOS_DEVICE_NOT_FOUND on failure

.. _`hv_msi_free`:

hv_msi_free
===========

.. c:function:: void hv_msi_free(struct irq_domain *domain, struct msi_domain_info *info, unsigned int irq)

    Free the MSI.

    :param struct irq_domain \*domain:
        The interrupt domain pointer

    :param struct msi_domain_info \*info:
        Extra MSI-related context

    :param unsigned int irq:
        Identifies the IRQ.

.. _`hv_msi_free.description`:

Description
-----------

The Hyper-V parent partition and hypervisor are tracking the
messages that are in use, keeping the interrupt redirection
table up to date.  This callback sends a message that frees
the IRT entry and related tracking nonsense.

.. _`hv_irq_unmask`:

hv_irq_unmask
=============

.. c:function:: void hv_irq_unmask(struct irq_data *data)

    "Unmask" the IRQ by setting its current affinity.

    :param struct irq_data \*data:
        Describes the IRQ

.. _`hv_irq_unmask.description`:

Description
-----------

Build new a destination for the MSI and make a hypercall to
update the Interrupt Redirection Table. "Device Logical ID"
is built out of this PCI bus's instance GUID and the function
number of the device.

.. _`hv_compose_msi_msg`:

hv_compose_msi_msg
==================

.. c:function:: void hv_compose_msi_msg(struct irq_data *data, struct msi_msg *msg)

    Supplies a valid MSI address/data

    :param struct irq_data \*data:
        Everything about this MSI

    :param struct msi_msg \*msg:
        Buffer that is filled in by this function

.. _`hv_compose_msi_msg.description`:

Description
-----------

This function unpacks the IRQ looking for target CPU set, IDT
vector and mode and sends a message to the parent partition
asking for a mapping for that tuple in this partition.  The
response supplies a data value and address to which that data
should be written to trigger that interrupt.

.. _`hv_pcie_init_irq_domain`:

hv_pcie_init_irq_domain
=======================

.. c:function:: int hv_pcie_init_irq_domain(struct hv_pcibus_device *hbus)

    Initialize IRQ domain

    :param struct hv_pcibus_device \*hbus:
        The root PCI bus

.. _`hv_pcie_init_irq_domain.description`:

Description
-----------

This function creates an IRQ domain which will be used for
interrupts from devices that have been passed through.  These
devices only support MSI and MSI-X, not line-based interrupts
or simulations of line-based interrupts through PCIe's
fabric-layer messages.  Because interrupts are remapped, we
can support multi-message MSI here.

.. _`hv_pcie_init_irq_domain.return`:

Return
------

'0' on success and error value on failure

.. _`get_bar_size`:

get_bar_size
============

.. c:function:: u64 get_bar_size(u64 bar_val)

    Get the address space consumed by a BAR

    :param u64 bar_val:
        Value that a BAR returned after -1 was written
        to it.

.. _`get_bar_size.description`:

Description
-----------

This function returns the size of the BAR, rounded up to 1
page.  It has to be rounded up because the hypervisor's page
table entry that maps the BAR into the VM can't specify an
offset within a page.  The invariant is that the hypervisor
must place any BARs of smaller than page length at the
beginning of a page.

.. _`get_bar_size.return`:

Return
------

Size in bytes of the consumed MMIO space.

.. _`survey_child_resources`:

survey_child_resources
======================

.. c:function:: void survey_child_resources(struct hv_pcibus_device *hbus)

    Total all MMIO requirements

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

.. _`prepopulate_bars`:

prepopulate_bars
================

.. c:function:: void prepopulate_bars(struct hv_pcibus_device *hbus)

    Fill in BARs with defaults

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

.. _`prepopulate_bars.description`:

Description
-----------

The core PCI driver code seems much, much happier if the BARs
for a device have values upon first scan. So fill them in.
The algorithm below works down from large sizes to small,
attempting to pack the assignments optimally. The assumption,
enforced in other parts of the code, is that the beginning of
the memory-mapped I/O space will be aligned on the largest
BAR size.

.. _`create_root_hv_pci_bus`:

create_root_hv_pci_bus
======================

.. c:function:: int create_root_hv_pci_bus(struct hv_pcibus_device *hbus)

    Expose a new root PCI bus

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

.. _`create_root_hv_pci_bus.return`:

Return
------

0 on success, -errno on failure

.. _`q_resource_requirements`:

q_resource_requirements
=======================

.. c:function:: void q_resource_requirements(void *context, struct pci_response *resp, int resp_packet_size)

    Query Resource Requirements

    :param void \*context:
        The completion context.

    :param struct pci_response \*resp:
        The response that came from the host.

    :param int resp_packet_size:
        The size in bytes of resp.

.. _`q_resource_requirements.description`:

Description
-----------

This function is invoked on completion of a Query Resource
Requirements packet.

.. _`new_pcichild_device`:

new_pcichild_device
===================

.. c:function:: struct hv_pci_dev *new_pcichild_device(struct hv_pcibus_device *hbus, struct pci_function_description *desc)

    Create a new child device

    :param struct hv_pcibus_device \*hbus:
        The internal struct tracking this root PCI bus.

    :param struct pci_function_description \*desc:
        The information supplied so far from the host
        about the device.

.. _`new_pcichild_device.description`:

Description
-----------

This function creates the tracking structure for a new child
device and kicks off the process of figuring out what it is.

.. _`new_pcichild_device.return`:

Return
------

Pointer to the new tracking struct

.. _`get_pcichild_wslot`:

get_pcichild_wslot
==================

.. c:function:: struct hv_pci_dev *get_pcichild_wslot(struct hv_pcibus_device *hbus, u32 wslot)

    Find device from slot

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

    :param u32 wslot:
        Location on the bus

.. _`get_pcichild_wslot.description`:

Description
-----------

This function looks up a PCI device and returns the internal
representation of it.  It acquires a reference on it, so that
the device won't be deleted while somebody is using it.  The
caller is responsible for calling \ :c:func:`put_pcichild`\  to release
this reference.

.. _`get_pcichild_wslot.return`:

Return
------

Internal representation of a PCI device

.. _`pci_devices_present_work`:

pci_devices_present_work
========================

.. c:function:: void pci_devices_present_work(struct work_struct *work)

    Handle new list of child devices

    :param struct work_struct \*work:
        Work struct embedded in struct hv_dr_work

.. _`pci_devices_present_work.description`:

Description
-----------

"Bus Relations" is the Windows term for "children of this
bus."  The terminology is preserved here for people trying to
debug the interaction between Hyper-V and Linux.  This
function is called when the parent partition reports a list
of functions that should be observed under this PCI Express
port (bus).

This function updates the list, and must tolerate being
called multiple times with the same information.  The typical
number of child devices is one, with very atypical cases
involving three or four, so the algorithms used here can be
simple and inefficient.

It must also treat the omission of a previously observed device as
notification that the device no longer exists.

Note that this function is a work item, and it may not be
invoked in the order that it was queued.  Back to back
updates of the list of present devices may involve queuing
multiple work items, and this one may run before ones that
were sent later. As such, this function only does something
if is the last one in the queue.

.. _`hv_pci_devices_present`:

hv_pci_devices_present
======================

.. c:function:: void hv_pci_devices_present(struct hv_pcibus_device *hbus, struct pci_bus_relations *relations)

    Handles list of new children

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

    :param struct pci_bus_relations \*relations:
        Packet from host listing children

.. _`hv_pci_devices_present.description`:

Description
-----------

This function is invoked whenever a new list of devices for
this bus appears.

.. _`hv_eject_device_work`:

hv_eject_device_work
====================

.. c:function:: void hv_eject_device_work(struct work_struct *work)

    Asynchronously handles ejection

    :param struct work_struct \*work:
        Work struct embedded in internal device struct

.. _`hv_eject_device_work.description`:

Description
-----------

This function handles ejecting a device.  Windows will
attempt to gracefully eject a device, waiting 60 seconds to
hear back from the guest OS that this completed successfully.
If this timer expires, the device will be forcibly removed.

.. _`hv_pci_eject_device`:

hv_pci_eject_device
===================

.. c:function:: void hv_pci_eject_device(struct hv_pci_dev *hpdev)

    Handles device ejection

    :param struct hv_pci_dev \*hpdev:
        Internal device tracking struct

.. _`hv_pci_eject_device.description`:

Description
-----------

This function is invoked when an ejection packet arrives.  It
just schedules work so that we don't re-enter the packet
delivery code handling the ejection.

.. _`hv_pci_onchannelcallback`:

hv_pci_onchannelcallback
========================

.. c:function:: void hv_pci_onchannelcallback(void *context)

    Handles incoming packets

    :param void \*context:
        Internal bus tracking struct

.. _`hv_pci_onchannelcallback.description`:

Description
-----------

This function is invoked whenever the host sends a packet to
this channel (which is private to this root PCI bus).

.. _`hv_pci_protocol_negotiation`:

hv_pci_protocol_negotiation
===========================

.. c:function:: int hv_pci_protocol_negotiation(struct hv_device *hdev)

    Set up protocol

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

.. _`hv_pci_protocol_negotiation.description`:

Description
-----------

This driver is intended to support running on Windows 10
(server) and later versions. It will not run on earlier
versions, as they assume that many of the operations which
Linux needs accomplished with a spinlock held were done via
asynchronous messaging via VMBus.  Windows 10 increases the
surface area of PCI emulation so that these actions can take
place by suspending a virtual processor for their duration.

This function negotiates the channel protocol version,
failing if the host doesn't support the necessary protocol
level.

.. _`hv_pci_free_bridge_windows`:

hv_pci_free_bridge_windows
==========================

.. c:function:: void hv_pci_free_bridge_windows(struct hv_pcibus_device *hbus)

    Release memory regions for the bus

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

.. _`hv_pci_allocate_bridge_windows`:

hv_pci_allocate_bridge_windows
==============================

.. c:function:: int hv_pci_allocate_bridge_windows(struct hv_pcibus_device *hbus)

    Allocate memory regions for the bus

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

.. _`hv_pci_allocate_bridge_windows.description`:

Description
-----------

This function calls \ :c:func:`vmbus_allocate_mmio`\ , which is itself a
bit of a compromise.  Ideally, we might change the pnp layer
in the kernel such that it comprehends either PCI devices
which are "grandchildren of ACPI," with some intermediate bus
node (in this case, VMBus) or change it such that it
understands VMBus.  The pnp layer, however, has been declared
deprecated, and not subject to change.

The workaround, implemented here, is to ask VMBus to allocate
MMIO space for this bus.  VMBus itself knows which ranges are
appropriate by looking at its own ACPI objects.  Then, after
these ranges are claimed, they're modified to look like they
would have looked if the ACPI and pnp code had allocated
bridge windows.  These descriptors have to exist in this form
in order to satisfy the code which will get invoked when the
endpoint PCI function driver calls \ :c:func:`request_mem_region`\  or
\ :c:func:`request_mem_region_exclusive`\ .

.. _`hv_pci_allocate_bridge_windows.return`:

Return
------

0 on success, -errno on failure

.. _`hv_allocate_config_window`:

hv_allocate_config_window
=========================

.. c:function:: int hv_allocate_config_window(struct hv_pcibus_device *hbus)

    Find MMIO space for PCI Config

    :param struct hv_pcibus_device \*hbus:
        Root PCI bus, as understood by this driver

.. _`hv_allocate_config_window.description`:

Description
-----------

This function claims memory-mapped I/O space for accessing
configuration space for the functions on this bus.

.. _`hv_allocate_config_window.return`:

Return
------

0 on success, -errno on failure

.. _`hv_pci_enter_d0`:

hv_pci_enter_d0
===============

.. c:function:: int hv_pci_enter_d0(struct hv_device *hdev)

    Bring the "bus" into the D0 power state

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

.. _`hv_pci_enter_d0.return`:

Return
------

0 on success, -errno on failure

.. _`hv_pci_query_relations`:

hv_pci_query_relations
======================

.. c:function:: int hv_pci_query_relations(struct hv_device *hdev)

    Ask host to send list of child devices

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

.. _`hv_pci_query_relations.return`:

Return
------

0 on success, -errno on failure

.. _`hv_send_resources_allocated`:

hv_send_resources_allocated
===========================

.. c:function:: int hv_send_resources_allocated(struct hv_device *hdev)

    Report local resource choices

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

.. _`hv_send_resources_allocated.description`:

Description
-----------

The host OS is expecting to be sent a request as a message
which contains all the resources that the device will use.
The response contains those same resources, "translated"
which is to say, the values which should be used by the
hardware, when it delivers an interrupt.  (MMIO resources are
used in local terms.)  This is nice for Windows, and lines up
with the FDO/PDO split, which doesn't exist in Linux.  Linux
is deeply expecting to scan an emulated PCI configuration
space.  So this message is sent here only to drive the state
machine on the host forward.

.. _`hv_send_resources_allocated.return`:

Return
------

0 on success, -errno on failure

.. _`hv_send_resources_released`:

hv_send_resources_released
==========================

.. c:function:: int hv_send_resources_released(struct hv_device *hdev)

    Report local resources released

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

.. _`hv_send_resources_released.return`:

Return
------

0 on success, -errno on failure

.. _`hv_pci_probe`:

hv_pci_probe
============

.. c:function:: int hv_pci_probe(struct hv_device *hdev, const struct hv_vmbus_device_id *dev_id)

    New VMBus channel probe, for a root PCI bus

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

    :param const struct hv_vmbus_device_id \*dev_id:
        Identifies the device itself

.. _`hv_pci_probe.return`:

Return
------

0 on success, -errno on failure

.. _`hv_pci_remove`:

hv_pci_remove
=============

.. c:function:: int hv_pci_remove(struct hv_device *hdev)

    Remove routine for this VMBus channel

    :param struct hv_device \*hdev:
        VMBus's tracking struct for this root PCI bus

.. _`hv_pci_remove.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

