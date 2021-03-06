.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_device.c

.. _`radeon_program_register_sequence`:

radeon_program_register_sequence
================================

.. c:function:: void radeon_program_register_sequence(struct radeon_device *rdev, const u32 *registers, const u32 array_size)

    program an array of registers.

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param registers:
        pointer to the register array
    :type registers: const u32 \*

    :param array_size:
        size of the register array
    :type array_size: const u32

.. _`radeon_program_register_sequence.description`:

Description
-----------

Programs an array or registers with and and or masks.
This is a helper for setting golden registers.

.. _`radeon_surface_init`:

radeon_surface_init
===================

.. c:function:: void radeon_surface_init(struct radeon_device *rdev)

    Clear GPU surface registers.

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_surface_init.description`:

Description
-----------

Clear GPU surface registers (r1xx-r5xx).

.. _`radeon_scratch_init`:

radeon_scratch_init
===================

.. c:function:: void radeon_scratch_init(struct radeon_device *rdev)

    Init scratch register driver information.

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_scratch_init.description`:

Description
-----------

Init CP scratch register driver information (r1xx-r5xx)

.. _`radeon_scratch_get`:

radeon_scratch_get
==================

.. c:function:: int radeon_scratch_get(struct radeon_device *rdev, uint32_t *reg)

    Allocate a scratch register

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param reg:
        scratch register mmio offset
    :type reg: uint32_t \*

.. _`radeon_scratch_get.description`:

Description
-----------

Allocate a CP scratch register for use by the driver (all asics).
Returns 0 on success or -EINVAL on failure.

.. _`radeon_scratch_free`:

radeon_scratch_free
===================

.. c:function:: void radeon_scratch_free(struct radeon_device *rdev, uint32_t reg)

    Free a scratch register

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param reg:
        scratch register mmio offset
    :type reg: uint32_t

.. _`radeon_scratch_free.description`:

Description
-----------

Free a CP scratch register allocated for use by the driver (all asics)

.. _`radeon_doorbell_init`:

radeon_doorbell_init
====================

.. c:function:: int radeon_doorbell_init(struct radeon_device *rdev)

    Init doorbell driver information.

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_doorbell_init.description`:

Description
-----------

Init doorbell driver information (CIK)
Returns 0 on success, error on failure.

.. _`radeon_doorbell_fini`:

radeon_doorbell_fini
====================

.. c:function:: void radeon_doorbell_fini(struct radeon_device *rdev)

    Tear down doorbell driver information.

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_doorbell_fini.description`:

Description
-----------

Tear down doorbell driver information (CIK)

.. _`radeon_doorbell_get`:

radeon_doorbell_get
===================

.. c:function:: int radeon_doorbell_get(struct radeon_device *rdev, u32 *doorbell)

    Allocate a doorbell entry

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param doorbell:
        doorbell index
    :type doorbell: u32 \*

.. _`radeon_doorbell_get.description`:

Description
-----------

Allocate a doorbell for use by the driver (all asics).
Returns 0 on success or -EINVAL on failure.

.. _`radeon_doorbell_free`:

radeon_doorbell_free
====================

.. c:function:: void radeon_doorbell_free(struct radeon_device *rdev, u32 doorbell)

    Free a doorbell entry

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param doorbell:
        doorbell index
    :type doorbell: u32

.. _`radeon_doorbell_free.description`:

Description
-----------

Free a doorbell allocated for use by the driver (all asics)

.. _`radeon_wb_disable`:

radeon_wb_disable
=================

.. c:function:: void radeon_wb_disable(struct radeon_device *rdev)

    Disable Writeback

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_wb_disable.description`:

Description
-----------

Disables Writeback (all asics).  Used for suspend.

.. _`radeon_wb_fini`:

radeon_wb_fini
==============

.. c:function:: void radeon_wb_fini(struct radeon_device *rdev)

    Disable Writeback and free memory

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_wb_fini.description`:

Description
-----------

Disables Writeback and frees the Writeback memory (all asics).
Used at driver shutdown.

.. _`radeon_wb_init`:

radeon_wb_init
==============

