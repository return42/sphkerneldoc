.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_debugfs.c

.. _`i40e_dbg_find_vsi`:

i40e_dbg_find_vsi
=================

.. c:function:: struct i40e_vsi *i40e_dbg_find_vsi(struct i40e_pf *pf, int seid)

    searches for the vsi with the given seid

    :param struct i40e_pf \*pf:
        the PF structure to search for the vsi

    :param int seid:
        seid of the vsi it is searching for

.. _`i40e_dbg_find_veb`:

i40e_dbg_find_veb
=================

.. c:function:: struct i40e_veb *i40e_dbg_find_veb(struct i40e_pf *pf, int seid)

    searches for the veb with the given seid

    :param struct i40e_pf \*pf:
        the PF structure to search for the veb

    :param int seid:
        seid of the veb it is searching for

.. _`i40e_dbg_command_read`:

i40e_dbg_command_read
=====================

.. c:function:: ssize_t i40e_dbg_command_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for command datum

    :param struct file \*filp:
        the opened file

    :param char __user \*buffer:
        where to write the data for the user to read

    :param size_t count:
        the size of the user's buffer

    :param loff_t \*ppos:
        file position offset

.. _`i40e_dbg_dump_vsi_seid`:

i40e_dbg_dump_vsi_seid
======================

.. c:function:: void i40e_dbg_dump_vsi_seid(struct i40e_pf *pf, int seid)

    handles dump vsi seid write into command datum

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

    :param int seid:
        the seid the user put in

.. _`i40e_dbg_dump_aq_desc`:

i40e_dbg_dump_aq_desc
=====================

.. c:function:: void i40e_dbg_dump_aq_desc(struct i40e_pf *pf)

    handles dump aq_desc write into command datum

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

.. _`i40e_dbg_dump_desc`:

i40e_dbg_dump_desc
==================

.. c:function:: void i40e_dbg_dump_desc(int cnt, int vsi_seid, int ring_id, int desc_n, struct i40e_pf *pf, bool is_rx_ring)

    handles dump desc write into command datum

    :param int cnt:
        number of arguments that the user supplied

    :param int vsi_seid:
        vsi id entered by user

    :param int ring_id:
        ring id entered by user

    :param int desc_n:
        descriptor number entered by user

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

    :param bool is_rx_ring:
        true if rx, false if tx

.. _`i40e_dbg_dump_vsi_no_seid`:

i40e_dbg_dump_vsi_no_seid
=========================

.. c:function:: void i40e_dbg_dump_vsi_no_seid(struct i40e_pf *pf)

    handles dump vsi write into command datum

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

.. _`i40e_dbg_dump_eth_stats`:

i40e_dbg_dump_eth_stats
=======================

.. c:function:: void i40e_dbg_dump_eth_stats(struct i40e_pf *pf, struct i40e_eth_stats *estats)

    handles dump stats write into command datum

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

    :param struct i40e_eth_stats \*estats:
        the eth stats structure to be dumped

.. _`i40e_dbg_dump_veb_seid`:

i40e_dbg_dump_veb_seid
======================

.. c:function:: void i40e_dbg_dump_veb_seid(struct i40e_pf *pf, int seid)

    handles dump stats of a single given veb

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

    :param int seid:
        the seid the user put in

.. _`i40e_dbg_dump_veb_all`:

i40e_dbg_dump_veb_all
=====================

.. c:function:: void i40e_dbg_dump_veb_all(struct i40e_pf *pf)

    dumps all known veb's stats

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

.. _`i40e_dbg_dump_vf`:

i40e_dbg_dump_vf
================

.. c:function:: void i40e_dbg_dump_vf(struct i40e_pf *pf, int vf_id)

    dump VF info

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

    :param int vf_id:
        the vf_id from the user

.. _`i40e_dbg_dump_vf_all`:

i40e_dbg_dump_vf_all
====================

.. c:function:: void i40e_dbg_dump_vf_all(struct i40e_pf *pf)

    dump VF info for all VFs

    :param struct i40e_pf \*pf:
        the i40e_pf created in command write

.. _`i40e_dbg_command_write`:

i40e_dbg_command_write
======================

.. c:function:: ssize_t i40e_dbg_command_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into command datum

    :param struct file \*filp:
        the opened file

    :param const char __user \*buffer:
        where to find the user's data

    :param size_t count:
        the length of the user's data

    :param loff_t \*ppos:
        file position offset

.. _`i40e_dbg_netdev_ops_read`:

i40e_dbg_netdev_ops_read
========================

.. c:function:: ssize_t i40e_dbg_netdev_ops_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for netdev_ops datum

    :param struct file \*filp:
        the opened file

    :param char __user \*buffer:
        where to write the data for the user to read

    :param size_t count:
        the size of the user's buffer

    :param loff_t \*ppos:
        file position offset

.. _`i40e_dbg_netdev_ops_write`:

i40e_dbg_netdev_ops_write
=========================

.. c:function:: ssize_t i40e_dbg_netdev_ops_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into netdev_ops datum

    :param struct file \*filp:
        the opened file

    :param const char __user \*buffer:
        where to find the user's data

    :param size_t count:
        the length of the user's data

    :param loff_t \*ppos:
        file position offset

.. _`i40e_dbg_pf_init`:

i40e_dbg_pf_init
================

.. c:function:: void i40e_dbg_pf_init(struct i40e_pf *pf)

    setup the debugfs directory for the PF

    :param struct i40e_pf \*pf:
        the PF that is starting up

.. _`i40e_dbg_pf_exit`:

i40e_dbg_pf_exit
================

.. c:function:: void i40e_dbg_pf_exit(struct i40e_pf *pf)

    clear out the PF's debugfs entries

    :param struct i40e_pf \*pf:
        the PF that is stopping

.. _`i40e_dbg_init`:

i40e_dbg_init
=============

.. c:function:: void i40e_dbg_init( void)

    start up debugfs for the driver

    :param  void:
        no arguments

.. _`i40e_dbg_exit`:

i40e_dbg_exit
=============

.. c:function:: void i40e_dbg_exit( void)

    clean out the driver's debugfs entries

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

