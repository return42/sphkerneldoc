.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/regmap.h

.. _`reg_default`:

struct reg_default
==================

.. c:type:: struct reg_default

    Default value for a register.

.. _`reg_default.definition`:

Definition
----------

.. code-block:: c

    struct reg_default {
        unsigned int reg;
        unsigned int def;
    }

.. _`reg_default.members`:

Members
-------

reg
    Register address.

def
    Register default value.

.. _`reg_default.description`:

Description
-----------

We use an array of structs rather than a simple array as many modern devices
have very sparse register maps.

.. _`reg_sequence`:

struct reg_sequence
===================

.. c:type:: struct reg_sequence

    An individual write from a sequence of writes.

.. _`reg_sequence.definition`:

Definition
----------

.. code-block:: c

    struct reg_sequence {
        unsigned int reg;
        unsigned int def;
        unsigned int delay_us;
    }

.. _`reg_sequence.members`:

Members
-------

reg
    Register address.

def
    Register value.

delay_us
    Delay to be applied after the register write in microseconds

.. _`reg_sequence.description`:

Description
-----------

Register/value pairs for sequences of writes with an optional delay in
microseconds to be applied after each write.

.. _`regmap_read_poll_timeout`:

regmap_read_poll_timeout
========================

.. c:function::  regmap_read_poll_timeout( map,  addr,  val,  cond,  sleep_us,  timeout_us)

    Poll until a condition is met or a timeout occurs

    :param  map:
        Regmap to read from

    :param  addr:
        Address to poll

    :param  val:
        Unsigned integer variable to read the value into

    :param  cond:
        Break condition (usually involving \ ``val``\ )

    :param  sleep_us:
        Maximum time to sleep between reads in us (0
        tight-loops).  Should be less than ~20ms since usleep_range
        is used (see Documentation/timers/timers-howto.txt).

    :param  timeout_us:
        Timeout in us, 0 means never timeout

.. _`regmap_read_poll_timeout.description`:

Description
-----------

Returns 0 on success and -ETIMEDOUT upon a timeout or the regmap_read
error return value in case of a error read. In the two former cases,
the last read value at \ ``addr``\  is stored in \ ``val``\ . Must not be called
from atomic context if sleep_us or timeout_us are used.

This is modelled after the readx_poll_timeout macros in linux/iopoll.h.

.. _`regmap_range`:

struct regmap_range
===================

.. c:type:: struct regmap_range

    A register range, used for access related checks (readable/writeable/volatile/precious checks)

.. _`regmap_range.definition`:

Definition
----------

.. code-block:: c

    struct regmap_range {
        unsigned int range_min;
        unsigned int range_max;
    }

.. _`regmap_range.members`:

Members
-------

range_min
    address of first register

range_max
    address of last register

.. _`regmap_access_table`:

struct regmap_access_table
==========================

.. c:type:: struct regmap_access_table

    A table of register ranges for access checks

.. _`regmap_access_table.definition`:

Definition
----------

.. code-block:: c

    struct regmap_access_table {
        const struct regmap_range *yes_ranges;
        unsigned int n_yes_ranges;
        const struct regmap_range *no_ranges;
        unsigned int n_no_ranges;
    }

.. _`regmap_access_table.members`:

Members
-------

yes_ranges
    pointer to an array of regmap ranges used as "yes ranges"

n_yes_ranges
    size of the above array

no_ranges
    pointer to an array of regmap ranges used as "no ranges"

n_no_ranges
    size of the above array

.. _`regmap_access_table.description`:

Description
-----------

A table of ranges including some yes ranges and some no ranges.
If a register belongs to a no_range, the corresponding check function
will return false. If a register belongs to a yes range, the corresponding
check function will return true. "no_ranges" are searched first.

.. _`regmap_config`:

struct regmap_config
====================

.. c:type:: struct regmap_config

    Configuration for the register map of a device.

.. _`regmap_config.definition`:

Definition
----------

