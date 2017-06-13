.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_ctl.h

.. _`mpt3iocinfo`:

MPT3IOCINFO
===========

.. c:function::  MPT3IOCINFO()

.. _`mpt3_ioctl_header`:

struct mpt3_ioctl_header
========================

.. c:type:: struct mpt3_ioctl_header

    main header structure \ ``ioc_number``\  -  IOC unit number \ ``port_number``\  - IOC port number \ ``max_data_size``\  - maximum number bytes to transfer on read

.. _`mpt3_ioctl_header.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_header {
        uint32_t ioc_number;
        uint32_t port_number;
        uint32_t max_data_size;
    }

.. _`mpt3_ioctl_header.members`:

Members
-------

ioc_number
    *undescribed*

port_number
    *undescribed*

max_data_size
    *undescribed*

.. _`mpt3_ioctl_diag_reset`:

struct mpt3_ioctl_diag_reset
============================

.. c:type:: struct mpt3_ioctl_diag_reset

    diagnostic reset \ ``hdr``\  - generic header

.. _`mpt3_ioctl_diag_reset.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_diag_reset {
        struct mpt3_ioctl_header hdr;
    }

.. _`mpt3_ioctl_diag_reset.members`:

Members
-------

hdr
    *undescribed*

.. _`mpt3_ioctl_pci_info`:

struct mpt3_ioctl_pci_info
==========================

.. c:type:: struct mpt3_ioctl_pci_info

    pci device info \ ``device``\  - pci device id \ ``function``\  - pci function id \ ``bus``\  - pci bus id \ ``segment_id``\  - pci segment id

.. _`mpt3_ioctl_pci_info.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_pci_info {
        union u;
        uint32_t segment_id;
    }

.. _`mpt3_ioctl_pci_info.members`:

Members
-------

u
    *undescribed*

segment_id
    *undescribed*

.. _`mpt3_ioctl_iocinfo`:

struct mpt3_ioctl_iocinfo
=========================

.. c:type:: struct mpt3_ioctl_iocinfo

    generic controller info \ ``hdr``\  - generic header \ ``adapter_type``\  - type of adapter (spi, fc, sas) \ ``port_number``\  - port number \ ``pci_id``\  - PCI Id \ ``hw_rev``\  - hardware revision \ ``sub_system_device``\  - PCI subsystem Device ID \ ``sub_system_vendor``\  - PCI subsystem Vendor ID \ ``rsvd0``\  - reserved \ ``firmware_version``\  - firmware version \ ``bios_version``\  - BIOS version \ ``driver_version``\  - driver version - 32 ASCII characters \ ``rsvd1``\  - reserved \ ``scsi_id``\  - scsi id of adapter 0 \ ``rsvd2``\  - reserved \ ``pci_information``\  - pci info (2nd revision)

.. _`mpt3_ioctl_iocinfo.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_iocinfo {
        struct mpt3_ioctl_header hdr;
        uint32_t adapter_type;
        uint32_t port_number;
        uint32_t pci_id;
        uint32_t hw_rev;
        uint32_t subsystem_device;
        uint32_t subsystem_vendor;
        uint32_t rsvd0;
        uint32_t firmware_version;
        uint32_t bios_version;
        uint8_t driver_version[MPT2_IOCTL_VERSION_LENGTH];
        uint8_t rsvd1;
        uint8_t scsi_id;
        uint16_t rsvd2;
        struct mpt3_ioctl_pci_info pci_information;
    }

.. _`mpt3_ioctl_iocinfo.members`:

Members
-------

hdr
    *undescribed*

adapter_type
    *undescribed*

port_number
    *undescribed*

pci_id
    *undescribed*

hw_rev
    *undescribed*

subsystem_device
    *undescribed*

subsystem_vendor
    *undescribed*

rsvd0
    *undescribed*

firmware_version
    *undescribed*

bios_version
    *undescribed*

rsvd1
    *undescribed*

scsi_id
    *undescribed*

