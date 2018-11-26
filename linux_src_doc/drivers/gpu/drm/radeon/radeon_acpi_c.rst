.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_acpi.c

.. _`radeon_atif_call`:

radeon_atif_call
================

.. c:function:: union acpi_object *radeon_atif_call(acpi_handle handle, int function, struct acpi_buffer *params)

    call an ATIF method

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param function:
        the ATIF function to execute
    :type function: int

    :param params:
        ATIF function params
    :type params: struct acpi_buffer \*

.. _`radeon_atif_call.description`:

Description
-----------

Executes the requested ATIF function (all asics).
Returns a pointer to the acpi output buffer.

.. _`radeon_atif_parse_notification`:

radeon_atif_parse_notification
==============================

.. c:function:: void radeon_atif_parse_notification(struct radeon_atif_notifications *n, u32 mask)

    parse supported notifications

    :param n:
        supported notifications struct
    :type n: struct radeon_atif_notifications \*

    :param mask:
        supported notifications mask from ATIF
    :type mask: u32

.. _`radeon_atif_parse_notification.description`:

Description
-----------

Use the supported notifications mask from ATIF function
ATIF_FUNCTION_VERIFY_INTERFACE to determine what notifications
are supported (all asics).

.. _`radeon_atif_parse_functions`:

radeon_atif_parse_functions
===========================

.. c:function:: void radeon_atif_parse_functions(struct radeon_atif_functions *f, u32 mask)

    parse supported functions

    :param f:
        supported functions struct
    :type f: struct radeon_atif_functions \*

    :param mask:
        supported functions mask from ATIF
    :type mask: u32

.. _`radeon_atif_parse_functions.description`:

Description
-----------

Use the supported functions mask from ATIF function
ATIF_FUNCTION_VERIFY_INTERFACE to determine what functions
are supported (all asics).

.. _`radeon_atif_verify_interface`:

radeon_atif_verify_interface
============================

.. c:function:: int radeon_atif_verify_interface(acpi_handle handle, struct radeon_atif *atif)

    verify ATIF

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param atif:
        radeon atif struct
    :type atif: struct radeon_atif \*

.. _`radeon_atif_verify_interface.description`:

Description
-----------

Execute the ATIF_FUNCTION_VERIFY_INTERFACE ATIF function
to initialize ATIF and determine what features are supported
(all asics).
returns 0 on success, error on failure.

.. _`radeon_atif_get_notification_params`:

radeon_atif_get_notification_params
===================================

.. c:function:: int radeon_atif_get_notification_params(acpi_handle handle, struct radeon_atif_notification_cfg *n)

    determine notify configuration

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param n:
        atif notification configuration struct
    :type n: struct radeon_atif_notification_cfg \*

.. _`radeon_atif_get_notification_params.description`:

Description
-----------

Execute the ATIF_FUNCTION_GET_SYSTEM_PARAMETERS ATIF function
to determine if a notifier is used and if so which one
(all asics).  This is either Notify(VGA, 0x81) or Notify(VGA, n)
where n is specified in the result if a notifier is used.
Returns 0 on success, error on failure.

.. _`radeon_atif_get_sbios_requests`:

radeon_atif_get_sbios_requests
==============================

.. c:function:: int radeon_atif_get_sbios_requests(acpi_handle handle, struct atif_sbios_requests *req)

    get requested sbios event

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param req:
        atif sbios request struct
    :type req: struct atif_sbios_requests \*

.. _`radeon_atif_get_sbios_requests.description`:

Description
-----------

Execute the ATIF_FUNCTION_GET_SYSTEM_BIOS_REQUESTS ATIF function
to determine what requests the sbios is making to the driver
(all asics).
Returns 0 on success, error on failure.

.. _`radeon_atif_handler`:

radeon_atif_handler
===================

.. c:function:: int radeon_atif_handler(struct radeon_device *rdev, struct acpi_bus_event *event)

    handle ATIF notify requests

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param event:
        atif sbios request struct
    :type event: struct acpi_bus_event \*

.. _`radeon_atif_handler.description`:

Description
-----------

Checks the acpi event and if it matches an atif event,
handles it.
Returns NOTIFY code

.. _`radeon_atcs_call`:

radeon_atcs_call
================

