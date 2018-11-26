.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/mmio.c

.. _`clocksource_mmio_init`:

clocksource_mmio_init
=====================

.. c:function:: int clocksource_mmio_init(void __iomem *base, const char *name, unsigned long hz, int rating, unsigned bits, u64 (*read)(struct clocksource *))

    Initialize a simple mmio based clocksource

    :param base:
        Virtual address of the clock readout register
    :type base: void __iomem \*

    :param name:
        Name of the clocksource
    :type name: const char \*

    :param hz:
        Frequency of the clocksource in Hz
    :type hz: unsigned long

    :param rating:
        Rating of the clocksource
    :type rating: int

    :param bits:
        Number of valid bits
    :type bits: unsigned

    :param u64 (\*read)(struct clocksource \*):
        One of clocksource_mmio_read\*() above

.. This file was automatic generated / don't edit.

