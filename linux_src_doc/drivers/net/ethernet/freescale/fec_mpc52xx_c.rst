.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/fec_mpc52xx.c

.. _`mpc52xx_fec_hw_init`:

mpc52xx_fec_hw_init
===================

.. c:function:: void mpc52xx_fec_hw_init(struct net_device *dev)

    :param dev:
        network device
    :type dev: struct net_device \*

.. _`mpc52xx_fec_hw_init.description`:

Description
-----------

Setup various hardware setting, only needed once on start

.. _`mpc52xx_fec_start`:

mpc52xx_fec_start
=================

.. c:function:: void mpc52xx_fec_start(struct net_device *dev)

    :param dev:
        network device
    :type dev: struct net_device \*

.. _`mpc52xx_fec_start.description`:

Description
-----------

This function is called to start or restart the FEC during a link
change.  This happens on fifo errors or when switching between half
and full duplex.

.. _`mpc52xx_fec_stop`:

mpc52xx_fec_stop
================

.. c:function:: void mpc52xx_fec_stop(struct net_device *dev)

    :param dev:
        network device
    :type dev: struct net_device \*

.. _`mpc52xx_fec_stop.description`:

Description
-----------

stop all activity on fec and empty dma buffers

.. This file was automatic generated / don't edit.

