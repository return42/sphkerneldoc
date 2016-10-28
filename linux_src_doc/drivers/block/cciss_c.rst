.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/cciss.c

.. _`add_to_scan_list`:

add_to_scan_list
================

.. c:function:: int add_to_scan_list(struct ctlr_info *h)

    add controller to rescan queue

    :param struct ctlr_info \*h:
        Pointer to the controller.

.. _`add_to_scan_list.description`:

Description
-----------

Adds the controller to the rescan queue if not already on the queue.

returns 1 if added to the queue, 0 if skipped (could be on the
queue already, or the controller could be initializing or shutting
down).

.. _`remove_from_scan_list`:

remove_from_scan_list
=====================

.. c:function:: void remove_from_scan_list(struct ctlr_info *h)

    remove controller from rescan queue

    :param struct ctlr_info \*h:
        Pointer to the controller.

.. _`remove_from_scan_list.description`:

Description
-----------

Removes the controller from the rescan queue if present. Blocks if
the controller is currently conducting a rescan.  The controller

.. _`remove_from_scan_list.can-be-in-one-of-three-states`:

can be in one of three states
-----------------------------

1. Doesn't need a scan
2. On the scan list, but not scanning yet (we remove it)
3. Busy scanning (and not on the list). In this case we want to wait for
the scan to complete to make sure the scanning thread for this
controller is completely idle.

.. _`scan_thread`:

scan_thread
===========

.. c:function:: int scan_thread(void *data)

    kernel thread used to rescan controllers

    :param void \*data:
        Ignored.

.. _`scan_thread.description`:

Description
-----------

A kernel thread used scan for drive topology changes on
controllers. The thread processes only one controller at a time
using a queue.  Controllers are added to the queue using
\ :c:func:`add_to_scan_list`\  and removed from the queue either after done
processing or using \ :c:func:`remove_from_scan_list`\ .

returns 0.

.. This file was automatic generated / don't edit.

