.. -*- coding: utf-8; mode: rst -*-

.. _netdev:

**********************
Network device support
**********************


Driver Support
==============


.. kernel-doc:: net/core/dev.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/ethernet/eth.c
    :man-sect: 9
    :export:


.. kernel-doc:: net/sched/sch_generic.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/etherdevice.h
    :man-sect: 9
    :internal:


.. kernel-doc:: include/linux/netdevice.h
    :man-sect: 9
    :internal:


PHY Support
===========


.. kernel-doc:: drivers/net/phy/phy.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/net/phy/phy.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/net/phy/phy_device.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/net/phy/phy_device.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/net/phy/mdio_bus.c
    :man-sect: 9
    :export:


.. kernel-doc:: drivers/net/phy/mdio_bus.c
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
