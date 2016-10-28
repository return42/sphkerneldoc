.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_atpx_handler.c

.. _`amdgpu_atpx_call`:

amdgpu_atpx_call
================

.. c:function:: union acpi_object *amdgpu_atpx_call(acpi_handle handle, int function, struct acpi_buffer *params)

    call an ATPX method

    :param acpi_handle handle:
        acpi handle

    :param int function:
        the ATPX function to execute

    :param struct acpi_buffer \*params:
        ATPX function params

.. _`amdgpu_atpx_call.description`:

Description
-----------

Executes the requested ATPX function (all asics).
Returns a pointer to the acpi output buffer.

.. _`amdgpu_atpx_parse_functions`:

amdgpu_atpx_parse_functions
===========================

.. c:function:: void amdgpu_atpx_parse_functions(struct amdgpu_atpx_functions *f, u32 mask)

    parse supported functions

    :param struct amdgpu_atpx_functions \*f:
        supported functions struct

    :param u32 mask:
        supported functions mask from ATPX

.. _`amdgpu_atpx_parse_functions.description`:

Description
-----------

Use the supported functions mask from ATPX function
ATPX_FUNCTION_VERIFY_INTERFACE to determine what functions
are supported (all asics).

.. _`amdgpu_atpx_validate`:

amdgpu_atpx_validate
====================

.. c:function:: int amdgpu_atpx_validate(struct amdgpu_atpx *atpx)

    validate ATPX functions

    :param struct amdgpu_atpx \*atpx:
        amdgpu atpx struct

.. _`amdgpu_atpx_validate.description`:

Description
-----------

Validate that required functions are enabled (all asics).
returns 0 on success, error on failure.

.. _`amdgpu_atpx_verify_interface`:

amdgpu_atpx_verify_interface
============================

.. c:function:: int amdgpu_atpx_verify_interface(struct amdgpu_atpx *atpx)

    verify ATPX

    :param struct amdgpu_atpx \*atpx:
        amdgpu atpx struct

.. _`amdgpu_atpx_verify_interface.description`:

Description
-----------

Execute the ATPX_FUNCTION_VERIFY_INTERFACE ATPX function
to initialize ATPX and determine what features are supported
(all asics).
returns 0 on success, error on failure.

.. _`amdgpu_atpx_set_discrete_state`:

amdgpu_atpx_set_discrete_state
==============================

.. c:function:: int amdgpu_atpx_set_discrete_state(struct amdgpu_atpx *atpx, u8 state)

    power up/down discrete GPU

    :param struct amdgpu_atpx \*atpx:
        atpx info struct

    :param u8 state:
        discrete GPU state (0 = power down, 1 = power up)

.. _`amdgpu_atpx_set_discrete_state.description`:

Description
-----------

Execute the ATPX_FUNCTION_POWER_CONTROL ATPX function to
power down/up the discrete GPU (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_switch_disp_mux`:

amdgpu_atpx_switch_disp_mux
===========================

.. c:function:: int amdgpu_atpx_switch_disp_mux(struct amdgpu_atpx *atpx, u16 mux_id)

    switch display mux

    :param struct amdgpu_atpx \*atpx:
        atpx info struct

    :param u16 mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)

.. _`amdgpu_atpx_switch_disp_mux.description`:

Description
-----------

Execute the ATPX_FUNCTION_DISPLAY_MUX_CONTROL ATPX function to
switch the display mux between the discrete GPU and integrated GPU
(all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_switch_i2c_mux`:

amdgpu_atpx_switch_i2c_mux
==========================

.. c:function:: int amdgpu_atpx_switch_i2c_mux(struct amdgpu_atpx *atpx, u16 mux_id)

    switch i2c/hpd mux

    :param struct amdgpu_atpx \*atpx:
        atpx info struct

    :param u16 mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)

.. _`amdgpu_atpx_switch_i2c_mux.description`:

Description
-----------

