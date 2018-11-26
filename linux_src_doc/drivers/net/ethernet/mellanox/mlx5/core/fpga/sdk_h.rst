.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx5/core/fpga/sdk.h

.. _`innova-sdk`:

Innova SDK
==========

This header defines the in-kernel API for Innova FPGA client drivers.

.. _`mlx5_fpga_access_type`:

enum mlx5_fpga_access_type
==========================

.. c:type:: enum mlx5_fpga_access_type

    Enumerated the different methods possible for accessing the device memory address space

.. _`mlx5_fpga_access_type.definition`:

Definition
----------

.. code-block:: c

    enum mlx5_fpga_access_type {
        MLX5_FPGA_ACCESS_TYPE_I2C,
        MLX5_FPGA_ACCESS_TYPE_DONTCARE
    };

.. _`mlx5_fpga_access_type.constants`:

Constants
---------

MLX5_FPGA_ACCESS_TYPE_I2C
    *undescribed*

MLX5_FPGA_ACCESS_TYPE_DONTCARE
    *undescribed*

.. _`mlx5_fpga_dma_entry`:

struct mlx5_fpga_dma_entry
==========================

.. c:type:: struct mlx5_fpga_dma_entry

    A scatter-gather DMA entry

.. _`mlx5_fpga_dma_entry.definition`:

Definition
----------

.. code-block:: c

    struct mlx5_fpga_dma_entry {
        void *data;
        unsigned int size;
        dma_addr_t dma_addr;
    }

.. _`mlx5_fpga_dma_entry.members`:

Members
-------

data
    Virtual address pointer to the data

size
    Size in bytes of the data

dma_addr
    Private member. Physical DMA-mapped address of the data

.. _`mlx5_fpga_dma_buf`:

struct mlx5_fpga_dma_buf
========================

.. c:type:: struct mlx5_fpga_dma_buf

    A packet buffer May contain up to 2 scatter-gather data entries

.. _`mlx5_fpga_dma_buf.definition`:

Definition
----------

.. code-block:: c

    struct mlx5_fpga_dma_buf {
        enum dma_data_direction dma_dir;
        struct mlx5_fpga_dma_entry sg[2];
        struct list_head list;
        void (*complete)(struct mlx5_fpga_conn *conn,struct mlx5_fpga_device *fdev, struct mlx5_fpga_dma_buf *buf, u8 status);
    }

.. _`mlx5_fpga_dma_buf.members`:

Members
-------

dma_dir
    DMA direction

sg
    Scatter-gather entries pointing to the data in memory

list
    Item in SQ backlog, for TX packets

complete
    Completion routine, for TX packets@conn: FPGA Connection this packet was sent to
    \ ``fdev``\ : FPGA device this packet was sent to
    \ ``buf``\ : The packet buffer
    \ ``status``\ : 0 if successful, or an error code otherwise

.. _`mlx5_fpga_conn_attr`:

struct mlx5_fpga_conn_attr
==========================

.. c:type:: struct mlx5_fpga_conn_attr

    FPGA connection attributes Describes the attributes of a connection

.. _`mlx5_fpga_conn_attr.definition`:

Definition
----------

.. code-block:: c

    struct mlx5_fpga_conn_attr {
        unsigned int tx_size;
        unsigned int rx_size;
        void (*recv_cb)(void *cb_arg, struct mlx5_fpga_dma_buf *buf);
        void *cb_arg;
    }

.. _`mlx5_fpga_conn_attr.members`:

Members
-------

tx_size
    Size of connection TX queue, in packets

rx_size
    Size of connection RX queue, in packets

recv_cb
    Callback function which is called for received packets@cb_arg: The value provided in mlx5_fpga_conn_attr.cb_arg
    \ ``buf``\ : A buffer containing a received packet

    buf is guaranteed to only contain a single scatter-gather entry.
    The size of the actual packet received is specified in buf.sg[0].size
    When this callback returns, the packet buffer may be re-used for
    subsequent receives.

cb_arg
    *undescribed*

.. _`mlx5_fpga_sbu_conn_create`:

mlx5_fpga_sbu_conn_create
=========================

.. c:function:: struct mlx5_fpga_conn *mlx5_fpga_sbu_conn_create(struct mlx5_fpga_device *fdev, struct mlx5_fpga_conn_attr *attr)

    Initialize a new FPGA SBU connection

    :param fdev:
        The FPGA device
    :type fdev: struct mlx5_fpga_device \*

    :param attr:
        Attributes of the new connection
    :type attr: struct mlx5_fpga_conn_attr \*

.. _`mlx5_fpga_sbu_conn_create.description`:

Description
-----------

Sets up a new FPGA SBU connection with the specified attributes.
The receive callback function may be called for incoming messages even
before this function returns.

The caller must eventually destroy the connection by calling
mlx5_fpga_sbu_conn_destroy.

