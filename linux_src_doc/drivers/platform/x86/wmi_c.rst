.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/wmi.c

.. _`set_required_buffer_size`:

set_required_buffer_size
========================

.. c:function:: int set_required_buffer_size(struct wmi_device *wdev, u64 length)

    Sets the buffer size needed for performing IOCTL

    :param wdev:
        A wmi bus device from a driver
    :type wdev: struct wmi_device \*

    :param length:
        *undescribed*
    :type length: u64

.. _`set_required_buffer_size.description`:

Description
-----------

Allocates memory needed for buffer, stores the buffer size in that memory

.. _`wmi_evaluate_method`:

wmi_evaluate_method
===================

.. c:function:: acpi_status wmi_evaluate_method(const char *guid_string, u8 instance, u32 method_id, const struct acpi_buffer *in, struct acpi_buffer *out)

    Evaluate a WMI method

    :param guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba
    :type guid_string: const char \*

    :param instance:
        Instance index
    :type instance: u8

    :param method_id:
        Method ID to call
        \ :c:type:`struct in <in>`\ : Buffer containing input for the method call
        \ :c:type:`struct out <out>`\ : Empty buffer to return the method results
    :type method_id: u32

    :param in:
        *undescribed*
    :type in: const struct acpi_buffer \*

    :param out:
        *undescribed*
    :type out: struct acpi_buffer \*

.. _`wmi_evaluate_method.description`:

Description
-----------

Call an ACPI-WMI method

.. _`wmidev_evaluate_method`:

wmidev_evaluate_method
======================

.. c:function:: acpi_status wmidev_evaluate_method(struct wmi_device *wdev, u8 instance, u32 method_id, const struct acpi_buffer *in, struct acpi_buffer *out)

    Evaluate a WMI method

    :param wdev:
        A wmi bus device from a driver
    :type wdev: struct wmi_device \*

    :param instance:
        Instance index
    :type instance: u8

    :param method_id:
        Method ID to call
        \ :c:type:`struct in <in>`\ : Buffer containing input for the method call
        \ :c:type:`struct out <out>`\ : Empty buffer to return the method results
    :type method_id: u32

    :param in:
        *undescribed*
    :type in: const struct acpi_buffer \*

    :param out:
        *undescribed*
    :type out: struct acpi_buffer \*

.. _`wmidev_evaluate_method.description`:

Description
-----------

Call an ACPI-WMI method

.. _`wmi_query_block`:

wmi_query_block
===============

.. c:function:: acpi_status wmi_query_block(const char *guid_string, u8 instance, struct acpi_buffer *out)

    Return contents of a WMI block (deprecated)

    :param guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba
    :type guid_string: const char \*

    :param instance:
        Instance index
        \ :c:type:`struct out <out>`\ : Empty buffer to return the contents of the data block to
    :type instance: u8

    :param out:
        *undescribed*
    :type out: struct acpi_buffer \*

.. _`wmi_query_block.description`:

Description
-----------

Return the contents of an ACPI-WMI data block to a buffer

.. _`wmi_set_block`:

wmi_set_block
=============

.. c:function:: acpi_status wmi_set_block(const char *guid_string, u8 instance, const struct acpi_buffer *in)

    Write to a WMI block

    :param guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba
    :type guid_string: const char \*

    :param instance:
        Instance index
        \ :c:type:`struct in <in>`\ : Buffer containing new values for the data block
    :type instance: u8

    :param in:
        *undescribed*
    :type in: const struct acpi_buffer \*

.. _`wmi_set_block.description`:

Description
-----------

Write the contents of the input buffer to an ACPI-WMI data block

.. _`wmi_install_notify_handler`:

wmi_install_notify_handler
==========================

.. c:function:: acpi_status wmi_install_notify_handler(const char *guid, wmi_notify_handler handler, void *data)

    Register handler for WMI events

    :param guid:
        *undescribed*
    :type guid: const char \*

    :param handler:
        Function to handle notifications
    :type handler: wmi_notify_handler

    :param data:
        Data to be returned to handler when event is fired
    :type data: void \*

.. _`wmi_install_notify_handler.description`:

Description
-----------

Register a handler for events sent to the ACPI-WMI mapper device.

.. _`wmi_remove_notify_handler`:

wmi_remove_notify_handler
=========================

.. c:function:: acpi_status wmi_remove_notify_handler(const char *guid)

    Unregister handler for WMI events

    :param guid:
        *undescribed*
    :type guid: const char \*

.. _`wmi_remove_notify_handler.description`:

Description
-----------

Unregister handler for events sent to the ACPI-WMI mapper device.

.. _`wmi_get_event_data`:

wmi_get_event_data
==================

.. c:function:: acpi_status wmi_get_event_data(u32 event, struct acpi_buffer *out)

    Get WMI data associated with an event

    :param event:
        Event to find
    :type event: u32

    :param out:
        Buffer to hold event data. out->pointer should be freed with \ :c:func:`kfree`\ 
    :type out: struct acpi_buffer \*

.. _`wmi_get_event_data.description`:

Description
-----------

Returns extra data associated with an event in WMI.

.. _`wmi_has_guid`:

wmi_has_guid
============

.. c:function:: bool wmi_has_guid(const char *guid_string)

    Check if a GUID is available

    :param guid_string:
        36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba
    :type guid_string: const char \*

.. _`wmi_has_guid.description`:

Description
-----------

Check if a given GUID is defined by \_WDG

.. This file was automatic generated / don't edit.

