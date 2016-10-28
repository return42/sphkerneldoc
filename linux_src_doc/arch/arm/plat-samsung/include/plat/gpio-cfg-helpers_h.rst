.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/gpio-cfg-helpers.h

.. _`s3c24xx_gpio_setpull_1up`:

s3c24xx_gpio_setpull_1up
========================

.. c:function:: int s3c24xx_gpio_setpull_1up(struct samsung_gpio_chip *chip, unsigned int off, samsung_gpio_pull_t pull)

    Pull configuration for choice of up or none.

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that is being configured.

    :param unsigned int off:
        The offset for the GPIO being configured.

    :param samsung_gpio_pull_t pull:
        *undescribed*

.. _`s3c24xx_gpio_setpull_1up.description`:

Description
-----------

This is a helper function for the case where we have GPIOs with one
bit configuring the presence of a pull-up resistor.

.. _`s3c24xx_gpio_setpull_1down`:

s3c24xx_gpio_setpull_1down
==========================

.. c:function:: int s3c24xx_gpio_setpull_1down(struct samsung_gpio_chip *chip, unsigned int off, samsung_gpio_pull_t pull)

    Pull configuration for choice of down or none

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that is being configured

    :param unsigned int off:
        The offset for the GPIO being configured

    :param samsung_gpio_pull_t pull:
        *undescribed*

.. _`s3c24xx_gpio_setpull_1down.description`:

Description
-----------

This is a helper function for the case where we have GPIOs with one
bit configuring the presence of a pull-down resistor.

.. _`samsung_gpio_setpull_updown`:

samsung_gpio_setpull_updown
===========================

.. c:function:: int samsung_gpio_setpull_updown(struct samsung_gpio_chip *chip, unsigned int off, samsung_gpio_pull_t pull)

    Pull configuration for choice of up, down or none

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that is being configured.

    :param unsigned int off:
        The offset for the GPIO being configured.

    :param samsung_gpio_pull_t pull:
        *undescribed*

.. _`samsung_gpio_setpull_updown.description`:

Description
-----------

This is a helper function for the case where we have GPIOs with two
bits configuring the presence of a pull resistor, in the following

.. _`samsung_gpio_setpull_updown.order`:

order
-----

00 = No pull resistor connected
01 = Pull-up resistor connected
10 = Pull-down resistor connected

.. _`samsung_gpio_getpull_updown`:

samsung_gpio_getpull_updown
===========================

.. c:function:: samsung_gpio_pull_t samsung_gpio_getpull_updown(struct samsung_gpio_chip *chip, unsigned int off)

    Get configuration for choice of up, down or none

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that the GPIO pin belongs to

    :param unsigned int off:
        The offset to the pin to get the configuration of.

.. _`samsung_gpio_getpull_updown.description`:

Description
-----------

This helper function reads the state of the pull-{up,down} resistor
for the given GPIO in the same case as samsung_gpio_setpull_upown.

.. _`s3c24xx_gpio_getpull_1up`:

s3c24xx_gpio_getpull_1up
========================

.. c:function:: samsung_gpio_pull_t s3c24xx_gpio_getpull_1up(struct samsung_gpio_chip *chip, unsigned int off)

    Get configuration for choice of up or none

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that the GPIO pin belongs to

    :param unsigned int off:
        The offset to the pin to get the configuration of.

.. _`s3c24xx_gpio_getpull_1up.description`:

Description
-----------

This helper function reads the state of the pull-up resistor for the
given GPIO in the same case as s3c24xx_gpio_setpull_1up.

.. _`s3c24xx_gpio_getpull_1down`:

s3c24xx_gpio_getpull_1down
==========================

.. c:function:: samsung_gpio_pull_t s3c24xx_gpio_getpull_1down(struct samsung_gpio_chip *chip, unsigned int off)

    Get configuration for choice of down or none

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that the GPIO pin belongs to

    :param unsigned int off:
        The offset to the pin to get the configuration of.

.. _`s3c24xx_gpio_getpull_1down.description`:

Description
-----------

This helper function reads the state of the pull-down resistor for the
given GPIO in the same case as s3c24xx_gpio_setpull_1down.

.. _`s3c2443_gpio_setpull`:

s3c2443_gpio_setpull
====================

.. c:function:: int s3c2443_gpio_setpull(struct samsung_gpio_chip *chip, unsigned int off, samsung_gpio_pull_t pull)

    Pull configuration for s3c2443.

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that is being configured.

    :param unsigned int off:
        The offset for the GPIO being configured.

    :param samsung_gpio_pull_t pull:
        *undescribed*

.. _`s3c2443_gpio_setpull.description`:

Description
-----------

This is a helper function for the case where we have GPIOs with two
bits configuring the presence of a pull resistor, in the following

.. _`s3c2443_gpio_setpull.order`:

order
-----

00 = Pull-up resistor connected
10 = Pull-down resistor connected
x1 = No pull up resistor

.. _`s3c2443_gpio_getpull`:

s3c2443_gpio_getpull
====================

.. c:function:: samsung_gpio_pull_t s3c2443_gpio_getpull(struct samsung_gpio_chip *chip, unsigned int off)

    Get configuration for s3c2443 pull resistors

    :param struct samsung_gpio_chip \*chip:
        The gpio chip that the GPIO pin belongs to.

    :param unsigned int off:
        The offset to the pin to get the configuration of.

.. _`s3c2443_gpio_getpull.description`:

Description
-----------

This helper function reads the state of the pull-{up,down} resistor for the
given GPIO in the same case as samsung_gpio_setpull_upown.

.. This file was automatic generated / don't edit.

