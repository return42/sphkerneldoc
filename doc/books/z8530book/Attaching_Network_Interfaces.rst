.. -*- coding: utf-8; mode: rst -*-

.. _Attaching_Network_Interfaces:

============================
Attaching Network Interfaces
============================

If you wish to use the network interface facilities of the driver, then
you need to attach a network device to each channel that is present and
in use. In addition to use the generic HDLC you need to follow some
additional plumbing rules. They may seem complex but a look at the
example hostess_sv11 driver should reassure you.

The network device used for each channel should be pointed to by the
netdevice field of each channel. The hdlc-> priv field of the network
device points to your private data - you will need to be able to find
your private data from this.

The way most drivers approach this particular problem is to create a
structure holding the Z8530 device definition and put that into the
private field of the network device. The network device fields of the
channels then point back to the network devices.

If you wish to use the generic HDLC then you need to register the HDLC
device.

Before you register your network device you will also need to provide
suitable handlers for most of the network device callbacks. See the
network device documentation for more details on this.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
