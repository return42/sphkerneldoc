.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/ishtp-dev.h

.. _`ishtp_fw_client`:

struct ishtp_fw_client
======================

.. c:type:: struct ishtp_fw_client

    representation of fw client

.. _`ishtp_fw_client.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_fw_client {
        struct ishtp_client_properties props;
        uint8_t client_id;
    }

.. _`ishtp_fw_client.members`:

Members
-------

props
    *undescribed*

client_id
    *undescribed*

.. _`ishtp_fw_client.description`:

Description
-----------

@props - client properties
\ ``client_id``\  - fw client id

.. _`ishtp_msg_data`:

struct ishtp_msg_data
=====================

.. c:type:: struct ishtp_msg_data

    ISHTP message data struct

.. _`ishtp_msg_data.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_msg_data {
        uint32_t size;
        unsigned char *data;
    }

.. _`ishtp_msg_data.members`:

Members
-------

size
    Size of data in the \*data

data
    Pointer to data

.. _`ishtp_device`:

struct ishtp_device
===================

.. c:type:: struct ishtp_device

    ISHTP private device struct

.. _`ishtp_device.definition`:

Definition
----------

.. code-block:: c

    struct ishtp_device {
        struct device *devc;
        struct pci_dev *pdev;
        wait_queue_head_t suspend_wait;
        bool suspend_flag;
        wait_queue_head_t resume_wait;
        bool resume_flag;
        spinlock_t device_lock;
        bool recvd_hw_ready;
        struct hbm_version version;
        int transfer_path;
        enum ishtp_dev_state dev_state;
        enum ishtp_hbm_state hbm_state;
        struct ishtp_cl_rb read_list;
        spinlock_t read_list_spinlock;
        struct list_head cl_list;
        spinlock_t cl_list_lock;
        long open_handle_count;
        struct list_head device_list;
        spinlock_t device_list_lock;
        wait_queue_head_t wait_hw_ready;
        wait_queue_head_t wait_hbm_recvd_msg;
        unsigned char rd_msg_fifo[RD_INT_FIFO_SIZE * IPC_PAYLOAD_SIZE];
        unsigned int rd_msg_fifo_head;
        unsigned int rd_msg_fifo_tail;
        spinlock_t rd_msg_spinlock;
        struct work_struct bh_hbm_work;
        struct wr_msg_ctl_info wr_processing_list_head;
        struct wr_msg_ctl_info wr_free_list_head;
        spinlock_t wr_processing_spinlock;
        spinlock_t out_ipc_spinlock;
        struct ishtp_fw_client *fw_clients;
        unsigned long fw_clients_map[BITS_TO_LONGS(ISHTP_CLIENTS_MAX)];
        unsigned long host_clients_map[BITS_TO_LONGS(ISHTP_CLIENTS_MAX)];
        uint8_t fw_clients_num;
        uint8_t fw_client_presentation_num;
        uint8_t fw_client_index;
        spinlock_t fw_clients_lock;
        int ishtp_host_dma_enabled;
        void *ishtp_host_dma_tx_buf;
        unsigned int ishtp_host_dma_tx_buf_size;
        uint64_t ishtp_host_dma_tx_buf_phys;
        int ishtp_dma_num_slots;
        uint8_t *ishtp_dma_tx_map;
        spinlock_t ishtp_dma_tx_lock;
        void *ishtp_host_dma_rx_buf;
        unsigned int ishtp_host_dma_rx_buf_size;
        uint64_t ishtp_host_dma_rx_buf_phys;
        void (*print_log)(struct ishtp_device *dev, char *format, ...);
        unsigned int ipc_rx_cnt;
        unsigned long long ipc_rx_bytes_cnt;
        unsigned int ipc_tx_cnt;
        unsigned long long ipc_tx_bytes_cnt;
        const struct ishtp_hw_ops *ops;
        size_t mtu;
        uint32_t ishtp_msg_hdr;
        char hw[0];
    }

.. _`ishtp_device.members`:

Members
-------

devc
    *undescribed*

pdev
    *undescribed*

suspend_wait
    *undescribed*

suspend_flag
    *undescribed*

resume_wait
    *undescribed*

resume_flag
    *undescribed*

device_lock
    *undescribed*

recvd_hw_ready
    *undescribed*

version
    *undescribed*

transfer_path
    *undescribed*

dev_state
    *undescribed*

hbm_state
    *undescribed*

read_list
    *undescribed*

read_list_spinlock
    *undescribed*

cl_list
    *undescribed*

cl_list_lock
    *undescribed*

open_handle_count
    *undescribed*

device_list
    *undescribed*

device_list_lock
    *undescribed*

wait_hw_ready
    *undescribed*

wait_hbm_recvd_msg
    *undescribed*

rd_msg_fifo_head
    *undescribed*

rd_msg_fifo_tail
    *undescribed*

rd_msg_spinlock
    *undescribed*

bh_hbm_work
    *undescribed*

wr_processing_list_head
    *undescribed*

wr_free_list_head
    *undescribed*

wr_processing_spinlock
    *undescribed*

out_ipc_spinlock
    *undescribed*

fw_clients
    *undescribed*

fw_clients_num
    *undescribed*

fw_client_presentation_num
    *undescribed*

fw_client_index
    *undescribed*

fw_clients_lock
    *undescribed*

ishtp_host_dma_enabled
    *undescribed*

ishtp_host_dma_tx_buf
    *undescribed*

ishtp_host_dma_tx_buf_size
    *undescribed*

ishtp_host_dma_tx_buf_phys
    *undescribed*

ishtp_dma_num_slots
    *undescribed*

ishtp_dma_tx_map
    *undescribed*

ishtp_dma_tx_lock
    *undescribed*

ishtp_host_dma_rx_buf
    *undescribed*

ishtp_host_dma_rx_buf_size
    *undescribed*

ishtp_host_dma_rx_buf_phys
    *undescribed*

print_log
    *undescribed*

ipc_rx_cnt
    *undescribed*

ipc_rx_bytes_cnt
    *undescribed*

ipc_tx_cnt
    *undescribed*

ipc_tx_bytes_cnt
    *undescribed*

ops
    *undescribed*

mtu
    *undescribed*

ishtp_msg_hdr
    *undescribed*

.. This file was automatic generated / don't edit.

