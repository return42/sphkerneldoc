.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_hwmod.h

.. _`omap_hwmod_rst_info`:

struct omap_hwmod_rst_info
==========================

.. c:type:: struct omap_hwmod_rst_info

    IPs reset lines use by hwmod

.. _`omap_hwmod_rst_info.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_rst_info {
        const char *name;
        u8 rst_shift;
        u8 st_shift;
    }

.. _`omap_hwmod_rst_info.members`:

Members
-------

name
    name of the reset line (module local name)

rst_shift
    Offset of the reset bit

st_shift
    Offset of the reset status bit (OMAP2/3 only)

.. _`omap_hwmod_rst_info.description`:

Description
-----------

@name should be something short, e.g., "cpu0" or "rst". It is defined
locally to the hwmod.

.. _`omap_hwmod_opt_clk`:

struct omap_hwmod_opt_clk
=========================

.. c:type:: struct omap_hwmod_opt_clk

    optional clocks used by this hwmod

.. _`omap_hwmod_opt_clk.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_opt_clk {
        const char *role;
        const char *clk;
        struct clk *_clk;
    }

.. _`omap_hwmod_opt_clk.members`:

Members
-------

role
    "sys", "32k", "tv", etc -- for use in \ :c:func:`clk_get`\ 

clk
    opt clock: OMAP clock name

_clk
    pointer to the struct clk (filled in at runtime)

.. _`omap_hwmod_opt_clk.description`:

Description
-----------

The module's interface clock and main functional clock should not
be added as optional clocks.

.. _`omap_hwmod_omap2_firewall`:

struct omap_hwmod_omap2_firewall
================================

.. c:type:: struct omap_hwmod_omap2_firewall

    OMAP2/3 device firewall data

.. _`omap_hwmod_omap2_firewall.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_omap2_firewall {
        u8 l3_perm_bit;
        u8 l4_fw_region;
        u8 l4_prot_group;
        u8 flags;
    }

.. _`omap_hwmod_omap2_firewall.members`:

Members
-------

l3_perm_bit
    bit shift for L3_PM\_\*\_PERMISSION\_\*

l4_fw_region
    L4 firewall region ID

l4_prot_group
    L4 protection group ID

flags
    (see omap_hwmod_omap2_firewall.flags macros above)

.. _`omap_hwmod_ocp_if`:

struct omap_hwmod_ocp_if
========================

.. c:type:: struct omap_hwmod_ocp_if

    OCP interface data

.. _`omap_hwmod_ocp_if.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_ocp_if {
        struct omap_hwmod *master;
        struct omap_hwmod *slave;
        struct omap_hwmod_addr_space *addr;
        const char *clk;
        struct clk *_clk;
        struct list_head node;
        union {
            struct omap_hwmod_omap2_firewall omap2;
        } fw;
        u8 width;
        u8 user;
        u8 flags;
        u8 _int_flags;
    }

.. _`omap_hwmod_ocp_if.members`:

Members
-------

master
    struct omap_hwmod that initiates OCP transactions on this link

slave
    struct omap_hwmod that responds to OCP transactions on this link

addr
    address space associated with this link

clk
    interface clock: OMAP clock name

_clk
    pointer to the interface struct clk (filled in at runtime)

node
    *undescribed*

fw
    interface firewall data

width
    OCP data width

user
    initiators using this interface (see OCP_USER\_\* macros above)

flags
    OCP interface flags (see OCPIF\_\* macros above)

_int_flags
    internal flags (see \_OCPIF_INT_FLAGS\* macros above)

.. _`omap_hwmod_ocp_if.description`:

Description
-----------

It may also be useful to add a tag_cnt field for OCP2.x devices.

Parameter names beginning with an underscore are managed internally by
the omap_hwmod code and should not be set during initialization.

.. _`omap_hwmod_class_sysconfig`:

struct omap_hwmod_class_sysconfig
=================================

.. c:type:: struct omap_hwmod_class_sysconfig

    hwmod class OCP_SYS\* data

