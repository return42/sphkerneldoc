.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib.c

.. _`gpio_to_desc`:

gpio_to_desc
============

.. c:function:: struct gpio_desc *gpio_to_desc(unsigned gpio)

    :param unsigned gpio:
        *undescribed*

.. _`gpiochip_get_desc`:

gpiochip_get_desc
=================

.. c:function:: struct gpio_desc *gpiochip_get_desc(struct gpio_chip *chip, u16 hwnum)

    :param struct gpio_chip \*chip:
        *undescribed*

    :param u16 hwnum:
        *undescribed*

.. _`desc_to_gpio`:

desc_to_gpio
============

.. c:function:: int desc_to_gpio(const struct gpio_desc *desc)

    This should disappear in the future but is needed since we still use GPIO numbers for error messages and sysfs nodes

    :param const struct gpio_desc \*desc:
        *undescribed*

.. _`gpiod_to_chip`:

gpiod_to_chip
=============

.. c:function:: struct gpio_chip *gpiod_to_chip(const struct gpio_desc *desc)

    Return the GPIO chip to which a GPIO descriptor belongs

    :param const struct gpio_desc \*desc:
        descriptor to return the chip of

.. _`gpiod_get_direction`:

gpiod_get_direction
===================

.. c:function:: int gpiod_get_direction(struct gpio_desc *desc)

    return the current direction of a GPIO

    :param struct gpio_desc \*desc:
        GPIO to get the direction of

.. _`gpiod_get_direction.description`:

Description
-----------

Return GPIOF_DIR_IN or GPIOF_DIR_OUT, or an error code in case of error.

This function may sleep if \ :c:func:`gpiod_cansleep`\  is true.

.. _`gpio_name_to_desc`:

gpio_name_to_desc
=================

.. c:function:: struct gpio_desc *gpio_name_to_desc(const char * const name)

    :param const char \* const name:
        *undescribed*

.. _`linehandle_state`:

struct linehandle_state
=======================

.. c:type:: struct linehandle_state

    contains the state of a userspace handle

.. _`linehandle_state.definition`:

Definition
----------

.. code-block:: c

    struct linehandle_state {
        struct gpio_device *gdev;
        const char *label;
        struct gpio_desc  *descs[GPIOHANDLES_MAX];
        u32 numdescs;
    }

.. _`linehandle_state.members`:

Members
-------

gdev
    the GPIO device the handle pertains to

label
    consumer label used to tag descriptors

descs
    the GPIO descriptors held by this handle

numdescs
    the number of descriptors held in the descs array

.. _`lineevent_state`:

struct lineevent_state
======================

.. c:type:: struct lineevent_state

    contains the state of a userspace event

.. _`lineevent_state.definition`:

Definition
----------

.. code-block:: c

    struct lineevent_state {
        struct gpio_device *gdev;
        const char *label;
        struct gpio_desc *desc;
        u32 eflags;
        int irq;
        wait_queue_head_t wait;
        DECLARE_KFIFO(events# struct gpioevent_data# 16);
        struct mutex read_lock;
    }

.. _`lineevent_state.members`:

Members
-------

gdev
    the GPIO device the event pertains to

label
    consumer label used to tag descriptors

desc
    the GPIO descriptor held by this event

eflags
    the event flags this line was requested with

irq
    the interrupt that trigger in response to events on this GPIO

wait
    wait queue that handles blocking reads of events

16)
    *undescribed*

read_lock
    mutex lock to protect reads from colliding with adding
    new events to the FIFO

.. _`gpio_ioctl`:

gpio_ioctl
==========

.. c:function:: long gpio_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    ioctl handler for the GPIO chardev

    :param struct file \*filp:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`gpio_chrdev_open`:

gpio_chrdev_open
================

.. c:function:: int gpio_chrdev_open(struct inode *inode, struct file *filp)

    open the chardev for ioctl operations

    :param struct inode \*inode:
        inode for this chardev

    :param struct file \*filp:
        file struct for storing private data
        Returns 0 on success

.. _`gpio_chrdev_release`:

gpio_chrdev_release
===================

.. c:function:: int gpio_chrdev_release(struct inode *inode, struct file *filp)

    close chardev after ioctl operations

    :param struct inode \*inode:
        inode for this chardev

    :param struct file \*filp:
        file struct for storing private data
        Returns 0 on success

.. _`gpiochip_add_data`:

gpiochip_add_data
=================

