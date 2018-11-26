.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpiolib.c

.. _`gpio_to_desc`:

gpio_to_desc
============

.. c:function:: struct gpio_desc *gpio_to_desc(unsigned gpio)

    Convert a GPIO number to its descriptor

    :param gpio:
        global GPIO number
    :type gpio: unsigned

.. _`gpio_to_desc.return`:

Return
------

The GPIO descriptor associated with the given GPIO, or \ ``NULL``\  if no GPIO
with the given number exists in the system.

.. _`gpiochip_get_desc`:

gpiochip_get_desc
=================

.. c:function:: struct gpio_desc *gpiochip_get_desc(struct gpio_chip *chip, u16 hwnum)

    get the GPIO descriptor corresponding to the given hardware number for this chip

    :param chip:
        GPIO chip
    :type chip: struct gpio_chip \*

    :param hwnum:
        hardware number of the GPIO for this chip
    :type hwnum: u16

.. _`gpiochip_get_desc.return`:

Return
------

A pointer to the GPIO descriptor or \ ``ERR_PTR``\ (-EINVAL) if no GPIO exists
in the given chip for the specified hardware number.

.. _`desc_to_gpio`:

desc_to_gpio
============

.. c:function:: int desc_to_gpio(const struct gpio_desc *desc)

    convert a GPIO descriptor to the integer namespace

    :param desc:
        GPIO descriptor
    :type desc: const struct gpio_desc \*

.. _`desc_to_gpio.description`:

Description
-----------

This should disappear in the future but is needed since we still
use GPIO numbers for error messages and sysfs nodes.

.. _`desc_to_gpio.return`:

Return
------

The global GPIO number for the GPIO specified by its descriptor.

.. _`gpiod_to_chip`:

gpiod_to_chip
=============

.. c:function:: struct gpio_chip *gpiod_to_chip(const struct gpio_desc *desc)

    Return the GPIO chip to which a GPIO descriptor belongs

    :param desc:
        descriptor to return the chip of
    :type desc: const struct gpio_desc \*

.. _`gpiod_get_direction`:

gpiod_get_direction
===================

.. c:function:: int gpiod_get_direction(struct gpio_desc *desc)

    return the current direction of a GPIO

    :param desc:
        GPIO to get the direction of
    :type desc: struct gpio_desc \*

.. _`gpiod_get_direction.description`:

Description
-----------

Returns 0 for output, 1 for input, or an error code in case of error.

This function may sleep if \ :c:func:`gpiod_cansleep`\  is true.

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
        struct gpio_desc *descs[GPIOHANDLES_MAX];
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
        DECLARE_KFIFO(events, struct gpioevent_data, 16);
        struct mutex read_lock;
        u64 timestamp;
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

events
    KFIFO for the GPIO events

read_lock
    mutex lock to protect reads from colliding with adding
    new events to the FIFO

timestamp
    cache for the timestamp storing it between hardirq
    and IRQ thread, used to bring the timestamp close to the actual
    event

.. _`gpio_chrdev_open`:

gpio_chrdev_open
================

.. c:function:: int gpio_chrdev_open(struct inode *inode, struct file *filp)

    open the chardev for ioctl operations

    :param inode:
        inode for this chardev
    :type inode: struct inode \*

    :param filp:
        file struct for storing private data
        Returns 0 on success
    :type filp: struct file \*

.. _`gpio_chrdev_release`:

gpio_chrdev_release
===================

.. c:function:: int gpio_chrdev_release(struct inode *inode, struct file *filp)

    close chardev after ioctl operations

    :param inode:
        inode for this chardev
    :type inode: struct inode \*

    :param filp:
        file struct for storing private data
        Returns 0 on success
    :type filp: struct file \*

.. _`gpiochip_get_data`:

gpiochip_get_data
=================

.. c:function:: void *gpiochip_get_data(struct gpio_chip *chip)

    get per-subdriver data for the chip

    :param chip:
        GPIO chip
    :type chip: struct gpio_chip \*

.. _`gpiochip_get_data.return`:

Return
------

The per-subdriver data for the chip.

.. _`gpiochip_remove`:

gpiochip_remove
===============

.. c:function:: void gpiochip_remove(struct gpio_chip *chip)

    unregister a gpio_chip

    :param chip:
        the chip to unregister
    :type chip: struct gpio_chip \*

.. _`gpiochip_remove.description`:

Description
-----------

A gpio_chip with any GPIOs still requested may not be removed.

