.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_debugfs.c

.. _`i40e_dbg_find_vsi`:

i40e_dbg_find_vsi
=================

.. c:function:: struct i40e_vsi *i40e_dbg_find_vsi(struct i40e_pf *pf, int seid)

    searches for the vsi with the given seid

    :param pf:
        the PF structure to search for the vsi
    :type pf: struct i40e_pf \*

    :param seid:
        seid of the vsi it is searching for
    :type seid: int

.. _`i40e_dbg_find_veb`:

i40e_dbg_find_veb
=================

.. c:function:: struct i40e_veb *i40e_dbg_find_veb(struct i40e_pf *pf, int seid)

    searches for the veb with the given seid

    :param pf:
        the PF structure to search for the veb
    :type pf: struct i40e_pf \*

    :param seid:
        seid of the veb it is searching for
    :type seid: int

.. _`i40e_dbg_command_read`:

i40e_dbg_command_read
=====================

.. c:function:: ssize_t i40e_dbg_command_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for command datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to write the data for the user to read
    :type buffer: char __user \*

    :param count:
        the size of the user's buffer
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`i40e_dbg_dump_vsi_seid`:

i40e_dbg_dump_vsi_seid
======================

.. c:function:: void i40e_dbg_dump_vsi_seid(struct i40e_pf *pf, int seid)

    handles dump vsi seid write into command datum

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

    :param seid:
        the seid the user put in
    :type seid: int

.. _`i40e_dbg_dump_aq_desc`:

i40e_dbg_dump_aq_desc
=====================

.. c:function:: void i40e_dbg_dump_aq_desc(struct i40e_pf *pf)

    handles dump aq_desc write into command datum

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

.. _`i40e_dbg_dump_desc`:

i40e_dbg_dump_desc
==================

.. c:function:: void i40e_dbg_dump_desc(int cnt, int vsi_seid, int ring_id, int desc_n, struct i40e_pf *pf, bool is_rx_ring)

    handles dump desc write into command datum

    :param cnt:
        number of arguments that the user supplied
    :type cnt: int

    :param vsi_seid:
        vsi id entered by user
    :type vsi_seid: int

    :param ring_id:
        ring id entered by user
    :type ring_id: int

    :param desc_n:
        descriptor number entered by user
    :type desc_n: int

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

    :param is_rx_ring:
        true if rx, false if tx
    :type is_rx_ring: bool

.. _`i40e_dbg_dump_vsi_no_seid`:

i40e_dbg_dump_vsi_no_seid
=========================

.. c:function:: void i40e_dbg_dump_vsi_no_seid(struct i40e_pf *pf)

    handles dump vsi write into command datum

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

.. _`i40e_dbg_dump_eth_stats`:

i40e_dbg_dump_eth_stats
=======================

.. c:function:: void i40e_dbg_dump_eth_stats(struct i40e_pf *pf, struct i40e_eth_stats *estats)

    handles dump stats write into command datum

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

    :param estats:
        the eth stats structure to be dumped
    :type estats: struct i40e_eth_stats \*

.. _`i40e_dbg_dump_veb_seid`:

i40e_dbg_dump_veb_seid
======================

.. c:function:: void i40e_dbg_dump_veb_seid(struct i40e_pf *pf, int seid)

    handles dump stats of a single given veb

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

    :param seid:
        the seid the user put in
    :type seid: int

.. _`i40e_dbg_dump_veb_all`:

i40e_dbg_dump_veb_all
=====================

.. c:function:: void i40e_dbg_dump_veb_all(struct i40e_pf *pf)

    dumps all known veb's stats

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

.. _`i40e_dbg_dump_vf`:

i40e_dbg_dump_vf
================

.. c:function:: void i40e_dbg_dump_vf(struct i40e_pf *pf, int vf_id)

    dump VF info

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

    :param vf_id:
        the vf_id from the user
    :type vf_id: int

.. _`i40e_dbg_dump_vf_all`:

i40e_dbg_dump_vf_all
====================

.. c:function:: void i40e_dbg_dump_vf_all(struct i40e_pf *pf)

    dump VF info for all VFs

    :param pf:
        the i40e_pf created in command write
    :type pf: struct i40e_pf \*

.. _`i40e_dbg_command_write`:

i40e_dbg_command_write
======================

.. c:function:: ssize_t i40e_dbg_command_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into command datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to find the user's data
    :type buffer: const char __user \*

    :param count:
        the length of the user's data
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`i40e_dbg_netdev_ops_read`:

i40e_dbg_netdev_ops_read
========================

.. c:function:: ssize_t i40e_dbg_netdev_ops_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for netdev_ops datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to write the data for the user to read
    :type buffer: char __user \*

    :param count:
        the size of the user's buffer
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`i40e_dbg_netdev_ops_write`:

i40e_dbg_netdev_ops_write
=========================

.. c:function:: ssize_t i40e_dbg_netdev_ops_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into netdev_ops datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to find the user's data
    :type buffer: const char __user \*

    :param count:
        the length of the user's data
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`i40e_dbg_pf_init`:

i40e_dbg_pf_init
================

.. c:function:: void i40e_dbg_pf_init(struct i40e_pf *pf)

    setup the debugfs directory for the PF

    :param pf:
        the PF that is starting up
    :type pf: struct i40e_pf \*

.. _`i40e_dbg_pf_exit`:

i40e_dbg_pf_exit
================

.. c:function:: void i40e_dbg_pf_exit(struct i40e_pf *pf)

    clear out the PF's debugfs entries

    :param pf:
        the PF that is stopping
    :type pf: struct i40e_pf \*

.. _`i40e_dbg_init`:

i40e_dbg_init
=============

.. c:function:: void i40e_dbg_init( void)

    start up debugfs for the driver

    :param void:
        no arguments
    :type void: 

.. _`i40e_dbg_exit`:

i40e_dbg_exit
=============

.. c:function:: void i40e_dbg_exit( void)

    clean out the driver's debugfs entries

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

