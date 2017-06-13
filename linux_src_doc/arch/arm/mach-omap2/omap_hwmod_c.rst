.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_hwmod.c

.. _`omap_hwmod_soc_ops`:

struct omap_hwmod_soc_ops
=========================

.. c:type:: struct omap_hwmod_soc_ops

    fn ptrs for some SoC-specific operations

.. _`omap_hwmod_soc_ops.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_soc_ops {
        void (*enable_module)(struct omap_hwmod *oh);
        int (*disable_module)(struct omap_hwmod *oh);
        int (*wait_target_ready)(struct omap_hwmod *oh);
        int (*assert_hardreset)(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri);
        int (*deassert_hardreset)(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri);
        int (*is_hardreset_asserted)(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri);
        int (*init_clkdm)(struct omap_hwmod *oh);
        void (*update_context_lost)(struct omap_hwmod *oh);
        int (*get_context_lost)(struct omap_hwmod *oh);
        int (*disable_direct_prcm)(struct omap_hwmod *oh);
    }

.. _`omap_hwmod_soc_ops.members`:

Members
-------

enable_module
    function to enable a module (via MODULEMODE)

disable_module
    function to disable a module (via MODULEMODE)

wait_target_ready
    *undescribed*

assert_hardreset
    *undescribed*

deassert_hardreset
    *undescribed*

is_hardreset_asserted
    *undescribed*

init_clkdm
    *undescribed*

update_context_lost
    *undescribed*

get_context_lost
    *undescribed*

disable_direct_prcm
    *undescribed*

.. _`omap_hwmod_soc_ops.description`:

Description
-----------

XXX Eventually this functionality will be hidden inside the PRM/CM
device drivers.  Until then, this should avoid huge blocks of cpu_is\_\*()
conditionals in this code.

.. _`_update_sysc_cache`:

_update_sysc_cache
==================

.. c:function:: int _update_sysc_cache(struct omap_hwmod *oh)

    return the module OCP_SYSCONFIG register, keep copy

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_update_sysc_cache.description`:

Description
-----------

Load the current value of the hwmod OCP_SYSCONFIG register into the
struct omap_hwmod for later use.  Returns -EINVAL if the hwmod has no
OCP_SYSCONFIG register or 0 upon success.

.. _`_write_sysconfig`:

_write_sysconfig
================

.. c:function:: void _write_sysconfig(u32 v, struct omap_hwmod *oh)

    write a value to the module's OCP_SYSCONFIG register

    :param u32 v:
        OCP_SYSCONFIG value to write

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_write_sysconfig.description`:

Description
-----------

Write \ ``v``\  into the module class' OCP_SYSCONFIG register, if it has
one.  No return value.

.. _`_set_master_standbymode`:

_set_master_standbymode
=======================

.. c:function:: int _set_master_standbymode(struct omap_hwmod *oh, u8 standbymode, u32 *v)

    set the OCP_SYSCONFIG MIDLEMODE field in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u8 standbymode:
        MIDLEMODE field bits

    :param u32 \*v:
        pointer to register contents to modify

.. _`_set_master_standbymode.description`:

Description
-----------

Update the master standby mode bits in \ ``v``\  to be \ ``standbymode``\  for
the \ ``oh``\  hwmod.  Does not write to the hardware.  Returns -EINVAL
upon error or 0 upon success.

.. _`_set_slave_idlemode`:

_set_slave_idlemode
===================

.. c:function:: int _set_slave_idlemode(struct omap_hwmod *oh, u8 idlemode, u32 *v)

    set the OCP_SYSCONFIG SIDLEMODE field in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u8 idlemode:
        SIDLEMODE field bits

    :param u32 \*v:
        pointer to register contents to modify

.. _`_set_slave_idlemode.description`:

Description
-----------

Update the slave idle mode bits in \ ``v``\  to be \ ``idlemode``\  for the \ ``oh``\ 
hwmod.  Does not write to the hardware.  Returns -EINVAL upon error
or 0 upon success.

.. _`_set_clockactivity`:

_set_clockactivity
==================

.. c:function:: int _set_clockactivity(struct omap_hwmod *oh, u8 clockact, u32 *v)

    set OCP_SYSCONFIG.CLOCKACTIVITY bits in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u8 clockact:
        CLOCKACTIVITY field bits

    :param u32 \*v:
        pointer to register contents to modify

.. _`_set_clockactivity.description`:

Description
-----------

Update the clockactivity mode bits in \ ``v``\  to be \ ``clockact``\  for the
\ ``oh``\  hwmod.  Used for additional powersaving on some modules.  Does
not write to the hardware.  Returns -EINVAL upon error or 0 upon
success.

.. _`_set_softreset`:

_set_softreset
==============

.. c:function:: int _set_softreset(struct omap_hwmod *oh, u32 *v)

    set OCP_SYSCONFIG.SOFTRESET bit in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u32 \*v:
        pointer to register contents to modify

.. _`_set_softreset.description`:

Description
-----------

Set the SOFTRESET bit in \ ``v``\  for hwmod \ ``oh``\ .  Returns -EINVAL upon
error or 0 upon success.

.. _`_clear_softreset`:

_clear_softreset
================

.. c:function:: int _clear_softreset(struct omap_hwmod *oh, u32 *v)

    clear OCP_SYSCONFIG.SOFTRESET bit in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u32 \*v:
        pointer to register contents to modify

.. _`_clear_softreset.description`:

Description
-----------

Clear the SOFTRESET bit in \ ``v``\  for hwmod \ ``oh``\ .  Returns -EINVAL upon
error or 0 upon success.

.. _`_wait_softreset_complete`:

_wait_softreset_complete
========================

.. c:function:: int _wait_softreset_complete(struct omap_hwmod *oh)

    wait for an OCP softreset to complete

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to wait on

.. _`_wait_softreset_complete.description`:

Description
-----------

Wait until the IP block represented by \ ``oh``\  reports that its OCP
softreset is complete.  This can be triggered by software (see
\_ocp_softreset()) or by hardware upon returning from off-mode (one
example is HSMMC).  Waits for up to MAX_MODULE_SOFTRESET_WAIT
microseconds.  Returns the number of microseconds waited.

.. _`_set_dmadisable`:

_set_dmadisable
===============

.. c:function:: int _set_dmadisable(struct omap_hwmod *oh)

    set OCP_SYSCONFIG.DMADISABLE bit in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_set_dmadisable.description`:

Description
-----------

The DMADISABLE bit is a semi-automatic bit present in sysconfig register
of some modules. When the DMA must perform read/write accesses, the
DMADISABLE bit is cleared by the hardware. But when the DMA must stop
for power management, software must set the DMADISABLE bit back to 1.

Set the DMADISABLE bit in \ ``v``\  for hwmod \ ``oh``\ .  Returns -EINVAL upon
error or 0 upon success.

.. _`_set_module_autoidle`:

_set_module_autoidle
====================

.. c:function:: int _set_module_autoidle(struct omap_hwmod *oh, u8 autoidle, u32 *v)

    set the OCP_SYSCONFIG AUTOIDLE field in \ ``v``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u8 autoidle:
        desired AUTOIDLE bitfield value (0 or 1)

    :param u32 \*v:
        pointer to register contents to modify

.. _`_set_module_autoidle.description`:

Description
-----------

Update the module autoidle bit in \ ``v``\  to be \ ``autoidle``\  for the \ ``oh``\ 
hwmod.  The autoidle bit controls whether the module can gate
internal clocks automatically when it isn't doing anything; the
exact function of this bit varies on a per-module basis.  This
function does not write to the hardware.  Returns -EINVAL upon
error or 0 upon success.

.. _`_enable_wakeup`:

_enable_wakeup
==============

