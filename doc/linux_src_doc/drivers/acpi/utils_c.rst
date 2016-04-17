.. -*- coding: utf-8; mode: rst -*-

=======
utils.c
=======


.. _`acpi_evaluate_ost`:

acpi_evaluate_ost
=================

.. c:function:: acpi_status acpi_evaluate_ost (acpi_handle handle, u32 source_event, u32 status_code, struct acpi_buffer *status_buf)

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

Evaluate _OST for hotplug operations. All ACPI hotplug handlers
must call this function when evaluating _OST for hotplug operations.
When the platform does not support _OST, this function has no effect.



.. _`acpi_handle_path`:

acpi_handle_path
================

.. c:function:: char *acpi_handle_path (acpi_handle handle)

    :param acpi_handle handle:

        *undescribed*



.. _`acpi_handle_path.description`:

Description
-----------


Caller must free the returned buffer



.. _`acpi_handle_printk`:

acpi_handle_printk
==================

.. c:function:: void acpi_handle_printk (const char *level, acpi_handle handle, const char *fmt,  ...)

    :param const char \*level:

        *undescribed*

    :param acpi_handle handle:

        *undescribed*

    :param const char \*fmt:

        *undescribed*

    :param ...:
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

.. c:function:: void __acpi_handle_debug (struct _ddebug *descriptor, acpi_handle handle, const char *fmt,  ...)

    :param struct _ddebug \*descriptor:

        *undescribed*

    :param acpi_handle handle:

        *undescribed*

    :param const char \*fmt:

        *undescribed*

    :param ...:
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

.. c:function:: bool acpi_has_method (acpi_handle handle, char *name)

    :param acpi_handle handle:
        ACPI device handle

    :param char \*name:
        name of object or method



.. _`acpi_has_method.description`:

Description
-----------

Check whether ``handle`` has a method named ``name``\ .



.. _`acpi_evaluate_ej0`:

acpi_evaluate_ej0
=================

.. c:function:: acpi_status acpi_evaluate_ej0 (acpi_handle handle)

    :param acpi_handle handle:
        ACPI device handle



.. _`acpi_evaluate_ej0.description`:

Description
-----------

Evaluate device's _EJ0 method for hotplug operations.



.. _`acpi_evaluate_lck`:

acpi_evaluate_lck
=================

.. c:function:: acpi_status acpi_evaluate_lck (acpi_handle handle, int lock)

    :param acpi_handle handle:
        ACPI device handle

    :param int lock:
        lock device if non-zero, otherwise unlock device



.. _`acpi_evaluate_lck.description`:

Description
-----------

Evaluate device's _LCK method if present to lock/unlock device



.. _`acpi_evaluate_dsm`:

acpi_evaluate_dsm
=================

.. c:function:: union acpi_object *acpi_evaluate_dsm (acpi_handle handle, const u8 *uuid, int rev, int func, union acpi_object *argv4)

    evaluate device's _DSM method

    :param acpi_handle handle:
        ACPI device handle

    :param const u8 \*uuid:
        UUID of requested functions, should be 16 bytes

    :param int rev:
        revision number of requested function

    :param int func:
        requested function number

    :param union acpi_object \*argv4:
        the function specific parameter



.. _`acpi_evaluate_dsm.description`:

Description
-----------

Evaluate device's _DSM method with specified UUID, revision id and
function number. Caller needs to free the returned object.

Though ACPI defines the fourth parameter for _DSM should be a package,
some old BIOSes do expect a buffer or an integer etc.



.. _`acpi_check_dsm`:

acpi_check_dsm
==============

.. c:function:: bool acpi_check_dsm (acpi_handle handle, const u8 *uuid, int rev, u64 funcs)

    check if _DSM method supports requested functions.

    :param acpi_handle handle:
        ACPI device handle

    :param const u8 \*uuid:
        UUID of requested functions, should be 16 bytes at least

    :param int rev:
        revision number of requested functions

    :param u64 funcs:
        bitmap of requested functions



.. _`acpi_check_dsm.description`:

Description
-----------

Evaluate device's _DSM method to check whether it supports requested
functions. Currently only support 64 functions at maximum, should be
enough for now.



.. _`acpi_dev_present`:

acpi_dev_present
================

.. c:function:: bool acpi_dev_present (const char *hid)

    Detect presence of a given ACPI device in the system.

    :param const char \*hid:
        Hardware ID of the device.



.. _`acpi_dev_present.description`:

Description
-----------

Return ``true`` if the device was present at the moment of invocation.
Note that if the device is pluggable, it may since have disappeared.

For this function to work, :c:func:`acpi_bus_scan` must have been executed
which happens in the :c:func:`subsys_initcall` subsection. Hence, do not
call from a :c:func:`subsys_initcall` or earlier (use :c:func:`acpi_get_devices`
instead). Calling from :c:func:`module_init` is fine (which is synonymous
with :c:func:`device_initcall`).

