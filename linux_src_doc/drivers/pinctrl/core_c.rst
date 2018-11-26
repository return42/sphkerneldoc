.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/core.c

.. _`pinctrl_provide_dummies`:

pinctrl_provide_dummies
=======================

.. c:function:: void pinctrl_provide_dummies( void)

    indicate if pinctrl provides dummy state support

    :param void:
        no arguments
    :type void: 

.. _`pinctrl_provide_dummies.description`:

Description
-----------

Usually this function is called by platforms without pinctrl driver support
but run with some shared drivers using pinctrl APIs.
After calling this function, the pinctrl core will return successfully
with creating a dummy state for the driver to keep going smoothly.

.. _`get_pinctrl_dev_from_devname`:

get_pinctrl_dev_from_devname
============================

.. c:function:: struct pinctrl_dev *get_pinctrl_dev_from_devname(const char *devname)

    look up pin controller device

    :param devname:
        the name of a device instance, as returned by \ :c:func:`dev_name`\ 
    :type devname: const char \*

.. _`get_pinctrl_dev_from_devname.description`:

Description
-----------

Looks up a pin control device matching a certain device name or pure device
pointer, the pure device pointer will take precedence.

.. _`pin_get_from_name`:

pin_get_from_name
=================

.. c:function:: int pin_get_from_name(struct pinctrl_dev *pctldev, const char *name)

    look up a pin number from a name

    :param pctldev:
        the pin control device to lookup the pin on
    :type pctldev: struct pinctrl_dev \*

    :param name:
        the name of the pin to look up
    :type name: const char \*

.. _`pin_get_name`:

pin_get_name
============

.. c:function:: const char *pin_get_name(struct pinctrl_dev *pctldev, const unsigned pin)

    look up a pin name from a pin id

    :param pctldev:
        the pin control device to lookup the pin on
    :type pctldev: struct pinctrl_dev \*

    :param pin:
        *undescribed*
    :type pin: const unsigned

.. _`pin_is_valid`:

pin_is_valid
============

.. c:function:: bool pin_is_valid(struct pinctrl_dev *pctldev, int pin)

    check if pin exists on controller

    :param pctldev:
        the pin control device to check the pin on
    :type pctldev: struct pinctrl_dev \*

    :param pin:
        pin to check, use the local pin controller index number
    :type pin: int

.. _`pin_is_valid.description`:

Description
-----------

This tells us whether a certain pin exist on a certain pin controller or
not. Pin lists may be sparse, so some pins may not exist.

.. _`gpio_to_pin`:

gpio_to_pin
===========

.. c:function:: int gpio_to_pin(struct pinctrl_gpio_range *range, unsigned int gpio)

    GPIO range GPIO number to pin number translation

    :param range:
        GPIO range used for the translation
    :type range: struct pinctrl_gpio_range \*

    :param gpio:
        gpio pin to translate to a pin number
    :type gpio: unsigned int

.. _`gpio_to_pin.description`:

Description
-----------

Finds the pin number for a given GPIO using the specified GPIO range
as a base for translation. The distinction between linear GPIO ranges
and pin list based GPIO ranges is managed correctly by this function.

This function assumes the gpio is part of the specified GPIO range, use
only after making sure this is the case (e.g. by calling it on the
result of successful pinctrl_get_device_gpio_range calls)!

.. _`pinctrl_match_gpio_range`:

pinctrl_match_gpio_range
========================

.. c:function:: struct pinctrl_gpio_range *pinctrl_match_gpio_range(struct pinctrl_dev *pctldev, unsigned gpio)

    check if a certain GPIO pin is in range

    :param pctldev:
        pin controller device to check
    :type pctldev: struct pinctrl_dev \*

    :param gpio:
        gpio pin to check taken from the global GPIO pin space
    :type gpio: unsigned

.. _`pinctrl_match_gpio_range.description`:

Description
-----------

Tries to match a GPIO pin number to the ranges handled by a certain pin
controller, return the range or NULL