.. c:function:: int _enable_wakeup(struct omap_hwmod *oh, u32 *v)

    set OCP_SYSCONFIG.ENAWAKEUP bit in the hardware

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u32 \*v:
        *undescribed*

.. _`_enable_wakeup.description`:

Description
-----------

Allow the hardware module \ ``oh``\  to send wakeups.  Returns -EINVAL
upon error or 0 upon success.

.. _`_disable_wakeup`:

_disable_wakeup
===============

.. c:function:: int _disable_wakeup(struct omap_hwmod *oh, u32 *v)

    clear OCP_SYSCONFIG.ENAWAKEUP bit in the hardware

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u32 \*v:
        *undescribed*

.. _`_disable_wakeup.description`:

Description
-----------

Prevent the hardware module \ ``oh``\  to send wakeups.  Returns -EINVAL
upon error or 0 upon success.

.. _`_add_initiator_dep`:

_add_initiator_dep
==================

.. c:function:: int _add_initiator_dep(struct omap_hwmod *oh, struct omap_hwmod *init_oh)

    prevent \ ``oh``\  from smart-idling while \ ``init_oh``\  is active

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param struct omap_hwmod \*init_oh:
        *undescribed*

.. _`_add_initiator_dep.description`:

Description
-----------

Prevent the hardware module \ ``oh``\  from entering idle while the
hardare module initiator \ ``init_oh``\  is active.  Useful when a module
will be accessed by a particular initiator (e.g., if a module will
be accessed by the IVA, there should be a sleepdep between the IVA
initiator and the module).  Only applies to modules in smart-idle
mode.  If the clockdomain is marked as not needing autodeps, return
0 without doing anything.  Otherwise, returns -EINVAL upon error or
passes along \ :c:func:`clkdm_add_sleepdep`\  value upon success.

.. _`_del_initiator_dep`:

_del_initiator_dep
==================

.. c:function:: int _del_initiator_dep(struct omap_hwmod *oh, struct omap_hwmod *init_oh)

    allow \ ``oh``\  to smart-idle even if \ ``init_oh``\  is active

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param struct omap_hwmod \*init_oh:
        *undescribed*

.. _`_del_initiator_dep.description`:

Description
-----------

Allow the hardware module \ ``oh``\  to enter idle while the hardare
module initiator \ ``init_oh``\  is active.  Useful when a module will not
be accessed by a particular initiator (e.g., if a module will not
be accessed by the IVA, there should be no sleepdep between the IVA
initiator and the module).  Only applies to modules in smart-idle
mode.  If the clockdomain is marked as not needing autodeps, return
0 without doing anything.  Returns -EINVAL upon error or passes
along \ :c:func:`clkdm_del_sleepdep`\  value upon success.

.. _`_init_main_clk`:

_init_main_clk
==============

.. c:function:: int _init_main_clk(struct omap_hwmod *oh)

    get a struct clk \* for the the hwmod's main functional clk

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_init_main_clk.description`:

Description
-----------

Called from \_init_clocks().  Populates the \ ``oh``\  \_clk (main
functional clock pointer) if a clock matching the hwmod name is found,
or a main_clk is present.  Returns 0 on success or -EINVAL on error.

.. _`_init_interface_clks`:

_init_interface_clks
====================

.. c:function:: int _init_interface_clks(struct omap_hwmod *oh)

    get a struct clk \* for the the hwmod's interface clks

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_init_interface_clks.description`:

Description
-----------

Called from \_init_clocks().  Populates the \ ``oh``\  OCP slave interface
clock pointers.  Returns 0 on success or -EINVAL on error.

.. _`_init_opt_clks`:

_init_opt_clks
==============

.. c:function:: int _init_opt_clks(struct omap_hwmod *oh)

    get a struct clk \* for the the hwmod's optional clocks

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_init_opt_clks.description`:

Description
-----------

Called from \_init_clocks().  Populates the \ ``oh``\  omap_hwmod_opt_clk
clock pointers.  Returns 0 on success or -EINVAL on error.

.. _`_enable_clocks`:

_enable_clocks
==============

.. c:function:: int _enable_clocks(struct omap_hwmod *oh)

    enable hwmod main clock and interface clocks

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_enable_clocks.description`:

Description
-----------

Enables all clocks necessary for register reads and writes to succeed
on the hwmod \ ``oh``\ .  Returns 0.

.. _`_disable_clocks`:

_disable_clocks
===============

.. c:function:: int _disable_clocks(struct omap_hwmod *oh)

    disable hwmod main clock and interface clocks

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_disable_clocks.description`:

Description
-----------

Disables the hwmod \ ``oh``\  main functional and interface clocks.  Returns 0.

.. _`_omap4_enable_module`:

_omap4_enable_module
====================

.. c:function:: void _omap4_enable_module(struct omap_hwmod *oh)

    enable CLKCTRL modulemode on OMAP4

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_omap4_enable_module.description`:

Description
-----------

Enables the PRCM module mode related to the hwmod \ ``oh``\ .
No return value.

.. _`_omap4_wait_target_disable`:

_omap4_wait_target_disable
==========================

.. c:function:: int _omap4_wait_target_disable(struct omap_hwmod *oh)

    wait for a module to be disabled on OMAP4

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_omap4_wait_target_disable.description`:

Description
-----------

Wait for a module \ ``oh``\  to enter slave idle.  Returns 0 if the module
does not have an IDLEST bit or if the module successfully enters
slave idle; otherwise, pass along the return value of the
appropriate \*\_cm\*\_wait_module_idle() function.

.. _`_count_mpu_irqs`:

_count_mpu_irqs
===============

.. c:function:: int _count_mpu_irqs(struct omap_hwmod *oh)

    count the number of MPU IRQ lines associated with \ ``oh``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*oh

.. _`_count_mpu_irqs.description`:

Description
-----------

Count and return the number of MPU IRQs associated with the hwmod
\ ``oh``\ .  Used to allocate struct resource data.  Returns 0 if \ ``oh``\  is
NULL.

.. _`_count_sdma_reqs`:

_count_sdma_reqs
================

.. c:function:: int _count_sdma_reqs(struct omap_hwmod *oh)

    count the number of SDMA request lines associated with \ ``oh``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*oh

.. _`_count_sdma_reqs.description`:

Description
-----------

Count and return the number of SDMA request lines associated with
the hwmod \ ``oh``\ .  Used to allocate struct resource data.  Returns 0
if \ ``oh``\  is NULL.

.. _`_count_ocp_if_addr_spaces`:

_count_ocp_if_addr_spaces
=========================

.. c:function:: int _count_ocp_if_addr_spaces(struct omap_hwmod_ocp_if *os)

    count the number of address space entries for \ ``oh``\ 

    :param struct omap_hwmod_ocp_if \*os:
        *undescribed*

.. _`_count_ocp_if_addr_spaces.description`:

Description
-----------

Count and return the number of address space ranges associated with
the hwmod \ ``oh``\ .  Used to allocate struct resource data.  Returns 0
if \ ``oh``\  is NULL.

.. _`_get_mpu_irq_by_name`:

_get_mpu_irq_by_name
====================

.. c:function:: int _get_mpu_irq_by_name(struct omap_hwmod *oh, const char *name, unsigned int *irq)

    fetch MPU interrupt line number by name

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to operate on

    :param const char \*name:
        pointer to the name of the MPU interrupt number to fetch (optional)

    :param unsigned int \*irq:
        pointer to an unsigned int to store the MPU IRQ number to

.. _`_get_mpu_irq_by_name.description`:

Description
-----------

Retrieve a MPU hardware IRQ line number named by \ ``name``\  associated
with the IP block pointed to by \ ``oh``\ .  The IRQ number will be filled
into the address pointed to by \ ``dma``\ .  When \ ``name``\  is non-null, the
IRQ line number associated with the named entry will be returned.
If \ ``name``\  is null, the first matching entry will be returned.  Data
order is not meaningful in hwmod data, so callers are strongly
encouraged to use a non-null \ ``name``\  whenever possible to avoid
unpredictable effects if hwmod data is later added that causes data
ordering to change.  Returns 0 upon success or a negative error
code upon error.

.. _`_get_sdma_req_by_name`:

_get_sdma_req_by_name
=====================

.. c:function:: int _get_sdma_req_by_name(struct omap_hwmod *oh, const char *name, unsigned int *dma)

    fetch SDMA request line ID by name

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to operate on

    :param const char \*name:
        pointer to the name of the SDMA request line to fetch (optional)

    :param unsigned int \*dma:
        pointer to an unsigned int to store the request line ID to

.. _`_get_sdma_req_by_name.description`:

Description
-----------

Retrieve an SDMA request line ID named by \ ``name``\  on the IP block
pointed to by \ ``oh``\ .  The ID will be filled into the address pointed
to by \ ``dma``\ .  When \ ``name``\  is non-null, the request line ID associated
with the named entry will be returned.  If \ ``name``\  is null, the first
matching entry will be returned.  Data order is not meaningful in
hwmod data, so callers are strongly encouraged to use a non-null
\ ``name``\  whenever possible to avoid unpredictable effects if hwmod
data is later added that causes data ordering to change.  Returns 0
upon success or a negative error code upon error.

.. _`_get_addr_space_by_name`:

_get_addr_space_by_name
=======================

.. c:function:: int _get_addr_space_by_name(struct omap_hwmod *oh, const char *name, u32 *pa_start, u32 *pa_end)

    fetch address space start & end by name

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to operate on

    :param const char \*name:
        pointer to the name of the address space to fetch (optional)

    :param u32 \*pa_start:
        pointer to a u32 to store the starting address to

    :param u32 \*pa_end:
        pointer to a u32 to store the ending address to

.. _`_get_addr_space_by_name.description`:

Description
-----------

Retrieve address space start and end addresses for the IP block
pointed to by \ ``oh``\ .  The data will be filled into the addresses
pointed to by \ ``pa_start``\  and \ ``pa_end``\ .  When \ ``name``\  is non-null, the
address space data associated with the named entry will be
returned.  If \ ``name``\  is null, the first matching entry will be
returned.  Data order is not meaningful in hwmod data, so callers
are strongly encouraged to use a non-null \ ``name``\  whenever possible
to avoid unpredictable effects if hwmod data is later added that
causes data ordering to change.  Returns 0 upon success or a
negative error code upon error.

.. _`_save_mpu_port_index`:

_save_mpu_port_index
====================

.. c:function:: void _save_mpu_port_index(struct omap_hwmod *oh)

    find and save the index to \ ``oh``\ 's MPU port

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_save_mpu_port_index.description`:

