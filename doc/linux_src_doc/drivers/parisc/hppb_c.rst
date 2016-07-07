.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/hppb.c

.. _`hppb_probe`:

hppb_probe
==========

.. c:function:: int hppb_probe(struct parisc_device *dev)

    Determine if the hppb driver should claim this device.

    :param struct parisc_device \*dev:
        The device which has been found

.. _`hppb_probe.description`:

Description
-----------

Determine if hppb driver should claim this chip (return 0) or not
(return 1). If so, initialize the chip and tell other partners in crime
they have work to do.

.. _`hppb_init`:

hppb_init
=========

.. c:function:: void hppb_init( void)

    HP-PB bus initialization procedure.

    :param  void:
        no arguments

.. _`hppb_init.description`:

Description
-----------

Register this driver.

.. This file was automatic generated / don't edit.

