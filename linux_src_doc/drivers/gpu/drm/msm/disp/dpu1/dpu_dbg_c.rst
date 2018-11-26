.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_dbg.c

.. _`dpu_dbg_reg_base`:

struct dpu_dbg_reg_base
=======================

.. c:type:: struct dpu_dbg_reg_base

    register region base. may sub-ranges: sub-ranges are used for dumping or may not have sub-ranges: dumping is base -> max_offset

.. _`dpu_dbg_reg_base.definition`:

Definition
----------

.. code-block:: c

    struct dpu_dbg_reg_base {
        struct list_head reg_base_head;
        char name[REG_BASE_NAME_LEN];
        void __iomem *base;
        size_t off;
        size_t cnt;
        size_t max_offset;
        char *buf;
        size_t buf_len;
        void (*cb)(void *ptr);
        void *cb_ptr;
    }

.. _`dpu_dbg_reg_base.members`:

Members
-------

reg_base_head
    head of this node

name
    register base name

base
    base pointer

off
    cached offset of region for manual register dumping

cnt
    cached range of region for manual register dumping

max_offset
    length of region

buf
    buffer used for manual register dumping

buf_len
    buffer length used for manual register dumping

cb
    callback for external dump function, null if not defined

cb_ptr
    private pointer to callback function

.. _`_dpu_dbg_enable_power`:

\_dpu_dbg_enable_power
======================

.. c:function:: void _dpu_dbg_enable_power(int enable)

    use callback to turn power on for hw register access

    :param enable:
        whether to turn power on or off
    :type enable: int

.. _`_dpu_dump_array`:

\_dpu_dump_array
================

.. c:function:: void _dpu_dump_array(const char *name, bool dump_dbgbus_dpu, bool dump_dbgbus_vbif_rt)

    dump array of register bases

    :param name:
        string indicating origin of dump
    :type name: const char \*

    :param dump_dbgbus_dpu:
        whether to dump the dpu debug bus
    :type dump_dbgbus_dpu: bool

    :param dump_dbgbus_vbif_rt:
        whether to dump the vbif rt debug bus
    :type dump_dbgbus_vbif_rt: bool

.. _`_dpu_dump_work`:

\_dpu_dump_work
===============

.. c:function:: void _dpu_dump_work(struct work_struct *work)

    deferred dump work function

    :param work:
        work structure
    :type work: struct work_struct \*

.. _`dpu_dbg_dump_write`:

dpu_dbg_dump_write
==================

.. c:function:: ssize_t dpu_dbg_dump_write(struct file *file, const char __user *user_buf, size_t count, loff_t *ppos)

    debugfs write handler for debug dump

    :param file:
        file handler
    :type file: struct file \*

    :param user_buf:
        user buffer content from debugfs
    :type user_buf: const char __user \*

    :param count:
        size of user buffer
    :type count: size_t

    :param ppos:
        position offset of user buffer
    :type ppos: loff_t \*

.. _`dpu_dbg_destroy`:

dpu_dbg_destroy
===============

.. c:function:: void dpu_dbg_destroy( void)

    destroy dpu debug facilities

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