.. code-block:: c

    struct regmap_config {
        const char *name;
        int reg_bits;
        int reg_stride;
        int pad_bits;
        int val_bits;
        bool (*writeable_reg)(struct device *dev, unsigned int reg);
        bool (*readable_reg)(struct device *dev, unsigned int reg);
        bool (*volatile_reg)(struct device *dev, unsigned int reg);
        bool (*precious_reg)(struct device *dev, unsigned int reg);
        regmap_lock lock;
        regmap_unlock unlock;
        void *lock_arg;
        int (*reg_read)(void *context, unsigned int reg, unsigned int *val);
        int (*reg_write)(void *context, unsigned int reg, unsigned int val);
        bool fast_io;
        unsigned int max_register;
        const struct regmap_access_table *wr_table;
        const struct regmap_access_table *rd_table;
        const struct regmap_access_table *volatile_table;
        const struct regmap_access_table *precious_table;
        const struct reg_default *reg_defaults;
        unsigned int num_reg_defaults;
        enum regcache_type cache_type;
        const void *reg_defaults_raw;
        unsigned int num_reg_defaults_raw;
        unsigned long read_flag_mask;
        unsigned long write_flag_mask;
        bool use_single_rw;
        bool can_multi_write;
        enum regmap_endian reg_format_endian;
        enum regmap_endian val_format_endian;
        const struct regmap_range_cfg *ranges;
        unsigned int num_ranges;
    }

.. _`regmap_config.members`:

Members
-------

name
    Optional name of the regmap. Useful when a device has multiple
    register regions.

reg_bits
    Number of bits in a register address, mandatory.

reg_stride
    The register address stride. Valid register addresses are a
    multiple of this value. If set to 0, a value of 1 will be
    used.

pad_bits
    Number of bits of padding between register and value.

val_bits
    Number of bits in a register value, mandatory.

writeable_reg
    Optional callback returning true if the register
    can be written to. If this field is NULL but wr_table
    (see below) is not, the check is performed on such table
    (a register is writeable if it belongs to one of the ranges
    specified by wr_table).

readable_reg
    Optional callback returning true if the register
    can be read from. If this field is NULL but rd_table
    (see below) is not, the check is performed on such table
    (a register is readable if it belongs to one of the ranges
    specified by rd_table).

volatile_reg
    Optional callback returning true if the register
    value can't be cached. If this field is NULL but
    volatile_table (see below) is not, the check is performed on
    such table (a register is volatile if it belongs to one of
    the ranges specified by volatile_table).

precious_reg
    Optional callback returning true if the register
    should not be read outside of a call from the driver
    (e.g., a clear on read interrupt status register). If this
    field is NULL but precious_table (see below) is not, the
    check is performed on such table (a register is precious if
    it belongs to one of the ranges specified by precious_table).

lock
    Optional lock callback (overrides regmap's default lock
    function, based on spinlock or mutex).

unlock
    As above for unlocking.

lock_arg
    this field is passed as the only argument of lock/unlock
    functions (ignored in case regular lock/unlock functions
    are not overridden).

reg_read
    Optional callback that if filled will be used to perform
    all the reads from the registers. Should only be provided for
    devices whose read operation cannot be represented as a simple
    read operation on a bus such as SPI, I2C, etc. Most of the
    devices do not need this.

reg_write
    Same as above for writing.

fast_io
    Register IO is fast. Use a spinlock instead of a mutex
    to perform locking. This field is ignored if custom lock/unlock
    functions are used (see fields lock/unlock of struct regmap_config).
    This field is a duplicate of a similar file in
    'struct regmap_bus' and serves exact same purpose.
    Use it only for "no-bus" cases.

max_register
    Optional, specifies the maximum valid register address.

wr_table
    Optional, points to a struct regmap_access_table specifying
    valid ranges for write access.

rd_table
    As above, for read access.

volatile_table
    As above, for volatile registers.

precious_table
    As above, for precious registers.

reg_defaults
    Power on reset values for registers (for use with
    register cache support).

num_reg_defaults
    Number of elements in reg_defaults.

cache_type
    The actual cache type.

reg_defaults_raw
    Power on reset values for registers (for use with
    register cache support).

num_reg_defaults_raw
    Number of elements in reg_defaults_raw.

read_flag_mask
    Mask to be set in the top bytes of the register when doing
    a read.

write_flag_mask
    Mask to be set in the top bytes of the register when doing
    a write. If both read_flag_mask and write_flag_mask are
    empty the regmap_bus default masks are used.

use_single_rw
    If set, converts the bulk read and write operations into
    a series of single read and write operations. This is useful
    for device that does not support bulk read and write.

