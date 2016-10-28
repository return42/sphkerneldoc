.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mach-au1x00/gpio-au1000.h

.. _`alchemy_gpio2_enable_int`:

alchemy_gpio2_enable_int
========================

.. c:function:: void alchemy_gpio2_enable_int(int gpio2)

    Enable a GPIO2 pins' shared irq contribution.

    :param int gpio2:
        The GPIO2 pin to activate (200...215).

.. _`alchemy_gpio2_enable_int.description`:

Description
-----------

GPIO208-215 have one shared interrupt line to the INTC.  They are
and'ed with a per-pin enable bit and finally or'ed together to form
a single irq request (useful for active-high sources).
With this function, a pins' individual contribution to the int request
can be enabled.  As with all other GPIO-based interrupts, the INTC
must be programmed to accept the GPIO208_215 interrupt as well.

.. _`alchemy_gpio2_enable_int.note`:

NOTE
----

Calling this macro is only necessary for GPIO208-215; all other
GPIO2-based interrupts have their own request to the INTC.  Please
consult your Alchemy databook for more information!

On the Au1550, GPIOs 201-205 also have a shared interrupt request
line to the INTC, GPIO201_205.  This function can be used for those
as well.

'gpio2' parameter must be in range of the GPIO2 numberspace
(200-215 by default). No sanity checks are made,

.. _`alchemy_gpio2_disable_int`:

alchemy_gpio2_disable_int
=========================

.. c:function:: void alchemy_gpio2_disable_int(int gpio2)

    Disable a GPIO2 pins' shared irq contribution.

    :param int gpio2:
        The GPIO2 pin to activate (200...215).

.. _`alchemy_gpio2_disable_int.description`:

Description
-----------

see function \ :c:func:`alchemy_gpio2_enable_int`\  for more information.

.. _`alchemy_gpio2_enable`:

alchemy_gpio2_enable
====================

.. c:function:: void alchemy_gpio2_enable( void)

    Activate GPIO2 block.

    :param  void:
        no arguments

.. _`alchemy_gpio2_enable.description`:

Description
-----------

The GPIO2 block must be enabled excplicitly to work.  On systems
where this isn't done by the bootloader, this macro can be used.

.. _`alchemy_gpio2_disable`:

alchemy_gpio2_disable
=====================

.. c:function:: void alchemy_gpio2_disable( void)

    disable GPIO2 block.

    :param  void:
        no arguments

.. _`alchemy_gpio2_disable.description`:

Description
-----------

Disable and put GPIO2 block in low-power mode.

.. This file was automatic generated / don't edit.

