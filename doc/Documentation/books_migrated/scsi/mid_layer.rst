.. -*- coding: utf-8; mode: rst -*-

.. _mid_layer:

**************
SCSI mid layer
**************


.. _midlayer_implementation:

SCSI midlayer implementation
============================


.. _scsi_device.h:

include/scsi/scsi_device.h
--------------------------


.. kernel-doc:: include/scsi/scsi_device.h
    :man-sect: 9
    :internal:


.. _scsi.c:

drivers/scsi/scsi.c
-------------------

Main file for the SCSI midlayer.


.. kernel-doc:: drivers/scsi/scsi.c
    :man-sect: 9
    :export:


.. _scsicam.c:

drivers/scsi/scsicam.c
----------------------

`SCSI Common Access Method <http://www.t10.org/ftp/t10/drafts/cam/cam-r12b.pdf>`__
support functions, for use with HDIO_GETGEO, etc.


.. kernel-doc:: drivers/scsi/scsicam.c
    :man-sect: 9
    :export:


.. _scsi_error.c:

drivers/scsi/scsi_error.c
-------------------------

Common SCSI error/timeout handling routines.


.. kernel-doc:: drivers/scsi/scsi_error.c
    :man-sect: 9
    :export:


.. _scsi_devinfo.c:

drivers/scsi/scsi_devinfo.c
---------------------------

Manage scsi_dev_info_list, which tracks blacklisted and whitelisted
devices.


.. kernel-doc:: drivers/scsi/scsi_devinfo.c
    :man-sect: 9
    :internal:


.. _scsi_ioctl.c:

drivers/scsi/scsi_ioctl.c
-------------------------

Handle ioctl() calls for SCSI devices.


.. kernel-doc:: drivers/scsi/scsi_ioctl.c
    :man-sect: 9
    :export:


.. _scsi_lib.c:

drivers/scsi/scsi_lib.c
-----------------------

SCSI queuing library.


.. kernel-doc:: drivers/scsi/scsi_lib.c
    :man-sect: 9
    :export:


.. _scsi_lib_dma.c:

drivers/scsi/scsi_lib_dma.c
---------------------------

SCSI library functions depending on DMA (map and unmap scatter-gather
lists).


.. kernel-doc:: drivers/scsi/scsi_lib_dma.c
    :man-sect: 9
    :export:


.. _scsi_module.c:

drivers/scsi/scsi_module.c
--------------------------

The file drivers/scsi/scsi_module.c contains legacy support for
old-style host templates. It should never be used by any new driver.


.. _scsi_proc.c:

drivers/scsi/scsi_proc.c
------------------------

