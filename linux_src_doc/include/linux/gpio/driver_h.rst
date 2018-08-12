.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gpio/driver.h

.. _`gpio_irq_chip`:

struct gpio_irq_chip
====================

.. c:type:: struct gpio_irq_chip

    GPIO interrupt controller

.. _`gpio_irq_chip.definition`:

Definition
----------

.. code-block:: c

    struct gpio_irq_chip {
        struct irq_chip *chip;
        struct irq_domain *domain;
        const struct irq_domain_ops *domain_ops;
        irq_flow_handler_t handler;
        unsigned int default_type;
        struct lock_class_key *lock_key;
        struct lock_class_key *request_key;
        irq_flow_handler_t parent_handler;
        void *parent_handler_data;
        unsigned int num_parents;
        unsigned int *parents;
        unsigned int *map;
        bool threaded;
        bool need_valid_mask;
        unsigned long *valid_mask;
        unsigned int first;
    }

.. _`gpio_irq_chip.members`:

Members
-------

chip

    GPIO IRQ chip implementation, provided by GPIO driver.

domain

    Interrupt translation domain; responsible for mapping between GPIO
    hwirq number and Linux IRQ number.

domain_ops

    Table of interrupt domain operations for this IRQ chip.

handler

    The IRQ handler to use (often a predefined IRQ core function) for
    GPIO IRQs, provided by GPIO driver.

default_type

    Default IRQ triggering type applied during GPIO driver
    initialization, provided by GPIO driver.

lock_key

    Per GPIO IRQ chip lockdep classes.

request_key
    *undescribed*

parent_handler

    The interrupt handler for the GPIO chip's parent interrupts, may be
    NULL if the parent interrupts are nested rather than cascaded.

parent_handler_data

    Data associated, and passed to, the handler for the parent
    interrupt.

num_parents

    The number of interrupt parents of a GPIO chip.

parents

    A list of interrupt parents of a GPIO chip. This is owned by the
    driver, so the core will only reference this list, not modify it.

map

    A list of interrupt parents for each line of a GPIO chip.

threaded

    True if set the interrupt handling uses nested threads.

need_valid_mask

    If set core allocates \ ``valid_mask``\  with all bits set to one.

valid_mask

    If not \ ``NULL``\  holds bitmask of GPIOs which are valid to be included
    in IRQ domain of the chip.

first

    Required for static IRQ allocation. If set, \ :c:func:`irq_domain_add_simple`\ 
    will allocate and map all IRQs during initialization.

.. _`gpio_chip`:

struct gpio_chip
================

.. c:type:: struct gpio_chip

    abstract a GPIO controller

.. _`gpio_chip.definition`:

Definition
----------

.. code-block:: c

    struct gpio_chip {
        const char *label;
        struct gpio_device *gpiodev;
        struct device *parent;
        struct module *owner;
        int (*request)(struct gpio_chip *chip, unsigned offset);
        void (*free)(struct gpio_chip *chip, unsigned offset);
        int (*get_direction)(struct gpio_chip *chip, unsigned offset);
        int (*direction_input)(struct gpio_chip *chip, unsigned offset);
        int (*direction_output)(struct gpio_chip *chip, unsigned offset, int value);
        int (*get)(struct gpio_chip *chip, unsigned offset);
        int (*get_multiple)(struct gpio_chip *chip,unsigned long *mask, unsigned long *bits);
        void (*set)(struct gpio_chip *chip, unsigned offset, int value);
        void (*set_multiple)(struct gpio_chip *chip,unsigned long *mask, unsigned long *bits);
        int (*set_config)(struct gpio_chip *chip,unsigned offset, unsigned long config);
        int (*to_irq)(struct gpio_chip *chip, unsigned offset);
        void (*dbg_show)(struct seq_file *s, struct gpio_chip *chip);
        int base;
        u16 ngpio;
        const char *const *names;
        bool can_sleep;
    #if IS_ENABLED(CONFIG_GPIO_GENERIC)
        unsigned long (*read_reg)(void __iomem *reg);
        void (*write_reg)(void __iomem *reg, unsigned long data);
        bool be_bits;
        void __iomem *reg_dat;
        void __iomem *reg_set;
        void __iomem *reg_clr;
        void __iomem *reg_dir;
        int bgpio_bits;
        spinlock_t bgpio_lock;
        unsigned long bgpio_data;
        unsigned long bgpio_dir;
    #endif
    #ifdef CONFIG_GPIOLIB_IRQCHIP
        struct gpio_irq_chip irq;
    #endif
        bool need_valid_mask;
        unsigned long *valid_mask;
    #if defined(CONFIG_OF_GPIO)
        struct device_node *of_node;
        unsigned int of_gpio_n_cells;
        int (*of_xlate)(struct gpio_chip *gc, const struct of_phandle_args *gpiospec, u32 *flags);
    #endif
    }

.. _`gpio_chip.members`:

Members
-------

label
    a functional name for the GPIO device, such as a part
    number or the name of the SoC IP-block implementing it.

gpiodev
    the internal state holder, opaque struct

parent
    optional parent device providing the GPIOs

owner
    helps prevent removal of modules exporting active GPIOs

request
    optional hook for chip-specific activation, such as
    enabling module power and clock; may sleep

free
    optional hook for chip-specific deactivation, such as
    disabling module power and clock; may sleep

get_direction
    returns direction for signal "offset", 0=out, 1=in,
    (same as GPIOF_DIR_XXX), or negative error

direction_input
    configures signal "offset" as input, or returns error

