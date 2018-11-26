.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/clk.h

.. _`tegra_clk_sync_source`:

struct tegra_clk_sync_source
============================

.. c:type:: struct tegra_clk_sync_source

    external clock source from codec

.. _`tegra_clk_sync_source.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_sync_source {
        struct clk_hw hw;
        unsigned long rate;
        unsigned long max_rate;
    }

.. _`tegra_clk_sync_source.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

rate
    input frequency from source

max_rate
    max rate allowed

.. _`tegra_clk_frac_div`:

struct tegra_clk_frac_div
=========================

.. c:type:: struct tegra_clk_frac_div

    fractional divider clock

.. _`tegra_clk_frac_div.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_frac_div {
        struct clk_hw hw;
        void __iomem *reg;
        u8 flags;
        u8 shift;
        u8 width;
        u8 frac_width;
        spinlock_t *lock;
    }

.. _`tegra_clk_frac_div.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing divider

flags
    hardware-specific flags

shift
    shift to the divider bit field

width
    width of the divider bit field

frac_width
    width of the fractional bit field

lock
    register lock

.. _`tegra_clk_frac_div.flags`:

Flags
-----

TEGRA_DIVIDER_ROUND_UP - This flags indicates to round up the divider value.
TEGRA_DIVIDER_FIXED - Fixed rate PLL dividers has addition override bit, this
flag indicates that this divider is for fixed rate PLL.
TEGRA_DIVIDER_INT - Some modules can not cope with the duty cycle when
fraction bit is set. This flags indicates to calculate divider for which
fracton bit will be zero.
TEGRA_DIVIDER_UART - UART module divider has additional enable bit which is
set when divider value is not 0. This flags indicates that the divider
is for UART module.

.. _`tegra_clk_pll_freq_table`:

struct tegra_clk_pll_freq_table
===============================

.. c:type:: struct tegra_clk_pll_freq_table

    PLL frequecy table

.. _`tegra_clk_pll_freq_table.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_pll_freq_table {
        unsigned long input_rate;
        unsigned long output_rate;
        u32 n;
        u32 m;
        u8 p;
        u8 cpcon;
        u16 sdm_data;
    }

.. _`tegra_clk_pll_freq_table.members`:

Members
-------

input_rate
    input rate from source

output_rate
    output rate from PLL for the input rate

n
    feedback divider

m
    input divider

p
    post divider

cpcon
    charge pump current

sdm_data
    fraction divider setting (0 = disabled)

.. _`pdiv_map`:

struct pdiv_map
===============

.. c:type:: struct pdiv_map

    map post divider to hw value

.. _`pdiv_map.definition`:

Definition
----------

.. code-block:: c

    struct pdiv_map {
        u8 pdiv;
        u8 hw_val;
    }

.. _`pdiv_map.members`:

Members
-------

pdiv
    post divider

hw_val
    value to be written to the PLL hw

.. _`div_nmp`:

struct div_nmp
==============

.. c:type:: struct div_nmp

    offset and width of m,n and p fields

.. _`div_nmp.definition`:

Definition
----------

.. code-block:: c

    struct div_nmp {
        u8 divn_shift;
        u8 divn_width;
        u8 divm_shift;
        u8 divm_width;
        u8 divp_shift;
        u8 divp_width;
        u8 override_divn_shift;
        u8 override_divm_shift;
        u8 override_divp_shift;
    }

.. _`div_nmp.members`:

Members
-------

divn_shift
    shift to the feedback divider bit field

divn_width
    width of the feedback divider bit field

divm_shift
    shift to the input divider bit field

divm_width
    width of the input divider bit field

divp_shift
    shift to the post divider bit field

divp_width
    width of the post divider bit field

override_divn_shift
    shift to the feedback divider bitfield in override reg

override_divm_shift
    shift to the input divider bitfield in override reg

override_divp_shift
    shift to the post divider bitfield in override reg

.. _`tegra_clk_pll_params`:

struct tegra_clk_pll_params
===========================

.. c:type:: struct tegra_clk_pll_params

    PLL parameters

.. _`tegra_clk_pll_params.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_pll_params {
        unsigned long input_min;
        unsigned long input_max;
        unsigned long cf_min;
        unsigned long cf_max;
        unsigned long vco_min;
        unsigned long vco_max;
        u32 base_reg;
        u32 misc_reg;
        u32 lock_reg;
        u32 lock_mask;
        u32 lock_enable_bit_idx;
        u32 iddq_reg;
        u32 iddq_bit_idx;
        u32 reset_reg;
        u32 reset_bit_idx;
        u32 sdm_din_reg;
        u32 sdm_din_mask;
        u32 sdm_ctrl_reg;
        u32 sdm_ctrl_en_mask;
        u32 ssc_ctrl_reg;
        u32 ssc_ctrl_en_mask;
        u32 aux_reg;
        u32 dyn_ramp_reg;
        u32 ext_misc_reg[MAX_PLL_MISC_REG_COUNT];
        u32 pmc_divnm_reg;
        u32 pmc_divp_reg;
        u32 flags;
        int stepa_shift;
        int stepb_shift;
        int lock_delay;
        int max_p;
        bool defaults_set;
        const struct pdiv_map *pdiv_tohw;
        struct div_nmp *div_nmp;
        struct tegra_clk_pll_freq_table *freq_table;
        unsigned long fixed_rate;
        u16 mdiv_default;
        u32 (*round_p_to_pdiv)(u32 p, u32 *pdiv);
        void (*set_gain)(struct tegra_clk_pll_freq_table *cfg);
        int (*calc_rate)(struct clk_hw *hw,struct tegra_clk_pll_freq_table *cfg, unsigned long rate, unsigned long parent_rate);
        unsigned long (*adjust_vco)(struct tegra_clk_pll_params *pll_params, unsigned long parent_rate);
        void (*set_defaults)(struct tegra_clk_pll *pll);
        int (*dyn_ramp)(struct tegra_clk_pll *pll, struct tegra_clk_pll_freq_table *cfg);
    }