.. _`devm_gpiochip_add_data`:

devm_gpiochip_add_data
======================

.. c:function:: int devm_gpiochip_add_data(struct device *dev, struct gpio_chip *chip, void *data)

    Resource manager \ :c:func:`gpiochip_add_data`\ 

    :param dev:
        pointer to the device that gpio_chip belongs to.
    :type dev: struct device \*

    :param chip:
        the chip to register, with chip->base initialized
    :type chip: struct gpio_chip \*

    :param data:
        driver-private data associated with this chip
    :type data: void \*

.. _`devm_gpiochip_add_data.context`:

Context
-------

potentially before irqs will work

.. _`devm_gpiochip_add_data.description`:

Description
-----------

The gpio chip automatically be released when the device is unbound.

.. _`devm_gpiochip_add_data.return`:

Return
------

A negative errno if the chip can't be registered, such as because the
chip->base is invalid or already associated with a different chip.
Otherwise it returns zero as a success code.

.. _`devm_gpiochip_remove`:

devm_gpiochip_remove
====================

.. c:function:: void devm_gpiochip_remove(struct device *dev, struct gpio_chip *chip)

    Resource manager of \ :c:func:`gpiochip_remove`\ 

    :param dev:
        device for which which resource was allocated
    :type dev: struct device \*

    :param chip:
        the chip to remove
    :type chip: struct gpio_chip \*

.. _`devm_gpiochip_remove.description`:

Description
-----------

A gpio_chip with any GPIOs still requested may not be removed.

.. _`gpiochip_find`:

gpiochip_find
=============

.. c:function:: struct gpio_chip *gpiochip_find(void *data, int (*match)(struct gpio_chip *chip, void *data))

    iterator for locating a specific gpio_chip

    :param data:
        data to pass to match function
    :type data: void \*

    :param int (\*match)(struct gpio_chip \*chip, void \*data):
        Callback function to check gpio_chip

.. _`gpiochip_find.description`:

Description
-----------

Similar to bus_find_device.  It returns a reference to a gpio_chip as
determined by a user supplied \ ``match``\  callback.  The callback should return
0 if the device doesn't match and non-zero if it does.  If the callback is
non-zero, this function will return to the caller and not iterate over any
more gpio_chips.

.. _`gpiochip_set_cascaded_irqchip`:

gpiochip_set_cascaded_irqchip
=============================

.. c:function:: void gpiochip_set_cascaded_irqchip(struct gpio_chip *gpiochip, unsigned int parent_irq, irq_flow_handler_t parent_handler)

    connects a cascaded irqchip to a gpiochip

    :param gpiochip:
        the gpiochip to set the irqchip chain to
    :type gpiochip: struct gpio_chip \*

    :param parent_irq:
        the irq number corresponding to the parent IRQ for this
        chained irqchip
    :type parent_irq: unsigned int

    :param parent_handler:
        the parent interrupt handler for the accumulated IRQ
        coming out of the gpiochip. If the interrupt is nested rather than
        cascaded, pass NULL in this handler argument
    :type parent_handler: irq_flow_handler_t

.. _`gpiochip_set_chained_irqchip`:

gpiochip_set_chained_irqchip
============================

.. c:function:: void gpiochip_set_chained_irqchip(struct gpio_chip *gpiochip, struct irq_chip *irqchip, unsigned int parent_irq, irq_flow_handler_t parent_handler)

    connects a chained irqchip to a gpiochip

    :param gpiochip:
        the gpiochip to set the irqchip chain to
    :type gpiochip: struct gpio_chip \*

    :param irqchip:
        the irqchip to chain to the gpiochip
    :type irqchip: struct irq_chip \*

    :param parent_irq:
        the irq number corresponding to the parent IRQ for this
        chained irqchip
    :type parent_irq: unsigned int

    :param parent_handler:
        the parent interrupt handler for the accumulated IRQ
        coming out of the gpiochip.
    :type parent_handler: irq_flow_handler_t

.. _`gpiochip_set_nested_irqchip`:

gpiochip_set_nested_irqchip
===========================

.. c:function:: void gpiochip_set_nested_irqchip(struct gpio_chip *gpiochip, struct irq_chip *irqchip, unsigned int parent_irq)

    connects a nested irqchip to a gpiochip

    :param gpiochip:
        the gpiochip to set the irqchip nested handler to
    :type gpiochip: struct gpio_chip \*

    :param irqchip:
        the irqchip to nest to the gpiochip
    :type irqchip: struct irq_chip \*

    :param parent_irq:
        the irq number corresponding to the parent IRQ for this
        nested irqchip
    :type parent_irq: unsigned int