.. c:function:: int gpiochip_add_data(struct gpio_chip *chip, void *data)

    register a gpio_chip

    :param struct gpio_chip \*chip:
        the chip to register, with chip->base initialized

    :param void \*data:
        *undescribed*

.. _`gpiochip_add_data.context`:

Context
-------

potentially before irqs will work

.. _`gpiochip_add_data.description`:

Description
-----------

Returns a negative errno if the chip can't be registered, such as
because the chip->base is invalid or already associated with a
different chip.  Otherwise it returns zero as a success code.

When \ :c:func:`gpiochip_add_data`\  is called very early during boot, so that GPIOs
can be freely used, the chip->parent device must be registered before
the gpio framework's \ :c:func:`arch_initcall`\ .  Otherwise sysfs initialization
for GPIOs will fail rudely.

\ :c:func:`gpiochip_add_data`\  must only be called after gpiolib initialization,
ie after \ :c:func:`core_initcall`\ .

If chip->base is negative, this requests dynamic assignment of
a range of valid GPIOs.

.. _`gpiochip_get_data`:

gpiochip_get_data
=================

.. c:function:: void *gpiochip_get_data(struct gpio_chip *chip)

    get per-subdriver data for the chip

    :param struct gpio_chip \*chip:
        *undescribed*

.. _`gpiochip_remove`:

gpiochip_remove
===============

.. c:function:: void gpiochip_remove(struct gpio_chip *chip)

    unregister a gpio_chip

    :param struct gpio_chip \*chip:
        the chip to unregister

.. _`gpiochip_remove.description`:

Description
-----------

A gpio_chip with any GPIOs still requested may not be removed.

.. _`devm_gpiochip_add_data`:

devm_gpiochip_add_data
======================

.. c:function:: int devm_gpiochip_add_data(struct device *dev, struct gpio_chip *chip, void *data)

    Resource manager \ :c:func:`piochip_add_data`\ 

    :param struct device \*dev:
        the device pointer on which irq_chip belongs to.

    :param struct gpio_chip \*chip:
        the chip to register, with chip->base initialized

    :param void \*data:
        *undescribed*

.. _`devm_gpiochip_add_data.context`:

Context
-------

potentially before irqs will work

.. _`devm_gpiochip_add_data.description`:

Description
-----------

Returns a negative errno if the chip can't be registered, such as
because the chip->base is invalid or already associated with a
different chip.  Otherwise it returns zero as a success code.

The gpio chip automatically be released when the device is unbound.

.. _`devm_gpiochip_remove`:

devm_gpiochip_remove
====================

.. c:function:: void devm_gpiochip_remove(struct device *dev, struct gpio_chip *chip)

    Resource manager of \ :c:func:`gpiochip_remove`\ 

    :param struct device \*dev:
        device for which which resource was allocated

    :param struct gpio_chip \*chip:
        the chip to remove

.. _`devm_gpiochip_remove.description`:

Description
-----------

A gpio_chip with any GPIOs still requested may not be removed.

.. _`gpiochip_find`:

gpiochip_find
=============

.. c:function:: struct gpio_chip *gpiochip_find(void *data, int (*match)(struct gpio_chip *chip, void *data))

    iterator for locating a specific gpio_chip

    :param void \*data:
        data to pass to match function

    :param int (\*match)(struct gpio_chip \*chip, void \*data):
        *undescribed*

.. _`gpiochip_find.description`:

Description
-----------

Similar to bus_find_device.  It returns a reference to a gpio_chip as
determined by a user supplied \ ``match``\  callback.  The callback should return
0 if the device doesn't match and non-zero if it does.  If the callback is
non-zero, this function will return to the caller and not iterate over any
more gpio_chips.

.. _`gpiochip_set_chained_irqchip`:

gpiochip_set_chained_irqchip
============================

.. c:function:: void gpiochip_set_chained_irqchip(struct gpio_chip *gpiochip, struct irq_chip *irqchip, int parent_irq, irq_flow_handler_t parent_handler)

    sets a chained irqchip to a gpiochip

    :param struct gpio_chip \*gpiochip:
        the gpiochip to set the irqchip chain to

    :param struct irq_chip \*irqchip:
        the irqchip to chain to the gpiochip

    :param int parent_irq:
        the irq number corresponding to the parent IRQ for this
        chained irqchip

    :param irq_flow_handler_t parent_handler:
        the parent interrupt handler for the accumulated IRQ
        coming out of the gpiochip. If the interrupt is nested rather than
        cascaded, pass NULL in this handler argument

