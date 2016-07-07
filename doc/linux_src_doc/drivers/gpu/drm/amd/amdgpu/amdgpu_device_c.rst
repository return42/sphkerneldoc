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

.. _`amdgpu_program_register_sequence`:

amdgpu_program_register_sequence
================================

.. c:function:: void amdgpu_program_register_sequence(struct amdgpu_device *adev, const u32 *registers, const u32 array_size)

    program an array of registers.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param const u32 \*registers:
        pointer to the register array

    :param const u32 array_size:
        size of the register array

.. _`amdgpu_program_register_sequence.description`:

Description
-----------

Programs an array or registers with and and or masks.
This is a helper for setting golden registers.

.. _`amdgpu_doorbell_init`:

amdgpu_doorbell_init
====================

.. c:function:: int amdgpu_doorbell_init(struct amdgpu_device *adev)

    Init doorbell driver information.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_doorbell_init.description`:

Description
-----------

Init doorbell driver information (CIK)
Returns 0 on success, error on failure.

.. _`amdgpu_doorbell_fini`:

amdgpu_doorbell_fini
====================

.. c:function:: void amdgpu_doorbell_fini(struct amdgpu_device *adev)

    Tear down doorbell driver information.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_doorbell_fini.description`:

Description
-----------

Tear down doorbell driver information (CIK)

.. _`amdgpu_doorbell_get_kfd_info`:

amdgpu_doorbell_get_kfd_info
============================

.. c:function:: void amdgpu_doorbell_get_kfd_info(struct amdgpu_device *adev, phys_addr_t *aperture_base, size_t *aperture_size, size_t *start_offset)

    Report doorbell configuration required to setup amdkfd

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param phys_addr_t \*aperture_base:
        output returning doorbell aperture base physical address

    :param size_t \*aperture_size:
        output returning doorbell aperture size in bytes

    :param size_t \*start_offset:
        output returning # of doorbell bytes reserved for amdgpu.

.. _`amdgpu_doorbell_get_kfd_info.description`:

Description
-----------

amdgpu and amdkfd share the doorbell aperture. amdgpu sets it up,
takes doorbells required for its own rings and reports the setup to amdkfd.
amdgpu reserved doorbells are at the start of the doorbell aperture.

.. _`amdgpu_wb_fini`:

amdgpu_wb_fini
==============

.. c:function:: void amdgpu_wb_fini(struct amdgpu_device *adev)

    Disable Writeback and free memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_wb_fini.description`:

Description
-----------

Disables Writeback and frees the Writeback memory (all asics).
Used at driver shutdown.

.. _`amdgpu_wb_init`:

amdgpu_wb_init
==============

.. c:function:: int amdgpu_wb_init(struct amdgpu_device *adev)

    Init Writeback driver info and allocate memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_wb_init.description`:

Description
-----------

Disables Writeback and frees the Writeback memory (all asics).
Used at driver startup.
Returns 0 on success or an -error on failure.

.. _`amdgpu_wb_get`:

amdgpu_wb_get
=============

.. c:function:: int amdgpu_wb_get(struct amdgpu_device *adev, u32 *wb)

    Allocate a wb entry

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 \*wb:
        wb index

.. _`amdgpu_wb_get.description`:

Description
-----------

Allocate a wb slot for use by the driver (all asics).
Returns 0 on success or -EINVAL on failure.

.. _`amdgpu_wb_free`:

amdgpu_wb_free
==============

.. c:function:: void amdgpu_wb_free(struct amdgpu_device *adev, u32 wb)

    Free a wb entry

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 wb:
        wb index

.. _`amdgpu_wb_free.description`:

Description
-----------

Free a wb slot allocated for use by the driver (all asics)

.. _`amdgpu_vram_location`:

amdgpu_vram_location
====================

.. c:function:: void amdgpu_vram_location(struct amdgpu_device *adev, struct amdgpu_mc *mc, u64 base)

    try to find VRAM location

    :param struct amdgpu_device \*adev:
        amdgpu device structure holding all necessary informations

    :param struct amdgpu_mc \*mc:
        memory controller structure holding memory informations

    :param u64 base:
        base address at which to put VRAM

.. _`amdgpu_vram_location.description`:

Description
-----------

Function will place try to place VRAM at base address provided
as parameter (which is so far either PCI aperture address or
for IGP TOM base address).

If there is not enough space to fit the unvisible VRAM in the 32bits
address space then we limit the VRAM size to the aperture.

.. _`amdgpu_vram_location.note`:

Note
----