Description
-----------

Determines the array index of the OCP slave port that the MPU uses
to address the device, and saves it into the struct omap_hwmod.
Intended to be called during hwmod registration only. No return
value.

.. _`_find_mpu_rt_port`:

_find_mpu_rt_port
=================

.. c:function:: struct omap_hwmod_ocp_if *_find_mpu_rt_port(struct omap_hwmod *oh)

    return omap_hwmod_ocp_if accessible by the MPU

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_find_mpu_rt_port.description`:

Description
-----------

Given a pointer to a struct omap_hwmod record \ ``oh``\ , return a pointer
to the struct omap_hwmod_ocp_if record that is used by the MPU to
communicate with the IP block.  This interface need not be directly
connected to the MPU (and almost certainly is not), but is directly
connected to the IP block represented by \ ``oh``\ .  Returns a pointer
to the struct omap_hwmod_ocp_if \* upon success, or returns NULL upon
error or if there does not appear to be a path from the MPU to this
IP block.

.. _`_find_mpu_rt_addr_space`:

_find_mpu_rt_addr_space
=======================

.. c:function:: struct omap_hwmod_addr_space *_find_mpu_rt_addr_space(struct omap_hwmod *oh)

    return MPU register target address space for \ ``oh``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_find_mpu_rt_addr_space.description`:

Description
-----------

Returns a pointer to the struct omap_hwmod_addr_space record representing
the register target MPU address space; or returns NULL upon error.

.. _`_enable_sysc`:

_enable_sysc
============

.. c:function:: void _enable_sysc(struct omap_hwmod *oh)

    try to bring a module out of idle via OCP_SYSCONFIG

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_enable_sysc.description`:

Description
-----------

Ensure that the OCP_SYSCONFIG register for the IP block represented
by \ ``oh``\  is set to indicate to the PRCM that the IP block is active.
Usually this means placing the module into smart-idle mode and
smart-standby, but if there is a bug in the automatic idle handling
for the IP block, it may need to be placed into the force-idle or
no-idle variants of these modes.  No return value.

.. _`_idle_sysc`:

_idle_sysc
==========

.. c:function:: void _idle_sysc(struct omap_hwmod *oh)

    try to put a module into idle via OCP_SYSCONFIG

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_idle_sysc.description`:

Description
-----------

If module is marked as SWSUP_SIDLE, force the module into slave
idle; otherwise, configure it for smart-idle.  If module is marked
as SWSUP_MSUSPEND, force the module into master standby; otherwise,
configure it for smart-standby.  No return value.

.. _`_shutdown_sysc`:

_shutdown_sysc
==============

.. c:function:: void _shutdown_sysc(struct omap_hwmod *oh)

    force a module into idle via OCP_SYSCONFIG

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_shutdown_sysc.description`:

Description
-----------

Force the module into slave idle and master suspend. No return
value.

.. _`_lookup`:

_lookup
=======

.. c:function:: struct omap_hwmod *_lookup(const char *name)

    find an omap_hwmod by name

    :param const char \*name:
        find an omap_hwmod by name

.. _`_lookup.description`:

Description
-----------

Return a pointer to an omap_hwmod by name, or NULL if not found.

.. _`_init_clkdm`:

_init_clkdm
===========

.. c:function:: int _init_clkdm(struct omap_hwmod *oh)

    look up a clockdomain name, store pointer in omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_init_clkdm.description`:

Description
-----------

Convert a clockdomain name stored in a struct omap_hwmod into a
clockdomain pointer, and save it into the struct omap_hwmod.
Return -EINVAL if the clkdm_name lookup failed.

.. _`_init_clocks`:

_init_clocks
============

.. c:function:: int _init_clocks(struct omap_hwmod *oh, void *data)

    clk_get() all clocks associated with this hwmod. Retrieve as well the clockdomain.

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param void \*data:
        not used; pass NULL

.. _`_init_clocks.description`:

Description
-----------

Called by omap_hwmod_setup\_\*() (after \ :c:func:`omap2_clk_init`\ ).
Resolves all clock names embedded in the hwmod.  Returns 0 on
success, or a negative error code on failure.

.. _`_lookup_hardreset`:

_lookup_hardreset
=================

.. c:function:: int _lookup_hardreset(struct omap_hwmod *oh, const char *name, struct omap_hwmod_rst_info *ohri)

    fill register bit info for this hwmod/reset line

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param const char \*name:
        name of the reset line in the context of this hwmod

    :param struct omap_hwmod_rst_info \*ohri:
        struct omap_hwmod_rst_info \* that this function will fill in

.. _`_lookup_hardreset.description`:

Description
-----------

Return the bit position of the reset line that match the
input name. Return -ENOENT if not found.

.. _`_assert_hardreset`:

_assert_hardreset
=================

.. c:function:: int _assert_hardreset(struct omap_hwmod *oh, const char *name)

    assert the HW reset line of submodules contained in the hwmod module.

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param const char \*name:
        name of the reset line to lookup and assert

.. _`_assert_hardreset.description`:

Description
-----------

