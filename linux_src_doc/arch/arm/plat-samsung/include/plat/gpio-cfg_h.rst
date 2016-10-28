.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/gpio-cfg.h

.. _`samsung_gpio_cfg`:

struct samsung_gpio_cfg
=======================

.. c:type:: struct samsung_gpio_cfg


.. _`samsung_gpio_cfg.definition`:

Definition
----------

.. code-block:: c

    struct samsung_gpio_cfg {
        unsigned int cfg_eint;
        samsung_gpio_pull_t (*get_pull)(struct samsung_gpio_chip *chip, unsigned offs);
        int (*set_pull)(struct samsung_gpio_chip *chip, unsigned offs,samsung_gpio_pull_t pull);
        unsigned (*get_config)(struct samsung_gpio_chip *chip, unsigned offs);
        int (*set_config)(struct samsung_gpio_chip *chip, unsigned offs,unsigned config);
    }

.. _`samsung_gpio_cfg.members`:

Members
-------

cfg_eint
    Configuration setting when used for external interrupt source

get_pull
    Read the current pull configuration for the GPIO

set_pull
    Set the current pull configuraiton for the GPIO

get_config
    Read the current configuration for the GPIO

set_config
    Set the current configuration for the GPIO

.. _`samsung_gpio_cfg.description`:

Description
-----------

Each chip can have more than one type of GPIO bank available and some
have different capabilites even when they have the same control register
layouts. Provide an point to vector control routine and provide any
per-bank configuration information that other systems such as the
external interrupt code will need.

\ ``sa``\  samsung_gpio_cfgpin
\ ``sa``\  s3c_gpio_getcfg
\ ``sa``\  s3c_gpio_setpull
\ ``sa``\  s3c_gpio_getpull

.. _`s3c_gpio_cfgpin`:

s3c_gpio_cfgpin
===============

.. c:function:: int s3c_gpio_cfgpin(unsigned int pin, unsigned int to)

    Change the GPIO function of a pin. \ ``pin``\  pin The pin number to configure. \ ``to``\  to The configuration for the pin's function.

    :param unsigned int pin:
        *undescribed*

    :param unsigned int to:
        *undescribed*

.. _`s3c_gpio_cfgpin.description`:

Description
-----------

Configure which function is actually connected to the external
pin, such as an gpio input, output or some form of special function
connected to an internal peripheral block.

The \ ``to``\  parameter can be one of the generic S3C_GPIO_INPUT, S3C_GPIO_OUTPUT
or \ :c:func:`S3C_GPIO_SFN`\  to indicate one of the possible values that the helper
will then generate the correct bit mask and shift for the configuration.

If a bank of GPIOs all needs to be set to special-function 2, then

.. _`s3c_gpio_cfgpin.the-following-code-will-work`:

the following code will work
----------------------------


for (gpio = start; gpio < end; gpio++)
s3c_gpio_cfgpin(gpio, S3C_GPIO_SFN(2));

The \ ``to``\  parameter can also be a specific value already shifted to the
correct position in the control register, although these are discouraged
in newer kernels and are only being kept for compatibility.

.. _`s3c_gpio_getcfg`:

s3c_gpio_getcfg
===============

.. c:function:: unsigned s3c_gpio_getcfg(unsigned int pin)

    Read the current function for a GPIO pin

    :param unsigned int pin:
        The pin to read the configuration value for.

.. _`s3c_gpio_getcfg.description`:

Description
-----------

Read the configuration state of the given \ ``pin``\ , returning a value that
could be passed back to \ :c:func:`s3c_gpio_cfgpin`\ .

\ ``sa``\  s3c_gpio_cfgpin

.. _`s3c_gpio_cfgpin_range`:

s3c_gpio_cfgpin_range
=====================

.. c:function:: int s3c_gpio_cfgpin_range(unsigned int start, unsigned int nr, unsigned int cfg)

    Change the GPIO function for configuring pin range

    :param unsigned int start:
        The pin number to start at

    :param unsigned int nr:
        The number of pins to configure from \ ``start``\ .

    :param unsigned int cfg:
        The configuration for the pin's function

.. _`s3c_gpio_cfgpin_range.description`:

Description
-----------

Call \ :c:func:`s3c_gpio_cfgpin`\  for the \ ``nr``\  pins starting at \ ``start``\ .

\ ``sa``\  s3c_gpio_cfgpin.

.. _`s3c_gpio_setpull`:

s3c_gpio_setpull
================

.. c:function:: int s3c_gpio_setpull(unsigned int pin, samsung_gpio_pull_t pull)

    set the state of a gpio pin pull resistor

    :param unsigned int pin:
        The pin number to configure the pull resistor.

    :param samsung_gpio_pull_t pull:
        The configuration for the pull resistor.

.. _`s3c_gpio_setpull.description`:

Description
-----------

This function sets the state of the pull-{up,down} resistor for the
specified pin. It will return 0 if successful, or a negative error
code if the pin cannot support the requested pull setting.

\ ``pull``\  is one of S3C_GPIO_PULL_NONE, S3C_GPIO_PULL_DOWN or S3C_GPIO_PULL_UP.

.. _`s3c_gpio_getpull`:

s3c_gpio_getpull
================

.. c:function:: samsung_gpio_pull_t s3c_gpio_getpull(unsigned int pin)

    get the pull resistor state of a gpio pin

    :param unsigned int pin:
        The pin number to get the settings for

.. _`s3c_gpio_getpull.description`:

Description
-----------

Read the pull resistor value for the specified pin.

.. _`s3c_gpio_cfgall_range`:

s3c_gpio_cfgall_range
=====================

.. c:function:: int s3c_gpio_cfgall_range(unsigned int start, unsigned int nr, unsigned int cfg, samsung_gpio_pull_t pull)

    configure range of gpio functtion and pull.

    :param unsigned int start:
        The gpio number to start at.

    :param unsigned int nr:
        The number of gpio to configure from \ ``start``\ .

    :param unsigned int cfg:
        The configuration to use

    :param samsung_gpio_pull_t pull:
        The pull setting to use.

.. _`s3c_gpio_cfgall_range.description`:

Description
-----------

Run \ :c:func:`s3c_gpio_cfgpin`\  and \ :c:func:`s3c_gpio_setpull`\  over the gpio range starting
\ ``gpio``\  and running for \ ``size``\ .

\ ``sa``\  s3c_gpio_cfgpin
\ ``sa``\  s3c_gpio_setpull
\ ``sa``\  s3c_gpio_cfgpin_range

.. This file was automatic generated / don't edit.

