.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/acpiphp_ibm.c

.. _`ibm_slot_from_id`:

ibm_slot_from_id
================

.. c:function:: union apci_descriptor *ibm_slot_from_id(int id)

    workaround for bad ibm hardware

    :param id:
        the slot number that linux refers to the slot by
    :type id: int

.. _`ibm_slot_from_id.description`:

Description
-----------

This method returns the aCPI slot descriptor
corresponding to the Linux slot number.  This descriptor
has info about the aPCI slot id and attention status.
This descriptor must be freed using kfree when done.

.. _`ibm_set_attention_status`:

ibm_set_attention_status
========================

.. c:function:: int ibm_set_attention_status(struct hotplug_slot *slot, u8 status)

    callback method to set the attention LED

    :param slot:
        the hotplug_slot to work with
    :type slot: struct hotplug_slot \*

    :param status:
        what to set the LED to (0 or 1)
    :type status: u8

.. _`ibm_set_attention_status.description`:

Description
-----------

This method is registered with the acpiphp module as a
callback to do the device specific task of setting the LED status.

.. _`ibm_get_attention_status`:

ibm_get_attention_status
========================

.. c:function:: int ibm_get_attention_status(struct hotplug_slot *slot, u8 *status)

    callback method to get attention LED status

    :param slot:
        the hotplug_slot to work with
    :type slot: struct hotplug_slot \*

    :param status:
        returns what the LED is set to (0 or 1)
    :type status: u8 \*

.. _`ibm_get_attention_status.description`:

Description
-----------

This method is registered with the acpiphp module as a
callback to do the device specific task of getting the LED status.

Because there is no direct method of getting the LED status directly
from an ACPI call, we read the aPCI table and parse out our
slot descriptor to read the status from that.

.. _`ibm_handle_events`:

ibm_handle_events
=================

.. c:function:: void ibm_handle_events(acpi_handle handle, u32 event, void *context)

    listens for ACPI events for the IBM37D0 device

    :param handle:
        an ACPI handle to the device that caused the event
    :type handle: acpi_handle

    :param event:
        the event info (device specific)
    :type event: u32

    :param context:
        passed context (our notification struct)
    :type context: void \*

.. _`ibm_handle_events.description`:

Description
-----------

This method is registered as a callback with the ACPI
subsystem it is called when this device has an event to notify the OS of.

The events actually come from the device as two events that get
synthesized into one event with data by this function.  The event
ID comes first and then the slot number that caused it.  We report
this as one event to the OS.

From section 5.6.2.2 of the ACPI 2.0 spec, I understand that the OSPM will
only re-enable the interrupt that causes this event AFTER this method
has returned, thereby enforcing serial access for the notification struct.

.. _`ibm_get_table_from_acpi`:

ibm_get_table_from_acpi
=======================

.. c:function:: int ibm_get_table_from_acpi(char **bufp)

    reads the APLS buffer from ACPI

    :param bufp:
        address to pointer to allocate for the table
    :type bufp: char \*\*

.. _`ibm_get_table_from_acpi.description`:

Description
-----------

This method reads the APLS buffer in from ACPI and
stores the "stripped" table into a single buffer
it allocates and passes the address back in bufp.

If NULL is passed in as buffer, this method only calculates
the size of the table and returns that without filling
in the buffer.

Returns < 0 on error or the size of the table on success.

.. _`ibm_read_apci_table`:

ibm_read_apci_table
===================

.. c:function:: ssize_t ibm_read_apci_table(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buffer, loff_t pos, size_t size)

    callback for the sysfs apci_table file

    :param filp:
        the open sysfs file
    :type filp: struct file \*

    :param kobj:
        the kobject this binary attribute is a part of
    :type kobj: struct kobject \*

    :param bin_attr:
        struct bin_attribute for this file
    :type bin_attr: struct bin_attribute \*

    :param buffer:
        the kernel space buffer to fill
    :type buffer: char \*

    :param pos:
        the offset into the file
    :type pos: loff_t

    :param size:
        the number of bytes requested
    :type size: size_t

.. _`ibm_read_apci_table.description`:

Description
-----------

Gets registered with sysfs as the reader callback
to be executed when /sys/bus/pci/slots/apci_table gets read.

Since we don't get notified on open and close for this file,
things get really tricky here...
our solution is to only allow reading the table in all at once.

.. _`ibm_find_acpi_device`:

ibm_find_acpi_device
====================

.. c:function:: acpi_status ibm_find_acpi_device(acpi_handle handle, u32 lvl, void *context, void **rv)

    callback to find our ACPI device

    :param handle:
        the ACPI handle of the device we are inspecting
    :type handle: acpi_handle

    :param lvl:
        depth into the namespace tree
    :type lvl: u32

    :param context:
        a pointer to our handle to fill when we find the device
    :type context: void \*

    :param rv:
        a return value to fill if desired
    :type rv: void \*\*

.. _`ibm_find_acpi_device.description`:

Description
-----------

Used as a callback when calling acpi_walk_namespace
to find our device.  When this method returns non-zero
acpi_walk_namespace quits its search and returns our value.

.. This file was automatic generated / don't edit.