.. _`tegra_clk_pll_params.members`:

Members
-------

input_min
    Minimum input frequency

input_max
    Maximum input frequency

cf_min
    Minimum comparison frequency

cf_max
    Maximum comparison frequency

vco_min
    Minimum VCO frequency

vco_max
    Maximum VCO frequency

base_reg
    PLL base reg offset

misc_reg
    PLL misc reg offset

lock_reg
    PLL lock reg offset

lock_mask
    Bitmask for PLL lock status

lock_enable_bit_idx
    Bit index to enable PLL lock

iddq_reg
    PLL IDDQ register offset

iddq_bit_idx
    Bit index to enable PLL IDDQ

reset_reg
    Register offset of where RESET bit is

reset_bit_idx
    Shift of reset bit in reset_reg

sdm_din_reg
    Register offset where SDM settings are

sdm_din_mask
    Mask of SDM divider bits

sdm_ctrl_reg
    Register offset where SDM enable is

sdm_ctrl_en_mask
    Mask of SDM enable bit

ssc_ctrl_reg
    Register offset where SSC settings are

ssc_ctrl_en_mask
    Mask of SSC enable bit

aux_reg
    AUX register offset

dyn_ramp_reg
    Dynamic ramp control register offset

ext_misc_reg
    Miscellaneous control register offsets

pmc_divnm_reg
    n, m divider PMC override register offset (PLLM)

pmc_divp_reg
    p divider PMC override register offset (PLLM)

flags
    PLL flags

stepa_shift
    Dynamic ramp step A field shift

stepb_shift
    Dynamic ramp step B field shift

lock_delay
    Delay in us if PLL lock is not used

max_p
    maximum value for the p divider

defaults_set
    Boolean signaling all reg defaults for PLL set.

pdiv_tohw
    mapping of p divider to register values

div_nmp
    offsets and widths on n, m and p fields

freq_table
    array of frequencies supported by PLL

fixed_rate
    PLL rate if it is fixed

mdiv_default
    Default value for fixed mdiv for this PLL

round_p_to_pdiv
    Callback used to round p to the closed pdiv

set_gain
    Callback to adjust N div for SDM enabled
    PLL's based on fractional divider value.

calc_rate
    Callback used to change how out of table
    rates (dividers and multipler) are calculated.

adjust_vco
    Callback to adjust the programming range of the
    divider range (if SDM is present)

set_defaults
    Callback which will try to initialize PLL
    registers to sane default values. This is first
    tried during PLL registration, but if the PLL
    is already enabled, it will be done the first
    time the rate is changed while the PLL is
    disabled.

dyn_ramp
    Callback which can be used to define a custom
    dynamic ramp function for a given PLL.

.. _`tegra_clk_pll_params.flags`:

Flags
-----

