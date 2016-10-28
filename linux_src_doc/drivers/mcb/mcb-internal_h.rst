.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mcb/mcb-internal.h

.. _`chameleon_fpga_header`:

struct chameleon_fpga_header
============================

.. c:type:: struct chameleon_fpga_header


.. _`chameleon_fpga_header.definition`:

Definition
----------

.. code-block:: c

    struct chameleon_fpga_header {
        u8 revision;
        char model;
        u8 minor;
        u8 bus_type;
        u16 magic;
        u16 reserved;
        char filename[CHAMELEON_FILENAME_LEN];
    }

.. _`chameleon_fpga_header.members`:

Members
-------

revision
    Revison of Chameleon table in FPGA

model
    Chameleon table model ASCII char

minor
    Revision minor

bus_type
    Bus type (usually \ ``CHAMELEON_BUS_WISHBONE``\ )

magic
    Chameleon header magic number (0xabce for version 2)

reserved
    Reserved

filename
    Filename of FPGA bitstream

.. _`chameleon_gdd`:

struct chameleon_gdd
====================

.. c:type:: struct chameleon_gdd

    Chameleon General Device Descriptor

.. _`chameleon_gdd.definition`:

Definition
----------

.. code-block:: c

    struct chameleon_gdd {
        __le32 reg1;
        __le32 reg2;
        __le32 offset;
        __le32 size;
    }

.. _`chameleon_gdd.members`:

Members
-------

reg1
    *undescribed*

reg2
    *undescribed*

offset
    beginning of the address window of desired module

size
    size of the module's address window

.. _`chameleon_bdd`:

struct chameleon_bdd
====================

.. c:type:: struct chameleon_bdd

    Chameleon Bridge Device Descriptor

.. _`chameleon_bdd.definition`:

Definition
----------

.. code-block:: c

    struct chameleon_bdd {
        unsigned int irq:6;
        unsigned int rev:6;
        unsigned int var:6;
        unsigned int dev:10;
        unsigned int dtype:4;
        unsigned int bar:3;
        unsigned int inst:6;
        unsigned int dbar:3;
        unsigned int group:6;
        unsigned int reserved:14;
        u32 chamoff;
        u32 offset;
        u32 size;
    }

.. _`chameleon_bdd.members`:

Members
-------

irq
    the position in the FPGA's IRQ controller vector

rev
    the revision of the variant's implementation

var
    the variant of the IP core

dev
    the device  the IP core is

dtype
    device descriptor type

bar
    BAR offset that must be added to module offset

inst
    the instance number of the device, 0 is first instance

dbar
    destination bar from the bus \_behind\_ the bridge

group
    *undescribed*

reserved
    *undescribed*

chamoff
    offset within the BAR of the source bus

offset
    *undescribed*

size
    *undescribed*

.. This file was automatic generated / don't edit.

