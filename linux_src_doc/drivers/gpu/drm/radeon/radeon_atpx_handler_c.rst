.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_atpx_handler.c

.. _`radeon_atpx_call`:

radeon_atpx_call
================

.. c:function:: union acpi_object *radeon_atpx_call(acpi_handle handle, int function, struct acpi_buffer *params)

    call an ATPX method

    :param handle:
        acpi handle
    :type handle: acpi_handle

    :param function:
        the ATPX function to execute
    :type function: int

    :param params:
        ATPX function params
    :type params: struct acpi_buffer \*

.. _`radeon_atpx_call.description`:

Description
-----------

Executes the requested ATPX function (all asics).
Returns a pointer to the acpi output buffer.

.. _`radeon_atpx_parse_functions`:

radeon_atpx_parse_functions
===========================

.. c:function:: void radeon_atpx_parse_functions(struct radeon_atpx_functions *f, u32 mask)

    parse supported functions

    :param f:
        supported functions struct
    :type f: struct radeon_atpx_functions \*

    :param mask:
        supported functions mask from ATPX
    :type mask: u32

.. _`radeon_atpx_parse_functions.description`:

Description
-----------

Use the supported functions mask from ATPX function
ATPX_FUNCTION_VERIFY_INTERFACE to determine what functions
are supported (all asics).

.. _`radeon_atpx_validate`:

radeon_atpx_validate
====================

.. c:function:: int radeon_atpx_validate(struct radeon_atpx *atpx)

    validate ATPX functions

    :param atpx:
        radeon atpx struct
    :type atpx: struct radeon_atpx \*

.. _`radeon_atpx_validate.description`:

Description
-----------

Validate that required functions are enabled (all asics).
returns 0 on success, error on failure.

.. _`radeon_atpx_verify_interface`:

radeon_atpx_verify_interface
============================

.. c:function:: int radeon_atpx_verify_interface(struct radeon_atpx *atpx)

    verify ATPX

    :param atpx:
        radeon atpx struct
    :type atpx: struct radeon_atpx \*

.. _`radeon_atpx_verify_interface.description`:

Description
-----------

Execute the ATPX_FUNCTION_VERIFY_INTERFACE ATPX function
to initialize ATPX and determine what features are supported
(all asics).
returns 0 on success, error on failure.

.. _`radeon_atpx_set_discrete_state`:

radeon_atpx_set_discrete_state
==============================

.. c:function:: int radeon_atpx_set_discrete_state(struct radeon_atpx *atpx, u8 state)

    power up/down discrete GPU

    :param atpx:
        atpx info struct
    :type atpx: struct radeon_atpx \*

    :param state:
        discrete GPU state (0 = power down, 1 = power up)
    :type state: u8

.. _`radeon_atpx_set_discrete_state.description`:

Description
-----------

Execute the ATPX_FUNCTION_POWER_CONTROL ATPX function to
power down/up the discrete GPU (all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_switch_disp_mux`:

radeon_atpx_switch_disp_mux
===========================

.. c:function:: int radeon_atpx_switch_disp_mux(struct radeon_atpx *atpx, u16 mux_id)

    switch display mux

    :param atpx:
        atpx info struct
    :type atpx: struct radeon_atpx \*

    :param mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)
    :type mux_id: u16

.. _`radeon_atpx_switch_disp_mux.description`:

Description
-----------

Execute the ATPX_FUNCTION_DISPLAY_MUX_CONTROL ATPX function to
switch the display mux between the discrete GPU and integrated GPU
(all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_switch_i2c_mux`:

radeon_atpx_switch_i2c_mux
==========================

.. c:function:: int radeon_atpx_switch_i2c_mux(struct radeon_atpx *atpx, u16 mux_id)

    switch i2c/hpd mux

    :param atpx:
        atpx info struct
    :type atpx: struct radeon_atpx \*

    :param mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)
    :type mux_id: u16

.. _`radeon_atpx_switch_i2c_mux.description`:

Description
-----------

