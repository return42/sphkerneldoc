
.. _controllers:

=============================
Peripheral Controller Drivers
=============================

The first hardware supporting this API was the NetChip 2280 controller, which supports USB 2.0 high speed and is based on PCI. This is the ``net2280`` driver module. The driver
supports Linux kernel versions 2.4 and 2.6; contact NetChip Technologies for development boards and product information.

Other hardware working in the "gadget" framework includes: Intel's PXA 25x and IXP42x series processors (``pxa2xx_udc``), Toshiba TC86c001 "Goku-S" (``goku_udc``), Renesas
SH7705/7727 (``sh_udc``), MediaQ 11xx (``mq11xx_udc``), Hynix HMS30C7202 (``h7202_udc``), National 9303/4 (``n9604_udc``), Texas Instruments OMAP (``omap_udc``), Sharp LH7A40x
(``lh7a40x_udc``), and more. Most of those are full speed controllers.

At this writing, there are people at work on drivers in this framework for several other USB device controllers, with plans to make many of them be widely available.

A partial USB simulator, the ``dummy_hcd`` driver, is available. It can act like a net2280, a pxa25x, or an sa11x0 in terms of available endpoints and device speeds; and it
simulates control, bulk, and to some extent interrupt transfers. That lets you develop some parts of a gadget driver on a normal PC, without any special hardware, and perhaps with
the assistance of tools such as GDB running with User Mode Linux. At least one person has expressed interest in adapting that approach, hooking it up to a simulator for a
microcontroller. Such simulators can help debug subsystems where the runtime hardware is unfriendly to software development, or is not yet available.

Support for other controllers is expected to be developed and contributed over time, as this driver framework evolves.
