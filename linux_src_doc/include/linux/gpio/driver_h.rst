.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gpio/driver.h

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
        unsigned long (*pin2mask)(struct gpio_chip *gc, unsigned int pin);
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
        struct irq_chip *irqchip;
        struct irq_domain *irqdomain;
        unsigned int irq_base;
        irq_flow_handler_t irq_handler;
        unsigned int irq_default_type;
        unsigned int irq_chained_parent;
        bool irq_nested;
        bool irq_need_valid_mask;
        unsigned long *irq_valid_mask;
        struct lock_class_key *lock_key;
    #endif
    #if defined(CONFIG_OF_GPIO)
        struct device_node *of_node;
        int of_gpio_n_cells;
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

pin2mask
    some generic GPIO controllers work with the big-endian bits
    notation, e.g. in a 8-bits register, GPIO7 is the least significant
    bit. This callback assigns the right bit mask.

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
    <register width> \* 8

bgpio_lock
    used to lock chip->bgpio_data. Also, this is needed to keep
    shadowed and real data registers writes together.

bgpio_data
    shadowed data register for generic GPIO to clear/set bits
    safely.

bgpio_dir
    shadowed direction register for generic GPIO to clear/set
    direction safely.

irqchip
    GPIO IRQ chip impl, provided by GPIO driver

irqdomain
    Interrupt translation domain; responsible for mapping
    between GPIO hwirq number and linux irq number

irq_base
    first linux IRQ number assigned to GPIO IRQ chip (deprecated)

irq_handler
    the irq handler to use (often a predefined irq core function)
    for GPIO IRQs, provided by GPIO driver

irq_default_type
    default IRQ triggering type applied during GPIO driver
    initialization, provided by GPIO driver

irq_chained_parent
    GPIO IRQ chip parent/bank linux irq number,
    provided by GPIO driver for chained interrupt (not for nested
    interrupts).

irq_nested
    True if set the interrupt handling is nested.

irq_need_valid_mask
    If set core allocates \ ``irq_valid_mask``\  with all
    bits set to one

irq_valid_mask
    If not \ ``NULL``\  holds bitmask of GPIOs which are valid to
    be included in IRQ domain of the chip

lock_key
    per GPIO IRQ chip lockdep class

of_node
    *undescribed*

of_gpio_n_cells
    *undescribed*

of_xlate
    *undescribed*

.. _`gpio_chip.deprecation`:

DEPRECATION
-----------

providing anything non-negative and nailing the base
offset of GPIO chips is deprecated. Please pass -1 as base to
let gpiolib select the chip base in all possible cases. We want to
get rid of the static GPIO number space in the long run.

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
    *undescribed*

pctldev
    pinctrl device which handles corresponding pins

range
    actual range of pins controlled by a gpio controller

.. This file was automatic generated / don't edit.