rsvd2
    *undescribed*

pci_information
    *undescribed*

.. _`mpt3_ioctl_eventquery`:

struct mpt3_ioctl_eventquery
============================

.. c:type:: struct mpt3_ioctl_eventquery

    query event count and type \ ``hdr``\  - generic header \ ``event_entries``\  - number of events returned by get_event_report \ ``rsvd``\  - reserved \ ``event_types``\  - type of events currently being captured

.. _`mpt3_ioctl_eventquery.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_eventquery {
        struct mpt3_ioctl_header hdr;
        uint16_t event_entries;
        uint16_t rsvd;
        uint32_t event_types[MPI2_EVENT_NOTIFY_EVENTMASK_WORDS];
    }

.. _`mpt3_ioctl_eventquery.members`:

Members
-------

hdr
    *undescribed*

event_entries
    *undescribed*

rsvd
    *undescribed*

.. _`mpt3_ioctl_eventenable`:

struct mpt3_ioctl_eventenable
=============================

.. c:type:: struct mpt3_ioctl_eventenable

    enable/disable event capturing \ ``hdr``\  - generic header \ ``event_types``\  - toggle off/on type of events to be captured

.. _`mpt3_ioctl_eventenable.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_eventenable {
        struct mpt3_ioctl_header hdr;
        uint32_t event_types[4];
    }

.. _`mpt3_ioctl_eventenable.members`:

Members
-------

hdr
    *undescribed*

.. _`mpt3_ioctl_events`:

struct MPT3_IOCTL_EVENTS
========================

.. c:type:: struct MPT3_IOCTL_EVENTS

    @event - the event that was reported \ ``context``\  - unique value for each event assigned by driver \ ``data``\  - event data returned in fw reply message

.. _`mpt3_ioctl_events.definition`:

Definition
----------

.. code-block:: c

    struct MPT3_IOCTL_EVENTS {
        uint32_t event;
        uint32_t context;
        uint8_t data[MPT3_EVENT_DATA_SIZE];
    }

.. _`mpt3_ioctl_events.members`:

Members
-------

event
    *undescribed*

context
    *undescribed*

.. _`mpt3_ioctl_eventreport`:

struct mpt3_ioctl_eventreport
=============================

.. c:type:: struct mpt3_ioctl_eventreport

    returing event log \ ``hdr``\  - generic header \ ``event_data``\  - (see struct MPT3_IOCTL_EVENTS)

.. _`mpt3_ioctl_eventreport.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_eventreport {
        struct mpt3_ioctl_header hdr;
        struct MPT3_IOCTL_EVENTS event_data[1];
    }

.. _`mpt3_ioctl_eventreport.members`:

Members
-------

hdr
    *undescribed*

.. _`mpt3_ioctl_command`:

struct mpt3_ioctl_command
=========================

.. c:type:: struct mpt3_ioctl_command

    generic mpt firmware passthru ioctl \ ``hdr``\  - generic header \ ``timeout``\  - command timeout in seconds. (if zero then use driver default value). \ ``reply_frame_buf_ptr``\  - reply location \ ``data_in_buf_ptr``\  - destination for read \ ``data_out_buf_ptr``\  - data source for write \ ``sense_data_ptr``\  - sense data location \ ``max_reply_bytes``\  - maximum number of reply bytes to be sent to app. \ ``data_in_size``\  - number bytes for data transfer in (read) \ ``data_out_size``\  - number bytes for data transfer out (write) \ ``max_sense_bytes``\  - maximum number of bytes for auto sense buffers \ ``data_sge_offset``\  - offset in words from the start of the request message to the first SGL \ ``mf``\ [1];

.. _`mpt3_ioctl_command.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_command {
        struct mpt3_ioctl_header hdr;
        uint32_t timeout;
        void __user *reply_frame_buf_ptr;
        void __user *data_in_buf_ptr;
        void __user *data_out_buf_ptr;
        void __user *sense_data_ptr;
        uint32_t max_reply_bytes;
        uint32_t data_in_size;
        uint32_t data_out_size;
        uint32_t max_sense_bytes;
        uint32_t data_sge_offset;
        uint8_t mf[1];
    }

