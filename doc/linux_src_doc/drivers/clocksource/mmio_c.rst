.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/mmio.c

.. _`clocksource_mmio_init`:

clocksource_mmio_init
=====================

.. c:function:: int clocksource_mmio_init(void __iomem *base, const char *name, unsigned long hz, int rating, unsigned bits, cycle_t (*read)(struct clocksource *))

    Initialize a simple mmio based clocksource

    :param void __iomem \*base:
        Virtual address of the clock readout register

    :param const char \*name:
        Name of the clocksource

    :param unsigned long hz:
        Frequency of the clocksource in Hz

    :param int rating:
        Rating of the clocksource

    :param unsigned bits:
        Number of valid bits

    :param cycle_t (\*read)(struct clocksource \*):
        One of clocksource_mmio_read\*() above

.. This file was automatic generated / don't edit.

