.. -*- coding: utf-8; mode: rst -*-

.. _mid_layer:

==============
SCSI mid layer
==============


.. _midlayer_implementation:

SCSI midlayer implementation
============================


.. _scsi_device.h:

include/scsi/scsi_device.h
--------------------------


.. toctree::
    :maxdepth: 1

    API-shost-for-each-device
    API---shost-for-each-device
    API-scsi-device-supports-vpd


.. _scsi.c:

drivers/scsi/scsi.c
-------------------

Main file for the SCSI midlayer.


.. toctree::
    :maxdepth: 1

    API-scsi-cmd-get-serial
    API-scsi-change-queue-depth
    API-scsi-track-queue-full
    API-scsi-get-vpd-page
    API-scsi-report-opcode
    API-scsi-device-get
    API-scsi-device-put
    API-starget-for-each-device
    API---starget-for-each-device
    API---scsi-device-lookup-by-target
    API-scsi-device-lookup-by-target
    API---scsi-device-lookup
    API-scsi-device-lookup


.. _scsicam.c:

drivers/scsi/scsicam.c
----------------------

`SCSI Common Access Method <http://www.t10.org/ftp/t10/drafts/cam/cam-r12b.pdf>`__
support functions, for use with HDIO_GETGEO, etc.


.. toctree::
    :maxdepth: 1

    API-scsi-bios-ptable
    API-scsicam-bios-param
    API-scsi-partsize


.. _scsi_error.c:

drivers/scsi/scsi_error.c
-------------------------

Common SCSI error/timeout handling routines.


.. toctree::
    :maxdepth: 1

    API-scsi-schedule-eh
    API-scsi-block-when-processing-errors
    API-scsi-eh-prep-cmnd
    API-scsi-eh-restore-cmnd
    API-scsi-eh-finish-cmd
    API-scsi-eh-get-sense
    API-scsi-eh-ready-devs
    API-scsi-eh-flush-done-q
    API-scsi-ioctl-reset
    API-scsi-get-sense-info-fld


.. _scsi_devinfo.c:

drivers/scsi/scsi_devinfo.c
---------------------------

Manage scsi_dev_info_list, which tracks blacklisted and whitelisted
devices.


.. toctree::
    :maxdepth: 1

    API-scsi-dev-info-list-add
    API-scsi-dev-info-list-find
    API-scsi-dev-info-list-add-str
    API-scsi-get-device-flags
    API-scsi-exit-devinfo
    API-scsi-init-devinfo


.. _scsi_ioctl.c:

drivers/scsi/scsi_ioctl.c
-------------------------

Handle ioctl() calls for SCSI devices.


.. toctree::
    :maxdepth: 1

    API-scsi-ioctl


.. _scsi_lib.c:

drivers/scsi/scsi_lib.c
-----------------------

SCSI queuing library.


.. toctree::
    :maxdepth: 1

    API-scsi-execute
    API-scsi-mode-select
    API-scsi-mode-sense
    API-scsi-test-unit-ready
    API-scsi-device-set-state
    API-sdev-evt-send
    API-sdev-evt-alloc
    API-sdev-evt-send-simple
    API-scsi-device-quiesce
    API-scsi-device-resume
    API-scsi-internal-device-block
    API-scsi-internal-device-unblock
    API-scsi-kmap-atomic-sg
    API-scsi-kunmap-atomic-sg
    API-scsi-vpd-lun-id


.. _scsi_lib_dma.c:

drivers/scsi/scsi_lib_dma.c
---------------------------

SCSI library functions depending on DMA (map and unmap scatter-gather
lists).


.. toctree::
    :maxdepth: 1

    API-scsi-dma-map
    API-scsi-dma-unmap


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


.. toctree::
    :maxdepth: 1

    API-scsi-proc-hostdir-add
    API-scsi-proc-hostdir-rm
    API-scsi-proc-host-add
    API-scsi-proc-host-rm
    API-proc-print-scsidevice
    API-scsi-add-single-device
    API-scsi-remove-single-device
    API-proc-scsi-write
    API-proc-scsi-open
    API-scsi-init-procfs
    API-scsi-exit-procfs


.. _scsi_netlink.c:

drivers/scsi/scsi_netlink.c
---------------------------

Infrastructure to provide async events from transports to userspace via
netlink, using a single NETLINK_SCSITRANSPORT protocol for all
transports. See
`the original patch submission <http://marc.info/?l=linux-scsi&m=115507374832500&w=2>`__
for more details.


.. toctree::
    :maxdepth: 1

    API-scsi-nl-rcv-msg
    API-scsi-netlink-init
    API-scsi-netlink-exit


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