.. _`omap_hwmod_class_sysconfig.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_class_sysconfig {
        u32 rev_offs;
        u32 sysc_offs;
        u32 syss_offs;
        u16 sysc_flags;
        struct sysc_regbits *sysc_fields;
        u8 srst_udelay;
        u8 idlemodes;
    }

.. _`omap_hwmod_class_sysconfig.members`:

Members
-------

rev_offs
    IP block revision register offset (from module base addr)

sysc_offs
    OCP_SYSCONFIG register offset (from module base addr)

syss_offs
    OCP_SYSSTATUS register offset (from module base addr)

sysc_flags
    SYS{C,S}_HAS\* flags indicating SYSCONFIG bits supported

sysc_fields
    structure containing the offset positions of various bits in
    SYSCONFIG register. This can be populated using omap_hwmod_sysc_type1 or
    omap_hwmod_sysc_type2 defined in omap_hwmod_common_data.c depending on
    whether the device ip is compliant with the original PRCM protocol
    defined for OMAP2420 or the new PRCM protocol for new OMAP4 IPs.
    If the device follows a different scheme for the sysconfig register ,
    then this field has to be populated with the correct offset structure.

srst_udelay
    Delay needed after doing a softreset in usecs

idlemodes
    One or more of {SIDLE,MSTANDBY}_{OFF,FORCE,SMART}

.. _`omap_hwmod_class_sysconfig.description`:

Description
-----------

@clockact describes to the module which clocks are likely to be
disabled when the PRCM issues its idle request to the module.  Some
modules have separate clockdomains for the interface clock and main
functional clock, and can check whether they should acknowledge the
idle request based on the internal module functionality that has
been associated with the clocks marked in \ ``clockact``\ .  This field is
only used if HWMOD_SET_DEFAULT_CLOCKACT is set (see below)

.. _`omap_hwmod_omap2_prcm`:

struct omap_hwmod_omap2_prcm
============================

.. c:type:: struct omap_hwmod_omap2_prcm

    OMAP2/3-specific PRCM data

.. _`omap_hwmod_omap2_prcm.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_omap2_prcm {
        s16 module_offs;
        u8 idlest_reg_id;
        u8 idlest_idle_bit;
    }

.. _`omap_hwmod_omap2_prcm.members`:

Members
-------

module_offs
    PRCM submodule offset from the start of the PRM/CM

idlest_reg_id
    IDLEST register ID (e.g., 3 for CM_IDLEST3)

idlest_idle_bit
    register bit shift for CM_IDLEST slave idle bit

.. _`omap_hwmod_omap2_prcm.description`:

Description
-----------

@prcm_reg_id and \ ``module_bit``\  are specific to the AUTOIDLE, WKST,
WKEN, GRPSEL registers.  In an ideal world, no extra information
would be needed for IDLEST information, but alas, there are some
exceptions, so \ ``idlest_reg_id``\ , \ ``idlest_idle_bit``\ , \ ``idlest_stdby_bit``\ 
are needed for the IDLEST registers (c.f. 2430 I2CHS, 3430 USBHOST)

.. _`omap_hwmod_omap4_prcm`:

struct omap_hwmod_omap4_prcm
============================

.. c:type:: struct omap_hwmod_omap4_prcm

    OMAP4-specific PRCM data

.. _`omap_hwmod_omap4_prcm.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_omap4_prcm {
        u16 clkctrl_offs;
        u16 rstctrl_offs;
        u16 rstst_offs;
        u16 context_offs;
        u32 lostcontext_mask;
        u8 submodule_wkdep_bit;
        u8 modulemode;
        u8 flags;
        int context_lost_counter;
    }

.. _`omap_hwmod_omap4_prcm.members`:

Members
-------

clkctrl_offs
    offset of the PRCM clock control register

rstctrl_offs
    offset of the XXX_RSTCTRL register located in the PRM

rstst_offs
    *undescribed*

context_offs
    offset of the RM\_\*\_CONTEXT register

lostcontext_mask
    bitmask for selecting bits from RM\_\*\_CONTEXT register

submodule_wkdep_bit
    bit shift of the WKDEP range

modulemode
    allowable modulemodes

flags
    PRCM register capabilities for this IP block

context_lost_counter
    Count of module level context lost

.. _`omap_hwmod_omap4_prcm.description`:

Description
-----------

If \ ``lostcontext_mask``\  is not defined, context loss check code uses
whole register without masking. \ ``lostcontext_mask``\  should only be
defined in cases where \ ``context_offs``\  register is shared by two or
more hwmods.

.. _`omap_hwmod_class`:

struct omap_hwmod_class
=======================

.. c:type:: struct omap_hwmod_class

    the type of an IP block

.. _`omap_hwmod_class.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod_class {
        const char *name;
        struct omap_hwmod_class_sysconfig *sysc;
        u32 rev;
        int (*pre_shutdown)(struct omap_hwmod *oh);
        int (*reset)(struct omap_hwmod *oh);
        int (*enable_preprogram)(struct omap_hwmod *oh);
        void (*lock)(struct omap_hwmod *oh);
        void (*unlock)(struct omap_hwmod *oh);
    }

.. _`omap_hwmod_class.members`:

Members
-------

name
    name of the hwmod_class

sysc
    device SYSCONFIG/SYSSTATUS register data

rev
    revision of the IP class

pre_shutdown
    ptr to fn to be executed immediately prior to device shutdown

reset
    ptr to fn to be executed in place of the standard hwmod reset fn