Some IP like dsp, ipu or iva contain processor that require an HW
reset line to be assert / deassert in order to enable fully the IP.
Returns -EINVAL if \ ``oh``\  is null, -ENOSYS if we have no way of
asserting the hardreset line on the currently-booted SoC, or passes
along the return value from \_lookup_hardreset() or the SoC's
assert_hardreset code.

.. _`_deassert_hardreset`:

_deassert_hardreset
===================

.. c:function:: int _deassert_hardreset(struct omap_hwmod *oh, const char *name)

    deassert the HW reset line of submodules contained in the hwmod module.

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param const char \*name:
        name of the reset line to look up and deassert

.. _`_deassert_hardreset.description`:

Description
-----------

Some IP like dsp, ipu or iva contain processor that require an HW
reset line to be assert / deassert in order to enable fully the IP.
Returns -EINVAL if \ ``oh``\  is null, -ENOSYS if we have no way of
deasserting the hardreset line on the currently-booted SoC, or passes
along the return value from \_lookup_hardreset() or the SoC's
deassert_hardreset code.

.. _`_read_hardreset`:

_read_hardreset
===============

.. c:function:: int _read_hardreset(struct omap_hwmod *oh, const char *name)

    read the HW reset line state of submodules contained in the hwmod module

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param const char \*name:
        name of the reset line to look up and read

.. _`_read_hardreset.description`:

Description
-----------

Return the state of the reset line.  Returns -EINVAL if \ ``oh``\  is
null, -ENOSYS if we have no way of reading the hardreset line
status on the currently-booted SoC, or passes along the return
value from \_lookup_hardreset() or the SoC's is_hardreset_asserted
code.

.. _`_are_all_hardreset_lines_asserted`:

_are_all_hardreset_lines_asserted
=================================

.. c:function:: bool _are_all_hardreset_lines_asserted(struct omap_hwmod *oh)

    return true if the \ ``oh``\  is hard-reset

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_are_all_hardreset_lines_asserted.description`:

Description
-----------

If all hardreset lines associated with \ ``oh``\  are asserted, then return true.
Otherwise, if part of \ ``oh``\  is out hardreset or if no hardreset lines
associated with \ ``oh``\  are asserted, then return false.
This function is used to avoid executing some parts of the IP block
enable/disable sequence if its hardreset line is set.

.. _`_are_any_hardreset_lines_asserted`:

_are_any_hardreset_lines_asserted
=================================

.. c:function:: bool _are_any_hardreset_lines_asserted(struct omap_hwmod *oh)

    return true if any part of \ ``oh``\  is hard-reset

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_are_any_hardreset_lines_asserted.description`:

Description
-----------

If any hardreset lines associated with \ ``oh``\  are asserted, then
return true.  Otherwise, if no hardreset lines associated with \ ``oh``\ 
are asserted, or if \ ``oh``\  has no hardreset lines, then return false.
This function is used to avoid executing some parts of the IP block
enable/disable sequence if any hardreset line is set.

.. _`_omap4_disable_module`:

_omap4_disable_module
=====================

.. c:function:: int _omap4_disable_module(struct omap_hwmod *oh)

    enable CLKCTRL modulemode on OMAP4

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_omap4_disable_module.description`:

Description
-----------

Disable the PRCM module mode related to the hwmod \ ``oh``\ .
Return EINVAL if the modulemode is not supported and 0 in case of success.

.. _`_ocp_softreset`:

_ocp_softreset
==============

.. c:function:: int _ocp_softreset(struct omap_hwmod *oh)

    reset an omap_hwmod via the OCP_SYSCONFIG bit

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_ocp_softreset.description`:

Description
-----------

Resets an omap_hwmod \ ``oh``\  via the OCP_SYSCONFIG bit.  hwmod must be
enabled for this to work.  Returns -ENOENT if the hwmod cannot be
reset this way, -EINVAL if the hwmod is in the wrong state,
-ETIMEDOUT if the module did not reset in time, or 0 upon success.

In OMAP3 a specific SYSSTATUS register is used to get the reset status.
Starting in OMAP4, some IPs do not have SYSSTATUS registers and instead
use the SYSCONFIG softreset bit to provide the status.

Note that some IP like McBSP do have reset control but don't have
reset status.

.. _`_reset`:

_reset
======

.. c:function:: int _reset(struct omap_hwmod *oh)

    reset an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_reset.description`:

Description
-----------

Resets an omap_hwmod \ ``oh``\ .  If the module has a custom reset
function pointer defined, then call it to reset the IP block, and
pass along its return value to the caller.  Otherwise, if the IP
block has an OCP_SYSCONFIG register with a SOFTRESET bitfield
associated with it, call a function to reset the IP block via that
method, and pass along the return value to the caller.  Finally, if
the IP block has some hardreset lines associated with it, assert
all of those, but do \_not\_ deassert them. (This is because driver
authors have expressed an apparent requirement to control the
deassertion of the hardreset lines themselves.)

The default software reset mechanism for most OMAP IP blocks is
triggered via the OCP_SYSCONFIG.SOFTRESET bit.  However, some
hwmods cannot be reset via this method.  Some are not targets and
therefore have no OCP header registers to access.  Others (like the
IVA) have idiosyncratic reset sequences.  So for these relatively
rare cases, custom reset code can be supplied in the struct
omap_hwmod_class .reset function pointer.

\_set_dmadisable() is called to set the DMADISABLE bit so that it
does not prevent idling of the system. This is necessary for cases
where ROMCODE/BOOTLOADER uses dma and transfers control to the
kernel without disabling dma.

Passes along the return value from either \_ocp_softreset() or the
custom reset function - these must return -EINVAL if the hwmod
cannot be reset this way or if the hwmod is in the wrong state,
-ETIMEDOUT if the module did not reset in time, or 0 upon success.

.. _`_omap4_update_context_lost`:

_omap4_update_context_lost
==========================

.. c:function:: void _omap4_update_context_lost(struct omap_hwmod *oh)

    increment hwmod context loss counter if hwmod context was lost, and clear hardware context loss reg

    :param struct omap_hwmod \*oh:
        hwmod to check for context loss

.. _`_omap4_update_context_lost.description`:

Description
-----------

If the PRCM indicates that the hwmod \ ``oh``\  lost context, increment
our in-memory context loss counter, and clear the RM\_\*\_CONTEXT
bits. No return value.

.. _`_omap4_get_context_lost`:

_omap4_get_context_lost
=======================

.. c:function:: int _omap4_get_context_lost(struct omap_hwmod *oh)

    get context loss counter for a hwmod

    :param struct omap_hwmod \*oh:
        hwmod to get context loss counter for

.. _`_omap4_get_context_lost.description`:

Description
-----------

Returns the in-memory context loss counter for a hwmod.

.. _`_enable_preprogram`:

_enable_preprogram
==================

.. c:function:: int _enable_preprogram(struct omap_hwmod *oh)

    Pre-program an IP block during the \_enable() process

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_enable_preprogram.description`:

Description
-----------

Some IP blocks (such as AESS) require some additional programming
after enable before they can enter idle.  If a function pointer to
do so is present in the hwmod data, then call it and pass along the
return value; otherwise, return 0.

.. _`_enable`:

_enable
=======

.. c:function:: int _enable(struct omap_hwmod *oh)

    enable an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_enable.description`:

Description
-----------

Enables an omap_hwmod \ ``oh``\  such that the MPU can access the hwmod's
register target.  Returns -EINVAL if the hwmod is in the wrong
state or passes along the return value of \_wait_target_ready().

.. _`_idle`:

_idle
=====

.. c:function:: int _idle(struct omap_hwmod *oh)

    idle an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_idle.description`:

Description
-----------

Idles an omap_hwmod \ ``oh``\ .  This should be called once the hwmod has
no further work.  Returns -EINVAL if the hwmod is in the wrong
state or returns 0.