.. toctree::
    :maxdepth: 1

    API-scsi-complete-async-scans
    API-scsi-unlock-floptical
    API-scsi-alloc-sdev
    API-scsi-target-reap-ref-release
    API-scsi-alloc-target
    API-scsi-target-reap
    API-scsi-probe-lun
    API-scsi-add-lun
    API-scsi-inq-str
    API-scsi-probe-and-add-lun
    API-scsi-sequential-lun-scan
    API-scsi-report-lun-scan
    API-scsi-prep-async-scan
    API-scsi-finish-async-scan


.. _scsi_sysctl.c:

drivers/scsi/scsi_sysctl.c
--------------------------

Set up the sysctl entry: "/dev/scsi/logging_level"
(DEV_SCSI_LOGGING_LEVEL) which sets/returns scsi_logging_level.


.. _scsi_sysfs.c:

drivers/scsi/scsi_sysfs.c
-------------------------

SCSI sysfs interface routines.


.. toctree::
    :maxdepth: 1

    API-scsi-remove-device
    API-scsi-remove-target


.. _hosts.c:

drivers/scsi/hosts.c
--------------------

mid to lowlevel SCSI driver interface


.. toctree::
    :maxdepth: 1

    API-scsi-host-set-state
    API-scsi-remove-host
    API-scsi-add-host-with-dma
    API-scsi-host-alloc
    API-scsi-host-lookup
    API-scsi-host-get
    API-scsi-host-put
    API-scsi-queue-work
    API-scsi-flush-work


.. _constants.c:

drivers/scsi/constants.c
------------------------

mid to lowlevel SCSI driver interface


.. toctree::
    :maxdepth: 1

    mid_layer-000-001-016-003


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


.. toctree::
    :maxdepth: 1

    API-fc-get-event-number
    API-fc-host-post-event
    API-fc-host-post-vendor-event
    API-fc-remove-host
    API-fc-remote-port-add
    API-fc-remote-port-delete
    API-fc-remote-port-rolechg
    API-fc-block-scsi-eh
    API-fc-vport-create
    API-fc-vport-terminate


.. _iSCSI_transport:

iSCSI transport class
---------------------

The file drivers/scsi/scsi_transport_iscsi.c defines transport
attributes for the iSCSI class, which sends SCSI packets over TCP/IP
connections.


.. toctree::
    :maxdepth: 1

    API-iscsi-create-flashnode-sess
    API-iscsi-create-flashnode-conn
    API-iscsi-is-flashnode-conn-dev
    API-iscsi-find-flashnode-sess
    API-iscsi-find-flashnode-conn
    API-iscsi-destroy-flashnode-sess
    API-iscsi-destroy-all-flashnode
    API-iscsi-scan-finished
    API-iscsi-block-scsi-eh
    API-iscsi-unblock-session
    API-iscsi-create-session
    API-iscsi-destroy-session
    API-iscsi-create-conn
    API-iscsi-destroy-conn
    API-iscsi-session-event


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


.. toctree::
    :maxdepth: 1

    API-is-sas-attached
    API-sas-remove-children
    API-sas-remove-host
    API-sas-get-address
    API-sas-tlr-supported
    API-sas-disable-tlr
    API-sas-enable-tlr
    API-sas-phy-alloc
    API-sas-phy-add
    API-sas-phy-free
    API-sas-phy-delete
    API-scsi-is-sas-phy
    API-sas-port-add
    API-sas-port-free
    API-sas-port-delete
    API-scsi-is-sas-port
    API-sas-port-get-phy
    API-sas-port-add-phy
    API-sas-port-delete-phy
    API-sas-end-device-alloc
    API-sas-expander-alloc
    API-sas-rphy-add
    API-sas-rphy-free
    API-sas-rphy-delete
    API-sas-rphy-unlink
    API-sas-rphy-remove
    API-scsi-is-sas-rphy
    API-sas-attach-transport
    API-sas-release-transport


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


.. toctree::
    :maxdepth: 1

    API-spi-schedule-dv-device
    API-spi-display-xfer-agreement
    API-spi-populate-tag-msg


.. _SRP_transport:

SCSI RDMA (SRP) transport class
-------------------------------

The file drivers/scsi/scsi_transport_srp.c defines transport
attributes for SCSI over Remote Direct Memory Access.


.. toctree::
    :maxdepth: 1

    API-srp-tmo-valid
    API-srp-start-tl-fail-timers
    API-srp-reconnect-rport
    API-srp-rport-get
    API-srp-rport-put
    API-srp-rport-add
    API-srp-rport-del
    API-srp-remove-host
    API-srp-stop-rport-timers
    API-srp-attach-transport
    API-srp-release-transport




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