.. _`pinctrl_ready_for_gpio_range`:

pinctrl_ready_for_gpio_range
============================

.. c:function:: bool pinctrl_ready_for_gpio_range(unsigned gpio)

    check if other GPIO pins of the same GPIO chip are in range

    :param gpio:
        gpio pin to check taken from the global GPIO pin space
    :type gpio: unsigned

.. _`pinctrl_ready_for_gpio_range.description`:

Description
-----------

This function is complement of \ :c:func:`pinctrl_match_gpio_range`\ . If the return
value of \ :c:func:`pinctrl_match_gpio_range`\  is NULL, this function could be used
to check whether pinctrl device is ready or not. Maybe some GPIO pins
of the same GPIO chip don't have back-end pinctrl interface.
If the return value is true, it means that pinctrl device is ready & the
certain GPIO pin doesn't have back-end pinctrl device. If the return value
is false, it means that pinctrl device may not be ready.

.. _`pinctrl_get_device_gpio_range`:

pinctrl_get_device_gpio_range
=============================

.. c:function:: int pinctrl_get_device_gpio_range(unsigned gpio, struct pinctrl_dev **outdev, struct pinctrl_gpio_range **outrange)

    find device for GPIO range

    :param gpio:
        the pin to locate the pin controller for
    :type gpio: unsigned

    :param outdev:
        the pin control device if found
    :type outdev: struct pinctrl_dev \*\*

    :param outrange:
        the GPIO range if found
    :type outrange: struct pinctrl_gpio_range \*\*

.. _`pinctrl_get_device_gpio_range.description`:

Description
-----------

Find the pin controller handling a certain GPIO pin from the pinspace of
the GPIO subsystem, return the device and the matching GPIO range. Returns
-EPROBE_DEFER if the GPIO range could not be found in any device since it
may still have not been registered.

.. _`pinctrl_add_gpio_range`:

pinctrl_add_gpio_range
======================

.. c:function:: void pinctrl_add_gpio_range(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range)

    register a GPIO range for a controller

    :param pctldev:
        pin controller device to add the range to
    :type pctldev: struct pinctrl_dev \*

    :param range:
        the GPIO range to add
    :type range: struct pinctrl_gpio_range \*

.. _`pinctrl_add_gpio_range.description`:

Description
-----------

This adds a range of GPIOs to be handled by a certain pin controller. Call
this to register handled ranges after registering your pin controller.

.. _`pinctrl_find_gpio_range_from_pin`:

pinctrl_find_gpio_range_from_pin
================================

.. c:function:: struct pinctrl_gpio_range *pinctrl_find_gpio_range_from_pin(struct pinctrl_dev *pctldev, unsigned int pin)

    locate the GPIO range for a pin

    :param pctldev:
        the pin controller device to look in
    :type pctldev: struct pinctrl_dev \*

    :param pin:
        a controller-local number to find the range for
    :type pin: unsigned int

.. _`pinctrl_remove_gpio_range`:

pinctrl_remove_gpio_range
=========================

.. c:function:: void pinctrl_remove_gpio_range(struct pinctrl_dev *pctldev, struct pinctrl_gpio_range *range)

    remove a range of GPIOs from a pin controller

    :param pctldev:
        pin controller device to remove the range from
    :type pctldev: struct pinctrl_dev \*

    :param range:
        the GPIO range to remove
    :type range: struct pinctrl_gpio_range \*

.. _`pinctrl_generic_get_group_count`:

pinctrl_generic_get_group_count
===============================

.. c:function:: int pinctrl_generic_get_group_count(struct pinctrl_dev *pctldev)

    returns the number of pin groups

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

.. _`pinctrl_generic_get_group_name`:

pinctrl_generic_get_group_name
==============================

.. c:function:: const char *pinctrl_generic_get_group_name(struct pinctrl_dev *pctldev, unsigned int selector)

    returns the name of a pin group

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        group number
    :type selector: unsigned int

