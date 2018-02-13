.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/rave-sp-wdt.c

.. _`rave_sp_wdt_variant`:

struct rave_sp_wdt_variant
==========================

.. c:type:: struct rave_sp_wdt_variant

    RAVE SP watchdog variant

.. _`rave_sp_wdt_variant.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_wdt_variant {
        unsigned int max_timeout;
        unsigned int min_timeout;
        int (*configure)(struct watchdog_device *, bool);
        int (*restart)(struct watchdog_device *);
    }

.. _`rave_sp_wdt_variant.members`:

Members
-------

max_timeout
    Largest possible watchdog timeout setting

min_timeout
    Smallest possible watchdog timeout setting

configure
    Function to send configuration command

restart
    Function to send "restart" command

.. _`rave_sp_wdt`:

struct rave_sp_wdt
==================

.. c:type:: struct rave_sp_wdt

    RAVE SP watchdog

.. _`rave_sp_wdt.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_wdt {
        struct watchdog_device wdd;
        struct rave_sp *sp;
        const struct rave_sp_wdt_variant *variant;
        struct notifier_block reboot_notifier;
    }

.. _`rave_sp_wdt.members`:

Members
-------

wdd
    Underlying watchdog device

sp
    Pointer to parent RAVE SP device

variant
    Device specific variant information

reboot_notifier
    Reboot notifier implementing machine reset

.. _`rave_sp_wdt_configure`:

rave_sp_wdt_configure
=====================

.. c:function:: int rave_sp_wdt_configure(struct watchdog_device *wdd, bool on)

    Configure watchdog device

    :param struct watchdog_device \*wdd:
        Device to configure

    :param bool on:
        Desired state of the watchdog timer (ON/OFF)

.. _`rave_sp_wdt_configure.this-function-configures-two-aspects-of-the-watchdog-timer`:

This function configures two aspects of the watchdog timer
----------------------------------------------------------


- Wheither it is ON or OFF
- Its timeout duration

with first aspect specified via function argument and second via
the value of 'wdd->timeout'.

.. This file was automatic generated / don't edit.