.. c:function:: union acpi_object *radeon_atcs_call(acpi_handle handle, int function, struct acpi_buffer *params)

    call an ATCS method

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param function:
        the ATCS function to execute
    :type function: int

    :param params:
        ATCS function params
    :type params: struct acpi_buffer \*

.. _`radeon_atcs_call.description`:

Description
-----------

Executes the requested ATCS function (all asics).
Returns a pointer to the acpi output buffer.

.. _`radeon_atcs_parse_functions`:

radeon_atcs_parse_functions
===========================

.. c:function:: void radeon_atcs_parse_functions(struct radeon_atcs_functions *f, u32 mask)

    parse supported functions

    :param f:
        supported functions struct
    :type f: struct radeon_atcs_functions \*

    :param mask:
        supported functions mask from ATCS
    :type mask: u32

.. _`radeon_atcs_parse_functions.description`:

Description
-----------

Use the supported functions mask from ATCS function
ATCS_FUNCTION_VERIFY_INTERFACE to determine what functions
are supported (all asics).

.. _`radeon_atcs_verify_interface`:

radeon_atcs_verify_interface
============================

.. c:function:: int radeon_atcs_verify_interface(acpi_handle handle, struct radeon_atcs *atcs)

    verify ATCS

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param atcs:
        radeon atcs struct
    :type atcs: struct radeon_atcs \*

.. _`radeon_atcs_verify_interface.description`:

Description
-----------

Execute the ATCS_FUNCTION_VERIFY_INTERFACE ATCS function
to initialize ATCS and determine what features are supported
(all asics).
returns 0 on success, error on failure.

.. _`radeon_acpi_is_pcie_performance_request_supported`:

radeon_acpi_is_pcie_performance_request_supported
=================================================

.. c:function:: bool radeon_acpi_is_pcie_performance_request_supported(struct radeon_device *rdev)

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_acpi_is_pcie_performance_request_supported.description`:

Description
-----------

Check if the ATCS pcie_perf_req and pcie_dev_rdy methods
are supported (all asics).
returns true if supported, false if not.

.. _`radeon_acpi_pcie_notify_device_ready`:

radeon_acpi_pcie_notify_device_ready
====================================

.. c:function:: int radeon_acpi_pcie_notify_device_ready(struct radeon_device *rdev)

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_acpi_pcie_notify_device_ready.description`:

Description
-----------

Executes the PCIE_DEVICE_READY_NOTIFICATION method
(all asics).
returns 0 on success, error on failure.

.. _`radeon_acpi_pcie_performance_request`:

radeon_acpi_pcie_performance_request
====================================

.. c:function:: int radeon_acpi_pcie_performance_request(struct radeon_device *rdev, u8 perf_req, bool advertise)

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param perf_req:
        requested perf level (pcie gen speed)
    :type perf_req: u8

    :param advertise:
        set advertise caps flag if set
    :type advertise: bool

.. _`radeon_acpi_pcie_performance_request.description`:

Description
-----------

Executes the PCIE_PERFORMANCE_REQUEST method to
change the pcie gen speed (all asics).
returns 0 on success, error on failure.

.. _`radeon_acpi_event`:

radeon_acpi_event
=================

.. c:function:: int radeon_acpi_event(struct notifier_block *nb, unsigned long val, void *data)

    handle notify events

    :param nb:
        notifier block
    :type nb: struct notifier_block \*

    :param val:
        val
    :type val: unsigned long

    :param data:
        acpi event
    :type data: void \*

.. _`radeon_acpi_event.description`:

Description
-----------

Calls relevant radeon functions in response to various
acpi events.
Returns NOTIFY code

.. _`radeon_acpi_init`:

radeon_acpi_init
================

.. c:function:: int radeon_acpi_init(struct radeon_device *rdev)

    init driver acpi support

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_acpi_init.description`:

Description
-----------

Verifies the AMD ACPI interfaces and registers with the acpi
notifier chain (all asics).
Returns 0 on success, error on failure.

.. _`radeon_acpi_fini`:

radeon_acpi_fini
================

.. c:function:: void radeon_acpi_fini(struct radeon_device *rdev)

    tear down driver acpi support

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_acpi_fini.description`:

Description
-----------

Unregisters with the acpi notifier chain (all asics).

.. This file was automatic generated / don't edit.