.. _`gpiochip_irq_map`:

gpiochip_irq_map
================

.. c:function:: int gpiochip_irq_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hwirq)

    maps an IRQ into a GPIO irqchip

    :param struct irq_domain \*d:
        the irqdomain used by this irqchip

    :param unsigned int irq:
        the global irq number used by this GPIO irqchip irq

    :param irq_hw_number_t hwirq:
        the local IRQ/GPIO line offset on this gpiochip

.. _`gpiochip_irq_map.description`:

Description
-----------

This function will set up the mapping for a certain IRQ line on a
gpiochip by assigning the gpiochip as chip data, and using the irqchip
stored inside the gpiochip.

.. _`gpiochip_irqchip_remove`:

gpiochip_irqchip_remove
=======================

.. c:function:: void gpiochip_irqchip_remove(struct gpio_chip *gpiochip)

    removes an irqchip added to a gpiochip

    :param struct gpio_chip \*gpiochip:
        the gpiochip to remove the irqchip from

.. _`gpiochip_irqchip_remove.description`:

Description
-----------

This is called only from \ :c:func:`gpiochip_remove`\ 

.. _`_gpiochip_irqchip_add`:

_gpiochip_irqchip_add
=====================

.. c:function:: int _gpiochip_irqchip_add(struct gpio_chip *gpiochip, struct irq_chip *irqchip, unsigned int first_irq, irq_flow_handler_t handler, unsigned int type, struct lock_class_key *lock_key)

    adds an irqchip to a gpiochip

    :param struct gpio_chip \*gpiochip:
        the gpiochip to add the irqchip to

    :param struct irq_chip \*irqchip:
        the irqchip to add to the gpiochip

    :param unsigned int first_irq:
        if not dynamically assigned, the base (first) IRQ to
        allocate gpiochip irqs from

    :param irq_flow_handler_t handler:
        the irq handler to use (often a predefined irq core function)

    :param unsigned int type:
        the default type for IRQs on this irqchip, pass IRQ_TYPE_NONE
        to have the core avoid setting up any default type in the hardware.

    :param struct lock_class_key \*lock_key:
        lockdep class

.. _`_gpiochip_irqchip_add.description`:

Description
-----------

This function closely associates a certain irqchip with a certain
gpiochip, providing an irq domain to translate the local IRQs to
global irqs in the gpiolib core, and making sure that the gpiochip
is passed as chip data to all related functions. Driver callbacks
need to use \ :c:func:`gpiochip_get_data`\  to get their local state containers back
from the gpiochip passed as chip data. An irqdomain will be stored
in the gpiochip that shall be used by the driver to handle IRQ number
translation. The gpiochip will need to be initialized and registered
before calling this function.

This function will handle two cell:ed simple IRQs and assumes all
the pins on the gpiochip can generate a unique IRQ. Everything else
need to be open coded.

.. _`gpiochip_generic_request`:

gpiochip_generic_request
========================

.. c:function:: int gpiochip_generic_request(struct gpio_chip *chip, unsigned offset)

    request the gpio function for a pin

    :param struct gpio_chip \*chip:
        the gpiochip owning the GPIO

    :param unsigned offset:
        the offset of the GPIO to request for GPIO function

.. _`gpiochip_generic_free`:

gpiochip_generic_free
=====================

.. c:function:: void gpiochip_generic_free(struct gpio_chip *chip, unsigned offset)

    free the gpio function from a pin

    :param struct gpio_chip \*chip:
        the gpiochip to request the gpio function for

    :param unsigned offset:
        the offset of the GPIO to free from GPIO function

.. _`gpiochip_add_pingroup_range`:

gpiochip_add_pingroup_range
===========================

.. c:function:: int gpiochip_add_pingroup_range(struct gpio_chip *chip, struct pinctrl_dev *pctldev, unsigned int gpio_offset, const char *pin_group)

    add a range for GPIO <-> pin mapping

    :param struct gpio_chip \*chip:
        the gpiochip to add the range for

    :param struct pinctrl_dev \*pctldev:
        the pin controller to map to

    :param unsigned int gpio_offset:
        the start offset in the current gpio_chip number space

    :param const char \*pin_group:
        name of the pin group inside the pin controller

.. _`gpiochip_add_pin_range`:

gpiochip_add_pin_range
======================