.. c:function:: int radeon_wb_init(struct radeon_device *rdev)

    Init Writeback driver info and allocate memory

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_wb_init.description`:

Description
-----------

Disables Writeback and frees the Writeback memory (all asics).
Used at driver startup.
Returns 0 on success or an -error on failure.

.. _`radeon_vram_location`:

radeon_vram_location
====================

.. c:function:: void radeon_vram_location(struct radeon_device *rdev, struct radeon_mc *mc, u64 base)

    try to find VRAM location

    :param rdev:
        radeon device structure holding all necessary informations
    :type rdev: struct radeon_device \*

    :param mc:
        memory controller structure holding memory informations
    :type mc: struct radeon_mc \*

    :param base:
        base address at which to put VRAM
    :type base: u64

.. _`radeon_vram_location.description`:

Description
-----------

Function will place try to place VRAM at base address provided
as parameter (which is so far either PCI aperture address or
for IGP TOM base address).

If there is not enough space to fit the unvisible VRAM in the 32bits
address space then we limit the VRAM size to the aperture.

If we are using AGP and if the AGP aperture doesn't allow us to have
room for all the VRAM than we restrict the VRAM to the PCI aperture
size and print a warning.

This function will never fails, worst case are limiting VRAM.

.. _`radeon_vram_location.note`:

Note
----

GTT start, end, size should be initialized before calling this
function on AGP platform.

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

.. _`radeon_vram_location.fixme`:

FIXME
-----

when reducing VRAM size align new size on power of 2.

.. _`radeon_gtt_location`:

radeon_gtt_location
===================

.. c:function:: void radeon_gtt_location(struct radeon_device *rdev, struct radeon_mc *mc)

    try to find GTT location

    :param rdev:
        radeon device structure holding all necessary informations
    :type rdev: struct radeon_device \*

    :param mc:
        memory controller structure holding memory informations
    :type mc: struct radeon_mc \*

.. _`radeon_gtt_location.description`:

Description
-----------

Function will place try to place GTT before or after VRAM.

If GTT size is bigger than space left then we ajust GTT size.
Thus function will never fails.

.. _`radeon_gtt_location.fixme`:

FIXME
-----

when reducing GTT size align new size on power of 2.

.. _`radeon_device_is_virtual`:

radeon_device_is_virtual
========================

.. c:function:: bool radeon_device_is_virtual( void)

    check if we are running is a virtual environment

    :param void:
        no arguments
    :type void: 

.. _`radeon_device_is_virtual.description`:

Description
-----------

Check if the asic has been passed through to a VM (all asics).
Used at driver startup.
Returns true if virtual or false if not.

.. _`radeon_card_posted`:

radeon_card_posted
==================

.. c:function:: bool radeon_card_posted(struct radeon_device *rdev)

    check if the hw has already been initialized

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_card_posted.description`:

Description
-----------

Check if the asic has been initialized (all asics).
Used at driver startup.
Returns true if initialized or false if not.

.. _`radeon_update_bandwidth_info`:

radeon_update_bandwidth_info
============================

.. c:function:: void radeon_update_bandwidth_info(struct radeon_device *rdev)

    update display bandwidth params

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_update_bandwidth_info.description`:

Description
-----------

Used when sclk/mclk are switched or display modes are set.
params are used to calculate display watermarks (all asics)

.. _`radeon_boot_test_post_card`:

radeon_boot_test_post_card
==========================

.. c:function:: bool radeon_boot_test_post_card(struct radeon_device *rdev)

    check and possibly initialize the hw

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_boot_test_post_card.description`:

Description
-----------

Check if the asic is initialized and if not, attempt to initialize
it (all asics).
Returns true if initialized or false if not.

.. _`radeon_dummy_page_init`:

radeon_dummy_page_init
======================

.. c:function:: int radeon_dummy_page_init(struct radeon_device *rdev)

    init dummy page used by the driver

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_dummy_page_init.description`:

Description
-----------

Allocate the dummy page used by the driver (all asics).
This dummy page is used by the driver as a filler for gart entries
when pages are taken out of the GART
Returns 0 on sucess, -ENOMEM on failure.

.. _`radeon_dummy_page_fini`:

radeon_dummy_page_fini
======================

.. c:function:: void radeon_dummy_page_fini(struct radeon_device *rdev)

    free dummy page used by the driver

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_dummy_page_fini.description`:

Description
-----------

Frees the dummy page used by the driver (all asics).

.. _`cail_pll_read`:

cail_pll_read
=============