Execute the ATPX_FUNCTION_I2C_MUX_CONTROL ATPX function to
switch the i2c/hpd mux between the discrete GPU and integrated GPU
(all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_switch_start`:

radeon_atpx_switch_start
========================

.. c:function:: int radeon_atpx_switch_start(struct radeon_atpx *atpx, u16 mux_id)

    notify the sbios of a GPU switch

    :param atpx:
        atpx info struct
    :type atpx: struct radeon_atpx \*

    :param mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)
    :type mux_id: u16

.. _`radeon_atpx_switch_start.description`:

Description
-----------

Execute the ATPX_FUNCTION_GRAPHICS_DEVICE_SWITCH_START_NOTIFICATION ATPX
function to notify the sbios that a switch between the discrete GPU and
integrated GPU has begun (all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_switch_end`:

radeon_atpx_switch_end
======================

.. c:function:: int radeon_atpx_switch_end(struct radeon_atpx *atpx, u16 mux_id)

    notify the sbios of a GPU switch

    :param atpx:
        atpx info struct
    :type atpx: struct radeon_atpx \*

    :param mux_id:
        mux state (0 = integrated GPU, 1 = discrete GPU)
    :type mux_id: u16

.. _`radeon_atpx_switch_end.description`:

Description
-----------

Execute the ATPX_FUNCTION_GRAPHICS_DEVICE_SWITCH_END_NOTIFICATION ATPX
function to notify the sbios that a switch between the discrete GPU and
integrated GPU has ended (all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_switchto`:

radeon_atpx_switchto
====================

.. c:function:: int radeon_atpx_switchto(enum vga_switcheroo_client_id id)

    switch to the requested GPU

    :param id:
        GPU to switch to
    :type id: enum vga_switcheroo_client_id

.. _`radeon_atpx_switchto.description`:

Description
-----------

Execute the necessary ATPX functions to switch between the discrete GPU and
integrated GPU (all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_power_state`:

radeon_atpx_power_state
=======================

.. c:function:: int radeon_atpx_power_state(enum vga_switcheroo_client_id id, enum vga_switcheroo_state state)

    power down/up the requested GPU

    :param id:
        GPU to power down/up
    :type id: enum vga_switcheroo_client_id

    :param state:
        requested power state (0 = off, 1 = on)
    :type state: enum vga_switcheroo_state

.. _`radeon_atpx_power_state.description`:

Description
-----------

Execute the necessary ATPX function to power down/up the discrete GPU
(all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_pci_probe_handle`:

radeon_atpx_pci_probe_handle
============================

.. c:function:: bool radeon_atpx_pci_probe_handle(struct pci_dev *pdev)

    look up the ATPX handle

    :param pdev:
        pci device
    :type pdev: struct pci_dev \*

.. _`radeon_atpx_pci_probe_handle.description`:

Description
-----------

Look up the ATPX handles (all asics).
Returns true if the handles are found, false if not.

.. _`radeon_atpx_init`:

radeon_atpx_init
================

.. c:function:: int radeon_atpx_init( void)

    verify the ATPX interface

    :param void:
        no arguments
    :type void: 

.. _`radeon_atpx_init.description`:

Description
-----------

Verify the ATPX interface (all asics).
Returns 0 on success, error on failure.

.. _`radeon_atpx_get_client_id`:

radeon_atpx_get_client_id
=========================

.. c:function:: enum vga_switcheroo_client_id radeon_atpx_get_client_id(struct pci_dev *pdev)

    get the client id

    :param pdev:
        pci device
    :type pdev: struct pci_dev \*

.. _`radeon_atpx_get_client_id.description`:

Description
-----------

look up whether we are the integrated or discrete GPU (all asics).
Returns the client id.

.. _`radeon_atpx_detect`:

radeon_atpx_detect
==================

.. c:function:: bool radeon_atpx_detect( void)

    detect whether we have PX

    :param void:
        no arguments
    :type void: 

.. _`radeon_atpx_detect.description`:

Description
-----------

Check if we have a PX system (all asics).
Returns true if we have a PX system, false if not.

.. _`radeon_register_atpx_handler`:

radeon_register_atpx_handler
============================

.. c:function:: void radeon_register_atpx_handler( void)

    register with vga_switcheroo

    :param void:
        no arguments
    :type void: 

.. _`radeon_register_atpx_handler.description`:

Description
-----------

Register the PX callbacks with vga_switcheroo (all asics).

.. _`radeon_unregister_atpx_handler`:

radeon_unregister_atpx_handler
==============================

.. c:function:: void radeon_unregister_atpx_handler( void)

    unregister with vga_switcheroo

    :param void:
        no arguments
    :type void: 

.. _`radeon_unregister_atpx_handler.description`:

Description
-----------

Unregister the PX callbacks with vga_switcheroo (all asics).

.. This file was automatic generated / don't edit.