.. c:function:: int gpiochip_add_pin_range(struct gpio_chip *chip, const char *pinctl_name, unsigned int gpio_offset, unsigned int pin_offset, unsigned int npins)

    add a range for GPIO <-> pin mapping

    :param struct gpio_chip \*chip:
        the gpiochip to add the range for

    :param const char \*pinctl_name:
        *undescribed*

    :param unsigned int gpio_offset:
        the start offset in the current gpio_chip number space

    :param unsigned int pin_offset:
        the start offset in the pin controller number space

    :param unsigned int npins:
        the number of pins from the offset of each pin space (GPIO and
        pin controller) to accumulate in this range

.. _`gpiochip_remove_pin_ranges`:

gpiochip_remove_pin_ranges
==========================

.. c:function:: void gpiochip_remove_pin_ranges(struct gpio_chip *chip)

    remove all the GPIO <-> pin mappings

    :param struct gpio_chip \*chip:
        the chip to remove all the mappings for

.. _`gpiochip_is_requested`:

gpiochip_is_requested
=====================

.. c:function:: const char *gpiochip_is_requested(struct gpio_chip *chip, unsigned offset)

    return string iff signal was requested

    :param struct gpio_chip \*chip:
        controller managing the signal

    :param unsigned offset:
        of signal within controller's 0..(ngpio - 1) range

.. _`gpiochip_is_requested.description`:

Description
-----------

Returns NULL if the GPIO is not currently requested, else a string.
The string returned is the label passed to \ :c:func:`gpio_request`\ ; if none has been
passed it is a meaningless, non-NULL constant.

This function is for use by GPIO controller drivers.  The label can
help with diagnostics, and knowing that the signal is used as a GPIO
can help avoid accidentally multiplexing it to another controller.

.. _`gpiochip_request_own_desc`:

gpiochip_request_own_desc
=========================

.. c:function:: struct gpio_desc *gpiochip_request_own_desc(struct gpio_chip *chip, u16 hwnum, const char *label)

    Allow GPIO chip to request its own descriptor

    :param struct gpio_chip \*chip:
        *undescribed*

    :param u16 hwnum:
        *undescribed*

    :param const char \*label:
        label for the GPIO

.. _`gpiochip_request_own_desc.description`:

Description
-----------

Function allows GPIO chip drivers to request and use their own GPIO
descriptors via gpiolib API. Difference to \ :c:func:`gpiod_request`\  is that this
function will not increase reference count of the GPIO chip module. This
allows the GPIO chip module to be unloaded as needed (we assume that the
GPIO chip driver handles freeing the GPIOs it has requested).

.. _`gpiochip_free_own_desc`:

gpiochip_free_own_desc
======================

.. c:function:: void gpiochip_free_own_desc(struct gpio_desc *desc)

    Free GPIO requested by the chip driver

    :param struct gpio_desc \*desc:
        GPIO descriptor to free

.. _`gpiochip_free_own_desc.description`:

Description
-----------

Function frees the given GPIO requested previously with
\ :c:func:`gpiochip_request_own_desc`\ .

.. _`gpiod_direction_input`:

gpiod_direction_input
=====================

.. c:function:: int gpiod_direction_input(struct gpio_desc *desc)

    set the GPIO direction to input

    :param struct gpio_desc \*desc:
        GPIO to set to input

.. _`gpiod_direction_input.description`:

Description
-----------

Set the direction of the passed GPIO to input, such as \ :c:func:`gpiod_get_value`\  can
be called safely on it.

Return 0 in case of success, else an error code.

.. _`gpiod_direction_output_raw`:

gpiod_direction_output_raw
==========================

.. c:function:: int gpiod_direction_output_raw(struct gpio_desc *desc, int value)

    set the GPIO direction to output

    :param struct gpio_desc \*desc:
        GPIO to set to output

    :param int value:
        initial output value of the GPIO

.. _`gpiod_direction_output_raw.description`:

Description
-----------

Set the direction of the passed GPIO to output, such as \ :c:func:`gpiod_set_value`\  can
be called safely on it. The initial value of the output must be specified
as raw value on the physical line without regard for the ACTIVE_LOW status.

Return 0 in case of success, else an error code.

.. _`gpiod_direction_output`:

gpiod_direction_output
======================

.. c:function:: int gpiod_direction_output(struct gpio_desc *desc, int value)

    set the GPIO direction to output

    :param struct gpio_desc \*desc:
        GPIO to set to output

    :param int value:
        initial output value of the GPIO

