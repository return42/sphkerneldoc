.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pwm/core.c

.. _`pwm_set_chip_data`:

pwm_set_chip_data
=================

.. c:function:: int pwm_set_chip_data(struct pwm_device *pwm, void *data)

    set private chip data for a PWM

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

    :param data:
        pointer to chip-specific data
    :type data: void \*

.. _`pwm_set_chip_data.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwm_get_chip_data`:

pwm_get_chip_data
=================

.. c:function:: void *pwm_get_chip_data(struct pwm_device *pwm)

    get private chip data for a PWM

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

.. _`pwm_get_chip_data.return`:

Return
------

A pointer to the chip-private data for the PWM device.

.. _`pwmchip_add_with_polarity`:

pwmchip_add_with_polarity
=========================

.. c:function:: int pwmchip_add_with_polarity(struct pwm_chip *chip, enum pwm_polarity polarity)

    register a new PWM chip

    :param chip:
        the PWM chip to add
    :type chip: struct pwm_chip \*

    :param polarity:
        initial polarity of PWM channels
    :type polarity: enum pwm_polarity

.. _`pwmchip_add_with_polarity.description`:

Description
-----------

Register a new PWM chip. If chip->base < 0 then a dynamically assigned base
will be used. The initial polarity for all channels is specified by the
\ ``polarity``\  parameter.

.. _`pwmchip_add_with_polarity.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwmchip_add`:

pwmchip_add
===========

.. c:function:: int pwmchip_add(struct pwm_chip *chip)

    register a new PWM chip

    :param chip:
        the PWM chip to add
    :type chip: struct pwm_chip \*

.. _`pwmchip_add.description`:

Description
-----------

Register a new PWM chip. If chip->base < 0 then a dynamically assigned base
will be used. The initial polarity for all channels is normal.

.. _`pwmchip_add.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwmchip_remove`:

pwmchip_remove
==============

.. c:function:: int pwmchip_remove(struct pwm_chip *chip)

    remove a PWM chip

    :param chip:
        the PWM chip to remove
    :type chip: struct pwm_chip \*

.. _`pwmchip_remove.description`:

Description
-----------

Removes a PWM chip. This function may return busy if the PWM chip provides
a PWM device that is still requested.

.. _`pwmchip_remove.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwm_request`:

pwm_request
===========

.. c:function:: struct pwm_device *pwm_request(int pwm, const char *label)

    request a PWM device

    :param pwm:
        global PWM device index
    :type pwm: int

    :param label:
        PWM device label
    :type label: const char \*

.. _`pwm_request.description`:

Description
-----------

This function is deprecated, use \ :c:func:`pwm_get`\  instead.

.. _`pwm_request.return`:

Return
------

A pointer to a PWM device or an \ :c:func:`ERR_PTR`\ -encoded error code on
failure.

.. _`pwm_request_from_chip`:

pwm_request_from_chip
=====================

.. c:function:: struct pwm_device *pwm_request_from_chip(struct pwm_chip *chip, unsigned int index, const char *label)

    request a PWM device relative to a PWM chip

    :param chip:
        PWM chip
    :type chip: struct pwm_chip \*

    :param index:
        per-chip index of the PWM to request
    :type index: unsigned int

    :param label:
        a literal description string of this PWM
    :type label: const char \*

.. _`pwm_request_from_chip.return`:

Return
------

A pointer to the PWM device at the given index of the given PWM
chip. A negative error code is returned if the index is not valid for the
specified PWM chip or if the PWM device cannot be requested.

.. _`pwm_free`:

pwm_free
========

.. c:function:: void pwm_free(struct pwm_device *pwm)

    free a PWM device

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

.. _`pwm_free.description`:

Description
-----------

This function is deprecated, use \ :c:func:`pwm_put`\  instead.

.. _`pwm_apply_state`:

pwm_apply_state
===============

.. c:function:: int pwm_apply_state(struct pwm_device *pwm, struct pwm_state *state)

    atomically apply a new state to a PWM device

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

    :param state:
        new state to apply. This can be adjusted by the PWM driver
        if the requested config is not achievable, for example,
        ->duty_cycle and ->period might be approximated.
    :type state: struct pwm_state \*

.. _`pwm_capture`:

pwm_capture
===========

.. c:function:: int pwm_capture(struct pwm_device *pwm, struct pwm_capture *result, unsigned long timeout)

    capture and report a PWM signal

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

    :param result:
        structure to fill with capture result
    :type result: struct pwm_capture \*

    :param timeout:
        time to wait, in milliseconds, before giving up on capture
    :type timeout: unsigned long

.. _`pwm_capture.return`:

Return
------

0 on success or a negative error code on failure.

.. _`pwm_adjust_config`:

pwm_adjust_config
=================

.. c:function:: int pwm_adjust_config(struct pwm_device *pwm)

    adjust the current PWM config to the PWM arguments

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

.. _`pwm_adjust_config.description`:

Description
-----------

This function will adjust the PWM config to the PWM arguments provided
by the DT or PWM lookup table. This is particularly useful to adapt
the bootloader config to the Linux one.

.. _`of_pwm_get`:

of_pwm_get
==========

.. c:function:: struct pwm_device *of_pwm_get(struct device_node *np, const char *con_id)

    request a PWM via the PWM framework

    :param np:
        device node to get the PWM from
    :type np: struct device_node \*

    :param con_id:
        consumer name
    :type con_id: const char \*

.. _`of_pwm_get.description`:

Description
-----------

Returns the PWM device parsed from the phandle and index specified in the
"pwms" property of a device tree node or a negative error-code on failure.
Values parsed from the device tree are stored in the returned PWM device
object.

If con_id is NULL, the first PWM device listed in the "pwms" property will
be requested. Otherwise the "pwm-names" property is used to do a reverse
lookup of the PWM index. This also means that the "pwm-names" property
becomes mandatory for devices that look up the PWM device via the con_id
parameter.

.. _`of_pwm_get.return`:

Return
------

A pointer to the requested PWM device or an \ :c:func:`ERR_PTR`\ -encoded
error code on failure.

.. _`pwm_add_table`:

pwm_add_table
=============

.. c:function:: void pwm_add_table(struct pwm_lookup *table, size_t num)

    register PWM device consumers

    :param table:
        array of consumers to register
    :type table: struct pwm_lookup \*

    :param num:
        number of consumers in table
    :type num: size_t

.. _`pwm_remove_table`:

pwm_remove_table
================

.. c:function:: void pwm_remove_table(struct pwm_lookup *table, size_t num)

    unregister PWM device consumers

    :param table:
        array of consumers to unregister
    :type table: struct pwm_lookup \*

    :param num:
        number of consumers in table
    :type num: size_t

.. _`pwm_get`:

pwm_get
=======

.. c:function:: struct pwm_device *pwm_get(struct device *dev, const char *con_id)

    look up and request a PWM device

    :param dev:
        device for PWM consumer
    :type dev: struct device \*

    :param con_id:
        consumer name
    :type con_id: const char \*

.. _`pwm_get.description`:

Description
-----------

Lookup is first attempted using DT. If the device was not instantiated from
a device tree, a PWM chip and a relative index is looked up via a table
supplied by board setup code (see \ :c:func:`pwm_add_table`\ ).

Once a PWM chip has been found the specified PWM device will be requested
and is ready to be used.

.. _`pwm_get.return`:

Return
------

A pointer to the requested PWM device or an \ :c:func:`ERR_PTR`\ -encoded
error code on failure.

.. _`pwm_put`:

pwm_put
=======

.. c:function:: void pwm_put(struct pwm_device *pwm)

    release a PWM device

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

.. _`devm_pwm_get`:

devm_pwm_get
============

.. c:function:: struct pwm_device *devm_pwm_get(struct device *dev, const char *con_id)

    resource managed \ :c:func:`pwm_get`\ 

    :param dev:
        device for PWM consumer
    :type dev: struct device \*

    :param con_id:
        consumer name
    :type con_id: const char \*

.. _`devm_pwm_get.description`:

Description
-----------

This function performs like \ :c:func:`pwm_get`\  but the acquired PWM device will
automatically be released on driver detach.

.. _`devm_pwm_get.return`:

Return
------

A pointer to the requested PWM device or an \ :c:func:`ERR_PTR`\ -encoded
error code on failure.

.. _`devm_of_pwm_get`:

devm_of_pwm_get
===============

.. c:function:: struct pwm_device *devm_of_pwm_get(struct device *dev, struct device_node *np, const char *con_id)

    resource managed \ :c:func:`of_pwm_get`\ 

    :param dev:
        device for PWM consumer
    :type dev: struct device \*

    :param np:
        device node to get the PWM from
    :type np: struct device_node \*

    :param con_id:
        consumer name
    :type con_id: const char \*

.. _`devm_of_pwm_get.description`:

Description
-----------

This function performs like \ :c:func:`of_pwm_get`\  but the acquired PWM device will
automatically be released on driver detach.

.. _`devm_of_pwm_get.return`:

Return
------

A pointer to the requested PWM device or an \ :c:func:`ERR_PTR`\ -encoded
error code on failure.

.. _`devm_pwm_put`:

devm_pwm_put
============

.. c:function:: void devm_pwm_put(struct device *dev, struct pwm_device *pwm)

    resource managed \ :c:func:`pwm_put`\ 

    :param dev:
        device for PWM consumer
    :type dev: struct device \*

    :param pwm:
        PWM device
    :type pwm: struct pwm_device \*

.. _`devm_pwm_put.description`:

Description
-----------

Release a PWM previously allocated using \ :c:func:`devm_pwm_get`\ . Calling this
function is usually not needed because devm-allocated resources are
automatically released on driver detach.

.. This file was automatic generated / don't edit.