.. _`mlx5_fpga_sbu_conn_create.return`:

Return
------

A new connection, or \ :c:func:`ERR_PTR`\  error value otherwise.

.. _`mlx5_fpga_sbu_conn_destroy`:

mlx5_fpga_sbu_conn_destroy
==========================

.. c:function:: void mlx5_fpga_sbu_conn_destroy(struct mlx5_fpga_conn *conn)

    Destroy an FPGA SBU connection

    :param conn:
        The FPGA SBU connection to destroy
    :type conn: struct mlx5_fpga_conn \*

.. _`mlx5_fpga_sbu_conn_destroy.description`:

Description
-----------

Cleans up an FPGA SBU connection which was previously created with
mlx5_fpga_sbu_conn_create.

.. _`mlx5_fpga_sbu_conn_sendmsg`:

mlx5_fpga_sbu_conn_sendmsg
==========================

.. c:function:: int mlx5_fpga_sbu_conn_sendmsg(struct mlx5_fpga_conn *conn, struct mlx5_fpga_dma_buf *buf)

    Queue the transmission of a packet

    :param conn:
        *undescribed*
    :type conn: struct mlx5_fpga_conn \*

    :param buf:
        The packet buffer
    :type buf: struct mlx5_fpga_dma_buf \*

.. _`mlx5_fpga_sbu_conn_sendmsg.description`:

Description
-----------

Queues a packet for transmission over an FPGA SBU connection.
The buffer should not be modified or freed until completion.
Upon completion, the buf's \ :c:func:`complete`\  callback is invoked, indicating the
success or error status of the transmission.

.. _`mlx5_fpga_sbu_conn_sendmsg.return`:

Return
------

0 if successful, or an error value otherwise.

.. _`mlx5_fpga_mem_read`:

mlx5_fpga_mem_read
==================

.. c:function:: int mlx5_fpga_mem_read(struct mlx5_fpga_device *fdev, size_t size, u64 addr, void *buf, enum mlx5_fpga_access_type access_type)

    Read from FPGA memory address space

    :param fdev:
        The FPGA device
    :type fdev: struct mlx5_fpga_device \*

    :param size:
        Size of chunk to read, in bytes
    :type size: size_t

    :param addr:
        Starting address to read from, in FPGA address space
    :type addr: u64

    :param buf:
        Buffer to read into
    :type buf: void \*

    :param access_type:
        Method for reading
    :type access_type: enum mlx5_fpga_access_type

.. _`mlx5_fpga_mem_read.description`:

Description
-----------

Reads from the specified address into the specified buffer.
The address may point to configuration space or to DDR.
Large reads may be performed internally as several non-atomic operations.
This function may sleep, so should not be called from atomic contexts.

.. _`mlx5_fpga_mem_read.return`:

Return
------

0 if successful, or an error value otherwise.

.. _`mlx5_fpga_mem_write`:

mlx5_fpga_mem_write
===================

.. c:function:: int mlx5_fpga_mem_write(struct mlx5_fpga_device *fdev, size_t size, u64 addr, void *buf, enum mlx5_fpga_access_type access_type)

    Write to FPGA memory address space

    :param fdev:
        The FPGA device
    :type fdev: struct mlx5_fpga_device \*

    :param size:
        Size of chunk to write, in bytes
    :type size: size_t

    :param addr:
        Starting address to write to, in FPGA address space
    :type addr: u64

    :param buf:
        Buffer which contains data to write
    :type buf: void \*

    :param access_type:
        Method for writing
    :type access_type: enum mlx5_fpga_access_type

.. _`mlx5_fpga_mem_write.description`:

Description
-----------

Writes the specified buffer data to FPGA memory at the specified address.
The address may point to configuration space or to DDR.
Large writes may be performed internally as several non-atomic operations.
This function may sleep, so should not be called from atomic contexts.

.. _`mlx5_fpga_mem_write.return`:

Return
------

0 if successful, or an error value otherwise.

.. _`mlx5_fpga_get_sbu_caps`:

mlx5_fpga_get_sbu_caps
======================

.. c:function:: int mlx5_fpga_get_sbu_caps(struct mlx5_fpga_device *fdev, int size, void *buf)

    Read the SBU capabilities

    :param fdev:
        The FPGA device
    :type fdev: struct mlx5_fpga_device \*

    :param size:
        Size of the buffer to read into
    :type size: int

    :param buf:
        Buffer to read the capabilities into
    :type buf: void \*

.. _`mlx5_fpga_get_sbu_caps.description`:

Description
-----------

Reads the FPGA SBU capabilities into the specified buffer.
The format of the capabilities buffer is SBU-dependent.

.. _`mlx5_fpga_get_sbu_caps.return`:

Return
------

0 if successful
-EINVAL if the buffer is not large enough to contain SBU caps
or any other error value otherwise.

.. This file was automatic generated / don't edit.