.. _`gpiochip_irq_map`:

gpiochip_irq_map
================

.. c:function:: int gpiochip_irq_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hwirq)

    maps an IRQ into a GPIO irqchip

    :param d:
        the irqdomain used by this irqchip
    :type d: struct irq_domain \*

    :param irq:
        the global irq number used by this GPIO irqchip irq
    :type irq: unsigned int

    :param hwirq:
        the local IRQ/GPIO line offset on this gpiochip
    :type hwirq: irq_hw_number_t

.. _`gpiochip_irq_map.description`:

Description
-----------

This function will set up the mapping for a certain IRQ line on a
gpiochip by assigning the gpiochip as chip data, and using the irqchip
stored inside the gpiochip.

.. _`gpiochip_add_irqchip`:

gpiochip_add_irqchip
====================

.. c:function:: int gpiochip_add_irqchip(struct gpio_chip *gpiochip, struct lock_class_key *lock_key, struct lock_class_key *request_key)

    adds an IRQ chip to a GPIO chip

    :param gpiochip:
        the GPIO chip to add the IRQ chip to
    :type gpiochip: struct gpio_chip \*

    :param lock_key:
        lockdep class for IRQ lock
    :type lock_key: struct lock_class_key \*

    :param request_key:
        lockdep class for IRQ request
    :type request_key: struct lock_class_key \*

.. _`gpiochip_irqchip_remove`:

gpiochip_irqchip_remove
=======================

.. c:function:: void gpiochip_irqchip_remove(struct gpio_chip *gpiochip)

    removes an irqchip added to a gpiochip

    :param gpiochip:
        the gpiochip to remove the irqchip from
    :type gpiochip: struct gpio_chip \*

.. _`gpiochip_irqchip_remove.description`:

Description
-----------

This is called only from \ :c:func:`gpiochip_remove`\ 

.. _`gpiochip_irqchip_add_key`:

gpiochip_irqchip_add_key
========================

.. c:function:: int gpiochip_irqchip_add_key(struct gpio_chip *gpiochip, struct irq_chip *irqchip, unsigned int first_irq, irq_flow_handler_t handler, unsigned int type, bool threaded, struct lock_class_key *lock_key, struct lock_class_key *request_key)

    adds an irqchip to a gpiochip

    :param gpiochip:
        the gpiochip to add the irqchip to
    :type gpiochip: struct gpio_chip \*

    :param irqchip:
        the irqchip to add to the gpiochip
    :type irqchip: struct irq_chip \*

    :param first_irq:
        if not dynamically assigned, the base (first) IRQ to
        allocate gpiochip irqs from
    :type first_irq: unsigned int

    :param handler:
        the irq handler to use (often a predefined irq core function)
    :type handler: irq_flow_handler_t

    :param type:
        the default type for IRQs on this irqchip, pass IRQ_TYPE_NONE
        to have the core avoid setting up any default type in the hardware.
    :type type: unsigned int

    :param threaded:
        whether this irqchip uses a nested thread handler
    :type threaded: bool

    :param lock_key:
        lockdep class for IRQ lock
    :type lock_key: struct lock_class_key \*

    :param request_key:
        lockdep class for IRQ request
    :type request_key: struct lock_class_key \*

.. _`gpiochip_irqchip_add_key.description`:

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

    :param chip:
        the gpiochip owning the GPIO
    :type chip: struct gpio_chip \*

    :param offset:
        the offset of the GPIO to request for GPIO function
    :type offset: unsigned

.. _`gpiochip_generic_free`:

gpiochip_generic_free
=====================

.. c:function:: void gpiochip_generic_free(struct gpio_chip *chip, unsigned offset)

    free the gpio function from a pin

    :param chip:
        the gpiochip to request the gpio function for
    :type chip: struct gpio_chip \*

    :param offset:
        the offset of the GPIO to free from GPIO function
    :type offset: unsigned

.. _`gpiochip_generic_config`:

gpiochip_generic_config
=======================

.. c:function:: int gpiochip_generic_config(struct gpio_chip *chip, unsigned offset, unsigned long config)

    apply configuration for a pin

    :param chip:
        the gpiochip owning the GPIO
    :type chip: struct gpio_chip \*

    :param offset:
        the offset of the GPIO to apply the configuration
    :type offset: unsigned

    :param config:
        the configuration to be applied
    :type config: unsigned long

