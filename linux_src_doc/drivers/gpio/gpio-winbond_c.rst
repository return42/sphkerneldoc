.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-winbond.c

.. _`winbond_gpio_port_conflict`:

struct winbond_gpio_port_conflict
=================================

.. c:type:: struct winbond_gpio_port_conflict

    possibly conflicting device information

.. _`winbond_gpio_port_conflict.definition`:

Definition
----------

.. code-block:: c

    struct winbond_gpio_port_conflict {
        const char *name;
        u8 dev;
        u8 testreg;
        u8 testbit;
        bool warnonly;
    }

.. _`winbond_gpio_port_conflict.members`:

Members
-------

name
    device name (NULL means no conflicting device defined)

dev
    Super I/O logical device number where the testreg register
    is located (or WB_SIO_DEV_NONE - don't select any
    logical device)

testreg
    register number where the testbit bit is located

testbit
    index of a bit to check whether an actual conflict exists

warnonly
    if set then a conflict isn't fatal (just warn about it),
    otherwise disable the particular GPIO port if a conflict
    is detected

.. _`winbond_gpio_info`:

struct winbond_gpio_info
========================

.. c:type:: struct winbond_gpio_info

    information about a particular GPIO port (device)

.. _`winbond_gpio_info.definition`:

Definition
----------

.. code-block:: c

    struct winbond_gpio_info {
        u8 dev;
        u8 enablereg;
        u8 enablebit;
        u8 outputreg;
        u8 outputppbit;
        u8 ioreg;
        u8 invreg;
        u8 datareg;
        struct winbond_gpio_port_conflict conflict;
    }

.. _`winbond_gpio_info.members`:

Members
-------

dev
    Super I/O logical device number of the registers
    specified below

enablereg
    port enable bit register number

enablebit
    index of a port enable bit

outputreg
    output driver mode bit register number

outputppbit
    index of a push-pull output driver mode bit

ioreg
    data direction register number

invreg
    pin data inversion register number

datareg
    pin data register number

conflict
    description of a device that possibly conflicts with
    this port

.. This file was automatic generated / don't edit.

