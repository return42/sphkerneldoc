.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_acpi.c

.. _`amdgpu_atif_call`:

amdgpu_atif_call
================

.. c:function:: union acpi_object *amdgpu_atif_call(struct amdgpu_atif *atif, int function, struct acpi_buffer *params)

    call an ATIF method

    :param atif:
        *undescribed*
    :type atif: struct amdgpu_atif \*

    :param function:
        the ATIF function to execute
    :type function: int

    :param params:
        ATIF function params
    :type params: struct acpi_buffer \*

.. _`amdgpu_atif_call.description`:

Description
-----------

Executes the requested ATIF function (all asics).
Returns a pointer to the acpi output buffer.

.. _`amdgpu_atif_parse_notification`:

amdgpu_atif_parse_notification
==============================

.. c:function:: void amdgpu_atif_parse_notification(struct amdgpu_atif_notifications *n, u32 mask)

    parse supported notifications

    :param n:
        supported notifications struct
    :type n: struct amdgpu_atif_notifications \*

    :param mask:
        supported notifications mask from ATIF
    :type mask: u32

.. _`amdgpu_atif_parse_notification.description`:

Description
-----------

Use the supported notifications mask from ATIF function
ATIF_FUNCTION_VERIFY_INTERFACE to determine what notifications
are supported (all asics).

.. _`amdgpu_atif_parse_functions`:

amdgpu_atif_parse_functions
===========================

.. c:function:: void amdgpu_atif_parse_functions(struct amdgpu_atif_functions *f, u32 mask)

    parse supported functions

    :param f:
        supported functions struct
    :type f: struct amdgpu_atif_functions \*

    :param mask:
        supported functions mask from ATIF
    :type mask: u32

.. _`amdgpu_atif_parse_functions.description`:

Description
-----------

Use the supported functions mask from ATIF function
ATIF_FUNCTION_VERIFY_INTERFACE to determine what functions
are supported (all asics).

.. _`amdgpu_atif_verify_interface`:

amdgpu_atif_verify_interface
============================

.. c:function:: int amdgpu_atif_verify_interface(struct amdgpu_atif *atif)

    verify ATIF

    :param atif:
        amdgpu atif struct
    :type atif: struct amdgpu_atif \*

.. _`amdgpu_atif_verify_interface.description`:

Description
-----------

Execute the ATIF_FUNCTION_VERIFY_INTERFACE ATIF function
to initialize ATIF and determine what features are supported
(all asics).
returns 0 on success, error on failure.

.. _`amdgpu_atif_get_notification_params`:

amdgpu_atif_get_notification_params
===================================

.. c:function:: int amdgpu_atif_get_notification_params(struct amdgpu_atif *atif)

    determine notify configuration

    :param atif:
        *undescribed*
    :type atif: struct amdgpu_atif \*

.. _`amdgpu_atif_get_notification_params.description`:

Description
-----------

Execute the ATIF_FUNCTION_GET_SYSTEM_PARAMETERS ATIF function
to determine if a notifier is used and if so which one
(all asics).  This is either Notify(VGA, 0x81) or Notify(VGA, n)
where n is specified in the result if a notifier is used.
Returns 0 on success, error on failure.

.. _`amdgpu_atif_get_sbios_requests`:

amdgpu_atif_get_sbios_requests
==============================

.. c:function:: int amdgpu_atif_get_sbios_requests(struct amdgpu_atif *atif, struct atif_sbios_requests *req)

    get requested sbios event

    :param atif:
        *undescribed*
    :type atif: struct amdgpu_atif \*

    :param req:
        atif sbios request struct
    :type req: struct atif_sbios_requests \*

.. _`amdgpu_atif_get_sbios_requests.description`:

Description
-----------