.. _`_shutdown`:

_shutdown
=========

.. c:function:: int _shutdown(struct omap_hwmod *oh)

    shutdown an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_shutdown.description`:

Description
-----------

Shut down an omap_hwmod \ ``oh``\ .  This should be called when the driver
used for the hwmod is removed or unloaded or if the driver is not
used by the system.  Returns -EINVAL if the hwmod is in the wrong
state or returns 0.

.. _`of_dev_hwmod_lookup`:

of_dev_hwmod_lookup
===================

.. c:function:: int of_dev_hwmod_lookup(struct device_node *np, struct omap_hwmod *oh, int *index, struct device_node **found)

    look up needed hwmod from dt blob

    :param struct device_node \*np:
        struct device_node \*

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param int \*index:
        index of the entry found

    :param struct device_node \*\*found:
        struct device_node \* found or NULL

.. _`of_dev_hwmod_lookup.description`:

Description
-----------

Parse the dt blob and find out needed hwmod. Recursive function is
implemented to take care hierarchical dt blob parsing.

.. _`of_dev_hwmod_lookup.return`:

Return
------

Returns 0 on success, -ENODEV when not found.

.. _`_init_mpu_rt_base`:

_init_mpu_rt_base
=================

.. c:function:: int _init_mpu_rt_base(struct omap_hwmod *oh, void *data, int index, struct device_node *np)

    populate the virtual address for a hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to locate the virtual address

    :param void \*data:
        (unused, caller should pass NULL)

    :param int index:
        index of the reg entry iospace in device tree

    :param struct device_node \*np:
        struct device_node \* of the IP block's device node in the DT data

.. _`_init_mpu_rt_base.description`:

Description
-----------

Cache the virtual address used by the MPU to access this IP block's
registers.  This address is needed early so the OCP registers that
are part of the device's address space can be ioremapped properly.

If SYSC access is not needed, the registers will not be remapped
and non-availability of MPU access is not treated as an error.

Returns 0 on success, -EINVAL if an invalid hwmod is passed, and
-ENXIO on absent or invalid register target address space.

.. _`_init`:

_init
=====

.. c:function:: int _init(struct omap_hwmod *oh, void *data)

    initialize internal data for the hwmod \ ``oh``\ 

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param void \*data:
        *undescribed*

.. _`_init.description`:

Description
-----------

Look up the clocks and the address space used by the MPU to access
registers belonging to the hwmod \ ``oh``\ .  \ ``oh``\  must already be
registered at this point.  This is the first of two phases for
hwmod initialization.  Code called here does not touch any hardware
registers, it simply prepares internal data structures.  Returns 0
upon success or if the hwmod isn't registered or if the hwmod's
address space is not defined, or -EINVAL upon failure.

.. _`_setup_iclk_autoidle`:

_setup_iclk_autoidle
====================

.. c:function:: void _setup_iclk_autoidle(struct omap_hwmod *oh)

    configure an IP block's interface clocks

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_setup_iclk_autoidle.description`:

Description
-----------

Set up the module's interface clocks.  XXX This function is still mostly
a stub; implementing this properly requires iclk autoidle usecounting in
the clock code.   No return value.

.. _`_setup_reset`:

_setup_reset
============

.. c:function:: int _setup_reset(struct omap_hwmod *oh)

    reset an IP block during the setup process

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_setup_reset.description`:

Description
-----------

Reset the IP block corresponding to the hwmod \ ``oh``\  during the setup
process.  The IP block is first enabled so it can be successfully
reset.  Returns 0 upon success or a negative error code upon
failure.

.. _`_setup_postsetup`:

_setup_postsetup
================

.. c:function:: void _setup_postsetup(struct omap_hwmod *oh)

    transition to the appropriate state after \_setup

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_setup_postsetup.description`:

Description
-----------

Place an IP block represented by \ ``oh``\  into a "post-setup" state --
either IDLE, ENABLED, or DISABLED.  ("post-setup" simply means that
this function is called at the end of \_setup().)  The postsetup
state for an IP block can be changed by calling
\ :c:func:`omap_hwmod_enter_postsetup_state`\  early in the boot process,
before one of the omap_hwmod_setup\*() functions are called for the
IP block.

The IP block stays in this state until a PM runtime-based driver is
loaded for that IP block.  A post-setup state of IDLE is
appropriate for almost all IP blocks with runtime PM-enabled
drivers, since those drivers are able to enable the IP block.  A
post-setup state of ENABLED is appropriate for kernels with PM
runtime disabled.  The DISABLED state is appropriate for unusual IP
blocks such as the MPU WDTIMER on kernels without WDTIMER drivers
included, since the WDTIMER starts running on reset and will reset
the MPU if left active.

This post-setup mechanism is deprecated.  Once all of the OMAP
drivers have been converted to use PM runtime, and all of the IP
block data and interconnect data is available to the hwmod code, it
should be possible to replace this mechanism with a "lazy reset"
arrangement.  In a "lazy reset" setup, each IP block is enabled
when the driver first probes, then all remaining IP blocks without
drivers are either shut down or enabled after the drivers have
loaded.  However, this cannot take place until the above
preconditions have been met, since otherwise the late reset code
has no way of knowing which IP blocks are in use by drivers, and
which ones are unused.

No return value.

.. _`_setup`:

_setup
======

.. c:function:: int _setup(struct omap_hwmod *oh, void *data)

    prepare IP block hardware for use

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param void \*data:
        *undescribed*

.. _`_setup.description`:

Description
-----------

Configure the IP block represented by \ ``oh``\ .  This may include
enabling the IP block, resetting it, and placing it into a
post-setup state, depending on the type of IP block and applicable
flags.  IP blocks are reset to prevent any previous configuration
by the bootloader or previous operating system from interfering
with power management or other parts of the system.  The reset can
be avoided; see \ :c:func:`omap_hwmod_no_setup_reset`\ .  This is the second of
two phases for hwmod initialization.  Code called here generally
affects the IP block hardware, or system integration hardware
associated with the IP block.  Returns 0.

.. _`_register`:

_register
=========

.. c:function:: int _register(struct omap_hwmod *oh)

    register a struct omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_register.description`:

Description
-----------

Registers the omap_hwmod \ ``oh``\ .  Returns -EEXIST if an omap_hwmod
already has been registered by the same name; -EINVAL if the
omap_hwmod is in the wrong state, if \ ``oh``\  is NULL, if the
omap_hwmod's class field is NULL; if the omap_hwmod is missing a
name, or if the omap_hwmod's class is missing a name; or 0 upon
success.

XXX The data should be copied into bootmem, so the original data
should be marked \__initdata and freed after init.  This would allow
unneeded omap_hwmods to be freed on multi-OMAP configurations.  Note
that the copy process would be relatively complex due to the large number
of substructures.

.. _`_add_link`:

_add_link
=========

.. c:function:: int _add_link(struct omap_hwmod_ocp_if *oi)

    add an interconnect between two IP blocks

    :param struct omap_hwmod_ocp_if \*oi:
        pointer to a struct omap_hwmod_ocp_if record

.. _`_add_link.description`:

Description
-----------

Add struct omap_hwmod_link records connecting the slave IP block
specified in \ ``oi``\ ->slave to \ ``oi``\ .  This code is assumed to run before
preemption or SMP has been enabled, thus avoiding the need for
locking in this code.  Changes to this assumption will require
additional locking.  Returns 0.

.. _`_register_link`:

_register_link
==============

.. c:function:: int _register_link(struct omap_hwmod_ocp_if *oi)

    register a struct omap_hwmod_ocp_if

    :param struct omap_hwmod_ocp_if \*oi:
        struct omap_hwmod_ocp_if \*

.. _`_register_link.description`:

Description
-----------

Registers the omap_hwmod_ocp_if record \ ``oi``\ .  Returns -EEXIST if it
has already been registered; -EINVAL if \ ``oi``\  is NULL or if the
record pointed to by \ ``oi``\  is missing required fields; or 0 upon
success.

XXX The data should be copied into bootmem, so the original data
should be marked \__initdata and freed after init.  This would allow
unneeded omap_hwmods to be freed on multi-OMAP configurations.

.. _`_omap2xxx_3xxx_wait_target_ready`:

_omap2xxx_3xxx_wait_target_ready
================================

.. c:function:: int _omap2xxx_3xxx_wait_target_ready(struct omap_hwmod *oh)

    wait for a module to leave slave idle

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_omap2xxx_3xxx_wait_target_ready.description`:

Description
-----------

Wait for a module \ ``oh``\  to leave slave idle.  Returns 0 if the module
does not have an IDLEST bit or if the module successfully leaves
slave idle; otherwise, pass along the return value of the
appropriate \*\_cm\*\_wait_module_ready() function.

.. _`_omap4_wait_target_ready`:

_omap4_wait_target_ready
========================

.. c:function:: int _omap4_wait_target_ready(struct omap_hwmod *oh)

    wait for a module to leave slave idle

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`_omap4_wait_target_ready.description`:

Description
-----------

Wait for a module \ ``oh``\  to leave slave idle.  Returns 0 if the module
does not have an IDLEST bit or if the module successfully leaves
slave idle; otherwise, pass along the return value of the
appropriate \*\_cm\*\_wait_module_ready() function.

.. _`_omap2_assert_hardreset`:

_omap2_assert_hardreset
=======================

.. c:function:: int _omap2_assert_hardreset(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call OMAP2 PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to assert hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_omap2_assert_hardreset.description`:

Description
-----------

Call \ :c:func:`omap2_prm_assert_hardreset`\  with parameters extracted from
the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .  Only intended for
use as an soc_ops function pointer.  Passes along the return value
from \ :c:func:`omap2_prm_assert_hardreset`\ .  XXX This function is scheduled
for removal when the PRM code is moved into drivers/.

.. _`_omap2_deassert_hardreset`:

_omap2_deassert_hardreset
=========================

.. c:function:: int _omap2_deassert_hardreset(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call OMAP2 PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to deassert hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_omap2_deassert_hardreset.description`:

Description
-----------

Call \ :c:func:`omap2_prm_deassert_hardreset`\  with parameters extracted from
the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .  Only intended for
use as an soc_ops function pointer.  Passes along the return value
from \ :c:func:`omap2_prm_deassert_hardreset`\ .  XXX This function is
scheduled for removal when the PRM code is moved into drivers/.

.. _`_omap2_is_hardreset_asserted`:

_omap2_is_hardreset_asserted
============================

.. c:function:: int _omap2_is_hardreset_asserted(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call OMAP2 PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to test hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_omap2_is_hardreset_asserted.description`:

Description
-----------

Call \ :c:func:`omap2_prm_is_hardreset_asserted`\  with parameters extracted
from the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .  Only
intended for use as an soc_ops function pointer.  Passes along the
return value from \ :c:func:`omap2_prm_is_hardreset_asserted`\ .  XXX This
function is scheduled for removal when the PRM code is moved into
drivers/.

.. _`_omap4_assert_hardreset`:

_omap4_assert_hardreset
=======================

.. c:function:: int _omap4_assert_hardreset(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call OMAP4 PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to assert hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_omap4_assert_hardreset.description`:

Description
-----------

Call \ :c:func:`omap4_prminst_assert_hardreset`\  with parameters extracted
from the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .  Only
intended for use as an soc_ops function pointer.  Passes along the
return value from \ :c:func:`omap4_prminst_assert_hardreset`\ .  XXX This
function is scheduled for removal when the PRM code is moved into
drivers/.

.. _`_omap4_deassert_hardreset`:

_omap4_deassert_hardreset
=========================

.. c:function:: int _omap4_deassert_hardreset(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call OMAP4 PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to deassert hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_omap4_deassert_hardreset.description`:

Description
-----------

Call \ :c:func:`omap4_prminst_deassert_hardreset`\  with parameters extracted
from the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .  Only
intended for use as an soc_ops function pointer.  Passes along the
return value from \ :c:func:`omap4_prminst_deassert_hardreset`\ .  XXX This
function is scheduled for removal when the PRM code is moved into
drivers/.

.. _`_omap4_is_hardreset_asserted`:

_omap4_is_hardreset_asserted
============================

.. c:function:: int _omap4_is_hardreset_asserted(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call OMAP4 PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to test hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_omap4_is_hardreset_asserted.description`:

Description
-----------

Call \ :c:func:`omap4_prminst_is_hardreset_asserted`\  with parameters
extracted from the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .
Only intended for use as an soc_ops function pointer.  Passes along
the return value from \ :c:func:`omap4_prminst_is_hardreset_asserted`\ .  XXX
This function is scheduled for removal when the PRM code is moved
into drivers/.

.. _`_omap4_disable_direct_prcm`:

_omap4_disable_direct_prcm
==========================

.. c:function:: int _omap4_disable_direct_prcm(struct omap_hwmod *oh)

    disable direct PRCM control for hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to disable control for

.. _`_omap4_disable_direct_prcm.description`:

Description
-----------

Disables direct PRCM clkctrl done by hwmod core. Instead, the hwmod
will be using its main_clk to enable/disable the module. Returns
0 if successful.

.. _`_am33xx_deassert_hardreset`:

_am33xx_deassert_hardreset
==========================

.. c:function:: int _am33xx_deassert_hardreset(struct omap_hwmod *oh, struct omap_hwmod_rst_info *ohri)

    call AM33XX PRM hardreset fn with hwmod args

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to deassert hardreset

    :param struct omap_hwmod_rst_info \*ohri:
        hardreset line data

.. _`_am33xx_deassert_hardreset.description`:

Description
-----------

Call \ :c:func:`am33xx_prminst_deassert_hardreset`\  with parameters extracted
from the hwmod \ ``oh``\  and the hardreset line data \ ``ohri``\ .  Only
intended for use as an soc_ops function pointer.  Passes along the
return value from \ :c:func:`am33xx_prminst_deassert_hardreset`\ .  XXX This
function is scheduled for removal when the PRM code is moved into
drivers/.

.. _`omap_hwmod_softreset`:

omap_hwmod_softreset
====================

.. c:function:: int omap_hwmod_softreset(struct omap_hwmod *oh)

    reset a module via SYSCONFIG.SOFTRESET bit

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_softreset.description`:

Description
-----------

This is a public function exposed to drivers. Some drivers may need to do
some settings before and after resetting the device.  Those drivers after
doing the necessary settings could use this function to start a reset by
setting the SYSCONFIG.SOFTRESET bit.

.. _`omap_hwmod_lookup`:

omap_hwmod_lookup
=================

.. c:function:: struct omap_hwmod *omap_hwmod_lookup(const char *name)

    look up a registered omap_hwmod by name

    :param const char \*name:
        name of the omap_hwmod to look up

.. _`omap_hwmod_lookup.description`:

Description
-----------

Given a \ ``name``\  of an omap_hwmod, return a pointer to the registered
struct omap_hwmod \*, or NULL upon error.

.. _`omap_hwmod_for_each`:

omap_hwmod_for_each
===================

.. c:function:: int omap_hwmod_for_each(int (*fn)(struct omap_hwmod *oh, void *data), void *data)

    call function for each registered omap_hwmod

    :param int (\*fn)(struct omap_hwmod \*oh, void \*data):
        pointer to a callback function

    :param void \*data:
        void \* data to pass to callback function

.. _`omap_hwmod_for_each.description`:

Description
-----------

Call \ ``fn``\  for each registered omap_hwmod, passing \ ``data``\  to each
function.  \ ``fn``\  must return 0 for success or any other value for
failure.  If \ ``fn``\  returns non-zero, the iteration across omap_hwmods
will stop and the non-zero return value will be passed to the
caller of \ :c:func:`omap_hwmod_for_each`\ .  \ ``fn``\  is called with
\ :c:func:`omap_hwmod_for_each`\  held.

.. _`omap_hwmod_register_links`:

omap_hwmod_register_links
=========================

.. c:function:: int omap_hwmod_register_links(struct omap_hwmod_ocp_if **ois)

    register an array of hwmod links

    :param struct omap_hwmod_ocp_if \*\*ois:
        pointer to an array of omap_hwmod_ocp_if to register

.. _`omap_hwmod_register_links.description`:

Description
-----------

Intended to be called early in boot before the clock framework is
initialized.  If \ ``ois``\  is not null, will register all omap_hwmods
listed in \ ``ois``\  that are valid for this chip.  Returns -EINVAL if
\ :c:func:`omap_hwmod_init`\  hasn't been called before calling this function,
-ENOMEM if the link memory area can't be allocated, or 0 upon
success.

.. _`_ensure_mpu_hwmod_is_setup`:

_ensure_mpu_hwmod_is_setup
==========================

.. c:function:: void _ensure_mpu_hwmod_is_setup(struct omap_hwmod *oh)

    ensure the MPU SS hwmod is init'ed and set up

    :param struct omap_hwmod \*oh:
        pointer to the hwmod currently being set up (usually not the MPU)

.. _`_ensure_mpu_hwmod_is_setup.description`:

Description
-----------

If the hwmod data corresponding to the MPU subsystem IP block
hasn't been initialized and set up yet, do so now.  This must be
done first since sleep dependencies may be added from other hwmods
to the MPU.  Intended to be called only by omap_hwmod_setup\*().  No
return value.

.. _`omap_hwmod_setup_one`:

omap_hwmod_setup_one
====================

.. c:function:: int omap_hwmod_setup_one(const char *oh_name)

    set up a single hwmod

    :param const char \*oh_name:
        const char \* name of the already-registered hwmod to set up

.. _`omap_hwmod_setup_one.description`:

Description
-----------

Initialize and set up a single hwmod.  Intended to be used for a
small number of early devices, such as the timer IP blocks used for
the scheduler clock.  Must be called after \ :c:func:`omap2_clk_init`\ .
Resolves the struct clk names to struct clk pointers for each
registered omap_hwmod.  Also calls \_setup() on each hwmod.  Returns
-EINVAL upon error or 0 upon success.

.. _`omap_hwmod_setup_earlycon_flags`:

omap_hwmod_setup_earlycon_flags
===============================

.. c:function:: void omap_hwmod_setup_earlycon_flags( void)

    set up flags for early console

    :param  void:
        no arguments

.. _`omap_hwmod_setup_earlycon_flags.description`:

Description
-----------

Enable DEBUG_OMAPUART_FLAGS for uart hwmod that is being used as
early concole so that hwmod core doesn't reset and keep it in idle
that specific uart.

.. _`omap_hwmod_setup_all`:

omap_hwmod_setup_all
====================

.. c:function:: int omap_hwmod_setup_all( void)

    set up all registered IP blocks

    :param  void:
        no arguments

.. _`omap_hwmod_setup_all.description`:

Description
-----------

Initialize and set up all IP blocks registered with the hwmod code.
Must be called after \ :c:func:`omap2_clk_init`\ .  Resolves the struct clk
names to struct clk pointers for each registered omap_hwmod.  Also
calls \_setup() on each hwmod.  Returns 0 upon success.

.. _`omap_hwmod_enable`:

omap_hwmod_enable
=================

.. c:function:: int omap_hwmod_enable(struct omap_hwmod *oh)

    enable an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_enable.description`:

Description
-----------

Enable an omap_hwmod \ ``oh``\ .  Intended to be called by \ :c:func:`omap_device_enable`\ .
Returns -EINVAL on error or passes along the return value from \_enable().

.. _`omap_hwmod_idle`:

omap_hwmod_idle
===============

.. c:function:: int omap_hwmod_idle(struct omap_hwmod *oh)

    idle an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_idle.description`:

Description
-----------

Idle an omap_hwmod \ ``oh``\ .  Intended to be called by \ :c:func:`omap_device_idle`\ .
Returns -EINVAL on error or passes along the return value from \_idle().

.. _`omap_hwmod_shutdown`:

omap_hwmod_shutdown
===================

.. c:function:: int omap_hwmod_shutdown(struct omap_hwmod *oh)

    shutdown an omap_hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_shutdown.description`:

Description
-----------

Shutdown an omap_hwmod \ ``oh``\ .  Intended to be called by
\ :c:func:`omap_device_shutdown`\ .  Returns -EINVAL on error or passes along
the return value from \_shutdown().

.. _`omap_hwmod_count_resources`:

omap_hwmod_count_resources
==========================

.. c:function:: int omap_hwmod_count_resources(struct omap_hwmod *oh, unsigned long flags)

    count number of struct resources needed by hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param unsigned long flags:
        Type of resources to include when counting (IRQ/DMA/MEM)

.. _`omap_hwmod_count_resources.description`:

Description
-----------

Count the number of struct resource array elements necessary to
contain omap_hwmod \ ``oh``\  resources.  Intended to be called by code
that registers omap_devices.  Intended to be used to determine the
size of a dynamically-allocated struct resource array, before
calling \ :c:func:`omap_hwmod_fill_resources`\ .  Returns the number of struct
resource array elements needed.

XXX This code is not optimized.  It could attempt to merge adjacent
resource IDs.

.. _`omap_hwmod_fill_resources`:

omap_hwmod_fill_resources
=========================

.. c:function:: int omap_hwmod_fill_resources(struct omap_hwmod *oh, struct resource *res)

    fill struct resource array with hwmod data

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param struct resource \*res:
        pointer to the first element of an array of struct resource to fill

.. _`omap_hwmod_fill_resources.description`:

Description
-----------

Fill the struct resource array \ ``res``\  with resource data from the
omap_hwmod \ ``oh``\ .  Intended to be called by code that registers
omap_devices.  See also \ :c:func:`omap_hwmod_count_resources`\ .  Returns the
number of array elements filled.

.. _`omap_hwmod_fill_dma_resources`:

omap_hwmod_fill_dma_resources
=============================

.. c:function:: int omap_hwmod_fill_dma_resources(struct omap_hwmod *oh, struct resource *res)

    fill struct resource array with dma data

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param struct resource \*res:
        pointer to the array of struct resource to fill

.. _`omap_hwmod_fill_dma_resources.description`:

Description
-----------

Fill the struct resource array \ ``res``\  with dma resource data from the
omap_hwmod \ ``oh``\ .  Intended to be called by code that registers
omap_devices.  See also \ :c:func:`omap_hwmod_count_resources`\ .  Returns the
number of array elements filled.

.. _`omap_hwmod_get_resource_byname`:

omap_hwmod_get_resource_byname
==============================

.. c:function:: int omap_hwmod_get_resource_byname(struct omap_hwmod *oh, unsigned int type, const char *name, struct resource *rsrc)

    fetch IP block integration data by name

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* to operate on

    :param unsigned int type:
        one of the IORESOURCE\_\* constants from include/linux/ioport.h

    :param const char \*name:
        pointer to the name of the data to fetch (optional)

    :param struct resource \*rsrc:
        pointer to a struct resource, allocated by the caller

.. _`omap_hwmod_get_resource_byname.description`:

Description
-----------

Retrieve MPU IRQ, SDMA request line, or address space start/end
data for the IP block pointed to by \ ``oh``\ .  The data will be filled
into a struct resource record pointed to by \ ``rsrc``\ .  The struct
resource must be allocated by the caller.  When \ ``name``\  is non-null,
the data associated with the matching entry in the IRQ/SDMA/address
space hwmod data arrays will be returned.  If \ ``name``\  is null, the
first array entry will be returned.  Data order is not meaningful
in hwmod data, so callers are strongly encouraged to use a non-null
\ ``name``\  whenever possible to avoid unpredictable effects if hwmod
data is later added that causes data ordering to change.  This
function is only intended for use by OMAP core code.  Device
drivers should not call this function - the appropriate bus-related
data accessor functions should be used instead.  Returns 0 upon
success or a negative error code upon error.

.. _`omap_hwmod_get_pwrdm`:

omap_hwmod_get_pwrdm
====================

.. c:function:: struct powerdomain *omap_hwmod_get_pwrdm(struct omap_hwmod *oh)

    return pointer to this module's main powerdomain

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_get_pwrdm.description`:

Description
-----------

Return the powerdomain pointer associated with the OMAP module
\ ``oh``\ 's main clock.  If \ ``oh``\  does not have a main clk, return the
powerdomain associated with the interface clock associated with the
module's MPU port. (XXX Perhaps this should use the SDMA port
instead?)  Returns NULL on error, or a struct powerdomain \* on
success.

.. _`omap_hwmod_get_mpu_rt_va`:

omap_hwmod_get_mpu_rt_va
========================

.. c:function:: void __iomem *omap_hwmod_get_mpu_rt_va(struct omap_hwmod *oh)

    return the module's base address (for the MPU)

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_get_mpu_rt_va.description`:

Description
-----------

Returns the virtual address corresponding to the beginning of the
module's register target, in the address range that is intended to
be used by the MPU.  Returns the virtual address upon success or NULL
upon error.

.. _`omap_hwmod_enable_wakeup`:

omap_hwmod_enable_wakeup
========================

.. c:function:: int omap_hwmod_enable_wakeup(struct omap_hwmod *oh)

    allow device to wake up the system

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_enable_wakeup.description`:

Description
-----------

Sets the module OCP socket ENAWAKEUP bit to allow the module to
send wakeups to the PRCM, and enable I/O ring wakeup events for
this IP block if it has dynamic mux entries.  Eventually this
should set PRCM wakeup registers to cause the PRCM to receive
wakeup events from the module.  Does not set any wakeup routing
registers beyond this point - if the module is to wake up any other
module or subsystem, that must be set separately.  Called by
omap_device code.  Returns -EINVAL on error or 0 upon success.

.. _`omap_hwmod_disable_wakeup`:

omap_hwmod_disable_wakeup
=========================

.. c:function:: int omap_hwmod_disable_wakeup(struct omap_hwmod *oh)

    prevent device from waking the system

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_disable_wakeup.description`:

Description
-----------

Clears the module OCP socket ENAWAKEUP bit to prevent the module
from sending wakeups to the PRCM, and disable I/O ring wakeup
events for this IP block if it has dynamic mux entries.  Eventually
this should clear PRCM wakeup registers to cause the PRCM to ignore
wakeup events from the module.  Does not set any wakeup routing
registers beyond this point - if the module is to wake up any other
module or subsystem, that must be set separately.  Called by
omap_device code.  Returns -EINVAL on error or 0 upon success.

.. _`omap_hwmod_assert_hardreset`:

omap_hwmod_assert_hardreset
===========================

.. c:function:: int omap_hwmod_assert_hardreset(struct omap_hwmod *oh, const char *name)

    assert the HW reset line of submodules contained in the hwmod module.

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param const char \*name:
        name of the reset line to lookup and assert

.. _`omap_hwmod_assert_hardreset.description`:

Description
-----------

Some IP like dsp, ipu or iva contain processor that require
an HW reset line to be assert / deassert in order to enable fully
the IP.  Returns -EINVAL if \ ``oh``\  is null or if the operation is not
yet supported on this OMAP; otherwise, passes along the return value
from \_assert_hardreset().

.. _`omap_hwmod_deassert_hardreset`:

omap_hwmod_deassert_hardreset
=============================

.. c:function:: int omap_hwmod_deassert_hardreset(struct omap_hwmod *oh, const char *name)

    deassert the HW reset line of submodules contained in the hwmod module.

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param const char \*name:
        name of the reset line to look up and deassert

.. _`omap_hwmod_deassert_hardreset.description`:

Description
-----------

Some IP like dsp, ipu or iva contain processor that require
an HW reset line to be assert / deassert in order to enable fully
the IP.  Returns -EINVAL if \ ``oh``\  is null or if the operation is not
yet supported on this OMAP; otherwise, passes along the return value
from \_deassert_hardreset().

.. _`omap_hwmod_for_each_by_class`:

omap_hwmod_for_each_by_class
============================

.. c:function:: int omap_hwmod_for_each_by_class(const char *classname, int (*fn)(struct omap_hwmod *oh, void *user), void *user)

    call \ ``fn``\  for each hwmod of class \ ``classname``\ 

    :param const char \*classname:
        struct omap_hwmod_class name to search for

    :param int (\*fn)(struct omap_hwmod \*oh, void \*user):
        callback function pointer to call for each hwmod in class \ ``classname``\ 

    :param void \*user:
        arbitrary context data to pass to the callback function

.. _`omap_hwmod_for_each_by_class.description`:

Description
-----------

For each omap_hwmod of class \ ``classname``\ , call \ ``fn``\ .
If the callback function returns something other than
zero, the iterator is terminated, and the callback function's return
value is passed back to the caller.  Returns 0 upon success, -EINVAL
if \ ``classname``\  or \ ``fn``\  are NULL, or passes back the error code from \ ``fn``\ .

.. _`omap_hwmod_set_postsetup_state`:

omap_hwmod_set_postsetup_state
==============================

.. c:function:: int omap_hwmod_set_postsetup_state(struct omap_hwmod *oh, u8 state)

    set the post-_setup() state for this hwmod

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

    :param u8 state:
        state that \_setup() should leave the hwmod in

.. _`omap_hwmod_set_postsetup_state.description`:

Description
-----------

Sets the hwmod state that \ ``oh``\  will enter at the end of \_setup()
(called by omap_hwmod_setup\_\*()).  See also the documentation
for \_setup_postsetup(), above.  Returns 0 upon success or
-EINVAL if there is a problem with the arguments or if the hwmod is
in the wrong state.

.. _`omap_hwmod_get_context_loss_count`:

omap_hwmod_get_context_loss_count
=================================

.. c:function:: int omap_hwmod_get_context_loss_count(struct omap_hwmod *oh)

    get lost context count

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_get_context_loss_count.description`:

Description
-----------

Returns the context loss count of associated \ ``oh``\ 
upon success, or zero if no context loss data is available.

On OMAP4, this queries the per-hwmod context loss register,
assuming one exists.  If not, or on OMAP2/3, this queries the
enclosing powerdomain context loss count.

.. _`omap_hwmod_init`:

omap_hwmod_init
===============

.. c:function:: void omap_hwmod_init( void)

    initialize the hwmod code

    :param  void:
        no arguments

.. _`omap_hwmod_init.description`:

Description
-----------

Sets up some function pointers needed by the hwmod code to operate on the
currently-booted SoC.  Intended to be called once during kernel init
before any hwmods are registered.  No return value.

.. _`omap_hwmod_get_main_clk`:

omap_hwmod_get_main_clk
=======================

.. c:function:: const char *omap_hwmod_get_main_clk(struct omap_hwmod *oh)

    get pointer to main clock name

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \*

.. _`omap_hwmod_get_main_clk.description`:

Description
-----------

Returns the main clock name assocated with \ ``oh``\  upon success,
or NULL if \ ``oh``\  is NULL.

.. This file was automatic generated / don't edit.