.. _`mpt3_ioctl_command.members`:

Members
-------

hdr
    *undescribed*

timeout
    *undescribed*

reply_frame_buf_ptr
    *undescribed*

data_in_buf_ptr
    *undescribed*

data_out_buf_ptr
    *undescribed*

sense_data_ptr
    *undescribed*

max_reply_bytes
    *undescribed*

data_in_size
    *undescribed*

data_out_size
    *undescribed*

max_sense_bytes
    *undescribed*

data_sge_offset
    *undescribed*

.. _`mpt3_ioctl_btdh_mapping`:

struct mpt3_ioctl_btdh_mapping
==============================

.. c:type:: struct mpt3_ioctl_btdh_mapping

    mapping info \ ``hdr``\  - generic header \ ``id``\  - target device identification number \ ``bus``\  - SCSI bus number that the target device exists on \ ``handle``\  - device handle for the target device \ ``rsvd``\  - reserved

.. _`mpt3_ioctl_btdh_mapping.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_ioctl_btdh_mapping {
        struct mpt3_ioctl_header hdr;
        uint32_t id;
        uint32_t bus;
        uint16_t handle;
        uint16_t rsvd;
    }

.. _`mpt3_ioctl_btdh_mapping.members`:

Members
-------

hdr
    *undescribed*

id
    *undescribed*

bus
    *undescribed*

handle
    *undescribed*

rsvd
    *undescribed*

.. _`mpt3_ioctl_btdh_mapping.description`:

Description
-----------

To obtain a bus/id the application sets
handle to valid handle, and bus/id to 0xFFFF.

To obtain the device handle the application sets
bus/id valid value, and the handle to 0xFFFF.

.. _`mpt3_diag_register`:

struct mpt3_diag_register
=========================

.. c:type:: struct mpt3_diag_register

    application register with driver \ ``hdr``\  - generic header \ ``reserved``\  - \ ``buffer_type``\  - specifies either TRACE, SNAPSHOT, or EXTENDED \ ``application_flags``\  - misc flags \ ``diagnostic_flags``\  - specifies flags affecting command processing \ ``product_specific``\  - product specific information \ ``requested_buffer_size``\  - buffers size in bytes \ ``unique_id``\  - tag specified by application that is used to signal ownership of the buffer.

.. _`mpt3_diag_register.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_diag_register {
        struct mpt3_ioctl_header hdr;
        uint8_t reserved;
        uint8_t buffer_type;
        uint16_t application_flags;
        uint32_t diagnostic_flags;
        uint32_t product_specific[MPT3_PRODUCT_SPECIFIC_DWORDS];
        uint32_t requested_buffer_size;
        uint32_t unique_id;
    }

.. _`mpt3_diag_register.members`:

Members
-------

hdr
    *undescribed*

reserved
    *undescribed*

buffer_type
    *undescribed*

application_flags
    *undescribed*

diagnostic_flags
    *undescribed*

requested_buffer_size
    *undescribed*

unique_id
    *undescribed*

.. _`mpt3_diag_register.description`:

Description
-----------

This will allow the driver to setup any required buffers that will be
needed by firmware to communicate with the driver.

.. _`mpt3_diag_unregister`:

struct mpt3_diag_unregister
===========================

.. c:type:: struct mpt3_diag_unregister

    application unregister with driver \ ``hdr``\  - generic header \ ``unique_id``\  - tag uniquely identifies the buffer to be unregistered