Execute the ATIF_FUNCTION_GET_SYSTEM_BIOS_REQUESTS ATIF function
to determine what requests the sbios is making to the driver
(all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atif_handler`:

amdgpu_atif_handler
===================

.. c:function:: int amdgpu_atif_handler(struct amdgpu_device *adev, struct acpi_bus_event *event)

    handle ATIF notify requests

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param event:
        atif sbios request struct
    :type event: struct acpi_bus_event \*

.. _`amdgpu_atif_handler.description`:

Description
-----------

Checks the acpi event and if it matches an atif event,
handles it.

.. _`amdgpu_atif_handler.return`:

Return
------

NOTIFY_BAD or NOTIFY_DONE, depending on the event.

.. _`amdgpu_atcs_call`:

amdgpu_atcs_call
================

.. c:function:: union acpi_object *amdgpu_atcs_call(acpi_handle handle, int function, struct acpi_buffer *params)

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

.. _`amdgpu_atcs_call.description`:

Description
-----------

Executes the requested ATCS function (all asics).
Returns a pointer to the acpi output buffer.

.. _`amdgpu_atcs_parse_functions`:

amdgpu_atcs_parse_functions
===========================

.. c:function:: void amdgpu_atcs_parse_functions(struct amdgpu_atcs_functions *f, u32 mask)

    parse supported functions

    :param f:
        supported functions struct
    :type f: struct amdgpu_atcs_functions \*

    :param mask:
        supported functions mask from ATCS
    :type mask: u32

.. _`amdgpu_atcs_parse_functions.description`:

Description
-----------

Use the supported functions mask from ATCS function
ATCS_FUNCTION_VERIFY_INTERFACE to determine what functions
are supported (all asics).

.. _`amdgpu_atcs_verify_interface`:

amdgpu_atcs_verify_interface
============================

.. c:function:: int amdgpu_atcs_verify_interface(acpi_handle handle, struct amdgpu_atcs *atcs)

    verify ATCS

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param atcs:
        amdgpu atcs struct
    :type atcs: struct amdgpu_atcs \*

.. _`amdgpu_atcs_verify_interface.description`:

Description
-----------

Execute the ATCS_FUNCTION_VERIFY_INTERFACE ATCS function
to initialize ATCS and determine what features are supported
(all asics).
returns 0 on success, error on failure.

.. _`amdgpu_acpi_is_pcie_performance_request_supported`:

amdgpu_acpi_is_pcie_performance_request_supported
=================================================

.. c:function:: bool amdgpu_acpi_is_pcie_performance_request_supported(struct amdgpu_device *adev)

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_acpi_is_pcie_performance_request_supported.description`:

Description
-----------

Check if the ATCS pcie_perf_req and pcie_dev_rdy methods
are supported (all asics).
returns true if supported, false if not.

.. _`amdgpu_acpi_pcie_notify_device_ready`:

amdgpu_acpi_pcie_notify_device_ready
====================================

.. c:function:: int amdgpu_acpi_pcie_notify_device_ready(struct amdgpu_device *adev)

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_acpi_pcie_notify_device_ready.description`:

Description
-----------

Executes the PCIE_DEVICE_READY_NOTIFICATION method
(all asics).
returns 0 on success, error on failure.

.. _`amdgpu_acpi_pcie_performance_request`:

amdgpu_acpi_pcie_performance_request
====================================

.. c:function:: int amdgpu_acpi_pcie_performance_request(struct amdgpu_device *adev, u8 perf_req, bool advertise)

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param perf_req:
        requested perf level (pcie gen speed)
    :type perf_req: u8

    :param advertise:
        set advertise caps flag if set
    :type advertise: bool

.. _`amdgpu_acpi_pcie_performance_request.description`:

Description
-----------

Executes the PCIE_PERFORMANCE_REQUEST method to
change the pcie gen speed (all asics).
returns 0 on success, error on failure.

.. _`amdgpu_acpi_event`:

amdgpu_acpi_event
=================

.. c:function:: int amdgpu_acpi_event(struct notifier_block *nb, unsigned long val, void *data)

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

.. _`amdgpu_acpi_event.description`:

Description
-----------

Calls relevant amdgpu functions in response to various
acpi events.
Returns NOTIFY code

.. _`amdgpu_acpi_init`:

amdgpu_acpi_init
================

.. c:function:: int amdgpu_acpi_init(struct amdgpu_device *adev)

    init driver acpi support

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_acpi_init.description`:

Description
-----------

Verifies the AMD ACPI interfaces and registers with the acpi
notifier chain (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_acpi_fini`:

amdgpu_acpi_fini
================

.. c:function:: void amdgpu_acpi_fini(struct amdgpu_device *adev)

    tear down driver acpi support

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_acpi_fini.description`:

Description
-----------

Unregisters with the acpi notifier chain (all asics).

.. This file was automatic generated / don't edit.

