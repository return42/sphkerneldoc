.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_device.c

.. _`amdgpu_device_is_px`:

amdgpu_device_is_px
===================

.. c:function:: bool amdgpu_device_is_px(struct drm_device *dev)

    Is the device is a dGPU with HG/PX power control

    :param struct drm_device \*dev:
        drm_device pointer

.. _`amdgpu_device_is_px.description`:

Description
-----------

Returns true if the device is a dGPU with HG/PX power control,
otherwise return false.

.. _`amdgpu_mm_rreg`:

amdgpu_mm_rreg
==============

.. c:function:: uint32_t amdgpu_mm_rreg(struct amdgpu_device *adev, uint32_t reg, uint32_t acc_flags)

    read a memory mapped IO register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t reg:
        dword aligned register offset

    :param uint32_t acc_flags:
        access flags which require special behavior

.. _`amdgpu_mm_rreg.description`:

Description
-----------

Returns the 32 bit value from the offset specified.

.. _`amdgpu_mm_rreg8`:

amdgpu_mm_rreg8
===============

.. c:function:: uint8_t amdgpu_mm_rreg8(struct amdgpu_device *adev, uint32_t offset)

    read a memory mapped IO register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t offset:
        byte aligned register offset

.. _`amdgpu_mm_rreg8.description`:

Description
-----------

Returns the 8 bit value from the offset specified.

.. _`amdgpu_mm_wreg8`:

amdgpu_mm_wreg8
===============

.. c:function:: void amdgpu_mm_wreg8(struct amdgpu_device *adev, uint32_t offset, uint8_t value)

    read a memory mapped IO register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t offset:
        byte aligned register offset

    :param uint8_t value:
        8 bit value to write

.. _`amdgpu_mm_wreg8.description`:

Description
-----------

Writes the value specified to the offset specified.

.. _`amdgpu_mm_wreg`:

amdgpu_mm_wreg
==============

.. c:function:: void amdgpu_mm_wreg(struct amdgpu_device *adev, uint32_t reg, uint32_t v, uint32_t acc_flags)

    write to a memory mapped IO register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t reg:
        dword aligned register offset

    :param uint32_t v:
        32 bit value to write to the register

    :param uint32_t acc_flags:
        access flags which require special behavior

.. _`amdgpu_mm_wreg.description`:

Description
-----------

Writes the value specified to the offset specified.

.. _`amdgpu_io_rreg`:

amdgpu_io_rreg
==============

.. c:function:: u32 amdgpu_io_rreg(struct amdgpu_device *adev, u32 reg)

    read an IO register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 reg:
        dword aligned register offset

.. _`amdgpu_io_rreg.description`:

Description
-----------

Returns the 32 bit value from the offset specified.

.. _`amdgpu_io_wreg`:

amdgpu_io_wreg
==============

.. c:function:: void amdgpu_io_wreg(struct amdgpu_device *adev, u32 reg, u32 v)

    write to an IO register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 reg:
        dword aligned register offset

    :param u32 v:
        32 bit value to write to the register

.. _`amdgpu_io_wreg.description`:

Description
-----------

Writes the value specified to the offset specified.

.. _`amdgpu_mm_rdoorbell`:

amdgpu_mm_rdoorbell
===================

.. c:function:: u32 amdgpu_mm_rdoorbell(struct amdgpu_device *adev, u32 index)

    read a doorbell dword

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 index:
        doorbell index

.. _`amdgpu_mm_rdoorbell.description`:

Description
-----------

Returns the value in the doorbell aperture at the
requested doorbell index (CIK).

.. _`amdgpu_mm_wdoorbell`:

amdgpu_mm_wdoorbell
===================

.. c:function:: void amdgpu_mm_wdoorbell(struct amdgpu_device *adev, u32 index, u32 v)

    write a doorbell dword

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 index:
        doorbell index

    :param u32 v:
        value to write

.. _`amdgpu_mm_wdoorbell.description`:

Description
-----------

Writes \ ``v``\  to the doorbell aperture at the
requested doorbell index (CIK).

.. _`amdgpu_mm_rdoorbell64`:

amdgpu_mm_rdoorbell64
=====================

.. c:function:: u64 amdgpu_mm_rdoorbell64(struct amdgpu_device *adev, u32 index)

    read a doorbell Qword

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 index:
        doorbell index

.. _`amdgpu_mm_rdoorbell64.description`:

Description
-----------

Returns the value in the doorbell aperture at the
requested doorbell index (VEGA10+).

.. _`amdgpu_mm_wdoorbell64`:

amdgpu_mm_wdoorbell64
=====================

.. c:function:: void amdgpu_mm_wdoorbell64(struct amdgpu_device *adev, u32 index, u64 v)

    write a doorbell Qword

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 index:
        doorbell index

    :param u64 v:
        value to write

.. _`amdgpu_mm_wdoorbell64.description`:

Description
-----------

Writes \ ``v``\  to the doorbell aperture at the
requested doorbell index (VEGA10+).

.. _`amdgpu_invalid_rreg`:

amdgpu_invalid_rreg
===================

.. c:function:: uint32_t amdgpu_invalid_rreg(struct amdgpu_device *adev, uint32_t reg)

    dummy reg read function

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param uint32_t reg:
        offset of register

.. _`amdgpu_invalid_rreg.description`:

Description
-----------

Dummy register read function.  Used for register blocks
that certain asics don't have (all asics).
Returns the value in the register.

.. _`amdgpu_invalid_wreg`:

amdgpu_invalid_wreg
===================

.. c:function:: void amdgpu_invalid_wreg(struct amdgpu_device *adev, uint32_t reg, uint32_t v)

    dummy reg write function

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param uint32_t reg:
        offset of register

    :param uint32_t v:
        value to write to the register

.. _`amdgpu_invalid_wreg.description`:

Description
-----------

Dummy register read function.  Used for register blocks
that certain asics don't have (all asics).

.. _`amdgpu_block_invalid_rreg`:

amdgpu_block_invalid_rreg
=========================

.. c:function:: uint32_t amdgpu_block_invalid_rreg(struct amdgpu_device *adev, uint32_t block, uint32_t reg)

    dummy reg read function

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param uint32_t block:
        offset of instance

    :param uint32_t reg:
        offset of register

.. _`amdgpu_block_invalid_rreg.description`:

Description
-----------

Dummy register read function.  Used for register blocks
that certain asics don't have (all asics).
Returns the value in the register.

.. _`amdgpu_block_invalid_wreg`:

amdgpu_block_invalid_wreg
=========================

.. c:function:: void amdgpu_block_invalid_wreg(struct amdgpu_device *adev, uint32_t block, uint32_t reg, uint32_t v)

    dummy reg write function

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param uint32_t block:
        offset of instance

    :param uint32_t reg:
        offset of register

    :param uint32_t v:
        value to write to the register

.. _`amdgpu_block_invalid_wreg.description`:

Description
-----------

Dummy register read function.  Used for register blocks
that certain asics don't have (all asics).

.. _`amdgpu_device_vram_scratch_init`:

amdgpu_device_vram_scratch_init
===============================

.. c:function:: int amdgpu_device_vram_scratch_init(struct amdgpu_device *adev)

    allocate the VRAM scratch page

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_device_vram_scratch_init.description`:

Description
-----------

Allocates a scratch page of VRAM for use by various things in the
driver.

.. _`amdgpu_device_vram_scratch_fini`:

amdgpu_device_vram_scratch_fini
===============================

.. c:function:: void amdgpu_device_vram_scratch_fini(struct amdgpu_device *adev)

    Free the VRAM scratch page

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_device_vram_scratch_fini.description`:

Description
-----------

Frees the VRAM scratch page.

.. _`amdgpu_device_program_register_sequence`:

amdgpu_device_program_register_sequence
=======================================

.. c:function:: void amdgpu_device_program_register_sequence(struct amdgpu_device *adev, const u32 *registers, const u32 array_size)

    program an array of registers.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param const u32 \*registers:
        pointer to the register array

    :param const u32 array_size:
        size of the register array

.. _`amdgpu_device_program_register_sequence.description`:

Description
-----------

Programs an array or registers with and and or masks.
This is a helper for setting golden registers.

.. _`amdgpu_device_pci_config_reset`:

amdgpu_device_pci_config_reset
==============================

.. c:function:: void amdgpu_device_pci_config_reset(struct amdgpu_device *adev)

    reset the GPU

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_pci_config_reset.description`:

Description
-----------

Resets the GPU using the pci config reset sequence.
Only applicable to asics prior to vega10.

.. _`amdgpu_device_doorbell_init`:

amdgpu_device_doorbell_init
===========================

.. c:function:: int amdgpu_device_doorbell_init(struct amdgpu_device *adev)

    Init doorbell driver information.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_doorbell_init.description`:

Description
-----------

Init doorbell driver information (CIK)
Returns 0 on success, error on failure.

.. _`amdgpu_device_doorbell_fini`:

amdgpu_device_doorbell_fini
===========================

.. c:function:: void amdgpu_device_doorbell_fini(struct amdgpu_device *adev)

    Tear down doorbell driver information.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_doorbell_fini.description`:

Description
-----------

Tear down doorbell driver information (CIK)

.. _`amdgpu_device_wb_fini`:

amdgpu_device_wb_fini
=====================

.. c:function:: void amdgpu_device_wb_fini(struct amdgpu_device *adev)

    Disable Writeback and free memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_wb_fini.description`:

Description
-----------

Disables Writeback and frees the Writeback memory (all asics).
Used at driver shutdown.

.. _`amdgpu_device_wb_init`:

amdgpu_device_wb_init
=====================

.. c:function:: int amdgpu_device_wb_init(struct amdgpu_device *adev)

    Init Writeback driver info and allocate memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_wb_init.description`:

Description
-----------

Initializes writeback and allocates writeback memory (all asics).
Used at driver startup.
Returns 0 on success or an -error on failure.

.. _`amdgpu_device_wb_get`:

amdgpu_device_wb_get
====================

.. c:function:: int amdgpu_device_wb_get(struct amdgpu_device *adev, u32 *wb)

    Allocate a wb entry

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 \*wb:
        wb index

.. _`amdgpu_device_wb_get.description`:

Description
-----------

Allocate a wb slot for use by the driver (all asics).
Returns 0 on success or -EINVAL on failure.

.. _`amdgpu_device_wb_free`:

amdgpu_device_wb_free
=====================

.. c:function:: void amdgpu_device_wb_free(struct amdgpu_device *adev, u32 wb)

    Free a wb entry

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 wb:
        wb index

.. _`amdgpu_device_wb_free.description`:

Description
-----------

Free a wb slot allocated for use by the driver (all asics)

.. _`amdgpu_device_vram_location`:

amdgpu_device_vram_location
===========================

.. c:function:: void amdgpu_device_vram_location(struct amdgpu_device *adev, struct amdgpu_gmc *mc, u64 base)

    try to find VRAM location

    :param struct amdgpu_device \*adev:
        amdgpu device structure holding all necessary informations

    :param struct amdgpu_gmc \*mc:
        memory controller structure holding memory informations

    :param u64 base:
        base address at which to put VRAM

.. _`amdgpu_device_vram_location.description`:

Description
-----------

Function will try to place VRAM at base address provided
as parameter.

.. _`amdgpu_device_gart_location`:

amdgpu_device_gart_location
===========================

.. c:function:: void amdgpu_device_gart_location(struct amdgpu_device *adev, struct amdgpu_gmc *mc)

    try to find GTT location

    :param struct amdgpu_device \*adev:
        amdgpu device structure holding all necessary informations

    :param struct amdgpu_gmc \*mc:
        memory controller structure holding memory informations

.. _`amdgpu_device_gart_location.description`:

Description
-----------

Function will place try to place GTT before or after VRAM.

If GTT size is bigger than space left then we ajust GTT size.
Thus function will never fails.

.. _`amdgpu_device_gart_location.fixme`:

FIXME
-----

when reducing GTT size align new size on power of 2.

.. _`amdgpu_device_resize_fb_bar`:

amdgpu_device_resize_fb_bar
===========================

.. c:function:: int amdgpu_device_resize_fb_bar(struct amdgpu_device *adev)

    try to resize FB BAR

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_resize_fb_bar.description`:

Description
-----------

Try to resize FB BAR to make all VRAM CPU accessible. We try very hard not
to fail, but if any of the BARs is not accessible after the size we abort
driver loading by returning -ENODEV.

.. _`amdgpu_device_need_post`:

amdgpu_device_need_post
=======================

.. c:function:: bool amdgpu_device_need_post(struct amdgpu_device *adev)

    check if the hw need post or not

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_need_post.description`:

Description
-----------

Check if the asic has been initialized (all asics) at driver startup
or post is needed if  hw reset is performed.
Returns true if need or false if not.

.. _`amdgpu_device_vga_set_decode`:

amdgpu_device_vga_set_decode
============================

.. c:function:: unsigned int amdgpu_device_vga_set_decode(void *cookie, bool state)

    enable/disable vga decode

    :param void \*cookie:
        amdgpu_device pointer

    :param bool state:
        enable/disable vga decode

.. _`amdgpu_device_vga_set_decode.description`:

Description
-----------

Enable/disable vga decode (all asics).
Returns VGA resource flags.

.. _`amdgpu_device_check_block_size`:

amdgpu_device_check_block_size
==============================

.. c:function:: void amdgpu_device_check_block_size(struct amdgpu_device *adev)

    validate the vm block size

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_check_block_size.description`:

Description
-----------

Validates the vm block size specified via module parameter.
The vm block size defines number of bits in page table versus page directory,
a page is 4KB so we have 12 bits offset, minimum 9 bits in the
page table and the remaining bits are in the page directory.

.. _`amdgpu_device_check_vm_size`:

amdgpu_device_check_vm_size
===========================

.. c:function:: void amdgpu_device_check_vm_size(struct amdgpu_device *adev)

    validate the vm size

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_check_vm_size.description`:

Description
-----------

Validates the vm size in GB specified via module parameter.
The VM size is the size of the GPU virtual memory space in GB.

.. _`amdgpu_device_check_arguments`:

amdgpu_device_check_arguments
=============================

.. c:function:: void amdgpu_device_check_arguments(struct amdgpu_device *adev)

    validate module params

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_check_arguments.description`:

Description
-----------

Validates certain module parameters and updates
the associated values used by the driver (all asics).

.. _`amdgpu_switcheroo_set_state`:

amdgpu_switcheroo_set_state
===========================

.. c:function:: void amdgpu_switcheroo_set_state(struct pci_dev *pdev, enum vga_switcheroo_state state)

    set switcheroo state

    :param struct pci_dev \*pdev:
        pci dev pointer

    :param enum vga_switcheroo_state state:
        vga_switcheroo state

.. _`amdgpu_switcheroo_set_state.description`:

Description
-----------

Callback for the switcheroo driver.  Suspends or resumes the
the asics before or after it is powered up using ACPI methods.

.. _`amdgpu_switcheroo_can_switch`:

amdgpu_switcheroo_can_switch
============================

.. c:function:: bool amdgpu_switcheroo_can_switch(struct pci_dev *pdev)

    see if switcheroo state can change

    :param struct pci_dev \*pdev:
        pci dev pointer

.. _`amdgpu_switcheroo_can_switch.description`:

Description
-----------

Callback for the switcheroo driver.  Check of the switcheroo
state can be changed.
Returns true if the state can be changed, false if not.

.. _`amdgpu_device_ip_set_clockgating_state`:

amdgpu_device_ip_set_clockgating_state
======================================

.. c:function:: int amdgpu_device_ip_set_clockgating_state(void *dev, enum amd_ip_block_type block_type, enum amd_clockgating_state state)

    set the CG state

    :param void \*dev:
        *undescribed*

    :param enum amd_ip_block_type block_type:
        Type of hardware IP (SMU, GFX, UVD, etc.)

    :param enum amd_clockgating_state state:
        clockgating state (gate or ungate)

.. _`amdgpu_device_ip_set_clockgating_state.description`:

Description
-----------

Sets the requested clockgating state for all instances of
the hardware IP specified.
Returns the error code from the last instance.

.. _`amdgpu_device_ip_set_powergating_state`:

amdgpu_device_ip_set_powergating_state
======================================

.. c:function:: int amdgpu_device_ip_set_powergating_state(void *dev, enum amd_ip_block_type block_type, enum amd_powergating_state state)

    set the PG state

    :param void \*dev:
        *undescribed*

    :param enum amd_ip_block_type block_type:
        Type of hardware IP (SMU, GFX, UVD, etc.)

    :param enum amd_powergating_state state:
        powergating state (gate or ungate)

.. _`amdgpu_device_ip_set_powergating_state.description`:

Description
-----------

Sets the requested powergating state for all instances of
the hardware IP specified.
Returns the error code from the last instance.

.. _`amdgpu_device_ip_get_clockgating_state`:

amdgpu_device_ip_get_clockgating_state
======================================

.. c:function:: void amdgpu_device_ip_get_clockgating_state(struct amdgpu_device *adev, u32 *flags)

    get the CG state

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 \*flags:
        clockgating feature flags

.. _`amdgpu_device_ip_get_clockgating_state.description`:

Description
-----------

Walks the list of IPs on the device and updates the clockgating
flags for each IP.
Updates \ ``flags``\  with the feature flags for each hardware IP where
clockgating is enabled.

.. _`amdgpu_device_ip_wait_for_idle`:

amdgpu_device_ip_wait_for_idle
==============================

.. c:function:: int amdgpu_device_ip_wait_for_idle(struct amdgpu_device *adev, enum amd_ip_block_type block_type)

    wait for idle

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amd_ip_block_type block_type:
        Type of hardware IP (SMU, GFX, UVD, etc.)

