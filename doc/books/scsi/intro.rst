
.. _intro:

============
Introduction
============


.. _protocol_vs_bus:

Protocol vs bus
===============

Once upon a time, the Small Computer Systems Interface defined both a parallel I/O bus and a data protocol to connect a wide variety of peripherals (disk drives, tape drives,
modems, printers, scanners, optical drives, test equipment, and medical devices) to a host computer.

Although the old parallel (fast/wide/ultra) SCSI bus has largely fallen out of use, the SCSI command set is more widely used than ever to communicate with devices over a number of
different busses.

The `SCSI protocol`_ is a big-endian peer-to-peer packet based protocol. SCSI commands are 6, 10, 12, or 16 bytes long, often followed by an associated data payload.

SCSI commands can be transported over just about any kind of bus, and are the default protocol for storage devices attached to USB, SATA, SAS, Fibre Channel, FireWire, and ATAPI
devices. SCSI packets are also commonly exchanged over Infiniband, `I20`_, TCP/IP (`iSCSI`_), even `Parallel ports`_.


.. _subsystem_design:

Design of the Linux SCSI subsystem
==================================

The SCSI subsystem uses a three layer design, with upper, mid, and low layers. Every operation involving the SCSI subsystem (such as reading a sector from a disk) uses one driver
at each of the 3 levels: one upper layer driver, one lower layer driver, and the SCSI midlayer.

The SCSI upper layer provides the interface between userspace and the kernel, in the form of block and char device nodes for I/O and ioctl(). The SCSI lower layer contains drivers
for specific hardware devices.

In between is the SCSI mid-layer, analogous to a network routing layer such as the IPv4 stack. The SCSI mid-layer routes a packet based data protocol between the upper layer's /dev
nodes and the corresponding devices in the lower layer. It manages command queues, provides error handling and power management functions, and responds to ioctl() requests.

.. _SCSI protocol: http://www.t10.org/scsi-3.htm
.. _I20: http://i2o.shadowconnect.com/faq.php
.. _iSCSI: https://en.wikipedia.org/wiki/ISCSI
.. _Parallel ports: http://cyberelk.net/tim/parport/parscsi.html