enable_preprogram
    ptr to fn to be executed during device enable

lock
    ptr to fn to be executed to lock IP registers

unlock
    ptr to fn to be executed to unlock IP registers

.. _`omap_hwmod_class.description`:

Description
-----------

Represent the class of a OMAP hardware "modules" (e.g. timer,
smartreflex, gpio, uart...)

\ ``pre_shutdown``\  is a function that will be run immediately before
hwmod clocks are disabled, etc.  It is intended for use for hwmods
like the MPU watchdog, which cannot be disabled with the standard
\ :c:func:`omap_hwmod_shutdown`\ .  The function should return 0 upon success,
or some negative error upon failure.  Returning an error will cause
\ :c:func:`omap_hwmod_shutdown`\  to abort the device shutdown and return an
error.

If \ ``reset``\  is defined, then the function it points to will be
executed in place of the standard hwmod \_reset() code in
mach-omap2/omap_hwmod.c.  This is needed for IP blocks which have
unusual reset sequences - usually processor IP blocks like the IVA.

.. _`omap_hwmod`:

struct omap_hwmod
=================

.. c:type:: struct omap_hwmod

    integration data for OMAP hardware "modules" (IP blocks)

.. _`omap_hwmod.definition`:

Definition
----------

.. code-block:: c

    struct omap_hwmod {
        const char *name;
        struct omap_hwmod_class *class;
        struct omap_device *od;
        struct omap_hwmod_rst_info *rst_lines;
        union {
            struct omap_hwmod_omap2_prcm omap2;
            struct omap_hwmod_omap4_prcm omap4;
        } prcm;
        const char *main_clk;
        struct clk *_clk;
        struct omap_hwmod_opt_clk *opt_clks;
        const char *clkdm_name;
        struct clockdomain *clkdm;
        struct list_head slave_ports;
        void *dev_attr;
        u32 _sysc_cache;
        void __iomem *_mpu_rt_va;
        spinlock_t _lock;
        struct lock_class_key hwmod_key;
        struct list_head node;
        struct omap_hwmod_ocp_if *_mpu_port;
        u32 flags;
        u8 mpu_rt_idx;
        u8 response_lat;
        u8 rst_lines_cnt;
        u8 opt_clks_cnt;
        u8 slaves_cnt;
        u8 hwmods_cnt;
        u8 _int_flags;
        u8 _state;
        u8 _postsetup_state;
        struct omap_hwmod *parent_hwmod;
    }

.. _`omap_hwmod.members`:

Members
-------

name
    name of the hwmod

class
    struct omap_hwmod_class \* to the class of this hwmod

od
    struct omap_device currently associated with this hwmod (internal use)

rst_lines
    *undescribed*

prcm
    PRCM data pertaining to this hwmod

main_clk
    main clock: OMAP clock name

_clk
    pointer to the main struct clk (filled in at runtime)

opt_clks
    other device clocks that drivers can request (0..\*)

clkdm_name
    *undescribed*

clkdm
    *undescribed*

slave_ports
    *undescribed*

dev_attr
    arbitrary device attributes that can be passed to the driver

_sysc_cache
    internal-use hwmod flags

_mpu_rt_va
    cached register target start address (internal use)

_lock
    spinlock serializing operations on this hwmod

hwmod_key
    *undescribed*

node
    list node for hwmod list (internal use)

_mpu_port
    cached MPU register target slave (internal use)

flags
    hwmod flags (documented below)

mpu_rt_idx
    index of device address space for register target (for DT boot)

response_lat
    device OCP response latency (in interface clock cycles)

rst_lines_cnt
    *undescribed*

opt_clks_cnt
    number of \ ``opt_clks``\ 

slaves_cnt
    number of \ ``slave``\  entries

hwmods_cnt
    *undescribed*

_int_flags
    internal-use hwmod flags

_state
    internal-use hwmod state

_postsetup_state
    internal-use state to leave the hwmod in after \_setup()

parent_hwmod
    (temporary) a pointer to the hierarchical parent of this hwmod

.. _`omap_hwmod.description`:

Description
-----------

@main_clk refers to this module's "main clock," which for our
purposes is defined as "the functional clock needed for register
accesses to complete."  Modules may not have a main clock if the
interface clock also serves as a main clock.

Parameter names beginning with an underscore are managed internally by
the omap_hwmod code and should not be set during initialization.

\ ``masters``\  and \ ``slaves``\  are now deprecated.

\ ``parent_hwmod``\  is temporary; there should be no need for it, as this
information should already be expressed in the OCP interface
structures.  \ ``parent_hwmod``\  is present as a workaround until we improve
handling for hwmods with multiple parents (e.g., OMAP4+ DSS with
multiple register targets across different interconnects).

.. This file was automatic generated / don't edit.