.. _`gpiochip_add_pingroup_range`:

gpiochip_add_pingroup_range
===========================

.. c:function:: int gpiochip_add_pingroup_range(struct gpio_chip *chip, struct pinctrl_dev *pctldev, unsigned int gpio_offset, const char *pin_group)

    add a range for GPIO <-> pin mapping

    :param chip:
        the gpiochip to add the range for
    :type chip: struct gpio_chip \*

    :param pctldev:
        the pin controller to map to
    :type pctldev: struct pinctrl_dev \*

    :param gpio_offset:
        the start offset in the current gpio_chip number space
    :type gpio_offset: unsigned int

    :param pin_group:
        name of the pin group inside the pin controller
    :type pin_group: const char \*

.. _`gpiochip_add_pingroup_range.description`:

Description
-----------

Calling this function directly from a DeviceTree-supported
pinctrl driver is DEPRECATED. Please see Section 2.1 of
Documentation/devicetree/bindings/gpio/gpio.txt on how to
bind pinctrl and gpio drivers via the "gpio-ranges" property.

.. _`gpiochip_add_pin_range`:

gpiochip_add_pin_range
======================

.. c:function:: int gpiochip_add_pin_range(struct gpio_chip *chip, const char *pinctl_name, unsigned int gpio_offset, unsigned int pin_offset, unsigned int npins)

    add a range for GPIO <-> pin mapping

    :param chip:
        the gpiochip to add the range for
    :type chip: struct gpio_chip \*

    :param pinctl_name:
        the \ :c:func:`dev_name`\  of the pin controller to map to
    :type pinctl_name: const char \*

    :param gpio_offset:
        the start offset in the current gpio_chip number space
    :type gpio_offset: unsigned int

    :param pin_offset:
        the start offset in the pin controller number space
    :type pin_offset: unsigned int

    :param npins:
        the number of pins from the offset of each pin space (GPIO and
        pin controller) to accumulate in this range
    :type npins: unsigned int

.. _`gpiochip_add_pin_range.return`:

Return
------

0 on success, or a negative error-code on failure.

Calling this function directly from a DeviceTree-supported
pinctrl driver is DEPRECATED. Please see Section 2.1 of
Documentation/devicetree/bindings/gpio/gpio.txt on how to
bind pinctrl and gpio drivers via the "gpio-ranges" property.

.. _`gpiochip_remove_pin_ranges`:

gpiochip_remove_pin_ranges
==========================

.. c:function:: void gpiochip_remove_pin_ranges(struct gpio_chip *chip)

    remove all the GPIO <-> pin mappings

    :param chip:
        the chip to remove all the mappings for
    :type chip: struct gpio_chip \*

.. _`gpiochip_is_requested`:

gpiochip_is_requested
=====================

.. c:function:: const char *gpiochip_is_requested(struct gpio_chip *chip, unsigned offset)

    return string iff signal was requested

    :param chip:
        controller managing the signal
    :type chip: struct gpio_chip \*

    :param offset:
        of signal within controller's 0..(ngpio - 1) range
    :type offset: unsigned

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

    :param chip:
        GPIO chip
    :type chip: struct gpio_chip \*

    :param hwnum:
        hardware number of the GPIO for which to request the descriptor
    :type hwnum: u16

    :param label:
        label for the GPIO
    :type label: const char \*

.. _`gpiochip_request_own_desc.description`:

Description
-----------

Function allows GPIO chip drivers to request and use their own GPIO
descriptors via gpiolib API. Difference to \ :c:func:`gpiod_request`\  is that this
function will not increase reference count of the GPIO chip module. This
allows the GPIO chip module to be unloaded as needed (we assume that the
GPIO chip driver handles freeing the GPIOs it has requested).

.. _`gpiochip_request_own_desc.return`:

Return
------

A pointer to the GPIO descriptor, or an \ :c:func:`ERR_PTR`\ -encoded negative error
code on failure.

.. _`gpiochip_free_own_desc`:

gpiochip_free_own_desc
======================

