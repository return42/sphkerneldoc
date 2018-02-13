.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_device.c

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

.. c:function:: void amdgpu_device_vram_location(struct amdgpu_device *adev, struct amdgpu_mc *mc, u64 base)

    try to find VRAM location

    :param struct amdgpu_device \*adev:
        amdgpu device structure holding all necessary informations

    :param struct amdgpu_mc \*mc:
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

.. c:function:: void amdgpu_device_gart_location(struct amdgpu_device *adev, struct amdgpu_mc *mc)

    try to find GTT location

    :param struct amdgpu_device \*adev:
        amdgpu device structure holding all necessary informations

    :param struct amdgpu_mc \*mc:
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

.. This file was automatic generated / don't edit.