can_multi_write
    If set, the device supports the multi write mode of bulk
    write operations, if clear multi write requests will be
    split into individual write operations

reg_format_endian
    Endianness for formatted register addresses. If this is
    DEFAULT, the \ ``reg_format_endian_default``\  value from the
    regmap bus is used.

val_format_endian
    Endianness for formatted register values. If this is
    DEFAULT, the \ ``reg_format_endian_default``\  value from the
    regmap bus is used.

ranges
    Array of configuration entries for virtual address ranges.

num_ranges
    Number of range configuration entries.

.. _`regmap_range_cfg`:

struct regmap_range_cfg
=======================

.. c:type:: struct regmap_range_cfg

    Configuration for indirectly accessed or paged registers.

.. _`regmap_range_cfg.definition`:

Definition
----------

.. code-block:: c

    struct regmap_range_cfg {
        const char *name;
        unsigned int range_min;
        unsigned int range_max;
        unsigned int selector_reg;
        unsigned int selector_mask;
        int selector_shift;
        unsigned int window_start;
        unsigned int window_len;
    }

.. _`regmap_range_cfg.members`:

Members
-------

name
    Descriptive name for diagnostics

range_min
    Address of the lowest register address in virtual range.

range_max
    Address of the highest register in virtual range.

selector_reg
    Register with selector field.

selector_mask
    Bit shift for selector value.

selector_shift
    Bit mask for selector value.

window_start
    Address of first (lowest) register in data window.

window_len
    Number of registers in data window.

.. _`regmap_range_cfg.description`:

Description
-----------

Registers, mapped to this virtual range, are accessed in two steps:
1. page selector register update;
2. access through data window registers.

.. _`regmap_bus`:

struct regmap_bus
=================

.. c:type:: struct regmap_bus

    Description of a hardware bus for the register map infrastructure.

.. _`regmap_bus.definition`:

Definition
----------

.. code-block:: c

    struct regmap_bus {
        bool fast_io;
        regmap_hw_write write;
        regmap_hw_gather_write gather_write;
        regmap_hw_async_write async_write;
        regmap_hw_reg_write reg_write;
        regmap_hw_reg_update_bits reg_update_bits;
        regmap_hw_read read;
        regmap_hw_reg_read reg_read;
        regmap_hw_free_context free_context;
        regmap_hw_async_alloc async_alloc;
        u8 read_flag_mask;
        enum regmap_endian reg_format_endian_default;
        enum regmap_endian val_format_endian_default;
        size_t max_raw_read;
        size_t max_raw_write;
    }

.. _`regmap_bus.members`:

Members
-------

fast_io
    Register IO is fast. Use a spinlock instead of a mutex
    to perform locking. This field is ignored if custom lock/unlock
    functions are used (see fields lock/unlock of
    struct regmap_config).

write
    Write operation.

gather_write
    Write operation with split register/value, return -ENOTSUPP
    if not implemented  on a given device.

async_write
    Write operation which completes asynchronously, optional and
    must serialise with respect to non-async I/O.

reg_write
    Write a single register value to the given register address. This
    write operation has to complete when returning from the function.

reg_update_bits
    Update bits operation to be used against volatile
    registers, intended for devices supporting some mechanism
    for setting clearing bits without having to
    read/modify/write.

read
    Read operation.  Data is returned in the buffer used to transmit
    data.

reg_read
    Read a single register value from a given register address.

free_context
    Free context.

async_alloc
    Allocate a \ :c:func:`regmap_async`\  structure.

read_flag_mask
    Mask to be set in the top byte of the register when doing
    a read.

reg_format_endian_default
    Default endianness for formatted register
    addresses. Used when the regmap_config specifies DEFAULT. If this is
    DEFAULT, BIG is assumed.

val_format_endian_default
    Default endianness for formatted register
    values. Used when the regmap_config specifies DEFAULT. If this is
    DEFAULT, BIG is assumed.

max_raw_read
    Max raw read size that can be used on the bus.

max_raw_write
    Max raw write size that can be used on the bus.

.. _`regmap_init`:

regmap_init
===========

.. c:function::  regmap_init( dev,  bus,  bus_context,  config)

    Initialise register map

    :param  dev:
        Device that will be interacted with

    :param  bus:
        Bus-specific callbacks to use with device

    :param  bus_context:
        Data passed to bus-specific callbacks

    :param  config:
        Configuration for register map