.. c:function:: void gpiochip_free_own_desc(struct gpio_desc *desc)

    Free GPIO requested by the chip driver

    :param desc:
        GPIO descriptor to free
    :type desc: struct gpio_desc \*

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

    :param desc:
        GPIO to set to input
    :type desc: struct gpio_desc \*

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

    :param desc:
        GPIO to set to output
    :type desc: struct gpio_desc \*

    :param value:
        initial output value of the GPIO
    :type value: int

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

    :param desc:
        GPIO to set to output
    :type desc: struct gpio_desc \*

    :param value:
        initial output value of the GPIO
    :type value: int

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

    sets \ ``debounce``\  time for a GPIO

    :param desc:
        descriptor of the GPIO for which to set debounce time
    :type desc: struct gpio_desc \*

    :param debounce:
        debounce time in microseconds
    :type debounce: unsigned

.. _`gpiod_set_debounce.return`:

Return
------

0 on success, \ ``-ENOTSUPP``\  if the controller doesn't support setting the
debounce time.

.. _`gpiod_set_transitory`:

gpiod_set_transitory
====================

.. c:function:: int gpiod_set_transitory(struct gpio_desc *desc, bool transitory)

    Lose or retain GPIO state on suspend or reset

    :param desc:
        descriptor of the GPIO for which to configure persistence
    :type desc: struct gpio_desc \*

    :param transitory:
        True to lose state on suspend or reset, false for persistence
    :type transitory: bool

.. _`gpiod_set_transitory.return`:

Return
------

0 on success, otherwise a negative error code.

.. _`gpiod_is_active_low`:

gpiod_is_active_low
===================

.. c:function:: int gpiod_is_active_low(const struct gpio_desc *desc)

    test whether a GPIO is active-low or not

    :param desc:
        the gpio descriptor to test
    :type desc: const struct gpio_desc \*

.. _`gpiod_is_active_low.description`:

Description
-----------

Returns 1 if the GPIO is active-low, 0 otherwise.

.. _`gpiod_get_raw_value`:

gpiod_get_raw_value
===================

.. c:function:: int gpiod_get_raw_value(const struct gpio_desc *desc)

    return a gpio's raw value

    :param desc:
        gpio whose value will be returned
    :type desc: const struct gpio_desc \*

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

    :param desc:
        gpio whose value will be returned
    :type desc: const struct gpio_desc \*

.. _`gpiod_get_value.description`:

Description
-----------

Return the GPIO's logical value, i.e. taking the ACTIVE_LOW status into
account, or negative errno on failure.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_get_raw_array_value`:

gpiod_get_raw_array_value
=========================

.. c:function:: int gpiod_get_raw_array_value(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    read raw values from an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be read
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap to store the read values
    :type value_bitmap: unsigned long \*

.. _`gpiod_get_raw_array_value.description`:

Description
-----------

Read the raw values of the GPIOs, i.e. the values of the physical lines
without regard for their ACTIVE_LOW status.  Return 0 in case of success,
else an error code.

This function should be called from contexts where we cannot sleep,
and it will complain if the GPIO chip functions potentially sleep.

.. _`gpiod_get_array_value`:

gpiod_get_array_value
=====================

.. c:function:: int gpiod_get_array_value(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    read values from an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be read
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap to store the read values
    :type value_bitmap: unsigned long \*

.. _`gpiod_get_array_value.description`:

Description
-----------

Read the logical values of the GPIOs, i.e. taking their ACTIVE_LOW status
into account.  Return 0 in case of success, else an error code.

This function should be called from contexts where we cannot sleep,
and it will complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_raw_value`:

gpiod_set_raw_value
===================

.. c:function:: void gpiod_set_raw_value(struct gpio_desc *desc, int value)

    assign a gpio's raw value

    :param desc:
        gpio whose value will be assigned
    :type desc: struct gpio_desc \*

    :param value:
        value to assign
    :type value: int

.. _`gpiod_set_raw_value.description`:

Description
-----------