.. _`gpiod_direction_output.description`:

Description
-----------

Set the direction of the passed GPIO to output, such as \ :c:func:`gpiod_set_value`\  can
be called safely on it. The initial value of the output must be specified
as the logical value of the GPIO, i.e. taking its ACTIVE_LOW status into
account.

Return 0 in case of success, else an error code.

.. _`gpiod_set_debounce`:

gpiod_set_debounce
==================

.. c:function:: int gpiod_set_debounce(struct gpio_desc *desc, unsigned debounce)

    sets \ ``debounce``\  time for a \ ``gpio``\ 

    :param struct gpio_desc \*desc:
        *undescribed*

    :param unsigned debounce:
        debounce time is microseconds

.. _`gpiod_set_debounce.description`:

Description
-----------

returns -ENOTSUPP if the controller does not support setting
debounce.

.. _`gpiod_is_active_low`:

gpiod_is_active_low
===================

.. c:function:: int gpiod_is_active_low(const struct gpio_desc *desc)

    test whether a GPIO is active-low or not

    :param const struct gpio_desc \*desc:
        the gpio descriptor to test

.. _`gpiod_is_active_low.description`:

Description
-----------

Returns 1 if the GPIO is active-low, 0 otherwise.

.. _`gpiod_get_raw_value`:

gpiod_get_raw_value
===================

.. c:function:: int gpiod_get_raw_value(const struct gpio_desc *desc)

    return a gpio's raw value

    :param const struct gpio_desc \*desc:
        gpio whose value will be returned

.. _`gpiod_get_raw_value.description`:

Description
-----------

Return the GPIO's raw value, i.e. the value of the physical line disregarding
its ACTIVE_LOW status, or negative errno on failure.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_get_value`:

gpiod_get_value
===============

.. c:function:: int gpiod_get_value(const struct gpio_desc *desc)

    return a gpio's value

    :param const struct gpio_desc \*desc:
        gpio whose value will be returned

.. _`gpiod_get_value.description`:

Description
-----------

Return the GPIO's logical value, i.e. taking the ACTIVE_LOW status into
account, or negative errno on failure.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_raw_value`:

gpiod_set_raw_value
===================

.. c:function:: void gpiod_set_raw_value(struct gpio_desc *desc, int value)

    assign a gpio's raw value

    :param struct gpio_desc \*desc:
        gpio whose value will be assigned

    :param int value:
        value to assign

.. _`gpiod_set_raw_value.description`:

Description
-----------

Set the raw value of the GPIO, i.e. the value of its physical line without
regard for its ACTIVE_LOW status.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_value`:

gpiod_set_value
===============

.. c:function:: void gpiod_set_value(struct gpio_desc *desc, int value)

    assign a gpio's value

    :param struct gpio_desc \*desc:
        gpio whose value will be assigned

    :param int value:
        value to assign

.. _`gpiod_set_value.description`:

Description
-----------

Set the logical value of the GPIO, i.e. taking its ACTIVE_LOW status into
account

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_raw_array_value`:

gpiod_set_raw_array_value
=========================

.. c:function:: void gpiod_set_raw_array_value(unsigned int array_size, struct gpio_desc **desc_array, int *value_array)

    assign values to an array of GPIOs

    :param unsigned int array_size:
        number of elements in the descriptor / value arrays

    :param struct gpio_desc \*\*desc_array:
        array of GPIO descriptors whose values will be assigned

    :param int \*value_array:
        array of values to assign

.. _`gpiod_set_raw_array_value.description`:

Description
-----------

Set the raw values of the GPIOs, i.e. the values of the physical lines
without regard for their ACTIVE_LOW status.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_array_value`:

gpiod_set_array_value
=====================

.. c:function:: void gpiod_set_array_value(unsigned int array_size, struct gpio_desc **desc_array, int *value_array)

    assign values to an array of GPIOs

    :param unsigned int array_size:
        number of elements in the descriptor / value arrays

    :param struct gpio_desc \*\*desc_array:
        array of GPIO descriptors whose values will be assigned

    :param int \*value_array:
        array of values to assign

.. _`gpiod_set_array_value.description`:

Description
-----------

Set the logical values of the GPIOs, i.e. taking their ACTIVE_LOW status
into account.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_cansleep`:

gpiod_cansleep
==============