TEGRA_PLL_USE_LOCK - This flag indicated to use lock bits for
PLL locking. If not set it will use lock_delay value to wait.
TEGRA_PLL_HAS_CPCON - This flag indicates that CPCON value needs
to be programmed to change output frequency of the PLL.
TEGRA_PLL_SET_LFCON - This flag indicates that LFCON value needs
to be programmed to change output frequency of the PLL.
TEGRA_PLL_SET_DCCON - This flag indicates that DCCON value needs
to be programmed to change output frequency of the PLL.
TEGRA_PLLU - PLLU has inverted post divider. This flags indicated
that it is PLLU and invert post divider value.
TEGRA_PLLM - PLLM has additional override settings in PMC. This
flag indicates that it is PLLM and use override settings.
TEGRA_PLL_FIXED - We are not supposed to change output frequency
of some plls.
TEGRA_PLLE_CONFIGURE - Configure PLLE when enabling.
TEGRA_PLL_LOCK_MISC - Lock bit is in the misc register instead of the
base register.
TEGRA_PLL_BYPASS - PLL has bypass bit
TEGRA_PLL_HAS_LOCK_ENABLE - PLL has bit to enable lock monitoring
TEGRA_MDIV_NEW - Switch to new method for calculating fixed mdiv
it may be more accurate (especially if SDM present)
TEGRA_PLLMB - PLLMB has should be treated similar to PLLM. This
flag indicated that it is PLLMB.
TEGRA_PLL_VCO_OUT - Used to indicate that the PLL has a VCO output

.. _`tegra_clk_pll`:

struct tegra_clk_pll
====================

.. c:type:: struct tegra_clk_pll

    Tegra PLL clock

.. _`tegra_clk_pll.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_pll {
        struct clk_hw hw;
        void __iomem *clk_base;
        void __iomem *pmc;
        spinlock_t *lock;
        struct tegra_clk_pll_params *params;
    }

.. _`tegra_clk_pll.members`:

Members
-------

hw
    handle between common and hardware-specifix interfaces

clk_base
    address of CAR controller

pmc
    address of PMC, required to read override bits

lock
    register lock

params
    PLL parameters

.. _`tegra_audio_clk_info`:

struct tegra_audio_clk_info
===========================

.. c:type:: struct tegra_audio_clk_info

    Tegra Audio Clk Information

.. _`tegra_audio_clk_info.definition`:

Definition
----------

.. code-block:: c

    struct tegra_audio_clk_info {
        char *name;
        struct tegra_clk_pll_params *pll_params;
        int clk_id;
        char *parent;
    }

.. _`tegra_audio_clk_info.members`:

Members
-------

name
    name for the audio pll

pll_params
    pll_params for audio pll

clk_id
    clk_ids for the audio pll

parent
    name of the parent of the audio pll

.. _`tegra_clk_pll_out`:

struct tegra_clk_pll_out
========================

.. c:type:: struct tegra_clk_pll_out

    PLL divider down clock

.. _`tegra_clk_pll_out.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_pll_out {
        struct clk_hw hw;
        void __iomem *reg;
        u8 enb_bit_idx;
        u8 rst_bit_idx;
        spinlock_t *lock;
        u8 flags;
    }

.. _`tegra_clk_pll_out.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing the PLL divider

enb_bit_idx
    bit to enable/disable PLL divider

rst_bit_idx
    bit to reset PLL divider

lock
    register lock

flags
    hardware-specific flags

.. _`tegra_clk_periph_regs`:

struct tegra_clk_periph_regs
============================

.. c:type:: struct tegra_clk_periph_regs

    Registers controlling peripheral clock

.. _`tegra_clk_periph_regs.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_periph_regs {
        u32 enb_reg;
        u32 enb_set_reg;
        u32 enb_clr_reg;
        u32 rst_reg;
        u32 rst_set_reg;
        u32 rst_clr_reg;
    }

.. _`tegra_clk_periph_regs.members`:

Members
-------

enb_reg
    read the enable status

enb_set_reg
    write 1 to enable clock

enb_clr_reg
    write 1 to disable clock

rst_reg
    read the reset status

rst_set_reg
    write 1 to assert the reset of peripheral

rst_clr_reg
    write 1 to deassert the reset of peripheral

.. _`tegra_clk_periph_gate`:

struct tegra_clk_periph_gate
============================

.. c:type:: struct tegra_clk_periph_gate

    peripheral gate clock

