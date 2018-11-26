.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/debugfs.c

.. _`wil6210_debugfs_init_offset`:

wil6210_debugfs_init_offset
===========================

.. c:function:: void wil6210_debugfs_init_offset(struct wil6210_priv *wil, struct dentry *dbg, void *base, const struct dbg_off * const tbl)

    create set of debugfs files \ ``wil``\  - driver's context, used for printing \ ``dbg``\  - directory on the debugfs, where files will be created \ ``base``\  - base address used in address calculation \ ``tbl``\  - table with file descriptions. Should be terminated with empty element.

    :param wil:
        *undescribed*
    :type wil: struct wil6210_priv \*

    :param dbg:
        *undescribed*
    :type dbg: struct dentry \*

    :param base:
        *undescribed*
    :type base: void \*

    :param tbl:
        *undescribed*
    :type tbl: const struct dbg_off \* const

.. _`wil6210_debugfs_init_offset.description`:

Description
-----------

Creates files accordingly to the \ ``tbl``\ .

.. This file was automatic generated / don't edit.