.. c:function:: int gpiod_cansleep(const struct gpio_desc *desc)

    report whether gpio value access may sleep

    :param const struct gpio_desc \*desc:
        gpio to check

.. _`gpiod_to_irq`:

gpiod_to_irq
============

.. c:function:: int gpiod_to_irq(const struct gpio_desc *desc)

    return the IRQ corresponding to a GPIO

    :param const struct gpio_desc \*desc:
        gpio whose IRQ will be returned (already requested)

.. _`gpiod_to_irq.description`:

Description
-----------

Return the IRQ corresponding to the passed GPIO, or an error code in case of
error.

.. _`gpiochip_lock_as_irq`:

gpiochip_lock_as_irq
====================

.. c:function:: int gpiochip_lock_as_irq(struct gpio_chip *chip, unsigned int offset)

    lock a GPIO to be used as IRQ

    :param struct gpio_chip \*chip:
        the chip the GPIO to lock belongs to

    :param unsigned int offset:
        the offset of the GPIO to lock as IRQ

.. _`gpiochip_lock_as_irq.description`:

Description
-----------

This is used directly by GPIO drivers that want to lock down
a certain GPIO line to be used for IRQs.

.. _`gpiochip_unlock_as_irq`:

gpiochip_unlock_as_irq
======================

.. c:function:: void gpiochip_unlock_as_irq(struct gpio_chip *chip, unsigned int offset)

    unlock a GPIO used as IRQ

    :param struct gpio_chip \*chip:
        the chip the GPIO to lock belongs to

    :param unsigned int offset:
        the offset of the GPIO to lock as IRQ

.. _`gpiochip_unlock_as_irq.description`:

Description
-----------

This is used directly by GPIO drivers that want to indicate
that a certain GPIO is no longer used exclusively for IRQ.

.. _`gpiod_get_raw_value_cansleep`:

gpiod_get_raw_value_cansleep
============================

.. c:function:: int gpiod_get_raw_value_cansleep(const struct gpio_desc *desc)

    return a gpio's raw value

    :param const struct gpio_desc \*desc:
        gpio whose value will be returned

.. _`gpiod_get_raw_value_cansleep.description`:

Description
-----------

Return the GPIO's raw value, i.e. the value of the physical line disregarding
its ACTIVE_LOW status, or negative errno on failure.

This function is to be called from contexts that can sleep.

.. _`gpiod_get_value_cansleep`:

gpiod_get_value_cansleep
========================

.. c:function:: int gpiod_get_value_cansleep(const struct gpio_desc *desc)

    return a gpio's value

    :param const struct gpio_desc \*desc:
        gpio whose value will be returned

.. _`gpiod_get_value_cansleep.description`:

Description
-----------

Return the GPIO's logical value, i.e. taking the ACTIVE_LOW status into
account, or negative errno on failure.

This function is to be called from contexts that can sleep.

.. _`gpiod_set_raw_value_cansleep`:

gpiod_set_raw_value_cansleep
============================

.. c:function:: void gpiod_set_raw_value_cansleep(struct gpio_desc *desc, int value)

    assign a gpio's raw value

    :param struct gpio_desc \*desc:
        gpio whose value will be assigned

    :param int value:
        value to assign

.. _`gpiod_set_raw_value_cansleep.description`:

Description
-----------

Set the raw value of the GPIO, i.e. the value of its physical line without
regard for its ACTIVE_LOW status.

This function is to be called from contexts that can sleep.

.. _`gpiod_set_value_cansleep`:

gpiod_set_value_cansleep
========================

.. c:function:: void gpiod_set_value_cansleep(struct gpio_desc *desc, int value)

    assign a gpio's value

    :param struct gpio_desc \*desc:
        gpio whose value will be assigned

    :param int value:
        value to assign

.. _`gpiod_set_value_cansleep.description`:

Description
-----------

Set the logical value of the GPIO, i.e. taking its ACTIVE_LOW status into
account

This function is to be called from contexts that can sleep.

.. _`gpiod_set_raw_array_value_cansleep`:

gpiod_set_raw_array_value_cansleep
==================================

.. c:function:: void gpiod_set_raw_array_value_cansleep(unsigned int array_size, struct gpio_desc **desc_array, int *value_array)

    assign values to an array of GPIOs

    :param unsigned int array_size:
        number of elements in the descriptor / value arrays

    :param struct gpio_desc \*\*desc_array:
        array of GPIO descriptors whose values will be assigned

    :param int \*value_array:
        array of values to assign