.. _`pinctrl_generic_get_group_pins`:

pinctrl_generic_get_group_pins
==============================

.. c:function:: int pinctrl_generic_get_group_pins(struct pinctrl_dev *pctldev, unsigned int selector, const unsigned int **pins, unsigned int *num_pins)

    gets the pin group pins

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        group number
    :type selector: unsigned int

    :param pins:
        pins in the group
    :type pins: const unsigned int \*\*

    :param num_pins:
        number of pins in the group
    :type num_pins: unsigned int \*

.. _`pinctrl_generic_get_group`:

pinctrl_generic_get_group
=========================

.. c:function:: struct group_desc *pinctrl_generic_get_group(struct pinctrl_dev *pctldev, unsigned int selector)

    returns a pin group based on the number

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        *undescribed*
    :type selector: unsigned int

.. _`pinctrl_generic_add_group`:

pinctrl_generic_add_group
=========================

.. c:function:: int pinctrl_generic_add_group(struct pinctrl_dev *pctldev, const char *name, int *pins, int num_pins, void *data)

    adds a new pin group

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param name:
        name of the pin group
    :type name: const char \*

    :param pins:
        pins in the pin group
    :type pins: int \*

    :param num_pins:
        number of pins in the pin group
    :type num_pins: int

    :param data:
        pin controller driver specific data
    :type data: void \*

.. _`pinctrl_generic_add_group.description`:

Description
-----------

Note that the caller must take care of locking.

.. _`pinctrl_generic_remove_group`:

pinctrl_generic_remove_group
============================

.. c:function:: int pinctrl_generic_remove_group(struct pinctrl_dev *pctldev, unsigned int selector)

    removes a numbered pin group

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

    :param selector:
        group number
    :type selector: unsigned int

.. _`pinctrl_generic_remove_group.description`:

Description
-----------

Note that the caller must take care of locking.

.. _`pinctrl_generic_free_groups`:

pinctrl_generic_free_groups
===========================

.. c:function:: void pinctrl_generic_free_groups(struct pinctrl_dev *pctldev)

    removes all pin groups

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

.. _`pinctrl_generic_free_groups.description`:

Description
-----------

Note that the caller must take care of locking. The pinctrl groups
are allocated with \ :c:func:`devm_kzalloc`\  so no need to free them here.

.. _`pinctrl_get_group_selector`:

pinctrl_get_group_selector
==========================

.. c:function:: int pinctrl_get_group_selector(struct pinctrl_dev *pctldev, const char *pin_group)

    returns the group selector for a group

    :param pctldev:
        the pin controller handling the group
    :type pctldev: struct pinctrl_dev \*

    :param pin_group:
        the pin group to look up
    :type pin_group: const char \*

.. _`pinctrl_gpio_request`:

pinctrl_gpio_request
====================

.. c:function:: int pinctrl_gpio_request(unsigned gpio)

    request a single pin to be used as GPIO

    :param gpio:
        the GPIO pin number from the GPIO subsystem number space
    :type gpio: unsigned

.. _`pinctrl_gpio_request.description`:

Description
-----------

This function should \*ONLY\* be used from gpiolib-based GPIO drivers,
as part of their \ :c:func:`gpio_request`\  semantics, platforms and individual drivers
shall \*NOT\* request GPIO pins to be muxed in.

.. _`pinctrl_gpio_free`:

pinctrl_gpio_free
=================

.. c:function:: void pinctrl_gpio_free(unsigned gpio)

    free control on a single pin, currently used as GPIO

    :param gpio:
        the GPIO pin number from the GPIO subsystem number space
    :type gpio: unsigned

.. _`pinctrl_gpio_free.description`:

Description
-----------

This function should \*ONLY\* be used from gpiolib-based GPIO drivers,
as part of their \ :c:func:`gpio_free`\  semantics, platforms and individual drivers
shall \*NOT\* request GPIO pins to be muxed out.

.. _`pinctrl_gpio_direction_input`:

