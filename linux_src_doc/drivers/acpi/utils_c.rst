.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/utils.c

.. _`acpi_evaluate_ost`:

acpi_evaluate_ost
=================

.. c:function:: acpi_status acpi_evaluate_ost(acpi_handle handle, u32 source_event, u32 status_code, struct acpi_buffer *status_buf)

    Evaluate \_OST for hotplug operations

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

    :param source_event:
        source event code
    :type source_event: u32

    :param status_code:
        status code
    :type status_code: u32

    :param status_buf:
        optional detailed information (NULL if none)
    :type status_buf: struct acpi_buffer \*

.. _`acpi_evaluate_ost.description`:

Description
-----------

Evaluate \_OST for hotplug operations. All ACPI hotplug handlers
must call this function when evaluating \_OST for hotplug operations.
When the platform does not support \_OST, this function has no effect.

.. _`acpi_handle_path`:

acpi_handle_path
================

.. c:function:: char *acpi_handle_path(acpi_handle handle)

    Return the object path of handle

    :param handle:
        *undescribed*
    :type handle: acpi_handle

.. _`acpi_handle_path.description`:

Description
-----------

Caller must free the returned buffer

.. _`acpi_handle_printk`:

acpi_handle_printk
==================

.. c:function:: void acpi_handle_printk(const char *level, acpi_handle handle, const char *fmt,  ...)

    Print message with ACPI prefix and object path

    :param level:
        *undescribed*
    :type level: const char \*

    :param handle:
        *undescribed*
    :type handle: acpi_handle

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`acpi_handle_printk.description`:

Description
-----------

This function is called through acpi_handle_<level> macros and prints
a message with ACPI prefix and object path.  This function acquires
the global namespace mutex to obtain an object path.  In interrupt
context, it shows the object path as <n/a>.

.. _`__acpi_handle_debug`:

\__acpi_handle_debug
====================

.. c:function:: void __acpi_handle_debug(struct _ddebug *descriptor, acpi_handle handle, const char *fmt,  ...)

    pr_debug with ACPI prefix and object path

    :param descriptor:
        *undescribed*
    :type descriptor: struct _ddebug \*

    :param handle:
        *undescribed*
    :type handle: acpi_handle

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`__acpi_handle_debug.description`:

Description
-----------

This function is called through acpi_handle_debug macro and debug
prints a message with ACPI prefix and object path. This function
acquires the global namespace mutex to obtain an object path.  In
interrupt context, it shows the object path as <n/a>.

.. _`acpi_has_method`:

acpi_has_method
===============

.. c:function:: bool acpi_has_method(acpi_handle handle, char *name)

    Check whether \ ``handle``\  has a method named \ ``name``\ 

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

    :param name:
        name of object or method
    :type name: char \*

.. _`acpi_has_method.description`:

Description
-----------

Check whether \ ``handle``\  has a method named \ ``name``\ .

.. _`acpi_evaluate_ej0`:

acpi_evaluate_ej0
=================

.. c:function:: acpi_status acpi_evaluate_ej0(acpi_handle handle)

    Evaluate \_EJ0 method for hotplug operations

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

.. _`acpi_evaluate_ej0.description`:

Description
-----------

Evaluate device's \_EJ0 method for hotplug operations.

.. _`acpi_evaluate_lck`:

acpi_evaluate_lck
=================

.. c:function:: acpi_status acpi_evaluate_lck(acpi_handle handle, int lock)

    Evaluate \_LCK method to lock/unlock device

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

    :param lock:
        lock device if non-zero, otherwise unlock device
    :type lock: int

.. _`acpi_evaluate_lck.description`:

Description
-----------

Evaluate device's \_LCK method if present to lock/unlock device

.. _`acpi_evaluate_dsm`:

acpi_evaluate_dsm
=================

.. c:function:: union acpi_object *acpi_evaluate_dsm(acpi_handle handle, const guid_t *guid, u64 rev, u64 func, union acpi_object *argv4)

    evaluate device's \_DSM method

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

    :param guid:
        GUID of requested functions, should be 16 bytes
    :type guid: const guid_t \*

    :param rev:
        revision number of requested function
    :type rev: u64

    :param func:
        requested function number
    :type func: u64

    :param argv4:
        the function specific parameter
    :type argv4: union acpi_object \*

.. _`acpi_evaluate_dsm.description`:

Description
-----------