We don't explicitly enforce VRAM start to be aligned on VRAM size,
this shouldn't be a problem as we are using the PCI aperture as a reference.
Otherwise this would be needed for rv280, all r3xx, and all r4xx, but
not IGP.

we use mc_vram_size as on some board we need to program the mc to
cover the whole aperture even if VRAM size is inferior to aperture size
Novell bug 204882 + along with lots of ubuntu ones

when limiting vram it's safe to overwritte real_vram_size because
we are not in case where real_vram_size is inferior to mc_vram_size (ie
note afected by bogus hw of Novell bug 204882 + along with lots of ubuntu
ones)

IGP TOM addr should be the same as the aperture addr, we don't
explicitly check for that thought.

.. _`amdgpu_vram_location.fixme`:

FIXME
-----

when reducing VRAM size align new size on power of 2.

.. _`amdgpu_gtt_location`:

amdgpu_gtt_location
===================

.. c:function:: void amdgpu_gtt_location(struct amdgpu_device *adev, struct amdgpu_mc *mc)

    try to find GTT location

    :param struct amdgpu_device \*adev:
        amdgpu device structure holding all necessary informations

    :param struct amdgpu_mc \*mc:
        memory controller structure holding memory informations

.. _`amdgpu_gtt_location.description`:

Description
-----------

Function will place try to place GTT before or after VRAM.

If GTT size is bigger than space left then we ajust GTT size.
Thus function will never fails.

.. _`amdgpu_gtt_location.fixme`:

FIXME
-----

when reducing GTT size align new size on power of 2.

.. _`amdgpu_card_posted`:

amdgpu_card_posted
==================

.. c:function:: bool amdgpu_card_posted(struct amdgpu_device *adev)

    check if the hw has already been initialized

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_card_posted.description`:

Description
-----------

Check if the asic has been initialized (all asics).
Used at driver startup.
Returns true if initialized or false if not.

.. _`amdgpu_dummy_page_init`:

amdgpu_dummy_page_init
======================

.. c:function:: int amdgpu_dummy_page_init(struct amdgpu_device *adev)

    init dummy page used by the driver

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_dummy_page_init.description`:

Description
-----------

Allocate the dummy page used by the driver (all asics).
This dummy page is used by the driver as a filler for gart entries
when pages are taken out of the GART
Returns 0 on sucess, -ENOMEM on failure.

.. _`amdgpu_dummy_page_fini`:

amdgpu_dummy_page_fini
======================

.. c:function:: void amdgpu_dummy_page_fini(struct amdgpu_device *adev)

    free dummy page used by the driver

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_dummy_page_fini.description`:

Description
-----------

Frees the dummy page used by the driver (all asics).

.. _`cail_pll_read`:

cail_pll_read
=============

.. c:function:: uint32_t cail_pll_read(struct card_info *info, uint32_t reg)

    read PLL register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        PLL register offset

.. _`cail_pll_read.description`:

Description
-----------

Provides a PLL register accessor for the atom interpreter (r4xx+).
Returns the value of the PLL register.

.. _`cail_pll_write`:

cail_pll_write
==============

.. c:function:: void cail_pll_write(struct card_info *info, uint32_t reg, uint32_t val)

    write PLL register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        PLL register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_pll_write.description`:

Description
-----------

Provides a PLL register accessor for the atom interpreter (r4xx+).

.. _`cail_mc_read`:

cail_mc_read
============

.. c:function:: uint32_t cail_mc_read(struct card_info *info, uint32_t reg)

    read MC (Memory Controller) register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MC register offset

.. _`cail_mc_read.description`:

Description
-----------

Provides an MC register accessor for the atom interpreter (r4xx+).
Returns the value of the MC register.

.. _`cail_mc_write`:

cail_mc_write
=============

.. c:function:: void cail_mc_write(struct card_info *info, uint32_t reg, uint32_t val)

    write MC (Memory Controller) register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MC register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_mc_write.description`:

Description
-----------

Provides a MC register accessor for the atom interpreter (r4xx+).

.. _`cail_reg_write`:

cail_reg_write
==============

.. c:function:: void cail_reg_write(struct card_info *info, uint32_t reg, uint32_t val)

    write MMIO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MMIO register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_reg_write.description`:

Description
-----------

Provides a MMIO register accessor for the atom interpreter (r4xx+).

.. _`cail_reg_read`:

cail_reg_read
=============

.. c:function:: uint32_t cail_reg_read(struct card_info *info, uint32_t reg)

    read MMIO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MMIO register offset

.. _`cail_reg_read.description`:

Description
-----------

Provides an MMIO register accessor for the atom interpreter (r4xx+).
Returns the value of the MMIO register.