.. _`gpiod_set_raw_array_value_cansleep.description`:

Description
-----------

Set the raw values of the GPIOs, i.e. the values of the physical lines
without regard for their ACTIVE_LOW status.

This function is to be called from contexts that can sleep.

.. _`gpiod_set_array_value_cansleep`:

gpiod_set_array_value_cansleep
==============================

.. c:function:: void gpiod_set_array_value_cansleep(unsigned int array_size, struct gpio_desc **desc_array, int *value_array)

    assign values to an array of GPIOs

    :param unsigned int array_size:
        number of elements in the descriptor / value arrays

    :param struct gpio_desc \*\*desc_array:
        array of GPIO descriptors whose values will be assigned

    :param int \*value_array:
        array of values to assign

.. _`gpiod_set_array_value_cansleep.description`:

Description
-----------

Set the logical values of the GPIOs, i.e. taking their ACTIVE_LOW status
into account.

This function is to be called from contexts that can sleep.

.. _`gpiod_add_lookup_table`:

gpiod_add_lookup_table
======================

.. c:function:: void gpiod_add_lookup_table(struct gpiod_lookup_table *table)

    register GPIO device consumers

    :param struct gpiod_lookup_table \*table:
        table of consumers to register

.. _`gpiod_remove_lookup_table`:

gpiod_remove_lookup_table
=========================

.. c:function:: void gpiod_remove_lookup_table(struct gpiod_lookup_table *table)

    unregister GPIO device consumers

    :param struct gpiod_lookup_table \*table:
        table of consumers to unregister

.. _`gpiod_count`:

gpiod_count
===========

.. c:function:: int gpiod_count(struct device *dev, const char *con_id)

    return the number of GPIOs associated with a device / function or -ENOENT if no GPIO has been assigned to the requested function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

.. _`gpiod_get`:

gpiod_get
=========

.. c:function:: struct gpio_desc *gpiod_get(struct device *dev, const char *con_id, enum gpiod_flags flags)

    obtain a GPIO for a given GPIO function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`gpiod_get.description`:

Description
-----------

Return the GPIO descriptor corresponding to the function con_id of device
dev, -ENOENT if no GPIO has been assigned to the requested function, or
another \ :c:func:`IS_ERR`\  code if an error occurred while trying to acquire the GPIO.

.. _`gpiod_get_optional`:

gpiod_get_optional
==================

.. c:function:: struct gpio_desc *gpiod_get_optional(struct device *dev, const char *con_id, enum gpiod_flags flags)

    obtain an optional GPIO for a given GPIO function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`gpiod_get_optional.description`:

Description
-----------

This is equivalent to \ :c:func:`gpiod_get`\ , except that when no GPIO was assigned to
the requested function it will return NULL. This is convenient for drivers
that need to handle optional GPIOs.

.. _`gpiod_configure_flags`:

gpiod_configure_flags
=====================

.. c:function:: int gpiod_configure_flags(struct gpio_desc *desc, const char *con_id, unsigned long lflags, enum gpiod_flags dflags)

    helper function to configure a given GPIO

    :param struct gpio_desc \*desc:
        gpio whose value will be assigned

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned long lflags:
        gpio_lookup_flags - returned from \ :c:func:`of_find_gpio`\  or
        \ :c:func:`of_get_gpio_hog`\ 

    :param enum gpiod_flags dflags:
        gpiod_flags - optional GPIO initialization flags

.. _`gpiod_configure_flags.description`:

Description
-----------

Return 0 on success, -ENOENT if no GPIO has been assigned to the
requested function and/or index, or another \ :c:func:`IS_ERR`\  code if an error
occurred while trying to acquire the GPIO.

.. _`gpiod_get_index`:

gpiod_get_index
===============

.. c:function:: struct gpio_desc *gpiod_get_index(struct device *dev, const char *con_id, unsigned int idx, enum gpiod_flags flags)

    obtain a GPIO from a multi-index GPIO function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned int idx:
        index of the GPIO to obtain in the consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`gpiod_get_index.description`:

Description
-----------

This variant of \ :c:func:`gpiod_get`\  allows to access GPIOs other than the first
defined one for functions that define several GPIOs.

Return a valid GPIO descriptor, -ENOENT if no GPIO has been assigned to the
requested function and/or index, or another \ :c:func:`IS_ERR`\  code if an error
occurred while trying to acquire the GPIO.

.. _`fwnode_get_named_gpiod`:

fwnode_get_named_gpiod
======================

.. c:function:: struct gpio_desc *fwnode_get_named_gpiod(struct fwnode_handle *fwnode, const char *propname)

    obtain a GPIO from firmware node

    :param struct fwnode_handle \*fwnode:
        handle of the firmware node

    :param const char \*propname:
        name of the firmware property representing the GPIO

.. _`fwnode_get_named_gpiod.description`:

Description
-----------

This function can be used for drivers that get their configuration
from firmware.

Function properly finds the corresponding GPIO using whatever is the
underlying firmware interface and then makes sure that the GPIO
descriptor is requested before it is returned to the caller.

In case of error an \ :c:func:`ERR_PTR`\  is returned.

.. _`gpiod_get_index_optional`:

gpiod_get_index_optional
========================

.. c:function:: struct gpio_desc *gpiod_get_index_optional(struct device *dev, const char *con_id, unsigned int index, enum gpiod_flags flags)

    obtain an optional GPIO from a multi-index GPIO function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

    :param unsigned int index:
        index of the GPIO to obtain in the consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`gpiod_get_index_optional.description`:

Description
-----------

This is equivalent to \ :c:func:`gpiod_get_index`\ , except that when no GPIO with the
specified index was assigned to the requested function it will return NULL.
This is convenient for drivers that need to handle optional GPIOs.

.. _`gpiod_hog`:

gpiod_hog
=========

.. c:function:: int gpiod_hog(struct gpio_desc *desc, const char *name, unsigned long lflags, enum gpiod_flags dflags)

    Hog the specified GPIO desc given the provided flags

    :param struct gpio_desc \*desc:
        gpio whose value will be assigned

    :param const char \*name:
        gpio line name

    :param unsigned long lflags:
        gpio_lookup_flags - returned from \ :c:func:`of_find_gpio`\  or
        \ :c:func:`of_get_gpio_hog`\ 

    :param enum gpiod_flags dflags:
        gpiod_flags - optional GPIO initialization flags

.. _`gpiochip_free_hogs`:

gpiochip_free_hogs
==================

.. c:function:: void gpiochip_free_hogs(struct gpio_chip *chip)

    Scan gpio-controller chip and release GPIO hog

    :param struct gpio_chip \*chip:
        gpio chip to act on

.. _`gpiochip_free_hogs.description`:

Description
-----------

This is only used by of_gpiochip_remove to free hogged gpios

.. _`gpiod_get_array`:

gpiod_get_array
===============

.. c:function:: struct gpio_descs *gpiod_get_array(struct device *dev, const char *con_id, enum gpiod_flags flags)

    obtain multiple GPIOs from a multi-index GPIO function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`gpiod_get_array.description`:

Description
-----------

This function acquires all the GPIOs defined under a given function.

Return a struct gpio_descs containing an array of descriptors, -ENOENT if
no GPIO has been assigned to the requested function, or another \ :c:func:`IS_ERR`\ 
code if an error occurred while trying to acquire the GPIOs.

.. _`gpiod_get_array_optional`:

gpiod_get_array_optional
========================

.. c:function:: struct gpio_descs *gpiod_get_array_optional(struct device *dev, const char *con_id, enum gpiod_flags flags)

    obtain multiple GPIOs from a multi-index GPIO function

    :param struct device \*dev:
        GPIO consumer, can be NULL for system-global GPIOs

    :param const char \*con_id:
        function within the GPIO consumer

    :param enum gpiod_flags flags:
        optional GPIO initialization flags

.. _`gpiod_get_array_optional.description`:

Description
-----------

This is equivalent to \ :c:func:`gpiod_get_array`\ , except that when no GPIO was
assigned to the requested function it will return NULL.

.. _`gpiod_put`:

gpiod_put
=========

.. c:function:: void gpiod_put(struct gpio_desc *desc)

    dispose of a GPIO descriptor

    :param struct gpio_desc \*desc:
        GPIO descriptor to dispose of

.. _`gpiod_put.description`:

Description
-----------

No descriptor can be used after \ :c:func:`gpiod_put`\  has been called on it.

.. _`gpiod_put_array`:

gpiod_put_array
===============

.. c:function:: void gpiod_put_array(struct gpio_descs *descs)

    dispose of multiple GPIO descriptors

    :param struct gpio_descs \*descs:
        struct gpio_descs containing an array of descriptors

.. This file was automatic generated / don't edit.