.. c:function:: uint32_t cail_pll_read(struct card_info *info, uint32_t reg)

    read PLL register

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        PLL register offset
    :type reg: uint32_t

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

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        PLL register offset
    :type reg: uint32_t

    :param val:
        value to write to the pll register
    :type val: uint32_t

.. _`cail_pll_write.description`:

Description
-----------

Provides a PLL register accessor for the atom interpreter (r4xx+).

.. _`cail_mc_read`:

cail_mc_read
============

.. c:function:: uint32_t cail_mc_read(struct card_info *info, uint32_t reg)

    read MC (Memory Controller) register

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        MC register offset
    :type reg: uint32_t

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

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        MC register offset
    :type reg: uint32_t

    :param val:
        value to write to the pll register
    :type val: uint32_t

.. _`cail_mc_write.description`:

Description
-----------

Provides a MC register accessor for the atom interpreter (r4xx+).

.. _`cail_reg_write`:

cail_reg_write
==============

.. c:function:: void cail_reg_write(struct card_info *info, uint32_t reg, uint32_t val)

    write MMIO register

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        MMIO register offset
    :type reg: uint32_t

    :param val:
        value to write to the pll register
    :type val: uint32_t

.. _`cail_reg_write.description`:

Description
-----------

Provides a MMIO register accessor for the atom interpreter (r4xx+).

.. _`cail_reg_read`:

cail_reg_read
=============

.. c:function:: uint32_t cail_reg_read(struct card_info *info, uint32_t reg)

    read MMIO register

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        MMIO register offset
    :type reg: uint32_t

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

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        IO register offset
    :type reg: uint32_t

    :param val:
        value to write to the pll register
    :type val: uint32_t

.. _`cail_ioreg_write.description`:

Description
-----------

Provides a IO register accessor for the atom interpreter (r4xx+).

.. _`cail_ioreg_read`:

cail_ioreg_read
===============

.. c:function:: uint32_t cail_ioreg_read(struct card_info *info, uint32_t reg)

    read IO register

    :param info:
        atom card_info pointer
    :type info: struct card_info \*

    :param reg:
        IO register offset
    :type reg: uint32_t

.. _`cail_ioreg_read.description`:

Description
-----------

Provides an IO register accessor for the atom interpreter (r4xx+).
Returns the value of the IO register.

.. _`radeon_atombios_init`:

radeon_atombios_init
====================

.. c:function:: int radeon_atombios_init(struct radeon_device *rdev)

    init the driver info and callbacks for atombios

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_atombios_init.description`:

Description
-----------

Initializes the driver info and register access callbacks for the
ATOM interpreter (r4xx+).
Returns 0 on sucess, -ENOMEM on failure.
Called at driver startup.

.. _`radeon_atombios_fini`:

radeon_atombios_fini
====================

.. c:function:: void radeon_atombios_fini(struct radeon_device *rdev)

    free the driver info and callbacks for atombios

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_atombios_fini.description`:

Description
-----------

Frees the driver info and register access callbacks for the ATOM
interpreter (r4xx+).
Called at driver shutdown.

.. _`radeon_combios_init`:

radeon_combios_init
===================

.. c:function:: int radeon_combios_init(struct radeon_device *rdev)

    init the driver info for combios

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_combios_init.description`:

Description
-----------

Initializes the driver info for combios (r1xx-r3xx).
Returns 0 on sucess.
Called at driver startup.

.. _`radeon_combios_fini`:

radeon_combios_fini
===================

.. c:function:: void radeon_combios_fini(struct radeon_device *rdev)

    free the driver info for combios

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_combios_fini.description`:

Description
-----------

Frees the driver info for combios (r1xx-r3xx).
Called at driver shutdown.

.. _`radeon_vga_set_decode`:

radeon_vga_set_decode
=====================

.. c:function:: unsigned int radeon_vga_set_decode(void *cookie, bool state)

    enable/disable vga decode

    :param cookie:
        radeon_device pointer
    :type cookie: void \*

    :param state:
        enable/disable vga decode
    :type state: bool

.. _`radeon_vga_set_decode.description`:

Description
-----------

Enable/disable vga decode (all asics).
Returns VGA resource flags.

.. _`radeon_check_pot_argument`:

radeon_check_pot_argument
=========================

