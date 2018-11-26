.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/pmc.c

.. _`wil_pmc_alloc`:

wil_pmc_alloc
=============

.. c:function:: void wil_pmc_alloc(struct wil6210_priv *wil, int num_descriptors, int descriptor_size)

    ring) and the required number of descriptors of required size. Initialize the descriptors as required by pmc dma. The descriptors' buffers dwords are initialized to hold dword's serial number in the lsw and reserved value PCM_DATA_INVALID_DW_VAL in the msw.

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param num_descriptors:
        *undescribed*
    :type num_descriptors: int

    :param descriptor_size:
        *undescribed*
    :type descriptor_size: int

.. _`wil_pmc_free`:

wil_pmc_free
============

.. c:function:: void wil_pmc_free(struct wil6210_priv *wil, int send_pmc_cmd)

    ring and release all buffers. At the end release the p-ring memory

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param send_pmc_cmd:
        *undescribed*
    :type send_pmc_cmd: int

.. _`wil_pmc_last_cmd_status`:

wil_pmc_last_cmd_status
=======================

.. c:function:: int wil_pmc_last_cmd_status(struct wil6210_priv *wil)

    alloc/free/read. 0 - success or negative errno

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

.. _`wil_pmc_read`:

wil_pmc_read
============

.. c:function:: ssize_t wil_pmc_read(struct file *filp, char __user *buf, size_t count, loff_t *f_pos)

    depends on descriptor size configured during alloc request.

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param f_pos:
        *undescribed*
    :type f_pos: loff_t \*

.. This file was automatic generated / don't edit.