direction_output
    configures signal "offset" as output, or returns error

get
    returns value for signal "offset", 0=low, 1=high, or negative error

get_multiple
    reads values for multiple signals defined by "mask" and
    stores them in "bits", returns 0 on success or negative error

set
    assigns output value for signal "offset"

set_multiple
    assigns output values for multiple signals defined by "mask"

set_config
    optional hook for all kinds of settings. Uses the same
    packed config format as generic pinconf.

to_irq
    optional hook supporting non-static \ :c:func:`gpio_to_irq`\  mappings;
    implementation may not sleep

dbg_show
    optional routine to show contents in debugfs; default code
    will be used when this is omitted, but custom code can show extra
    state (such as pullup/pulldown configuration).

base
    identifies the first GPIO number handled by this chip;
    or, if negative during registration, requests dynamic ID allocation.
    DEPRECATION: providing anything non-negative and nailing the base
    offset of GPIO chips is deprecated. Please pass -1 as base to
    let gpiolib select the chip base in all possible cases. We want to
    get rid of the static GPIO number space in the long run.

ngpio
    the number of GPIOs handled by this controller; the last GPIO
    handled is (base + ngpio - 1).

names
    if set, must be an array of strings to use as alternative
    names for the GPIOs in this chip. Any entry in the array
    may be NULL if there is no alias for the GPIO, however the
    array must be \ ``ngpio``\  entries long.  A name can include a single printk
    format specifier for an unsigned int.  It is substituted by the actual
    number of the gpio.

can_sleep
    flag must be set iff \ :c:func:`get`\ /set() methods sleep, as they
    must while accessing GPIO expander chips over I2C or SPI. This
    implies that if the chip supports IRQs, these IRQs need to be threaded
    as the chip access may sleep when e.g. reading out the IRQ status
    registers.

read_reg
    reader function for generic GPIO

write_reg
    writer function for generic GPIO

be_bits
    if the generic GPIO has big endian bit order (bit 31 is representing
    line 0, bit 30 is line 1 ... bit 0 is line 31) this is set to true by the
    generic GPIO core. It is for internal housekeeping only.

reg_dat
    data (in) register for generic GPIO

reg_set
    output set register (out=high) for generic GPIO

reg_clr
    output clear register (out=low) for generic GPIO

reg_dir
    direction setting register for generic GPIO

bgpio_bits
    number of register bits used for a generic GPIO i.e.
    <register width> * 8

bgpio_lock
    used to lock chip->bgpio_data. Also, this is needed to keep
    shadowed and real data registers writes together.

bgpio_data
    shadowed data register for generic GPIO to clear/set bits
    safely.

bgpio_dir
    shadowed direction register for generic GPIO to clear/set
    direction safely.

irq

    Integrates interrupt chip functionality with the GPIO chip. Can be
    used to handle IRQs for most practical cases.

need_valid_mask

    If set core allocates \ ``valid_mask``\  with all bits set to one.

valid_mask

    If not \ ``NULL``\  holds bitmask of GPIOs which are valid to be used
    from the chip.

of_node

    Pointer to a device tree node representing this GPIO controller.

of_gpio_n_cells

    Number of cells used to form the GPIO specifier.

of_xlate

    Callback to translate a device tree GPIO specifier into a chip-
    relative GPIO number and flags.

.. _`gpio_chip.description`:

Description
-----------

A gpio_chip can help platforms abstract various sources of GPIOs so
they can all be accessed through a common programing interface.
Example sources would be SOC controllers, FPGAs, multifunction
chips, dedicated GPIO expanders, and so on.

Each chip controls a number of signals, identified in method calls
by "offset" values in the range 0..(@ngpio - 1).  When those signals
are referenced through calls like gpio_get_value(gpio), the offset
is calculated by subtracting \ ``base``\  from the gpio number.

.. _`gpiochip_add_data`:

gpiochip_add_data
=================

.. c:function::  gpiochip_add_data( chip,  data)

    register a gpio_chip

    :param  chip:
        the chip to register, with chip->base initialized

    :param  data:
        driver-private data associated with this chip

.. _`gpiochip_add_data.context`:

Context
-------

potentially before irqs will work

.. _`gpiochip_add_data.description`:

Description
-----------

When \ :c:func:`gpiochip_add_data`\  is called very early during boot, so that GPIOs
can be freely used, the chip->parent device must be registered before
the gpio framework's \ :c:func:`arch_initcall`\ .  Otherwise sysfs initialization
for GPIOs will fail rudely.

\ :c:func:`gpiochip_add_data`\  must only be called after gpiolib initialization,
ie after \ :c:func:`core_initcall`\ .

If chip->base is negative, this requests dynamic assignment of
a range of valid GPIOs.

.. _`gpiochip_add_data.return`:

Return
------

A negative errno if the chip can't be registered, such as because the
chip->base is invalid or already associated with a different chip.
Otherwise it returns zero as a success code.

.. _`gpio_pin_range`:

struct gpio_pin_range
=====================

.. c:type:: struct gpio_pin_range

    pin range controlled by a gpio chip

.. _`gpio_pin_range.definition`:

Definition
----------

.. code-block:: c

    struct gpio_pin_range {
        struct list_head node;
        struct pinctrl_dev *pctldev;
        struct pinctrl_gpio_range range;
    }

.. _`gpio_pin_range.members`:

Members
-------

node
    list for maintaining set of pin ranges, used internally

pctldev
    pinctrl device which handles corresponding pins

range
    actual range of pins controlled by a gpio controller

.. This file was automatic generated / don't edit.