pinctrl_gpio_direction_input
============================

.. c:function:: int pinctrl_gpio_direction_input(unsigned gpio)

    request a GPIO pin to go into input mode

    :param gpio:
        the GPIO pin number from the GPIO subsystem number space
    :type gpio: unsigned

.. _`pinctrl_gpio_direction_input.description`:

Description
-----------

This function should \*ONLY\* be used from gpiolib-based GPIO drivers,
as part of their \ :c:func:`gpio_direction_input`\  semantics, platforms and individual
drivers shall \*NOT\* touch pin control GPIO calls.

.. _`pinctrl_gpio_direction_output`:

pinctrl_gpio_direction_output
=============================

.. c:function:: int pinctrl_gpio_direction_output(unsigned gpio)

    request a GPIO pin to go into output mode

    :param gpio:
        the GPIO pin number from the GPIO subsystem number space
    :type gpio: unsigned

.. _`pinctrl_gpio_direction_output.description`:

Description
-----------

This function should \*ONLY\* be used from gpiolib-based GPIO drivers,
as part of their \ :c:func:`gpio_direction_output`\  semantics, platforms and individual
drivers shall \*NOT\* touch pin control GPIO calls.

.. _`pinctrl_gpio_set_config`:

pinctrl_gpio_set_config
=======================

.. c:function:: int pinctrl_gpio_set_config(unsigned gpio, unsigned long config)

    Apply config to given GPIO pin

    :param gpio:
        the GPIO pin number from the GPIO subsystem number space
    :type gpio: unsigned

    :param config:
        the configuration to apply to the GPIO
    :type config: unsigned long

.. _`pinctrl_gpio_set_config.description`:

Description
-----------

This function should \*ONLY\* be used from gpiolib-based GPIO drivers, if
they need to call the underlying pin controller to change GPIO config
(for example set debounce time).

.. _`pinctrl_get`:

pinctrl_get
===========

.. c:function:: struct pinctrl *pinctrl_get(struct device *dev)

    retrieves the pinctrl handle for a device

    :param dev:
        the device to obtain the handle for
    :type dev: struct device \*

.. _`pinctrl_release`:

pinctrl_release
===============

.. c:function:: void pinctrl_release(struct kref *kref)

    release the pinctrl handle

    :param kref:
        the kref in the pinctrl being released
    :type kref: struct kref \*

.. _`pinctrl_put`:

pinctrl_put
===========

.. c:function:: void pinctrl_put(struct pinctrl *p)

    decrease use count on a previously claimed pinctrl handle

    :param p:
        the pinctrl handle to release
    :type p: struct pinctrl \*

.. _`pinctrl_lookup_state`:

pinctrl_lookup_state
====================

.. c:function:: struct pinctrl_state *pinctrl_lookup_state(struct pinctrl *p, const char *name)

    retrieves a state handle from a pinctrl handle

    :param p:
        the pinctrl handle to retrieve the state from
    :type p: struct pinctrl \*

    :param name:
        the state name to retrieve
    :type name: const char \*

.. _`pinctrl_commit_state`:

pinctrl_commit_state
====================

.. c:function:: int pinctrl_commit_state(struct pinctrl *p, struct pinctrl_state *state)

    select/activate/program a pinctrl state to HW

    :param p:
        the pinctrl handle for the device that requests configuration
    :type p: struct pinctrl \*

    :param state:
        the state handle to select/activate/program
    :type state: struct pinctrl_state \*

.. _`pinctrl_select_state`:

pinctrl_select_state
====================

.. c:function:: int pinctrl_select_state(struct pinctrl *p, struct pinctrl_state *state)

    select/activate/program a pinctrl state to HW

    :param p:
        the pinctrl handle for the device that requests configuration
    :type p: struct pinctrl \*

    :param state:
        the state handle to select/activate/program
    :type state: struct pinctrl_state \*

.. _`devm_pinctrl_put`:

devm_pinctrl_put
================

