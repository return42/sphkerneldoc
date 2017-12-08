.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mod_devicetable.h

.. _`usb_device_id`:

struct usb_device_id
====================

.. c:type:: struct usb_device_id

    identifies USB devices for probing and hotplugging

.. _`usb_device_id.definition`:

Definition
----------

.. code-block:: c

    struct usb_device_id {
        __u16 match_flags;
        __u16 idVendor;
        __u16 idProduct;
        __u16 bcdDevice_lo;
        __u16 bcdDevice_hi;
        __u8 bDeviceClass;
        __u8 bDeviceSubClass;
        __u8 bDeviceProtocol;
        __u8 bInterfaceClass;
        __u8 bInterfaceSubClass;
        __u8 bInterfaceProtocol;
        __u8 bInterfaceNumber;
        kernel_ulong_t driver_info __attribute__((aligned(sizeof(kernel_ulong_t))));
    }

.. _`usb_device_id.members`:

Members
-------

match_flags
    Bit mask controlling which of the other fields are used to
    match against new devices. Any field except for driver_info may be
    used, although some only make sense in conjunction with other fields.
    This is usually set by a USB_DEVICE_*() macro, which sets all
    other fields in this structure except for driver_info.

idVendor
    USB vendor ID for a device; numbers are assigned
    by the USB forum to its members.

idProduct
    Vendor-assigned product ID.

bcdDevice_lo
    Low end of range of vendor-assigned product version numbers.
    This is also used to identify individual product versions, for
    a range consisting of a single device.

bcdDevice_hi
    High end of version number range.  The range of product
    versions is inclusive.

bDeviceClass
    Class of device; numbers are assigned
    by the USB forum.  Products may choose to implement classes,
    or be vendor-specific.  Device classes specify behavior of all
    the interfaces on a device.

bDeviceSubClass
    Subclass of device; associated with bDeviceClass.

bDeviceProtocol
    Protocol of device; associated with bDeviceClass.

bInterfaceClass
    Class of interface; numbers are assigned
    by the USB forum.  Products may choose to implement classes,
    or be vendor-specific.  Interface classes specify behavior only
    of a given interface; other interfaces may support other classes.

bInterfaceSubClass
    Subclass of interface; associated with bInterfaceClass.

bInterfaceProtocol
    Protocol of interface; associated with bInterfaceClass.

bInterfaceNumber
    Number of interface; composite devices may use
    fixed interface numbers to differentiate between vendor-specific
    interfaces.

driver_info
    Holds information used by the driver.  Usually it holds
    a pointer to a descriptor understood by the driver, or perhaps
    device flags.

.. _`usb_device_id.description`:

Description
-----------

In most cases, drivers will create a table of device IDs by using
\ :c:func:`USB_DEVICE`\ , or similar macros designed for that purpose.
They will then export it to userspace using \ :c:func:`MODULE_DEVICE_TABLE`\ ,
and provide it to the USB core through their usb_driver structure.

See the \ :c:func:`usb_match_id`\  function for information about how matches are
performed.  Briefly, you will normally use one of several macros to help
construct these entries.  Each entry you provide will either identify
one or more specific products, or will identify a class of products
which have agreed to behave the same.  You should put the more specific
matches towards the beginning of your table, so that driver_info can
record quirks of specific products.

.. _`mdio_device_id`:

struct mdio_device_id
=====================

.. c:type:: struct mdio_device_id

    identifies PHY devices on an MDIO/MII bus

.. _`mdio_device_id.definition`:

Definition
----------

.. code-block:: c

    struct mdio_device_id {
        __u32 phy_id;
        __u32 phy_id_mask;
    }

.. _`mdio_device_id.members`:

Members
-------

phy_id
    The result of
    (mdio_read(&MII_PHYSID1) << 16 | mdio_read(&PHYSID2)) & \ ``phy_id_mask``\ 
    for this PHY type

phy_id_mask
    Defines the significant bits of \ ``phy_id``\ .  A value of 0
    is used to terminate an array of struct mdio_device_id.

