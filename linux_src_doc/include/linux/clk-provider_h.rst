.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clk-provider.h

.. _`clk_rate_request`:

struct clk_rate_request
=======================

.. c:type:: struct clk_rate_request

    Structure encoding the clk constraints that a clock user might require.

.. _`clk_rate_request.definition`:

Definition
----------

.. code-block:: c

    struct clk_rate_request {
        unsigned long rate;
        unsigned long min_rate;
        unsigned long max_rate;
        unsigned long best_parent_rate;
        struct clk_hw *best_parent_hw;
    }

.. _`clk_rate_request.members`:

Members
-------

rate
    Requested clock rate. This field will be adjusted by
    clock drivers according to hardware capabilities.

min_rate
    Minimum rate imposed by clk users.

max_rate
    Maximum rate imposed by clk users.

best_parent_rate
    The best parent rate a parent can provide to fulfill the
    requested constraints.

best_parent_hw
    The most appropriate parent clock that fulfills the
    requested constraints.

.. _`clk_ops`:

struct clk_ops
==============

.. c:type:: struct clk_ops

    Callback operations for hardware clocks; these are to be provided by the clock implementation, and will be called by drivers through the clk\_\* api.

.. _`clk_ops.definition`:

Definition
----------

.. code-block:: c

    struct clk_ops {
        int (*prepare)(struct clk_hw *hw);
        void (*unprepare)(struct clk_hw *hw);
        int (*is_prepared)(struct clk_hw *hw);
        void (*unprepare_unused)(struct clk_hw *hw);
        int (*enable)(struct clk_hw *hw);
        void (*disable)(struct clk_hw *hw);
        int (*is_enabled)(struct clk_hw *hw);
        void (*disable_unused)(struct clk_hw *hw);
        unsigned long (*recalc_rate)(struct clk_hw *hw, unsigned long parent_rate);
        long (*round_rate)(struct clk_hw *hw, unsigned long rate, unsigned long *parent_rate);
        int (*determine_rate)(struct clk_hw *hw, struct clk_rate_request *req);
        int (*set_parent)(struct clk_hw *hw, u8 index);
        u8 (*get_parent)(struct clk_hw *hw);
        int (*set_rate)(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate);
        int (*set_rate_and_parent)(struct clk_hw *hw,unsigned long rate, unsigned long parent_rate, u8 index);
        unsigned long (*recalc_accuracy)(struct clk_hw *hw, unsigned long parent_accuracy);
        int (*get_phase)(struct clk_hw *hw);
        int (*set_phase)(struct clk_hw *hw, int degrees);
        void (*init)(struct clk_hw *hw);
        int (*debug_init)(struct clk_hw *hw, struct dentry *dentry);
    }

.. _`clk_ops.members`:

Members
-------

prepare
    Prepare the clock for enabling. This must not return until
    the clock is fully prepared, and it's safe to call clk_enable.
    This callback is intended to allow clock implementations to
    do any initialisation that may sleep. Called with
    prepare_lock held.

unprepare
    Release the clock from its prepared state. This will typically
    undo any work done in the \ ``prepare``\  callback. Called with
    prepare_lock held.

is_prepared
    Queries the hardware to determine if the clock is prepared.
    This function is allowed to sleep. Optional, if this op is not
    set then the prepare count will be used.

unprepare_unused
    Unprepare the clock atomically.  Only called from
    clk_disable_unused for prepare clocks with special needs.
    Called with prepare mutex held. This function may sleep.

enable
    Enable the clock atomically. This must not return until the
    clock is generating a valid clock signal, usable by consumer
    devices. Called with enable_lock held. This function must not
    sleep.

disable
    Disable the clock atomically. Called with enable_lock held.
    This function must not sleep.

is_enabled
    Queries the hardware to determine if the clock is enabled.
    This function must not sleep. Optional, if this op is not
    set then the enable count will be used.

disable_unused
    Disable the clock atomically.  Only called from
    clk_disable_unused for gate clocks with special needs.
    Called with enable_lock held.  This function must not
    sleep.

recalc_rate
    *undescribed*

round_rate
    Given a target rate as input, returns the closest rate actually
    supported by the clock. The parent rate is an input/output
    parameter.

determine_rate
    Given a target rate as input, returns the closest rate
    actually supported by the clock, and optionally the parent clock
    that should be used to provide the clock rate.

set_parent
    Change the input source of this clock; for clocks with multiple
    possible parents specify a new parent by passing in the index
    as a u8 corresponding to the parent in either the .parent_names
    or .parents arrays.  This function in affect translates an
    array index into the value programmed into the hardware.
    Returns 0 on success, -EERROR otherwise.

