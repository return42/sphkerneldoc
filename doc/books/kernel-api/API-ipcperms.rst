.. -*- coding: utf-8; mode: rst -*-

.. _API-ipcperms:

========
ipcperms
========

*man ipcperms(9)*

*4.6.0-rc5*

check ipc permissions


Synopsis
========

.. c:function:: int ipcperms( struct ipc_namespace * ns, struct kern_ipc_perm * ipcp, short flag )

Arguments
=========

``ns``
    ipc namespace

``ipcp``
    ipc permission set

``flag``
    desired permission set


Description
===========

Check user, group, other permissions for access to ipc resources. return
0 if allowed

``flag`` will most probably be 0 or S_...UGO from <linux/stat.h>


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