The functions in this file provide an interface between the PROC file
system and the SCSI device drivers It is mainly used for debugging,
statistics and to pass information directly to the lowlevel driver. I.E.
plumbing to manage /proc/scsi/*


.. kernel-doc:: drivers/scsi/scsi_proc.c
    :man-sect: 9
    :internal:


.. _scsi_netlink.c:

drivers/scsi/scsi_netlink.c
---------------------------

Infrastructure to provide async events from transports to userspace via
netlink, using a single NETLINK_SCSITRANSPORT protocol for all
transports. See
`the original patch submission <http://marc.info/?l=linux-scsi&m=115507374832500&w=2>`__
for more details.


.. kernel-doc:: drivers/scsi/scsi_netlink.c
    :man-sect: 9
    :internal:


.. _scsi_scan.c:

drivers/scsi/scsi_scan.c
------------------------

Scan a host to determine which (if any) devices are attached. The
general scanning/probing algorithm is as follows, exceptions are made to
it depending on device specific flags, compilation options, and global
variable (boot or module load time) settings. A specific LUN is scanned
via an INQUIRY command; if the LUN has a device attached, a scsi_device
is allocated and setup for it. For every id of every channel on the
given host, start by scanning LUN 0. Skip hosts that don't respond at
all to a scan of LUN 0. Otherwise, if LUN 0 has a device attached,
allocate and setup a scsi_device for it. If target is SCSI-3 or up,
issue a REPORT LUN, and scan all of the LUNs returned by the REPORT LUN;
else, sequentially scan LUNs up until some maximum is reached, or a LUN
is seen that cannot have a device attached to it.


.. kernel-doc:: drivers/scsi/scsi_scan.c
    :man-sect: 9
    :internal:


.. _scsi_sysctl.c:

drivers/scsi/scsi_sysctl.c
--------------------------

Set up the sysctl entry: "/dev/scsi/logging_level"
(DEV_SCSI_LOGGING_LEVEL) which sets/returns scsi_logging_level.


.. _scsi_sysfs.c:

drivers/scsi/scsi_sysfs.c
-------------------------

SCSI sysfs interface routines.


.. kernel-doc:: drivers/scsi/scsi_sysfs.c
    :man-sect: 9
    :export:


.. _hosts.c:

drivers/scsi/hosts.c
--------------------

mid to lowlevel SCSI driver interface


.. kernel-doc:: drivers/scsi/hosts.c
    :man-sect: 9
    :export:


.. _constants.c:

drivers/scsi/constants.c
------------------------

mid to lowlevel SCSI driver interface


.. kernel-doc:: drivers/scsi/constants.c
    :man-sect: 9
    :export:


.. _Transport_classes:

Transport classes
=================

Transport classes are service libraries for drivers in the SCSI lower
layer, which expose transport attributes in sysfs.


.. _Fibre_Channel_transport:

Fibre Channel transport
-----------------------

The file drivers/scsi/scsi_transport_fc.c defines transport attributes
for Fibre Channel.


.. kernel-doc:: drivers/scsi/scsi_transport_fc.c
    :man-sect: 9
    :export:


.. _iSCSI_transport:

iSCSI transport class
---------------------

The file drivers/scsi/scsi_transport_iscsi.c defines transport
attributes for the iSCSI class, which sends SCSI packets over TCP/IP
connections.


.. kernel-doc:: drivers/scsi/scsi_transport_iscsi.c
    :man-sect: 9
    :export:


.. _SAS_transport:

Serial Attached SCSI (SAS) transport class
------------------------------------------

The file drivers/scsi/scsi_transport_sas.c defines transport
attributes for Serial Attached SCSI, a variant of SATA aimed at large
high-end systems.

The SAS transport class contains common code to deal with SAS HBAs, an
aproximated representation of SAS topologies in the driver model, and
various sysfs attributes to expose these topologies and management
interfaces to userspace.

In addition to the basic SCSI core objects this transport class
introduces two additional intermediate objects: The SAS PHY as
represented by struct sas_phy defines an "outgoing" PHY on a SAS HBA or
Expander, and the SAS remote PHY represented by struct sas_rphy defines
an "incoming" PHY on a SAS Expander or end device. Note that this is
purely a software concept, the underlying hardware for a PHY and a
remote PHY is the exactly the same.

There is no concept of a SAS port in this code, users can see what PHYs
form a wide port based on the port_identifier attribute, which is the
same for all PHYs in a port.


.. kernel-doc:: drivers/scsi/scsi_transport_sas.c
    :man-sect: 9
    :export:


.. _SATA_transport:

SATA transport class
--------------------

The SATA transport is handled by libata, which has its own book of
documentation in this directory.


.. _SPI_transport:

Parallel SCSI (SPI) transport class
-----------------------------------

The file drivers/scsi/scsi_transport_spi.c defines transport
attributes for traditional (fast/wide/ultra) SCSI busses.


.. kernel-doc:: drivers/scsi/scsi_transport_spi.c
    :man-sect: 9
    :export:


.. _SRP_transport:

SCSI RDMA (SRP) transport class
-------------------------------

The file drivers/scsi/scsi_transport_srp.c defines transport
attributes for SCSI over Remote Direct Memory Access.


.. kernel-doc:: drivers/scsi/scsi_transport_srp.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