Evaluate device's \_DSM method with specified GUID, revision id and
function number. Caller needs to free the returned object.

Though ACPI defines the fourth parameter for \_DSM should be a package,
some old BIOSes do expect a buffer or an integer etc.

.. _`acpi_check_dsm`:

acpi_check_dsm
==============

.. c:function:: bool acpi_check_dsm(acpi_handle handle, const guid_t *guid, u64 rev, u64 funcs)

    check if \_DSM method supports requested functions.

    :param handle:
        ACPI device handle
    :type handle: acpi_handle

    :param guid:
        GUID of requested functions, should be 16 bytes at least
    :type guid: const guid_t \*

    :param rev:
        revision number of requested functions
    :type rev: u64

    :param funcs:
        bitmap of requested functions
    :type funcs: u64

.. _`acpi_check_dsm.description`:

Description
-----------

Evaluate device's \_DSM method to check whether it supports requested
functions. Currently only support 64 functions at maximum, should be
enough for now.

.. _`acpi_dev_found`:

acpi_dev_found
==============

.. c:function:: bool acpi_dev_found(const char *hid)

    Detect presence of a given ACPI device in the namespace.

    :param hid:
        Hardware ID of the device.
    :type hid: const char \*

.. _`acpi_dev_found.description`:

Description
-----------

Return \ ``true``\  if the device was present at the moment of invocation.
Note that if the device is pluggable, it may since have disappeared.

For this function to work, \ :c:func:`acpi_bus_scan`\  must have been executed
which happens in the \ :c:func:`subsys_initcall`\  subsection. Hence, do not
call from a \ :c:func:`subsys_initcall`\  or earlier (use \ :c:func:`acpi_get_devices`\ 
instead). Calling from \ :c:func:`module_init`\  is fine (which is synonymous
with \ :c:func:`device_initcall`\ ).

.. _`acpi_dev_present`:

acpi_dev_present
================

.. c:function:: bool acpi_dev_present(const char *hid, const char *uid, s64 hrv)

    Detect that a given ACPI device is present

    :param hid:
        Hardware ID of the device.
    :type hid: const char \*

    :param uid:
        Unique ID of the device, pass NULL to not check \_UID
    :type uid: const char \*

    :param hrv:
        Hardware Revision of the device, pass -1 to not check \_HRV
    :type hrv: s64

.. _`acpi_dev_present.description`:

Description
-----------

Return \ ``true``\  if a matching device was present at the moment of invocation.
Note that if the device is pluggable, it may since have disappeared.

Note that unlike \ :c:func:`acpi_dev_found`\  this function checks the status
of the device. So for devices which are present in the dsdt, but
which are disabled (their \_STA callback returns 0) this function
will return false.

For this function to work, \ :c:func:`acpi_bus_scan`\  must have been executed
which happens in the \ :c:func:`subsys_initcall`\  subsection. Hence, do not
call from a \ :c:func:`subsys_initcall`\  or earlier (use \ :c:func:`acpi_get_devices`\ 
instead). Calling from \ :c:func:`module_init`\  is fine (which is synonymous
with \ :c:func:`device_initcall`\ ).

.. _`acpi_dev_get_first_match_name`:

acpi_dev_get_first_match_name
=============================

.. c:function:: const char *acpi_dev_get_first_match_name(const char *hid, const char *uid, s64 hrv)

    Return name of first match of ACPI device

    :param hid:
        Hardware ID of the device.
    :type hid: const char \*

    :param uid:
        Unique ID of the device, pass NULL to not check \_UID
    :type uid: const char \*

    :param hrv:
        Hardware Revision of the device, pass -1 to not check \_HRV
    :type hrv: s64

.. _`acpi_dev_get_first_match_name.description`:

Description
-----------

Return device name if a matching device was present
at the moment of invocation, or NULL otherwise.

See additional information in \ :c:func:`acpi_dev_present`\  as well.

.. _`acpi_match_platform_list`:

acpi_match_platform_list
========================

.. c:function:: int acpi_match_platform_list(const struct acpi_platform_list *plat)

    Check if the system matches with a given list

    :param plat:
        pointer to acpi_platform_list table terminated by a NULL entry
    :type plat: const struct acpi_platform_list \*

.. _`acpi_match_platform_list.description`:

Description
-----------

Return the matched index if the system is found in the platform list.
Otherwise, return a negative error code.

.. This file was automatic generated / don't edit.