get_parent
    Queries the hardware to determine the parent of a clock.  The
    return value is a u8 which specifies the index corresponding to
    the parent clock.  This index can be applied to either the
    .parent_names or .parents arrays.  In short, this function
    translates the parent value read from hardware into an array
    index.  Currently only called when the clock is initialized by
    \__clk_init.  This callback is mandatory for clocks with
    multiple parents.  It is optional (and unnecessary) for clocks
    with 0 or 1 parents.

set_rate
    Change the rate of this clock. The requested rate is specified
    by the second argument, which should typically be the return
    of .round_rate call.  The third argument gives the parent rate
    which is likely helpful for most .set_rate implementation.
    Returns 0 on success, -EERROR otherwise.

set_rate_and_parent
    Change the rate and the parent of this clock. The
    requested rate is specified by the second argument, which
    should typically be the return of .round_rate call.  The
    third argument gives the parent rate which is likely helpful
    for most .set_rate_and_parent implementation. The fourth
    argument gives the parent index. This callback is optional (and
    unnecessary) for clocks with 0 or 1 parents as well as
    for clocks that can tolerate switching the rate and the parent
    separately via calls to .set_parent and .set_rate.
    Returns 0 on success, -EERROR otherwise.

recalc_accuracy
    Recalculate the accuracy of this clock. The clock accuracy
    is expressed in ppb (parts per billion). The parent accuracy is
    an input parameter.
    Returns the calculated accuracy.  Optional - if this op is not
    set then clock accuracy will be initialized to parent accuracy
    or 0 (perfect clock) if clock has no parent.

get_phase
    Queries the hardware to get the current phase of a clock.
    Returned values are 0-359 degrees on success, negative
    error codes on failure.

set_phase
    Shift the phase this clock signal in degrees specified
    by the second argument. Valid values for degrees are
    0-359. Return 0 on success, otherwise -EERROR.

init
    Perform platform-specific initialization magic.
    This is not not used by any of the basic clock types.
    Please consider other ways of solving initialization problems
    before using this callback, as its use is discouraged.

debug_init
    Set up type-specific debugfs entries for this clock.  This
    is called once, after the debugfs directory entry for this
    clock has been created.  The dentry pointer representing that
    directory is provided as an argument.  Called with
    prepare_lock held.  Returns 0 on success, -EERROR otherwise.

.. _`clk_ops.description`:

Description
-----------

@recalc_rate Recalculate the rate of this clock, by querying hardware. The
parent rate is an input parameter.  It is up to the caller to
ensure that the prepare_mutex is held across this call.
Returns the calculated rate.  Optional, but recommended - if
this op is not set then clock rate will be initialized to 0.


The clk_enable/clk_disable and clk_prepare/clk_unprepare pairs allow
implementations to split any work between atomic (enable) and sleepable
(prepare) contexts.  If enabling a clock requires code that might sleep,
this must be done in clk_prepare.  Clock enable code that will never be
called in a sleepable context may be implemented in clk_enable.

Typically, drivers will call clk_prepare when a clock may be needed later
(eg. when a device is opened), and clk_enable when the clock is actually
required (eg. from an interrupt). Note that clk_prepare MUST have been
called before clk_enable.

.. _`clk_init_data`:

struct clk_init_data
====================

.. c:type:: struct clk_init_data

    holds init data that's common to all clocks and is shared between the clock provider and the common clock framework.

.. _`clk_init_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_init_data {
        const char *name;
        const struct clk_ops *ops;
        const char * const *parent_names;
        u8 num_parents;
        unsigned long flags;
    }

.. _`clk_init_data.members`:

Members
-------

name
    clock name

ops
    operations this clock supports

parent_names
    array of string names for all possible parents

num_parents
    number of possible parents

flags
    framework-level hints and quirks

.. _`clk_hw`:

struct clk_hw
=============

.. c:type:: struct clk_hw

    handle for traversing from a struct clk to its corresponding hardware-specific structure.  struct clk_hw should be declared within struct clk_foo and then referenced by the struct clk instance that uses struct clk_foo's clk_ops

.. _`clk_hw.definition`:

Definition
----------

.. code-block:: c

    struct clk_hw {
        struct clk_core *core;
        struct clk *clk;
        const struct clk_init_data *init;
    }

.. _`clk_hw.members`:

Members
-------

core
    pointer to the struct clk_core instance that points back to this
    struct clk_hw instance

clk
    pointer to the per-user struct clk instance that can be used to call
    into the clk API

init
    pointer to struct clk_init_data that contains the init data shared
    with the common clock framework.

.. _`clk_fixed_rate`:

struct clk_fixed_rate
=====================

.. c:type:: struct clk_fixed_rate

    fixed-rate clock

.. _`clk_fixed_rate.definition`:

Definition
----------

.. code-block:: c

    struct clk_fixed_rate {
        struct clk_hw hw;
        unsigned long fixed_rate;
        unsigned long fixed_accuracy;
        u8 flags;
    }

.. _`clk_fixed_rate.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