.. _`mpt3_diag_unregister.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_diag_unregister {
        struct mpt3_ioctl_header hdr;
        uint32_t unique_id;
    }

.. _`mpt3_diag_unregister.members`:

Members
-------

hdr
    *undescribed*

unique_id
    *undescribed*

.. _`mpt3_diag_unregister.description`:

Description
-----------

This will allow the driver to cleanup any memory allocated for diag
messages and to free up any resources.

.. _`mpt3_diag_query`:

struct mpt3_diag_query
======================

.. c:type:: struct mpt3_diag_query

    query relevant info associated with diag buffers \ ``hdr``\  - generic header \ ``reserved``\  - \ ``buffer_type``\  - specifies either TRACE, SNAPSHOT, or EXTENDED \ ``application_flags``\  - misc flags \ ``diagnostic_flags``\  - specifies flags affecting command processing \ ``product_specific``\  - product specific information \ ``total_buffer_size``\  - diag buffer size in bytes \ ``driver_added_buffer_size``\  - size of extra space appended to end of buffer \ ``unique_id``\  - unique id associated with this buffer.

.. _`mpt3_diag_query.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_diag_query {
        struct mpt3_ioctl_header hdr;
        uint8_t reserved;
        uint8_t buffer_type;
        uint16_t application_flags;
        uint32_t diagnostic_flags;
        uint32_t product_specific[MPT3_PRODUCT_SPECIFIC_DWORDS];
        uint32_t total_buffer_size;
        uint32_t driver_added_buffer_size;
        uint32_t unique_id;
    }

.. _`mpt3_diag_query.members`:

Members
-------

hdr
    *undescribed*

reserved
    *undescribed*

buffer_type
    *undescribed*

application_flags
    *undescribed*

diagnostic_flags
    *undescribed*

total_buffer_size
    *undescribed*

driver_added_buffer_size
    *undescribed*

unique_id
    *undescribed*

.. _`mpt3_diag_query.description`:

Description
-----------

The application will send only buffer_type and unique_id.  Driver will
inspect unique_id first, if valid, fill in all the info.  If unique_id is
0x00, the driver will return info specified by Buffer Type.

.. _`mpt3_diag_release`:

struct mpt3_diag_release
========================

.. c:type:: struct mpt3_diag_release

    request to send Diag Release Message to firmware \ ``hdr``\  - generic header \ ``unique_id``\  - tag uniquely identifies the buffer to be released

.. _`mpt3_diag_release.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_diag_release {
        struct mpt3_ioctl_header hdr;
        uint32_t unique_id;
    }

.. _`mpt3_diag_release.members`:

Members
-------

hdr
    *undescribed*

unique_id
    *undescribed*

.. _`mpt3_diag_release.description`:

Description
-----------

This allows ownership of the specified buffer to returned to the driver,
allowing an application to read the buffer without fear that firmware is
overwriting information in the buffer.

.. _`mpt3_diag_read_buffer`:

struct mpt3_diag_read_buffer
============================

.. c:type:: struct mpt3_diag_read_buffer

    request for copy of the diag buffer \ ``hdr``\  - generic header \ ``status``\  - \ ``reserved``\  - \ ``flags``\  - misc flags \ ``starting_offset``\  - starting offset within drivers buffer where to start reading data at into the specified application buffer \ ``bytes_to_read``\  - number of bytes to copy from the drivers buffer into the application buffer starting at starting_offset. \ ``unique_id``\  - unique id associated with this buffer. \ ``diagnostic_data``\  - data payload

.. _`mpt3_diag_read_buffer.definition`:

Definition
----------

.. code-block:: c

    struct mpt3_diag_read_buffer {
        struct mpt3_ioctl_header hdr;
        uint8_t status;
        uint8_t reserved;
        uint16_t flags;
        uint32_t starting_offset;
        uint32_t bytes_to_read;
        uint32_t unique_id;
        uint32_t diagnostic_data[1];
    }

.. _`mpt3_diag_read_buffer.members`:

Members
-------

hdr
    *undescribed*

status
    *undescribed*

reserved
    *undescribed*

flags
    *undescribed*

starting_offset
    *undescribed*

bytes_to_read
    *undescribed*

unique_id
    *undescribed*

.. This file was automatic generated / don't edit.

