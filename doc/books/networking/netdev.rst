.. -*- coding: utf-8; mode: rst -*-

.. _netdev:

======================
Network device support
======================


Driver Support
==============


.. kernel-doc:: net/core/dev.c
    :export:

.. kernel-doc:: net/ethernet/eth.c
    :export:

.. kernel-doc:: net/sched/sch_generic.c
    :export:

.. kernel-doc:: include/linux/etherdevice.h
    :internal:

.. kernel-doc:: include/linux/netdevice.h
    :internal:

PHY Support
===========


.. kernel-doc:: drivers/net/phy/phy.c
    :export:

.. kernel-doc:: drivers/net/phy/phy.c
    :internal:

.. kernel-doc:: drivers/net/phy/phy_device.c
    :export:

.. kernel-doc:: drivers/net/phy/phy_device.c
    :internal:

.. kernel-doc:: drivers/net/phy/mdio_bus.c
    :export:

.. kernel-doc:: drivers/net/phy/mdio_bus.c
    :internal:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