.. _`amba_id`:

struct amba_id
==============

.. c:type:: struct amba_id

    identifies a device on an AMBA bus

.. _`amba_id.definition`:

Definition
----------

.. code-block:: c

    struct amba_id {
        unsigned int id;
        unsigned int mask;
        void *data;
    }

.. _`amba_id.members`:

Members
-------

id
    The significant bits if the hardware device ID

mask
    Bitmask specifying which bits of the id field are significant when
    matching.  A driver binds to a device when ((hardware device ID) & mask)
    == id.

data
    Private data used by the driver.

.. _`mips_cdmm_device_id`:

struct mips_cdmm_device_id
==========================

.. c:type:: struct mips_cdmm_device_id

    identifies devices in MIPS CDMM bus

.. _`mips_cdmm_device_id.definition`:

Definition
----------

.. code-block:: c

    struct mips_cdmm_device_id {
        __u8 type;
    }

.. _`mips_cdmm_device_id.members`:

Members
-------

type
    Device type identifier.

.. _`mei_cl_device_id`:

struct mei_cl_device_id
=======================

.. c:type:: struct mei_cl_device_id

    MEI client device identifier

.. _`mei_cl_device_id.definition`:

Definition
----------

.. code-block:: c

    struct mei_cl_device_id {
        char name[MEI_CL_NAME_SIZE];
        uuid_le uuid;
        __u8 version;
        kernel_ulong_t driver_info;
    }

.. _`mei_cl_device_id.members`:

Members
-------

name
    helper name

uuid
    client uuid

version
    client protocol version

driver_info
    information used by the driver.

.. _`mei_cl_device_id.description`:

Description
-----------

identifies mei client device by uuid and name

.. _`rio_device_id`:

struct rio_device_id
====================

.. c:type:: struct rio_device_id

    RIO device identifier

.. _`rio_device_id.definition`:

Definition
----------

.. code-block:: c

    struct rio_device_id {
        __u16 did, vid;
        __u16 asm_did, asm_vid;
    }

.. _`rio_device_id.members`:

Members
-------

did
    RapidIO device ID

vid
    RapidIO vendor ID

asm_did
    RapidIO assembly device ID

asm_vid
    RapidIO assembly vendor ID

.. _`rio_device_id.description`:

Description
-----------

Identifies a RapidIO device based on both the device/vendor IDs and
the assembly device/vendor IDs.

.. _`fsl_mc_device_id`:

struct fsl_mc_device_id
=======================

.. c:type:: struct fsl_mc_device_id

    MC object device identifier

.. _`fsl_mc_device_id.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_device_id {
        __u16 vendor;
        const char obj_type[16];
    }

.. _`fsl_mc_device_id.members`:

Members
-------

vendor
    vendor ID

obj_type
    MC object type

.. _`fsl_mc_device_id.description`:

Description
-----------

Type of entries in the "device Id" table for MC object devices supported by
a MC object device driver. The last entry of the table has vendor set to 0x0

.. _`tb_service_id`:

struct tb_service_id
====================

.. c:type:: struct tb_service_id

    Thunderbolt service identifiers

.. _`tb_service_id.definition`:

Definition
----------

.. code-block:: c

    struct tb_service_id {
        __u32 match_flags;
        char protocol_key[8 + 1];
        __u32 protocol_id;
        __u32 protocol_version;
        __u32 protocol_revision;
        kernel_ulong_t driver_data;
    }

.. _`tb_service_id.members`:

Members
-------

match_flags
    Flags used to match the structure

protocol_key
    Protocol key the service supports

protocol_id
    Protocol id the service supports

protocol_version
    Version of the protocol

protocol_revision
    Revision of the protocol software

driver_data
    Driver specific data

.. _`tb_service_id.description`:

Description
-----------

Thunderbolt XDomain services are exposed as devices where each device
carries the protocol information the service supports. Thunderbolt
XDomain service drivers match against that information.

.. This file was automatic generated / don't edit.