.. c:function:: void devm_pinctrl_put(struct pinctrl *p)

    Resource managed \ :c:func:`pinctrl_put`\ 

    :param p:
        the pinctrl handle to release
    :type p: struct pinctrl \*

.. _`devm_pinctrl_put.description`:

Description
-----------

Deallocate a struct pinctrl obtained via \ :c:func:`devm_pinctrl_get`\ . Normally
this function will not need to be called and the resource management
code will ensure that the resource is freed.

.. _`pinctrl_register_mappings`:

pinctrl_register_mappings
=========================

.. c:function:: int pinctrl_register_mappings(const struct pinctrl_map *maps, unsigned num_maps)

    register a set of pin controller mappings

    :param maps:
        the pincontrol mappings table to register. This should probably be
        marked with \__initdata so it can be discarded after boot. This
        function will perform a shallow copy for the mapping entries.
    :type maps: const struct pinctrl_map \*

    :param num_maps:
        the number of maps in the mapping table
    :type num_maps: unsigned

.. _`pinctrl_force_sleep`:

pinctrl_force_sleep
===================

.. c:function:: int pinctrl_force_sleep(struct pinctrl_dev *pctldev)

    turn a given controller device into sleep state

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

.. _`pinctrl_force_default`:

pinctrl_force_default
=====================

.. c:function:: int pinctrl_force_default(struct pinctrl_dev *pctldev)

    turn a given controller device into default state

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*

.. _`pinctrl_init_done`:

pinctrl_init_done
=================

.. c:function:: int pinctrl_init_done(struct device *dev)

    tell pinctrl probe is done

    :param dev:
        device to that's done probing
    :type dev: struct device \*

.. _`pinctrl_init_done.description`:

Description
-----------

We'll use this time to switch the pins from "init" to "default" unless the
driver selected some other state.

.. _`pinctrl_pm_select_state`:

pinctrl_pm_select_state
=======================

.. c:function:: int pinctrl_pm_select_state(struct device *dev, struct pinctrl_state *state)

    select pinctrl state for PM

    :param dev:
        device to select default state for
    :type dev: struct device \*

    :param state:
        state to set
    :type state: struct pinctrl_state \*

.. _`pinctrl_pm_select_default_state`:

pinctrl_pm_select_default_state
===============================

.. c:function:: int pinctrl_pm_select_default_state(struct device *dev)

    select default pinctrl state for PM

    :param dev:
        device to select default state for
    :type dev: struct device \*

.. _`pinctrl_pm_select_sleep_state`:

pinctrl_pm_select_sleep_state
=============================

.. c:function:: int pinctrl_pm_select_sleep_state(struct device *dev)

    select sleep pinctrl state for PM

    :param dev:
        device to select sleep state for
    :type dev: struct device \*

.. _`pinctrl_pm_select_idle_state`:

pinctrl_pm_select_idle_state
============================

.. c:function:: int pinctrl_pm_select_idle_state(struct device *dev)

    select idle pinctrl state for PM

    :param dev:
        device to select idle state for
    :type dev: struct device \*

.. _`pinctrl_init_controller`:

pinctrl_init_controller
=======================

.. c:function:: struct pinctrl_dev *pinctrl_init_controller(struct pinctrl_desc *pctldesc, struct device *dev, void *driver_data)

    init a pin controller device

    :param pctldesc:
        descriptor for this pin controller
    :type pctldesc: struct pinctrl_desc \*

    :param dev:
        parent device for this pin controller
    :type dev: struct device \*

    :param driver_data:
        private pin controller data for this pin controller
    :type driver_data: void \*

.. _`pinctrl_register`:

pinctrl_register
================

.. c:function:: struct pinctrl_dev *pinctrl_register(struct pinctrl_desc *pctldesc, struct device *dev, void *driver_data)

    register a pin controller device

    :param pctldesc:
        descriptor for this pin controller
    :type pctldesc: struct pinctrl_desc \*

    :param dev:
        parent device for this pin controller
    :type dev: struct device \*

    :param driver_data:
        private pin controller data for this pin controller
    :type driver_data: void \*

