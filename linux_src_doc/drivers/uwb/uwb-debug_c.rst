.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/uwb-debug.c

.. _`uwb_dbg_add_rc`:

uwb_dbg_add_rc
==============

.. c:function:: void uwb_dbg_add_rc(struct uwb_rc *rc)

    add a debug interface for a radio controller

    :param rc:
        the radio controller
    :type rc: struct uwb_rc \*

.. _`uwb_dbg_del_rc`:

uwb_dbg_del_rc
==============

.. c:function:: void uwb_dbg_del_rc(struct uwb_rc *rc)

    remove a radio controller's debug interface

    :param rc:
        the radio controller
    :type rc: struct uwb_rc \*

.. _`uwb_dbg_init`:

uwb_dbg_init
============

.. c:function:: void uwb_dbg_init( void)

    initialize the debug interface sub-module

    :param void:
        no arguments
    :type void: 

.. _`uwb_dbg_exit`:

uwb_dbg_exit
============

.. c:function:: void uwb_dbg_exit( void)

    clean-up the debug interface sub-module

    :param void:
        no arguments
    :type void: 

.. _`uwb_dbg_create_pal_dir`:

uwb_dbg_create_pal_dir
======================

.. c:function:: struct dentry *uwb_dbg_create_pal_dir(struct uwb_pal *pal)

    create a debugfs directory for a PAL

    :param pal:
        The PAL.
    :type pal: struct uwb_pal \*

.. This file was automatic generated / don't edit.

