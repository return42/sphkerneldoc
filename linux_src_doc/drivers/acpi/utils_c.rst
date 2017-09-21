.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/utils.c

.. _`acpi_evaluate_ost`:

acpi_evaluate_ost
=================

.. c:function:: acpi_status acpi_evaluate_ost(acpi_handle handle, u32 source_event, u32 status_code, struct acpi_buffer *status_buf)

    Evaluate \_OST for hotplug operations

    :param acpi_handle handle:
        ACPI device handle

    :param u32 source_event:
        source event code

    :param u32 status_code:
        status code

    :param struct acpi_buffer \*status_buf:
        optional detailed information (NULL if none)

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

    :param acpi_handle handle:
        *undescribed*

.. _`acpi_handle_path.description`:

Description
-----------

Caller must free the returned buffer

.. _`acpi_handle_printk`:

acpi_handle_printk
==================

.. c:function:: void acpi_handle_printk(const char *level, acpi_handle handle, const char *fmt,  ...)

    Print message with ACPI prefix and object path

    :param const char \*level:
        *undescribed*

    :param acpi_handle handle:
        *undescribed*

    :param const char \*fmt:
        *undescribed*

    :param ... :
        variable arguments

.. _`acpi_handle_printk.description`:

Description
-----------

This function is called through acpi_handle_<level> macros and prints
a message with ACPI prefix and object path.  This function acquires
the global namespace mutex to obtain an object path.  In interrupt
context, it shows the object path as <n/a>.

.. _`__acpi_handle_debug`:

__acpi_handle_debug
===================

.. c:function:: void __acpi_handle_debug(struct _ddebug *descriptor, acpi_handle handle, const char *fmt,  ...)

    pr_debug with ACPI prefix and object path

    :param struct _ddebug \*descriptor:
        *undescribed*

    :param acpi_handle handle:
        *undescribed*

    :param const char \*fmt:
        *undescribed*

    :param ... :
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

    :param acpi_handle handle:
        ACPI device handle

    :param char \*name:
        name of object or method

.. _`acpi_has_method.description`:

Description
-----------

Check whether \ ``handle``\  has a method named \ ``name``\ .

.. _`acpi_evaluate_ej0`:

acpi_evaluate_ej0
=================

.. c:function:: acpi_status acpi_evaluate_ej0(acpi_handle handle)

    Evaluate \_EJ0 method for hotplug operations

    :param acpi_handle handle:
        ACPI device handle

.. _`acpi_evaluate_ej0.description`:

Description
-----------

Evaluate device's \_EJ0 method for hotplug operations.

.. _`acpi_evaluate_lck`:

acpi_evaluate_lck
=================

.. c:function:: acpi_status acpi_evaluate_lck(acpi_handle handle, int lock)

    Evaluate \_LCK method to lock/unlock device

    :param acpi_handle handle:
        ACPI device handle

    :param int lock:
        lock device if non-zero, otherwise unlock device

.. _`acpi_evaluate_lck.description`:

Description
-----------

Evaluate device's \_LCK method if present to lock/unlock device

.. _`acpi_evaluate_dsm`:

acpi_evaluate_dsm
=================

.. c:function:: union acpi_object *acpi_evaluate_dsm(acpi_handle handle, const guid_t *guid, u64 rev, u64 func, union acpi_object *argv4)

    evaluate device's \_DSM method

    :param acpi_handle handle:
        ACPI device handle

    :param const guid_t \*guid:
        GUID of requested functions, should be 16 bytes

    :param u64 rev:
        revision number of requested function

    :param u64 func:
        requested function number

    :param union acpi_object \*argv4:
        the function specific parameter

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

    :param acpi_handle handle:
        ACPI device handle

    :param const guid_t \*guid:
        GUID of requested functions, should be 16 bytes at least

    :param u64 rev:
        revision number of requested functions

    :param u64 funcs:
        bitmap of requested functions

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

    :param const char \*hid:
        Hardware ID of the device.

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

    :param const char \*hid:
        Hardware ID of the device.

    :param const char \*uid:
        Unique ID of the device, pass NULL to not check \_UID

    :param s64 hrv:
        Hardware Revision of the device, pass -1 to not check \_HRV

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

.. _`acpi_match_platform_list`:

acpi_match_platform_list
========================

.. c:function:: int acpi_match_platform_list(const struct acpi_platform_list *plat)

    Check if the system matches with a given list

    :param const struct acpi_platform_list \*plat:
        pointer to acpi_platform_list table terminated by a NULL entry

.. _`acpi_match_platform_list.description`:

Description
-----------

Return the matched index if the system is found in the platform list.
Otherwise, return a negative error code.

.. This file was automatic generated / don't edit.