.. _`regmap_init.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.  This function should generally not be called
directly, it should be called by bus-specific init functions.

.. _`regmap_init_i2c`:

regmap_init_i2c
===============

.. c:function::  regmap_init_i2c( i2c,  config)

    Initialise register map

    :param  i2c:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_i2c.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_spi`:

regmap_init_spi
===============

.. c:function::  regmap_init_spi( dev,  config)

    Initialise register map

    :param  dev:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_spi.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_spmi_base`:

regmap_init_spmi_base
=====================

.. c:function::  regmap_init_spmi_base( dev,  config)

    Create regmap for the Base register space

    :param  dev:
        SPMI device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_spmi_base.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_spmi_ext`:

regmap_init_spmi_ext
====================

.. c:function::  regmap_init_spmi_ext( dev,  config)

    Create regmap for Ext register space

    :param  dev:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_spmi_ext.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_mmio_clk`:

regmap_init_mmio_clk
====================

.. c:function::  regmap_init_mmio_clk( dev,  clk_id,  regs,  config)

    Initialise register map with register clock

    :param  dev:
        Device that will be interacted with

    :param  clk_id:
        register clock consumer ID

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`regmap_init_mmio_clk.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_mmio`:

regmap_init_mmio
================

.. c:function::  regmap_init_mmio( dev,  regs,  config)

    Initialise register map

    :param  dev:
        Device that will be interacted with

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`regmap_init_mmio.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`regmap_init_ac97`:

regmap_init_ac97
================

.. c:function::  regmap_init_ac97( ac97,  config)

    Initialise AC'97 register map

    :param  ac97:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`regmap_init_ac97.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to
a struct regmap.

.. _`devm_regmap_init`:

devm_regmap_init
================

.. c:function::  devm_regmap_init( dev,  bus,  bus_context,  config)

    Initialise managed register map

    :param  dev:
        Device that will be interacted with

    :param  bus:
        Bus-specific callbacks to use with device

    :param  bus_context:
        Data passed to bus-specific callbacks

    :param  config:
        Configuration for register map

.. _`devm_regmap_init.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  This function should generally not be called
directly, it should be called by bus-specific init functions.  The
map will be automatically freed by the device management code.

.. _`devm_regmap_init_i2c`:

devm_regmap_init_i2c
====================

.. c:function::  devm_regmap_init_i2c( i2c,  config)

    Initialise managed register map

    :param  i2c:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_i2c.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_spi`:

devm_regmap_init_spi
====================

.. c:function::  devm_regmap_init_spi( dev,  config)

    Initialise register map

    :param  dev:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_spi.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The map will be automatically freed by the
device management code.

.. _`devm_regmap_init_spmi_base`:

devm_regmap_init_spmi_base
==========================

.. c:function::  devm_regmap_init_spmi_base( dev,  config)

    Create managed regmap for Base register space

    :param  dev:
        SPMI device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_spmi_base.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_spmi_ext`:

devm_regmap_init_spmi_ext
=========================

.. c:function::  devm_regmap_init_spmi_ext( dev,  config)

    Create managed regmap for Ext register space

    :param  dev:
        SPMI device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_spmi_ext.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_mmio_clk`:

devm_regmap_init_mmio_clk
=========================

.. c:function::  devm_regmap_init_mmio_clk( dev,  clk_id,  regs,  config)

    Initialise managed register map with clock

    :param  dev:
        Device that will be interacted with

    :param  clk_id:
        register clock consumer ID

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_mmio_clk.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_mmio`:

devm_regmap_init_mmio
=====================

.. c:function::  devm_regmap_init_mmio( dev,  regs,  config)

    Initialise managed register map

    :param  dev:
        Device that will be interacted with

    :param  regs:
        Pointer to memory-mapped IO region

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_mmio.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`devm_regmap_init_ac97`:

devm_regmap_init_ac97
=====================

.. c:function::  devm_regmap_init_ac97( ac97,  config)

    Initialise AC'97 register map

    :param  ac97:
        Device that will be interacted with

    :param  config:
        Configuration for register map

.. _`devm_regmap_init_ac97.description`:

Description
-----------

The return value will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct regmap.  The regmap will be automatically freed by the
device management code.

.. _`reg_field`:

struct reg_field
================

