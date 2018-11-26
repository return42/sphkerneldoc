.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_dbg.h

.. _`dpu_dbg_init_dbg_buses`:

dpu_dbg_init_dbg_buses
======================

.. c:function:: void dpu_dbg_init_dbg_buses(u32 hwversion)

    initialize debug bus dumping support for the chipset

    :param hwversion:
        Chipset revision
    :type hwversion: u32

.. _`dpu_dbg_init`:

dpu_dbg_init
============

.. c:function:: int dpu_dbg_init(struct device *dev)

    initialize global dpu debug facilities: regdump

    :param dev:
        device handle
    :type dev: struct device \*

.. _`dpu_dbg_init.return`:

Return
------

0 or -ERROR

.. _`dpu_dbg_debugfs_register`:

dpu_dbg_debugfs_register
========================

.. c:function:: int dpu_dbg_debugfs_register(struct dentry *debugfs_root)

    register entries at the given debugfs dir

    :param debugfs_root:
        debugfs root in which to create dpu debug entries
    :type debugfs_root: struct dentry \*

.. _`dpu_dbg_debugfs_register.return`:

Return
------

0 or -ERROR

.. _`dpu_dbg_destroy`:

dpu_dbg_destroy
===============

.. c:function:: void dpu_dbg_destroy( void)

    destroy the global dpu debug facilities

    :param void:
        no arguments
    :type void: 

.. _`dpu_dbg_destroy.return`:

Return
------

none

.. _`dpu_dbg_dump`:

dpu_dbg_dump
============

.. c:function:: void dpu_dbg_dump(bool queue_work, const char *name, bool dump_dbgbus_dpu, bool dump_dbgbus_vbif_rt)

    trigger dumping of all dpu_dbg facilities

    :param queue_work:
        whether to queue the dumping work to the work_struct
    :type queue_work: bool

    :param name:
        string indicating origin of dump
    :type name: const char \*

    :param dump_dbgbus_dpu:
        *undescribed*
    :type dump_dbgbus_dpu: bool

    :param dump_dbgbus_vbif_rt:
        *undescribed*
    :type dump_dbgbus_vbif_rt: bool

.. _`dpu_dbg_dump.return`:

Return
------

none

.. _`dpu_dbg_set_dpu_top_offset`:

dpu_dbg_set_dpu_top_offset
==========================

.. c:function:: void dpu_dbg_set_dpu_top_offset(u32 blk_off)

    set the target specific offset from mdss base address of the top registers. Used for accessing debug bus controls.

    :param blk_off:
        offset from mdss base of the top block
    :type blk_off: u32

.. This file was automatic generated / don't edit.