fixed_rate
    constant frequency of clock

fixed_accuracy
    *undescribed*

flags
    *undescribed*

.. _`clk_gate`:

struct clk_gate
===============

.. c:type:: struct clk_gate

    gating clock

.. _`clk_gate.definition`:

Definition
----------

.. code-block:: c

    struct clk_gate {
        struct clk_hw hw;
        void __iomem *reg;
        u8 bit_idx;
        u8 flags;
        spinlock_t *lock;
    }

.. _`clk_gate.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register controlling gate

bit_idx
    single bit controlling gate

flags
    hardware-specific flags

lock
    register lock

.. _`clk_gate.description`:

Description
-----------

Clock which can gate its output.  Implements .enable & .disable

.. _`clk_gate.flags`:

Flags
-----

CLK_GATE_SET_TO_DISABLE - by default this clock sets the bit at bit_idx to
enable the clock.  Setting this flag does the opposite: setting the bit
disable the clock and clearing it enables the clock
CLK_GATE_HIWORD_MASK - The gate settings are only in lower 16-bit
of this register, and mask of gate bits are in higher 16-bit of this
register.  While setting the gate bits, higher 16-bit should also be
updated to indicate changing gate bits.

.. _`clk_divider`:

struct clk_divider
==================

.. c:type:: struct clk_divider

    adjustable divider clock

.. _`clk_divider.definition`:

Definition
----------

.. code-block:: c

    struct clk_divider {
        struct clk_hw hw;
        void __iomem *reg;
        u8 shift;
        u8 width;
        u8 flags;
        const struct clk_div_table *table;
        spinlock_t *lock;
    }

.. _`clk_divider.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing the divider

shift
    shift to the divider bit field

width
    width of the divider bit field

flags
    *undescribed*

table
    array of value/divider pairs, last entry should have div = 0

lock
    register lock

.. _`clk_divider.description`:

Description
-----------

Clock with an adjustable divider affecting its output frequency.  Implements
.recalc_rate, .set_rate and .round_rate

.. _`clk_divider.flags`:

Flags
-----

CLK_DIVIDER_ONE_BASED - by default the divisor is the value read from the
register plus one.  If CLK_DIVIDER_ONE_BASED is set then the divider is
the raw value read from the register, with the value of zero considered
invalid, unless CLK_DIVIDER_ALLOW_ZERO is set.
CLK_DIVIDER_POWER_OF_TWO - clock divisor is 2 raised to the value read from
the hardware register
CLK_DIVIDER_ALLOW_ZERO - Allow zero divisors.  For dividers which have
CLK_DIVIDER_ONE_BASED set, it is possible to end up with a zero divisor.
Some hardware implementations gracefully handle this case and allow a
zero divisor by not modifying their input clock
(divide by one / bypass).
CLK_DIVIDER_HIWORD_MASK - The divider settings are only in lower 16-bit
of this register, and mask of divider bits are in higher 16-bit of this
register.  While setting the divider bits, higher 16-bit should also be
updated to indicate changing divider bits.
CLK_DIVIDER_ROUND_CLOSEST - Makes the best calculated divider to be rounded
to the closest integer instead of the up one.
CLK_DIVIDER_READ_ONLY - The divider settings are preconfigured and should
not be changed by the clock framework.
CLK_DIVIDER_MAX_AT_ZERO - For dividers which are like CLK_DIVIDER_ONE_BASED
except when the value read from the register is zero, the divisor is
2^width of the field.

.. _`clk_mux`:

struct clk_mux
==============

.. c:type:: struct clk_mux

    multiplexer clock

.. _`clk_mux.definition`:

Definition
----------

.. code-block:: c

    struct clk_mux {
        struct clk_hw hw;
        void __iomem *reg;
        u32 *table;
        u32 mask;
        u8 shift;
        u8 flags;
        spinlock_t *lock;
    }