.. _`cail_ioreg_write`:

cail_ioreg_write
================

.. c:function:: void cail_ioreg_write(struct card_info *info, uint32_t reg, uint32_t val)

    write IO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        IO register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_ioreg_write.description`:

Description
-----------

Provides a IO register accessor for the atom interpreter (r4xx+).

.. _`cail_ioreg_read`:

cail_ioreg_read
===============

.. c:function:: uint32_t cail_ioreg_read(struct card_info *info, uint32_t reg)

    read IO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        IO register offset

.. _`cail_ioreg_read.description`:

Description
-----------

Provides an IO register accessor for the atom interpreter (r4xx+).
Returns the value of the IO register.

.. _`amdgpu_atombios_fini`:

amdgpu_atombios_fini
====================

.. c:function:: void amdgpu_atombios_fini(struct amdgpu_device *adev)

    free the driver info and callbacks for atombios

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_atombios_fini.description`:

Description
-----------

Frees the driver info and register access callbacks for the ATOM
interpreter (r4xx+).
Called at driver shutdown.

.. _`amdgpu_atombios_init`:

amdgpu_atombios_init
====================

.. c:function:: int amdgpu_atombios_init(struct amdgpu_device *adev)

    init the driver info and callbacks for atombios

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_atombios_init.description`:

Description
-----------

Initializes the driver info and register access callbacks for the
ATOM interpreter (r4xx+).
Returns 0 on sucess, -ENOMEM on failure.
Called at driver startup.

.. _`amdgpu_vga_set_decode`:

amdgpu_vga_set_decode
=====================

.. c:function:: unsigned int amdgpu_vga_set_decode(void *cookie, bool state)

    enable/disable vga decode

    :param void \*cookie:
        amdgpu_device pointer

    :param bool state:
        enable/disable vga decode

.. _`amdgpu_vga_set_decode.description`:

Description
-----------

Enable/disable vga decode (all asics).
Returns VGA resource flags.

.. _`amdgpu_check_pot_argument`:

amdgpu_check_pot_argument
=========================

.. c:function:: bool amdgpu_check_pot_argument(int arg)

    check that argument is a power of two

    :param int arg:
        value to check

.. _`amdgpu_check_pot_argument.description`:

Description
-----------

Validates that a certain argument is a power of two (all asics).
Returns true if argument is valid.

.. _`amdgpu_check_arguments`:

amdgpu_check_arguments
======================

.. c:function:: void amdgpu_check_arguments(struct amdgpu_device *adev)

    validate module params

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_check_arguments.description`:

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

.. _`amdgpu_ip_block_version_cmp`:

amdgpu_ip_block_version_cmp
===========================

.. c:function:: int amdgpu_ip_block_version_cmp(struct amdgpu_device *adev, enum amd_ip_block_type type, u32 major, u32 minor)

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amd_ip_block_type type:
        enum amd_ip_block_type

    :param u32 major:
        major version

    :param u32 minor:
        minor version

.. _`amdgpu_ip_block_version_cmp.description`:

Description
-----------

return 0 if equal or greater
return 1 if smaller or the ip_block doesn't exist

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

.. _`amdgpu_suspend_kms`:

amdgpu_suspend_kms
==================

.. c:function:: int amdgpu_suspend_kms(struct drm_device *dev, bool suspend, bool fbcon)

    initiate device suspend

    :param struct drm_device \*dev:
        *undescribed*

    :param bool suspend:
        *undescribed*

    :param bool fbcon:
        *undescribed*

.. _`amdgpu_suspend_kms.description`:

Description
-----------

Puts the hw in the suspend state (all asics).
Returns 0 for success or an error on failure.
Called at driver suspend.

.. _`amdgpu_resume_kms`:

amdgpu_resume_kms
=================

.. c:function:: int amdgpu_resume_kms(struct drm_device *dev, bool resume, bool fbcon)

    initiate device resume

    :param struct drm_device \*dev:
        *undescribed*

    :param bool resume:
        *undescribed*

    :param bool fbcon:
        *undescribed*

.. _`amdgpu_resume_kms.description`:

Description
-----------

Bring the hw back to operating state (all asics).
Returns 0 for success or an error on failure.
Called at driver resume.

.. _`amdgpu_gpu_reset`:

amdgpu_gpu_reset
================

.. c:function:: int amdgpu_gpu_reset(struct amdgpu_device *adev)

    reset the asic

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_gpu_reset.description`:

Description
-----------

Attempt the reset the GPU if it has hung (all asics).
Returns 0 for success or an error on failure.

.. This file was automatic generated / don't edit.

