.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/auxdisplay/arm-charlcd.c

.. _`charlcd`:

struct charlcd
==============

.. c:type:: struct charlcd

    Private data structure

.. _`charlcd.definition`:

Definition
----------

.. code-block:: c

    struct charlcd {
        struct device *dev;
        u32 phybase;
        u32 physize;
        void __iomem *virtbase;
        int irq;
        struct completion complete;
        struct delayed_work init_work;
    }

.. _`charlcd.members`:

Members
-------

dev
    a pointer back to containing device

phybase
    the offset to the controller in physical memory

physize
    the size of the physical page

virtbase
    the offset to the controller in virtual memory

irq
    reserved interrupt number

complete
    completion structure for the last LCD command

init_work
    delayed work structure to initialize the display on boot

.. This file was automatic generated / don't edit.