.. _`clk_mux.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register controlling multiplexer

table
    *undescribed*

mask
    *undescribed*

shift
    shift to multiplexer bit field

flags
    hardware-specific flags

lock
    register lock

.. _`clk_mux.description`:

Description
-----------

Clock with multiple selectable parents.  Implements .get_parent, .set_parent
and .recalc_rate

.. _`clk_mux.flags`:

Flags
-----

CLK_MUX_INDEX_ONE - register index starts at 1, not 0
CLK_MUX_INDEX_BIT - register index is a single bit (power of two)
CLK_MUX_HIWORD_MASK - The mux settings are only in lower 16-bit of this
register, and mask of mux bits are in higher 16-bit of this register.
While setting the mux bits, higher 16-bit should also be updated to
indicate changing mux bits.
CLK_MUX_ROUND_CLOSEST - Use the parent rate that is closest to the desired
frequency.

.. _`clk_fixed_factor`:

struct clk_fixed_factor
=======================

.. c:type:: struct clk_fixed_factor

    fixed multiplier and divider clock

.. _`clk_fixed_factor.definition`:

Definition
----------

.. code-block:: c

    struct clk_fixed_factor {
        struct clk_hw hw;
        unsigned int mult;
        unsigned int div;
    }

.. _`clk_fixed_factor.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

mult
    multiplier

div
    divider

.. _`clk_fixed_factor.description`:

Description
-----------

Clock with a fixed multiplier and divider. The output frequency is the
parent clock rate divided by div and multiplied by mult.
Implements .recalc_rate, .set_rate and .round_rate

.. _`clk_fractional_divider`:

struct clk_fractional_divider
=============================

.. c:type:: struct clk_fractional_divider

    adjustable fractional divider clock

.. _`clk_fractional_divider.definition`:

Definition
----------

.. code-block:: c

    struct clk_fractional_divider {
        struct clk_hw hw;
        void __iomem *reg;
        u8 mshift;
        u8 mwidth;
        u32 mmask;
        u8 nshift;
        u8 nwidth;
        u32 nmask;
        u8 flags;
        spinlock_t *lock;
    }

.. _`clk_fractional_divider.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing the divider

mshift
    shift to the numerator bit field

mwidth
    width of the numerator bit field

mmask
    *undescribed*

nshift
    shift to the denominator bit field

nwidth
    width of the denominator bit field

nmask
    *undescribed*

flags
    *undescribed*

lock
    register lock

.. _`clk_fractional_divider.description`:

Description
-----------

Clock with adjustable fractional divider affecting its output frequency.

.. _`clk_multiplier`:

struct clk_multiplier
=====================

.. c:type:: struct clk_multiplier

    adjustable multiplier clock

.. _`clk_multiplier.definition`:

Definition
----------

.. code-block:: c

    struct clk_multiplier {
        struct clk_hw hw;
        void __iomem *reg;
        u8 shift;
        u8 width;
        u8 flags;
        spinlock_t *lock;
    }

.. _`clk_multiplier.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    register containing the multiplier

shift
    shift to the multiplier bit field

width
    width of the multiplier bit field

flags
    *undescribed*

lock
    register lock

.. _`clk_multiplier.description`:

Description
-----------

Clock with an adjustable multiplier affecting its output frequency.
Implements .recalc_rate, .set_rate and .round_rate

.. _`clk_multiplier.flags`:

Flags
-----

CLK_MULTIPLIER_ZERO_BYPASS - By default, the multiplier is the value read
from the register, with 0 being a valid value effectively
zeroing the output clock rate. If CLK_MULTIPLIER_ZERO_BYPASS is
set, then a null multiplier will be considered as a bypass,
leaving the parent rate unmodified.
CLK_MULTIPLIER_ROUND_CLOSEST - Makes the best calculated divider to be
rounded to the closest integer instead of the down one.

.. _`clk_register`:

clk_register
============

.. c:function:: struct clk *clk_register(struct device *dev, struct clk_hw *hw)

    allocate a new clock, register it and return an opaque cookie

    :param struct device \*dev:
        device that is registering this clock

    :param struct clk_hw \*hw:
        link to hardware-specific clock data

.. _`clk_register.description`:

Description
-----------

clk_register is the primary interface for populating the clock tree with new
clock nodes.  It returns a pointer to the newly allocated struct clk which
cannot be dereferenced by driver code but may be used in conjuction with the
rest of the clock API.  In the event of an error clk_register will return an
error code; drivers must test for an error code after calling clk_register.

.. This file was automatic generated / don't edit.

