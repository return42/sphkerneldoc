.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spi/spi-mem.h

.. _`spi_mem_data_dir`:

enum spi_mem_data_dir
=====================

.. c:type:: enum spi_mem_data_dir

    describes the direction of a SPI memory data transfer from the controller perspective

.. _`spi_mem_data_dir.definition`:

Definition
----------

.. code-block:: c

    enum spi_mem_data_dir {
        SPI_MEM_DATA_IN,
        SPI_MEM_DATA_OUT
    };

.. _`spi_mem_data_dir.constants`:

Constants
---------

SPI_MEM_DATA_IN
    data coming from the SPI memory

SPI_MEM_DATA_OUT
    data sent the SPI memory

.. _`spi_mem_op`:

struct spi_mem_op
=================

.. c:type:: struct spi_mem_op

    describes a SPI memory operation

.. _`spi_mem_op.definition`:

Definition
----------

.. code-block:: c

    struct spi_mem_op {
        struct {
            u8 buswidth;
            u8 opcode;
        } cmd;
        struct {
            u8 nbytes;
            u8 buswidth;
            u64 val;
        } addr;
        struct {
            u8 nbytes;
            u8 buswidth;
        } dummy;
        struct {
            u8 buswidth;
            enum spi_mem_data_dir dir;
            unsigned int nbytes;
            union {
                void *in;
                const void *out;
            } buf;
        } data;
    }

.. _`spi_mem_op.members`:

Members
-------

cmd
    *undescribed*

cmd.buswidth
    number of IO lines used to transmit the command

cmd.opcode
    operation opcode

addr
    *undescribed*

addr.nbytes
    number of address bytes to send. Can be zero if the operation
    does not need to send an address

addr.buswidth
    number of IO lines used to transmit the address cycles

addr.val
    address value. This value is always sent MSB first on the bus.
    Note that only \ ``addr.nbytes``\  are taken into account in this
    address value, so users should make sure the value fits in the
    assigned number of bytes.

dummy
    *undescribed*

dummy.nbytes
    number of dummy bytes to send after an opcode or address. Can
    be zero if the operation does not require dummy bytes

dummy.buswidth
    number of IO lanes used to transmit the dummy bytes

data
    *undescribed*

data.buswidth
    number of IO lanes used to send/receive the data

data.dir
    direction of the transfer

data.nbytes
    number of data bytes to send/receive. Can be zero if the
    operation does not involve transferring data

data.buf.in
    input buffer (must be DMA-able)

data.buf.out
    output buffer (must be DMA-able)

.. _`spi_mem`:

struct spi_mem
==============

.. c:type:: struct spi_mem

    describes a SPI memory device

.. _`spi_mem.definition`:

Definition
----------

.. code-block:: c

    struct spi_mem {
        struct spi_device *spi;
        void *drvpriv;
        const char *name;
    }

.. _`spi_mem.members`:

Members
-------

spi
    the underlying SPI device

drvpriv
    spi_mem_driver private data

name
    name of the SPI memory device

.. _`spi_mem.description`:

Description
-----------

Extra information that describe the SPI memory device and may be needed by
the controller to properly handle this device should be placed here.

One example would be the device size since some controller expose their SPI
mem devices through a io-mapped region.

.. _`spi_mem_driver`:

struct spi_mem_driver
=====================

.. c:type:: struct spi_mem_driver

    SPI memory driver

.. _`spi_mem_driver.definition`:

Definition
----------

.. code-block:: c

    struct spi_mem_driver {
        struct spi_driver spidrv;
        int (*probe)(struct spi_mem *mem);
        int (*remove)(struct spi_mem *mem);
        void (*shutdown)(struct spi_mem *mem);
    }

.. _`spi_mem_driver.members`:

Members
-------

spidrv
    inherit from a SPI driver

probe
    probe a SPI memory. Usually where detection/initialization takes
    place

remove
    remove a SPI memory

shutdown
    take appropriate action when the system is shutdown

.. _`spi_mem_driver.description`:

Description
-----------

This is just a thin wrapper around a spi_driver. The core takes care of
allocating the spi_mem object and forwarding the probe/remove/shutdown
request to the spi_mem_driver. The reason we use this wrapper is because
we might have to stuff more information into the spi_mem struct to let
SPI controllers know more about the SPI memory they interact with, and
having this intermediate layer allows us to do that without adding more
useless fields to the spi_device object.

.. This file was automatic generated / don't edit.

