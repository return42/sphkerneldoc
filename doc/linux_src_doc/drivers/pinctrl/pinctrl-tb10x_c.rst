.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-tb10x.c

.. _`tb10x_port`:

struct tb10x_port
=================

.. c:type:: struct tb10x_port

    state of an I/O port

.. _`tb10x_port.definition`:

Definition
----------

.. code-block:: c

    struct tb10x_port {
        unsigned int mode;
        unsigned int count;
    }

.. _`tb10x_port.members`:

Members
-------

mode
    Node this port is currently in.

count
    Number of enabled functions which require this port to be
    configured in \ ``mode``\ .

.. _`tb10x_pinctrl`:

struct tb10x_pinctrl
====================

.. c:type:: struct tb10x_pinctrl

    TB10x pin controller internal state

.. _`tb10x_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct tb10x_pinctrl {
        struct pinctrl_dev *pctl;
        void *base;
        const struct tb10x_pinfuncgrp *pingroups;
        unsigned int pinfuncgrpcnt;
        struct tb10x_of_pinfunc *pinfuncs;
        unsigned int pinfuncnt;
        struct mutex mutex;
        struct tb10x_port ports[TB10X_PORTS];
        unsigned long gpios\[BITS_TO_LONGS(MAX_PIN + 1)\];
    }

.. _`tb10x_pinctrl.members`:

Members
-------

pctl
    pointer to the pinctrl_dev structure of this pin controller.

base
    register set base address.

pingroups
    pointer to an array of the pin groups this driver manages.

pinfuncgrpcnt
    number of pingroups in \ ``pingroups``\ .

pinfuncs
    pointer to an array of pin functions this driver manages.

pinfuncnt
    number of pin functions in \ ``pinfuncs``\ .

mutex
    mutex for exclusive access to a pin controller's state.

ports
    current state of each port.

.. This file was automatic generated / don't edit.