.. c:function:: bool radeon_check_pot_argument(int arg)

    check that argument is a power of two

    :param arg:
        value to check
    :type arg: int

.. _`radeon_check_pot_argument.description`:

Description
-----------

Validates that a certain argument is a power of two (all asics).
Returns true if argument is valid.

.. _`radeon_gart_size_auto`:

radeon_gart_size_auto
=====================

.. c:function:: int radeon_gart_size_auto(enum radeon_family family)

    :param family:
        *undescribed*
    :type family: enum radeon_family

.. _`radeon_gart_size_auto.description`:

Description
-----------

\ ``family``\  ASIC family name

.. _`radeon_check_arguments`:

radeon_check_arguments
======================

.. c:function:: void radeon_check_arguments(struct radeon_device *rdev)

    validate module params

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_check_arguments.description`:

Description
-----------

Validates certain module parameters and updates
the associated values used by the driver (all asics).

.. _`radeon_switcheroo_set_state`:

radeon_switcheroo_set_state
===========================

.. c:function:: void radeon_switcheroo_set_state(struct pci_dev *pdev, enum vga_switcheroo_state state)

    set switcheroo state

    :param pdev:
        pci dev pointer
    :type pdev: struct pci_dev \*

    :param state:
        vga_switcheroo state
    :type state: enum vga_switcheroo_state

.. _`radeon_switcheroo_set_state.description`:

Description
-----------

Callback for the switcheroo driver.  Suspends or resumes the
the asics before or after it is powered up using ACPI methods.

.. _`radeon_switcheroo_can_switch`:

radeon_switcheroo_can_switch
============================

.. c:function:: bool radeon_switcheroo_can_switch(struct pci_dev *pdev)

    see if switcheroo state can change

    :param pdev:
        pci dev pointer
    :type pdev: struct pci_dev \*

.. _`radeon_switcheroo_can_switch.description`:

Description
-----------

Callback for the switcheroo driver.  Check of the switcheroo
state can be changed.
Returns true if the state can be changed, false if not.

.. _`radeon_device_init`:

radeon_device_init
==================

.. c:function:: int radeon_device_init(struct radeon_device *rdev, struct drm_device *ddev, struct pci_dev *pdev, uint32_t flags)

    initialize the driver

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ddev:
        *undescribed*
    :type ddev: struct drm_device \*

    :param pdev:
        pci dev pointer
    :type pdev: struct pci_dev \*

    :param flags:
        driver flags
    :type flags: uint32_t

.. _`radeon_device_init.description`:

Description
-----------

Initializes the driver info and hw (all asics).
Returns 0 for success or an error on failure.
Called at driver startup.

.. _`radeon_device_fini`:

radeon_device_fini
==================

.. c:function:: void radeon_device_fini(struct radeon_device *rdev)

    tear down the driver

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_device_fini.description`:

Description
-----------

Tear down the driver info (all asics).
Called at driver shutdown.

.. _`radeon_suspend_kms`:

radeon_suspend_kms
==================

.. c:function:: int radeon_suspend_kms(struct drm_device *dev, bool suspend, bool fbcon, bool freeze)

    initiate device suspend

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param suspend:
        *undescribed*
    :type suspend: bool

    :param fbcon:
        *undescribed*
    :type fbcon: bool

    :param freeze:
        *undescribed*
    :type freeze: bool

.. _`radeon_suspend_kms.description`:

Description
-----------

Puts the hw in the suspend state (all asics).
Returns 0 for success or an error on failure.
Called at driver suspend.

.. _`radeon_resume_kms`:

radeon_resume_kms
=================

.. c:function:: int radeon_resume_kms(struct drm_device *dev, bool resume, bool fbcon)

    initiate device resume

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param resume:
        *undescribed*
    :type resume: bool

    :param fbcon:
        *undescribed*
    :type fbcon: bool

.. _`radeon_resume_kms.description`:

Description
-----------

Bring the hw back to operating state (all asics).
Returns 0 for success or an error on failure.
Called at driver resume.

.. _`radeon_gpu_reset`:

radeon_gpu_reset
================

.. c:function:: int radeon_gpu_reset(struct radeon_device *rdev)

    reset the asic

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_gpu_reset.description`:

Description
-----------

Attempt the reset the GPU if it has hung (all asics).
Returns 0 for success or an error on failure.

.. This file was automatic generated / don't edit.