Set the raw value of the GPIO, i.e. the value of its physical line without
regard for its ACTIVE_LOW status.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_value_nocheck`:

gpiod_set_value_nocheck
=======================

.. c:function:: void gpiod_set_value_nocheck(struct gpio_desc *desc, int value)

    set a GPIO line value without checking

    :param desc:
        the descriptor to set the value on
    :type desc: struct gpio_desc \*

    :param value:
        value to set
    :type value: int

.. _`gpiod_set_value_nocheck.description`:

Description
-----------

This sets the value of a GPIO line backing a descriptor, applying
different semantic quirks like active low and open drain/source
handling.

.. _`gpiod_set_value`:

gpiod_set_value
===============

.. c:function:: void gpiod_set_value(struct gpio_desc *desc, int value)

    assign a gpio's value

    :param desc:
        gpio whose value will be assigned
    :type desc: struct gpio_desc \*

    :param value:
        value to assign
    :type value: int

.. _`gpiod_set_value.description`:

Description
-----------

Set the logical value of the GPIO, i.e. taking its ACTIVE_LOW,
OPEN_DRAIN and OPEN_SOURCE flags into account.

This function should be called from contexts where we cannot sleep, and will
complain if the GPIO chip functions potentially sleep.

.. _`gpiod_set_raw_array_value`:

gpiod_set_raw_array_value
=========================

.. c:function:: int gpiod_set_raw_array_value(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    assign values to an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be assigned
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap of values to assign
    :type value_bitmap: unsigned long \*

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

.. c:function:: int gpiod_set_array_value(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    assign values to an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be assigned
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap of values to assign
    :type value_bitmap: unsigned long \*

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

    :param desc:
        gpio to check
    :type desc: const struct gpio_desc \*

.. _`gpiod_set_consumer_name`:

gpiod_set_consumer_name
=======================

.. c:function:: void gpiod_set_consumer_name(struct gpio_desc *desc, const char *name)

    set the consumer name for the descriptor

    :param desc:
        gpio to set the consumer name on
    :type desc: struct gpio_desc \*

    :param name:
        the new consumer name
    :type name: const char \*

.. _`gpiod_to_irq`:

gpiod_to_irq
============

.. c:function:: int gpiod_to_irq(const struct gpio_desc *desc)

    return the IRQ corresponding to a GPIO

    :param desc:
        gpio whose IRQ will be returned (already requested)
    :type desc: const struct gpio_desc \*

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

    :param chip:
        the chip the GPIO to lock belongs to
    :type chip: struct gpio_chip \*

    :param offset:
        the offset of the GPIO to lock as IRQ
    :type offset: unsigned int

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

    :param chip:
        the chip the GPIO to lock belongs to
    :type chip: struct gpio_chip \*

    :param offset:
        the offset of the GPIO to lock as IRQ
    :type offset: unsigned int

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

    :param desc:
        gpio whose value will be returned
    :type desc: const struct gpio_desc \*

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

    :param desc:
        gpio whose value will be returned
    :type desc: const struct gpio_desc \*

.. _`gpiod_get_value_cansleep.description`:

Description
-----------

Return the GPIO's logical value, i.e. taking the ACTIVE_LOW status into
account, or negative errno on failure.

This function is to be called from contexts that can sleep.

.. _`gpiod_get_raw_array_value_cansleep`:

gpiod_get_raw_array_value_cansleep
==================================

.. c:function:: int gpiod_get_raw_array_value_cansleep(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    read raw values from an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be read
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap to store the read values
    :type value_bitmap: unsigned long \*

.. _`gpiod_get_raw_array_value_cansleep.description`:

Description
-----------

Read the raw values of the GPIOs, i.e. the values of the physical lines
without regard for their ACTIVE_LOW status.  Return 0 in case of success,
else an error code.

This function is to be called from contexts that can sleep.

.. _`gpiod_get_array_value_cansleep`:

gpiod_get_array_value_cansleep
==============================

.. c:function:: int gpiod_get_array_value_cansleep(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    read values from an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be read
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap to store the read values
    :type value_bitmap: unsigned long \*

.. _`gpiod_get_array_value_cansleep.description`:

Description
-----------

Read the logical values of the GPIOs, i.e. taking their ACTIVE_LOW status
into account.  Return 0 in case of success, else an error code.

This function is to be called from contexts that can sleep.

.. _`gpiod_set_raw_value_cansleep`:

gpiod_set_raw_value_cansleep
============================

.. c:function:: void gpiod_set_raw_value_cansleep(struct gpio_desc *desc, int value)

    assign a gpio's raw value

    :param desc:
        gpio whose value will be assigned
    :type desc: struct gpio_desc \*

    :param value:
        value to assign
    :type value: int

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

    :param desc:
        gpio whose value will be assigned
    :type desc: struct gpio_desc \*

    :param value:
        value to assign
    :type value: int

.. _`gpiod_set_value_cansleep.description`:

Description
-----------

Set the logical value of the GPIO, i.e. taking its ACTIVE_LOW status into
account

This function is to be called from contexts that can sleep.

.. _`gpiod_set_raw_array_value_cansleep`:

gpiod_set_raw_array_value_cansleep
==================================

.. c:function:: int gpiod_set_raw_array_value_cansleep(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    assign values to an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be assigned
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap of values to assign
    :type value_bitmap: unsigned long \*

.. _`gpiod_set_raw_array_value_cansleep.description`:

Description
-----------

Set the raw values of the GPIOs, i.e. the values of the physical lines
without regard for their ACTIVE_LOW status.

This function is to be called from contexts that can sleep.

.. _`gpiod_add_lookup_tables`:

gpiod_add_lookup_tables
=======================

.. c:function:: void gpiod_add_lookup_tables(struct gpiod_lookup_table **tables, size_t n)

    register GPIO device consumers

    :param tables:
        list of tables of consumers to register
    :type tables: struct gpiod_lookup_table \*\*

    :param n:
        number of tables in the list
    :type n: size_t

.. _`gpiod_set_array_value_cansleep`:

gpiod_set_array_value_cansleep
==============================

.. c:function:: int gpiod_set_array_value_cansleep(unsigned int array_size, struct gpio_desc **desc_array, struct gpio_array *array_info, unsigned long *value_bitmap)

    assign values to an array of GPIOs

    :param array_size:
        number of elements in the descriptor array / value bitmap
    :type array_size: unsigned int

    :param desc_array:
        array of GPIO descriptors whose values will be assigned
    :type desc_array: struct gpio_desc \*\*

    :param array_info:
        information on applicability of fast bitmap processing path
    :type array_info: struct gpio_array \*

    :param value_bitmap:
        bitmap of values to assign
    :type value_bitmap: unsigned long \*

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

    :param table:
        table of consumers to register
    :type table: struct gpiod_lookup_table \*

.. _`gpiod_remove_lookup_table`:

gpiod_remove_lookup_table
=========================

.. c:function:: void gpiod_remove_lookup_table(struct gpiod_lookup_table *table)

    unregister GPIO device consumers

    :param table:
        table of consumers to unregister
    :type table: struct gpiod_lookup_table \*

.. _`gpiod_add_hogs`:

gpiod_add_hogs
==============

.. c:function:: void gpiod_add_hogs(struct gpiod_hog *hogs)

    register a set of GPIO hogs from machine code

    :param hogs:
        table of gpio hog entries with a zeroed sentinel at the end
    :type hogs: struct gpiod_hog \*

.. _`gpiod_count`:

gpiod_count
===========

.. c:function:: int gpiod_count(struct device *dev, const char *con_id)

    return the number of GPIOs associated with a device / function or -ENOENT if no GPIO has been assigned to the requested function

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

.. _`gpiod_get`:

gpiod_get
=========

.. c:function:: struct gpio_desc *gpiod_get(struct device *dev, const char *con_id, enum gpiod_flags flags)

    obtain a GPIO for a given GPIO function

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param flags:
        optional GPIO initialization flags
    :type flags: enum gpiod_flags

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

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param flags:
        optional GPIO initialization flags
    :type flags: enum gpiod_flags

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

    :param desc:
        gpio whose value will be assigned
    :type desc: struct gpio_desc \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param lflags:
        gpio_lookup_flags - returned from \ :c:func:`of_find_gpio`\  or
        \ :c:func:`of_get_gpio_hog`\ 
    :type lflags: unsigned long

    :param dflags:
        gpiod_flags - optional GPIO initialization flags
    :type dflags: enum gpiod_flags

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

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param idx:
        index of the GPIO to obtain in the consumer
    :type idx: unsigned int

    :param flags:
        optional GPIO initialization flags
    :type flags: enum gpiod_flags

.. _`gpiod_get_index.description`:

Description
-----------

This variant of \ :c:func:`gpiod_get`\  allows to access GPIOs other than the first
defined one for functions that define several GPIOs.

Return a valid GPIO descriptor, -ENOENT if no GPIO has been assigned to the
requested function and/or index, or another \ :c:func:`IS_ERR`\  code if an error
occurred while trying to acquire the GPIO.

.. _`gpiod_get_from_of_node`:

gpiod_get_from_of_node
======================

.. c:function:: struct gpio_desc *gpiod_get_from_of_node(struct device_node *node, const char *propname, int index, enum gpiod_flags dflags, const char *label)

    obtain a GPIO from an OF node

    :param node:
        handle of the OF node
    :type node: struct device_node \*

    :param propname:
        name of the DT property representing the GPIO
    :type propname: const char \*

    :param index:
        index of the GPIO to obtain for the consumer
    :type index: int

    :param dflags:
        GPIO initialization flags
    :type dflags: enum gpiod_flags

    :param label:
        label to attach to the requested GPIO
    :type label: const char \*

.. _`gpiod_get_from_of_node.return`:

Return
------

On successful request the GPIO pin is configured in accordance with
provided \ ``dflags``\ . If the node does not have the requested GPIO
property, NULL is returned.

In case of error an \ :c:func:`ERR_PTR`\  is returned.

.. _`fwnode_get_named_gpiod`:

fwnode_get_named_gpiod
======================

.. c:function:: struct gpio_desc *fwnode_get_named_gpiod(struct fwnode_handle *fwnode, const char *propname, int index, enum gpiod_flags dflags, const char *label)

    obtain a GPIO from firmware node

    :param fwnode:
        handle of the firmware node
    :type fwnode: struct fwnode_handle \*

    :param propname:
        name of the firmware property representing the GPIO
    :type propname: const char \*

    :param index:
        index of the GPIO to obtain for the consumer
    :type index: int

    :param dflags:
        GPIO initialization flags
    :type dflags: enum gpiod_flags

    :param label:
        label to attach to the requested GPIO
    :type label: const char \*

.. _`fwnode_get_named_gpiod.description`:

Description
-----------

This function can be used for drivers that get their configuration
from opaque firmware.

The function properly finds the corresponding GPIO using whatever is the
underlying firmware interface and then makes sure that the GPIO
descriptor is requested before it is returned to the caller.

.. _`fwnode_get_named_gpiod.return`:

Return
------

On successful request the GPIO pin is configured in accordance with
provided \ ``dflags``\ .

In case of error an \ :c:func:`ERR_PTR`\  is returned.

.. _`gpiod_get_index_optional`:

gpiod_get_index_optional
========================

.. c:function:: struct gpio_desc *gpiod_get_index_optional(struct device *dev, const char *con_id, unsigned int index, enum gpiod_flags flags)

    obtain an optional GPIO from a multi-index GPIO function

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param index:
        index of the GPIO to obtain in the consumer
    :type index: unsigned int

    :param flags:
        optional GPIO initialization flags
    :type flags: enum gpiod_flags

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

    :param desc:
        gpio whose value will be assigned
    :type desc: struct gpio_desc \*

    :param name:
        gpio line name
    :type name: const char \*

    :param lflags:
        gpio_lookup_flags - returned from \ :c:func:`of_find_gpio`\  or
        \ :c:func:`of_get_gpio_hog`\ 
    :type lflags: unsigned long

    :param dflags:
        gpiod_flags - optional GPIO initialization flags
    :type dflags: enum gpiod_flags

.. _`gpiochip_free_hogs`:

gpiochip_free_hogs
==================

.. c:function:: void gpiochip_free_hogs(struct gpio_chip *chip)

    Scan gpio-controller chip and release GPIO hog

    :param chip:
        gpio chip to act on
    :type chip: struct gpio_chip \*

.. _`gpiochip_free_hogs.description`:

Description
-----------

This is only used by of_gpiochip_remove to free hogged gpios

.. _`gpiod_get_array`:

gpiod_get_array
===============

.. c:function:: struct gpio_descs *gpiod_get_array(struct device *dev, const char *con_id, enum gpiod_flags flags)

    obtain multiple GPIOs from a multi-index GPIO function

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param flags:
        optional GPIO initialization flags
    :type flags: enum gpiod_flags

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

    :param dev:
        GPIO consumer, can be NULL for system-global GPIOs
    :type dev: struct device \*

    :param con_id:
        function within the GPIO consumer
    :type con_id: const char \*

    :param flags:
        optional GPIO initialization flags
    :type flags: enum gpiod_flags

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

    :param desc:
        GPIO descriptor to dispose of
    :type desc: struct gpio_desc \*

.. _`gpiod_put.description`:

Description
-----------

No descriptor can be used after \ :c:func:`gpiod_put`\  has been called on it.

.. _`gpiod_put_array`:

gpiod_put_array
===============

.. c:function:: void gpiod_put_array(struct gpio_descs *descs)

    dispose of multiple GPIO descriptors

    :param descs:
        struct gpio_descs containing an array of descriptors
    :type descs: struct gpio_descs \*

.. This file was automatic generated / don't edit.