.. _`pinctrl_register.description`:

Description
-----------

Note that \ :c:func:`pinctrl_register`\  is known to have problems as the pin
controller driver functions are called before the driver has a
struct pinctrl_dev handle. To avoid issues later on, please use the
new \ :c:func:`pinctrl_register_and_init`\  below instead.

.. _`pinctrl_register_and_init`:

pinctrl_register_and_init
=========================

.. c:function:: int pinctrl_register_and_init(struct pinctrl_desc *pctldesc, struct device *dev, void *driver_data, struct pinctrl_dev **pctldev)

    register and init pin controller device

    :param pctldesc:
        descriptor for this pin controller
    :type pctldesc: struct pinctrl_desc \*

    :param dev:
        parent device for this pin controller
    :type dev: struct device \*

    :param driver_data:
        private pin controller data for this pin controller
    :type driver_data: void \*

    :param pctldev:
        pin controller device
    :type pctldev: struct pinctrl_dev \*\*

.. _`pinctrl_register_and_init.description`:

Description
-----------

Note that \ :c:func:`pinctrl_enable`\  still needs to be manually called after
this once the driver is ready.

.. _`pinctrl_unregister`:

pinctrl_unregister
==================

.. c:function:: void pinctrl_unregister(struct pinctrl_dev *pctldev)

    unregister pinmux

    :param pctldev:
        pin controller to unregister
    :type pctldev: struct pinctrl_dev \*

.. _`pinctrl_unregister.description`:

Description
-----------

Called by pinmux drivers to unregister a pinmux.

.. _`devm_pinctrl_register`:

devm_pinctrl_register
=====================

.. c:function:: struct pinctrl_dev *devm_pinctrl_register(struct device *dev, struct pinctrl_desc *pctldesc, void *driver_data)

    Resource managed version of \ :c:func:`pinctrl_register`\ .

    :param dev:
        parent device for this pin controller
    :type dev: struct device \*

    :param pctldesc:
        descriptor for this pin controller
    :type pctldesc: struct pinctrl_desc \*

    :param driver_data:
        private pin controller data for this pin controller
    :type driver_data: void \*

.. _`devm_pinctrl_register.description`:

Description
-----------

Returns an error pointer if pincontrol register failed. Otherwise
it returns valid pinctrl handle.

The pinctrl device will be automatically released when the device is unbound.

.. _`devm_pinctrl_register_and_init`:

devm_pinctrl_register_and_init
==============================

.. c:function:: int devm_pinctrl_register_and_init(struct device *dev, struct pinctrl_desc *pctldesc, void *driver_data, struct pinctrl_dev **pctldev)

    Resource managed pinctrl register and init

    :param dev:
        parent device for this pin controller
    :type dev: struct device \*

    :param pctldesc:
        descriptor for this pin controller
    :type pctldesc: struct pinctrl_desc \*

    :param driver_data:
        private pin controller data for this pin controller
    :type driver_data: void \*

    :param pctldev:
        *undescribed*
    :type pctldev: struct pinctrl_dev \*\*

.. _`devm_pinctrl_register_and_init.description`:

Description
-----------

Returns an error pointer if pincontrol register failed. Otherwise
it returns valid pinctrl handle.

The pinctrl device will be automatically released when the device is unbound.

.. _`devm_pinctrl_unregister`:

devm_pinctrl_unregister
=======================

.. c:function:: void devm_pinctrl_unregister(struct device *dev, struct pinctrl_dev *pctldev)

    Resource managed version of \ :c:func:`pinctrl_unregister`\ .

    :param dev:
        device for which which resource was allocated
    :type dev: struct device \*

    :param pctldev:
        the pinctrl device to unregister.
    :type pctldev: struct pinctrl_dev \*

.. This file was automatic generated / don't edit.