.. _`amdgpu_device_ip_wait_for_idle.description`:

Description
-----------

Waits for the request hardware IP to be idle.
Returns 0 for success or a negative error code on failure.

.. _`amdgpu_device_ip_is_idle`:

amdgpu_device_ip_is_idle
========================

.. c:function:: bool amdgpu_device_ip_is_idle(struct amdgpu_device *adev, enum amd_ip_block_type block_type)

    is the hardware IP idle

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amd_ip_block_type block_type:
        Type of hardware IP (SMU, GFX, UVD, etc.)

.. _`amdgpu_device_ip_is_idle.description`:

Description
-----------

Check if the hardware IP is idle or not.
Returns true if it the IP is idle, false if not.

.. _`amdgpu_device_ip_get_ip_block`:

amdgpu_device_ip_get_ip_block
=============================

.. c:function:: struct amdgpu_ip_block *amdgpu_device_ip_get_ip_block(struct amdgpu_device *adev, enum amd_ip_block_type type)

    get a hw IP pointer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amd_ip_block_type type:
        *undescribed*

.. _`amdgpu_device_ip_get_ip_block.description`:

Description
-----------

Returns a pointer to the hardware IP block structure
if it exists for the asic, otherwise NULL.

.. _`amdgpu_device_ip_block_version_cmp`:

amdgpu_device_ip_block_version_cmp
==================================

.. c:function:: int amdgpu_device_ip_block_version_cmp(struct amdgpu_device *adev, enum amd_ip_block_type type, u32 major, u32 minor)

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amd_ip_block_type type:
        enum amd_ip_block_type

    :param u32 major:
        major version

    :param u32 minor:
        minor version

.. _`amdgpu_device_ip_block_version_cmp.description`:

Description
-----------

return 0 if equal or greater
return 1 if smaller or the ip_block doesn't exist

.. _`amdgpu_device_ip_block_add`:

amdgpu_device_ip_block_add
==========================

.. c:function:: int amdgpu_device_ip_block_add(struct amdgpu_device *adev, const struct amdgpu_ip_block_version *ip_block_version)

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param const struct amdgpu_ip_block_version \*ip_block_version:
        pointer to the IP to add

.. _`amdgpu_device_ip_block_add.description`:

Description
-----------

Adds the IP block driver information to the collection of IPs
on the asic.

.. _`amdgpu_device_enable_virtual_display`:

amdgpu_device_enable_virtual_display
====================================

.. c:function:: void amdgpu_device_enable_virtual_display(struct amdgpu_device *adev)

    enable virtual display feature

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_enable_virtual_display.description`:

Description
-----------

Enabled the virtual display feature if the user has enabled it via
the module parameter virtual_display.  This feature provides a virtual
display hardware on headless boards or in virtualized environments.
This function parses and validates the configuration string specified by
the user and configues the virtual display configuration (number of
virtual connectors, crtcs, etc.) specified.

.. _`amdgpu_device_parse_gpu_info_fw`:

amdgpu_device_parse_gpu_info_fw
===============================

.. c:function:: int amdgpu_device_parse_gpu_info_fw(struct amdgpu_device *adev)

    parse gpu info firmware

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_parse_gpu_info_fw.description`:

Description
-----------

Parses the asic configuration parameters specified in the gpu info
firmware and makes them availale to the driver for use in configuring
the asic.
Returns 0 on success, -EINVAL on failure.

.. _`amdgpu_device_ip_early_init`:

amdgpu_device_ip_early_init
===========================

.. c:function:: int amdgpu_device_ip_early_init(struct amdgpu_device *adev)

    run early init for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_early_init.description`:

Description
-----------

Early initialization pass for hardware IPs.  The hardware IPs that make
up each asic are discovered each IP's early_init callback is run.  This
is the first stage in initializing the asic.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_init`:

amdgpu_device_ip_init
=====================

.. c:function:: int amdgpu_device_ip_init(struct amdgpu_device *adev)

    run init for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_init.description`:

Description
-----------

Main initialization pass for hardware IPs.  The list of all the hardware
IPs that make up the asic is walked and the sw_init and hw_init callbacks
are run.  sw_init initializes the software state associated with each IP
and hw_init initializes the hardware associated with each IP.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_fill_reset_magic`:

amdgpu_device_fill_reset_magic
==============================