.. c:type:: struct reg_field

    Description of an register field

.. _`reg_field.definition`:

Definition
----------

.. code-block:: c

    struct reg_field {
        unsigned int reg;
        unsigned int lsb;
        unsigned int msb;
        unsigned int id_size;
        unsigned int id_offset;
    }

.. _`reg_field.members`:

Members
-------

reg
    Offset of the register within the regmap bank

lsb
    lsb of the register field.

msb
    msb of the register field.

id_size
    port size if it has some ports

id_offset
    address offset for each ports

.. _`regmap_irq`:

struct regmap_irq
=================

.. c:type:: struct regmap_irq

    Description of an IRQ for the generic regmap irq_chip.

.. _`regmap_irq.definition`:

Definition
----------

.. code-block:: c

    struct regmap_irq {
        unsigned int reg_offset;
        unsigned int mask;
        unsigned int type_reg_offset;
        unsigned int type_rising_mask;
        unsigned int type_falling_mask;
    }

.. _`regmap_irq.members`:

Members
-------

reg_offset
    Offset of the status/mask register within the bank

mask
    Mask used to flag/control the register.

type_reg_offset
    Offset register for the irq type setting.

type_rising_mask
    Mask bit to configure RISING type irq.

type_falling_mask
    Mask bit to configure FALLING type irq.

.. _`regmap_irq_chip`:

struct regmap_irq_chip
======================

.. c:type:: struct regmap_irq_chip

    Description of a generic regmap irq_chip.

.. _`regmap_irq_chip.definition`:

Definition
----------

.. code-block:: c

    struct regmap_irq_chip {
        const char *name;
        unsigned int status_base;
        unsigned int mask_base;
        unsigned int unmask_base;
        unsigned int ack_base;
        unsigned int wake_base;
        unsigned int type_base;
        unsigned int irq_reg_stride;
        bool init_ack_masked:1;
        bool mask_invert:1;
        bool use_ack:1;
        bool ack_invert:1;
        bool wake_invert:1;
        bool runtime_pm:1;
        bool type_invert:1;
        int num_regs;
        const struct regmap_irq *irqs;
        int num_irqs;
        int num_type_reg;
        unsigned int type_reg_stride;
        int (*handle_pre_irq)(void *irq_drv_data);
        int (*handle_post_irq)(void *irq_drv_data);
        void *irq_drv_data;
    }

.. _`regmap_irq_chip.members`:

Members
-------

name
    Descriptive name for IRQ controller.

status_base
    Base status register address.

mask_base
    Base mask register address.

unmask_base
    Base unmask register address. for chips who have
    separate mask and unmask registers

ack_base
    Base ack address. If zero then the chip is clear on read.
    Using zero value is possible with \ ``use_ack``\  bit.

wake_base
    Base address for wake enables.  If zero unsupported.

type_base
    Base address for irq type.  If zero unsupported.

irq_reg_stride
    Stride to use for chips where registers are not contiguous.

init_ack_masked
    Ack all masked interrupts once during initalization.

mask_invert
    Inverted mask register: cleared bits are masked out.

use_ack
    Use \ ``ack``\  register even if it is zero.

ack_invert
    Inverted ack register: cleared bits for ack.

wake_invert
    Inverted wake register: cleared bits are wake enabled.

runtime_pm
    Hold a runtime PM lock on the device when accessing it.

type_invert
    Invert the type flags.

num_regs
    Number of registers in each control bank.

irqs
    Descriptors for individual IRQs.  Interrupt numbers are
    assigned based on the index in the array of the interrupt.

num_irqs
    Number of descriptors.

num_type_reg
    Number of type registers.

type_reg_stride
    Stride to use for chips where type registers are not
    contiguous.

handle_pre_irq
    Driver specific callback to handle interrupt from device
    before regmap_irq_handler process the interrupts.

handle_post_irq
    Driver specific callback to handle interrupt from device
    after handling the interrupts in \ :c:func:`regmap_irq_handler`\ .

irq_drv_data
    Driver specific IRQ data which is passed as parameter when
    driver specific pre/post interrupt handler is called.

.. _`regmap_irq_chip.description`:

Description
-----------

This is not intended to handle every possible interrupt controller, but
it should handle a substantial proportion of those that are found in the
wild.

.. This file was automatic generated / don't edit.