Execute the ATPX_FUNCTION_I2C_MUX_CONTROL ATPX function to
switch the i2c/hpd mux between the discrete GPU and integrated GPU
(all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_switch_start`:

amdgpu_atpx_switch_start
========================

.. c:function:: int amdgpu_atpx_switch_start(struct amdgpu_atpx *atpx, u16 mux_id)

    notify the sbios of a GPU switch

    :param struct amdgpu_atpx \*atpx:
        atpx info struct

    :param u16 mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)

.. _`amdgpu_atpx_switch_start.description`:

Description
-----------

Execute the ATPX_FUNCTION_GRAPHICS_DEVICE_SWITCH_START_NOTIFICATION ATPX
function to notify the sbios that a switch between the discrete GPU and
integrated GPU has begun (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_switch_end`:

amdgpu_atpx_switch_end
======================

.. c:function:: int amdgpu_atpx_switch_end(struct amdgpu_atpx *atpx, u16 mux_id)

    notify the sbios of a GPU switch

    :param struct amdgpu_atpx \*atpx:
        atpx info struct

    :param u16 mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)

.. _`amdgpu_atpx_switch_end.description`:

Description
-----------

Execute the ATPX_FUNCTION_GRAPHICS_DEVICE_SWITCH_END_NOTIFICATION ATPX
function to notify the sbios that a switch between the discrete GPU and
integrated GPU has ended (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_switchto`:

amdgpu_atpx_switchto
====================

.. c:function:: int amdgpu_atpx_switchto(enum vga_switcheroo_client_id id)

    switch to the requested GPU

    :param enum vga_switcheroo_client_id id:
        GPU to switch to

.. _`amdgpu_atpx_switchto.description`:

Description
-----------

Execute the necessary ATPX functions to switch between the discrete GPU and
integrated GPU (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_power_state`:

amdgpu_atpx_power_state
=======================

.. c:function:: int amdgpu_atpx_power_state(enum vga_switcheroo_client_id id, enum vga_switcheroo_state state)

    power down/up the requested GPU

    :param enum vga_switcheroo_client_id id:
        GPU to power down/up

    :param enum vga_switcheroo_state state:
        requested power state (0 = off, 1 = on)

.. _`amdgpu_atpx_power_state.description`:

Description
-----------

Execute the necessary ATPX function to power down/up the discrete GPU
(all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_pci_probe_handle`:

amdgpu_atpx_pci_probe_handle
============================

.. c:function:: bool amdgpu_atpx_pci_probe_handle(struct pci_dev *pdev)

    look up the ATPX handle

    :param struct pci_dev \*pdev:
        pci device

.. _`amdgpu_atpx_pci_probe_handle.description`:

Description
-----------

Look up the ATPX handles (all asics).
Returns true if the handles are found, false if not.

.. _`amdgpu_atpx_init`:

amdgpu_atpx_init
================

.. c:function:: int amdgpu_atpx_init( void)

    verify the ATPX interface

    :param  void:
        no arguments

.. _`amdgpu_atpx_init.description`:

Description
-----------

Verify the ATPX interface (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_atpx_get_client_id`:

amdgpu_atpx_get_client_id
=========================

.. c:function:: int amdgpu_atpx_get_client_id(struct pci_dev *pdev)

    get the client id

    :param struct pci_dev \*pdev:
        pci device

.. _`amdgpu_atpx_get_client_id.description`:

Description
-----------

look up whether we are the integrated or discrete GPU (all asics).
Returns the client id.

.. _`amdgpu_atpx_detect`:

amdgpu_atpx_detect
==================

.. c:function:: bool amdgpu_atpx_detect( void)

    detect whether we have PX

    :param  void:
        no arguments

.. _`amdgpu_atpx_detect.description`:

Description
-----------

Check if we have a PX system (all asics).
Returns true if we have a PX system, false if not.

.. _`amdgpu_register_atpx_handler`:

amdgpu_register_atpx_handler
============================

.. c:function:: void amdgpu_register_atpx_handler( void)

    register with vga_switcheroo

    :param  void:
        no arguments

.. _`amdgpu_register_atpx_handler.description`:

Description
-----------

Register the PX callbacks with vga_switcheroo (all asics).

.. _`amdgpu_unregister_atpx_handler`:

amdgpu_unregister_atpx_handler
==============================

.. c:function:: void amdgpu_unregister_atpx_handler( void)

    unregister with vga_switcheroo

    :param  void:
        no arguments

.. _`amdgpu_unregister_atpx_handler.description`:

Description
-----------

Unregister the PX callbacks with vga_switcheroo (all asics).

.. This file was automatic generated / don't edit.