.. c:function:: void amdgpu_device_fill_reset_magic(struct amdgpu_device *adev)

    writes reset magic to gart pointer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_fill_reset_magic.description`:

Description
-----------

Writes a reset magic value to the gart pointer in VRAM.  The driver calls
this function before a GPU reset.  If the value is retained after a
GPU reset, VRAM has not been lost.  Some GPU resets may destry VRAM contents.

.. _`amdgpu_device_check_vram_lost`:

amdgpu_device_check_vram_lost
=============================

.. c:function:: bool amdgpu_device_check_vram_lost(struct amdgpu_device *adev)

    check if vram is valid

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_check_vram_lost.description`:

Description
-----------

Checks the reset magic value written to the gart pointer in VRAM.
The driver calls this after a GPU reset to see if the contents of
VRAM is lost or now.
returns true if vram is lost, false if not.

.. _`amdgpu_device_ip_late_set_cg_state`:

amdgpu_device_ip_late_set_cg_state
==================================

.. c:function:: int amdgpu_device_ip_late_set_cg_state(struct amdgpu_device *adev)

    late init for clockgating

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_late_set_cg_state.description`:

Description
-----------

Late initialization pass enabling clockgating for hardware IPs.
The list of all the hardware IPs that make up the asic is walked and the
set_clockgating_state callbacks are run.  This stage is run late
in the init process.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_late_init`:

amdgpu_device_ip_late_init
==========================

.. c:function:: int amdgpu_device_ip_late_init(struct amdgpu_device *adev)

    run late init for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_late_init.description`:

Description
-----------

Late initialization pass for hardware IPs.  The list of all the hardware
IPs that make up the asic is walked and the late_init callbacks are run.
late_init covers any special initialization that an IP requires
after all of the have been initialized or something that needs to happen
late in the init process.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_fini`:

amdgpu_device_ip_fini
=====================

.. c:function:: int amdgpu_device_ip_fini(struct amdgpu_device *adev)

    run fini for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_fini.description`:

Description
-----------

Main teardown pass for hardware IPs.  The list of all the hardware
IPs that make up the asic is walked and the hw_fini and sw_fini callbacks
are run.  hw_fini tears down the hardware associated with each IP
and sw_fini tears down any software state associated with each IP.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_late_init_func_handler`:

amdgpu_device_ip_late_init_func_handler
=======================================

.. c:function:: void amdgpu_device_ip_late_init_func_handler(struct work_struct *work)

    work handler for clockgating

    :param struct work_struct \*work:
        work_struct

.. _`amdgpu_device_ip_late_init_func_handler.description`:

Description
-----------

Work handler for amdgpu_device_ip_late_set_cg_state.  We put the
clockgating setup into a worker thread to speed up driver init and
resume from suspend.

.. _`amdgpu_device_ip_suspend`:

amdgpu_device_ip_suspend
========================

.. c:function:: int amdgpu_device_ip_suspend(struct amdgpu_device *adev)

    run suspend for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_suspend.description`:

Description
-----------

Main suspend function for hardware IPs.  The list of all the hardware
IPs that make up the asic is walked, clockgating is disabled and the
suspend callbacks are run.  suspend puts the hardware and software state
in each IP into a state suitable for suspend.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_resume_phase1`:

amdgpu_device_ip_resume_phase1
==============================

.. c:function:: int amdgpu_device_ip_resume_phase1(struct amdgpu_device *adev)

    run resume for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_resume_phase1.description`:

Description
-----------

First resume function for hardware IPs.  The list of all the hardware
IPs that make up the asic is walked and the resume callbacks are run for
COMMON, GMC, and IH.  resume puts the hardware into a functional state
after a suspend and updates the software state as necessary.  This
function is also used for restoring the GPU after a GPU reset.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_resume_phase2`:

amdgpu_device_ip_resume_phase2
==============================

.. c:function:: int amdgpu_device_ip_resume_phase2(struct amdgpu_device *adev)

    run resume for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_resume_phase2.description`:

Description
-----------

First resume function for hardware IPs.  The list of all the hardware
IPs that make up the asic is walked and the resume callbacks are run for
all blocks except COMMON, GMC, and IH.  resume puts the hardware into a
functional state after a suspend and updates the software state as
necessary.  This function is also used for restoring the GPU after a GPU
reset.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_resume`:

amdgpu_device_ip_resume
=======================

.. c:function:: int amdgpu_device_ip_resume(struct amdgpu_device *adev)

    run resume for hardware IPs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_resume.description`:

Description
-----------

Main resume function for hardware IPs.  The hardware IPs
are split into two resume functions because they are
are also used in in recovering from a GPU reset and some additional
steps need to be take between them.  In this case (S3/S4) they are
run sequentially.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_detect_sriov_bios`:

amdgpu_device_detect_sriov_bios
===============================

.. c:function:: void amdgpu_device_detect_sriov_bios(struct amdgpu_device *adev)

    determine if the board supports SR-IOV

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_detect_sriov_bios.description`:

Description
-----------

Query the VBIOS data tables to determine if the board supports SR-IOV.

.. _`amdgpu_device_asic_has_dc_support`:

amdgpu_device_asic_has_dc_support
=================================

.. c:function:: bool amdgpu_device_asic_has_dc_support(enum amd_asic_type asic_type)

    determine if DC supports the asic

    :param enum amd_asic_type asic_type:
        AMD asic type

.. _`amdgpu_device_asic_has_dc_support.description`:

Description
-----------

Check if there is DC (new modesetting infrastructre) support for an asic.
returns true if DC has support, false if not.

.. _`amdgpu_device_has_dc_support`:

amdgpu_device_has_dc_support
============================

.. c:function:: bool amdgpu_device_has_dc_support(struct amdgpu_device *adev)

    check if dc is supported

    :param struct amdgpu_device \*adev:
        amdgpu_device_pointer

.. _`amdgpu_device_has_dc_support.description`:

Description
-----------

Returns true for supported, false for not supported

.. _`amdgpu_device_init`:

amdgpu_device_init
==================

.. c:function:: int amdgpu_device_init(struct amdgpu_device *adev, struct drm_device *ddev, struct pci_dev *pdev, uint32_t flags)

    initialize the driver

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct drm_device \*ddev:
        *undescribed*

    :param struct pci_dev \*pdev:
        pci dev pointer

    :param uint32_t flags:
        driver flags

.. _`amdgpu_device_init.description`:

Description
-----------

Initializes the driver info and hw (all asics).
Returns 0 for success or an error on failure.
Called at driver startup.

.. _`amdgpu_device_fini`:

amdgpu_device_fini
==================

.. c:function:: void amdgpu_device_fini(struct amdgpu_device *adev)

    tear down the driver

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_fini.description`:

Description
-----------

Tear down the driver info (all asics).
Called at driver shutdown.

.. _`amdgpu_device_suspend`:

amdgpu_device_suspend
=====================

.. c:function:: int amdgpu_device_suspend(struct drm_device *dev, bool suspend, bool fbcon)

    initiate device suspend

    :param struct drm_device \*dev:
        *undescribed*

    :param bool suspend:
        *undescribed*

    :param bool fbcon:
        *undescribed*

.. _`amdgpu_device_suspend.description`:

Description
-----------

Puts the hw in the suspend state (all asics).
Returns 0 for success or an error on failure.
Called at driver suspend.

.. _`amdgpu_device_resume`:

amdgpu_device_resume
====================

.. c:function:: int amdgpu_device_resume(struct drm_device *dev, bool resume, bool fbcon)

    initiate device resume

    :param struct drm_device \*dev:
        *undescribed*

    :param bool resume:
        *undescribed*

    :param bool fbcon:
        *undescribed*

.. _`amdgpu_device_resume.description`:

Description
-----------

Bring the hw back to operating state (all asics).
Returns 0 for success or an error on failure.
Called at driver resume.

.. _`amdgpu_device_ip_check_soft_reset`:

amdgpu_device_ip_check_soft_reset
=================================

.. c:function:: bool amdgpu_device_ip_check_soft_reset(struct amdgpu_device *adev)

    did soft reset succeed

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_check_soft_reset.description`:

Description
-----------

The list of all the hardware IPs that make up the asic is walked and
the check_soft_reset callbacks are run.  check_soft_reset determines
if the asic is still hung or not.
Returns true if any of the IPs are still in a hung state, false if not.

.. _`amdgpu_device_ip_pre_soft_reset`:

amdgpu_device_ip_pre_soft_reset
===============================

.. c:function:: int amdgpu_device_ip_pre_soft_reset(struct amdgpu_device *adev)

    prepare for soft reset

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_pre_soft_reset.description`:

Description
-----------

The list of all the hardware IPs that make up the asic is walked and the
pre_soft_reset callbacks are run if the block is hung.  pre_soft_reset
handles any IP specific hardware or software state changes that are
necessary for a soft reset to succeed.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_need_full_reset`:

amdgpu_device_ip_need_full_reset
================================

.. c:function:: bool amdgpu_device_ip_need_full_reset(struct amdgpu_device *adev)

    check if a full asic reset is needed

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_need_full_reset.description`:

Description
-----------

Some hardware IPs cannot be soft reset.  If they are hung, a full gpu
reset is necessary to recover.
Returns true if a full asic reset is required, false if not.

.. _`amdgpu_device_ip_soft_reset`:

amdgpu_device_ip_soft_reset
===========================

.. c:function:: int amdgpu_device_ip_soft_reset(struct amdgpu_device *adev)

    do a soft reset

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_soft_reset.description`:

Description
-----------

The list of all the hardware IPs that make up the asic is walked and the
soft_reset callbacks are run if the block is hung.  soft_reset handles any
IP specific hardware or software state changes that are necessary to soft
reset the IP.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_ip_post_soft_reset`:

amdgpu_device_ip_post_soft_reset
================================

.. c:function:: int amdgpu_device_ip_post_soft_reset(struct amdgpu_device *adev)

    clean up from soft reset

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_ip_post_soft_reset.description`:

Description
-----------

The list of all the hardware IPs that make up the asic is walked and the
post_soft_reset callbacks are run if the asic was hung.  post_soft_reset
handles any IP specific hardware or software state changes that are
necessary after the IP has been soft reset.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_recover_vram_from_shadow`:

amdgpu_device_recover_vram_from_shadow
======================================

.. c:function:: int amdgpu_device_recover_vram_from_shadow(struct amdgpu_device *adev, struct amdgpu_ring *ring, struct amdgpu_bo *bo, struct dma_fence **fence)

    restore shadowed VRAM buffers

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring for the engine handling the buffer operations

    :param struct amdgpu_bo \*bo:
        amdgpu_bo buffer whose shadow is being restored

    :param struct dma_fence \*\*fence:
        dma_fence associated with the operation

.. _`amdgpu_device_recover_vram_from_shadow.description`:

Description
-----------

Restores the VRAM buffer contents from the shadow in GTT.  Used to
restore things like GPUVM page tables after a GPU reset where
the contents of VRAM might be lost.
Returns 0 on success, negative error code on failure.

.. _`amdgpu_device_handle_vram_lost`:

amdgpu_device_handle_vram_lost
==============================

.. c:function:: int amdgpu_device_handle_vram_lost(struct amdgpu_device *adev)

    Handle the loss of VRAM contents

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_handle_vram_lost.description`:

Description
-----------

Restores the contents of VRAM buffers from the shadows in GTT.  Used to
restore things like GPUVM page tables after a GPU reset where
the contents of VRAM might be lost.
Returns 0 on success, 1 on failure.

.. _`amdgpu_device_reset`:

amdgpu_device_reset
===================

.. c:function:: int amdgpu_device_reset(struct amdgpu_device *adev)

    reset ASIC/GPU for bare-metal or passthrough

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_device_reset.description`:

Description
-----------

attempt to do soft-reset or full-reset and reinitialize Asic
return 0 means successed otherwise failed

.. _`amdgpu_device_reset_sriov`:

amdgpu_device_reset_sriov
=========================

.. c:function:: int amdgpu_device_reset_sriov(struct amdgpu_device *adev, bool from_hypervisor)

    reset ASIC for SR-IOV vf

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param bool from_hypervisor:
        *undescribed*

.. _`amdgpu_device_reset_sriov.description`:

Description
-----------

do VF FLR and reinitialize Asic
return 0 means successed otherwise failed

.. _`amdgpu_device_gpu_recover`:

amdgpu_device_gpu_recover
=========================

.. c:function:: int amdgpu_device_gpu_recover(struct amdgpu_device *adev, struct amdgpu_job *job, bool force)

    reset the asic and recover scheduler

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_job \*job:
        which job trigger hang
        \ ``force``\  forces reset regardless of amdgpu_gpu_recovery

    :param bool force:
        *undescribed*

.. _`amdgpu_device_gpu_recover.description`:

Description
-----------

Attempt to reset the GPU if it has hung (all asics).
Returns 0 for success or an error on failure.

.. _`amdgpu_device_get_pcie_info`:

amdgpu_device_get_pcie_info
===========================

.. c:function:: void amdgpu_device_get_pcie_info(struct amdgpu_device *adev)

    fence pcie info about the PCIE slot

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_device_get_pcie_info.description`:

Description
-----------

Fetchs and stores in the driver the PCIE capabilities (gen speed
and lanes) of the slot the device is in. Handles APUs and
virtualized environments where PCIE config space may not be available.

.. This file was automatic generated / don't edit.