.. _`tegra_clk_periph_gate.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_periph_gate {
        u32 magic;
        struct clk_hw hw;
        void __iomem *clk_base;
        u8 flags;
        int clk_num;
        int *enable_refcnt;
        const struct tegra_clk_periph_regs *regs;
    }

.. _`tegra_clk_periph_gate.members`:

Members
-------

magic
    magic number to validate type

hw
    handle between common and hardware-specific interfaces

clk_base
    address of CAR controller

flags
    hardware-specific flags

clk_num
    Clock number

enable_refcnt
    array to maintain reference count of the clock

regs
    Registers to control the peripheral

.. _`tegra_clk_periph_gate.flags`:

Flags
-----

TEGRA_PERIPH_NO_RESET - This flag indicates that reset is not allowed
for this module.
TEGRA_PERIPH_MANUAL_RESET - This flag indicates not to reset module
after clock enable and driver for the module is responsible for
doing reset.
TEGRA_PERIPH_ON_APB - If peripheral is in the APB bus then read the
bus to flush the write operation in apb bus. This flag indicates
that this peripheral is in apb bus.
TEGRA_PERIPH_WAR_1005168 - Apply workaround for Tegra114 MSENC bug

.. _`tegra_clk_periph`:

struct tegra_clk_periph
=======================

.. c:type:: struct tegra_clk_periph

    periph - peripheral clock

.. _`tegra_clk_periph.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_periph {
        u32 magic;
        struct clk_hw hw;
        struct clk_mux mux;
        struct tegra_clk_frac_div divider;
        struct tegra_clk_periph_gate gate;
        const struct clk_ops *mux_ops;
        const struct clk_ops *div_ops;
        const struct clk_ops *gate_ops;
    }

.. _`tegra_clk_periph.members`:

Members
-------

magic
    magic number to validate type

hw
    handle between common and hardware-specific interfaces

mux
    mux clock

divider
    divider clock

gate
    gate clock

mux_ops
    mux clock ops

div_ops
    divider clock ops

gate_ops
    gate clock ops

.. _`tegra_clk_super_mux`:

struct tegra_clk_super_mux
==========================

.. c:type:: struct tegra_clk_super_mux

    super clock

.. _`tegra_clk_super_mux.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_super_mux {
        struct clk_hw hw;
        void __iomem *reg;
        struct tegra_clk_frac_div frac_div;
        const struct clk_ops *div_ops;
        u8 width;
        u8 flags;
        u8 div2_index;
        u8 pllx_index;
        spinlock_t *lock;
    }

.. _`tegra_clk_super_mux.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register controlling multiplexer

frac_div
    *undescribed*

div_ops
    *undescribed*

width
    width of the multiplexer bit field

flags
    hardware-specific flags

div2_index
    bit controlling divide-by-2

pllx_index
    PLLX index in the parent list

lock
    register lock

.. _`tegra_clk_super_mux.flags`:

Flags
-----

TEGRA_DIVIDER_2 - LP cluster has additional divider. This flag indicates
that this is LP cluster clock.

.. _`tegra_sdmmc_mux`:

struct tegra_sdmmc_mux
======================

.. c:type:: struct tegra_sdmmc_mux

    switch divider with Low Jitter inputs for SDMMC

.. _`tegra_sdmmc_mux.definition`:

Definition
----------

.. code-block:: c

    struct tegra_sdmmc_mux {
        struct clk_hw hw;
        void __iomem *reg;
        spinlock_t *lock;
        const struct clk_ops *gate_ops;
        struct tegra_clk_periph_gate gate;
        u8 div_flags;
    }

.. _`tegra_sdmmc_mux.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register controlling mux and divider

lock
    optional register lock

gate_ops
    gate clock ops

gate
    gate clock

div_flags
    *undescribed*

.. _`tegra_clk_init_table`:

struct tegra_clk_init_table
===========================

.. c:type:: struct tegra_clk_init_table

    clock initialization table

.. _`tegra_clk_init_table.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_init_table {
        unsigned int clk_id;
        unsigned int parent_id;
        unsigned long rate;
        int state;
    }

.. _`tegra_clk_init_table.members`:

Members
-------

clk_id
    clock id as mentioned in device tree bindings

parent_id
    parent clock id as mentioned in device tree bindings

rate
    rate to set

state
    enable/disable

.. _`tegra_clk_duplicate`:

struct tegra_clk_duplicate
==========================

.. c:type:: struct tegra_clk_duplicate

    duplicate clocks

.. _`tegra_clk_duplicate.definition`:

Definition
----------

.. code-block:: c

    struct tegra_clk_duplicate {
        int clk_id;
        struct clk_lookup lookup;
    }

.. _`tegra_clk_duplicate.members`:

Members
-------

clk_id
    clock id as mentioned in device tree bindings

lookup
    duplicate lookup entry for the clock

.. This file was automatic generated / don't edit.

