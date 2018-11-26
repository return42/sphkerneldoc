.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wimax/stack.c

.. _`wimax_state_change`:

wimax_state_change
==================

.. c:function:: void wimax_state_change(struct wimax_dev *wimax_dev, enum wimax_st new_state)

    Set the current state of a WiMAX device

    :param wimax_dev:
        WiMAX device descriptor (properly referenced)
    :type wimax_dev: struct wimax_dev \*

    :param new_state:
        New state to switch to
    :type new_state: enum wimax_st

.. _`wimax_state_change.description`:

Description
-----------

This implements the state changes for the wimax devices. It will

- verify that the state transition is legal (for now it'll just
  print a warning if not) according to the table in
  linux/wimax.h's documentation for 'enum wimax_st'.

- perform the actions needed for leaving the current state and
  whichever are needed for entering the new state.

- issue a report to user space indicating the new state (and an
  optional payload with information about the new state).

.. _`wimax_state_change.note`:

NOTE
----

\ ``wimax_dev``\  must be locked

.. _`wimax_state_get`:

wimax_state_get
===============

.. c:function:: enum wimax_st wimax_state_get(struct wimax_dev *wimax_dev)

    Return the current state of a WiMAX device

    :param wimax_dev:
        WiMAX device descriptor
    :type wimax_dev: struct wimax_dev \*

.. _`wimax_state_get.return`:

Return
------

Current state of the device according to its driver.

.. _`wimax_dev_init`:

wimax_dev_init
==============

.. c:function:: void wimax_dev_init(struct wimax_dev *wimax_dev)

    initialize a newly allocated instance

    :param wimax_dev:
        WiMAX device descriptor to initialize.
    :type wimax_dev: struct wimax_dev \*

.. _`wimax_dev_init.description`:

Description
-----------

Initializes fields of a freshly allocated \ ``wimax_dev``\  instance. This
function assumes that after allocation, the memory occupied by
\ ``wimax_dev``\  was zeroed.

.. _`wimax_dev_add`:

wimax_dev_add
=============

.. c:function:: int wimax_dev_add(struct wimax_dev *wimax_dev, struct net_device *net_dev)

    Register a new WiMAX device

    :param wimax_dev:
        WiMAX device descriptor (as embedded in your \ ``net_dev``\ 's
        priv data). You must have called \ :c:func:`wimax_dev_init`\  on it before.
    :type wimax_dev: struct wimax_dev \*

    :param net_dev:
        net device the \ ``wimax_dev``\  is associated with. The
        function expects \ :c:func:`SET_NETDEV_DEV`\  and \ :c:func:`register_netdev`\  were
        already called on it.
    :type net_dev: struct net_device \*

.. _`wimax_dev_add.description`:

Description
-----------

Registers the new WiMAX device, sets up the user-kernel control
interface (generic netlink) and common WiMAX infrastructure.

Note that the parts that will allow interaction with user space are
setup at the very end, when the rest is in place, as once that
happens, the driver might get user space control requests via
netlink or from debugfs that might translate into calls into
wimax_dev->op_*().

.. _`wimax_dev_rm`:

wimax_dev_rm
============

.. c:function:: void wimax_dev_rm(struct wimax_dev *wimax_dev)

    Unregister an existing WiMAX device

    :param wimax_dev:
        WiMAX device descriptor
    :type wimax_dev: struct wimax_dev \*

.. _`wimax_dev_rm.description`:

Description
-----------

Unregisters a WiMAX device previously registered for use with
\ :c:func:`wimax_add_rm`\ .

IMPORTANT! Must call before calling \ :c:func:`unregister_netdev`\ .

After this function returns, you will not get any more user space
control requests (via netlink or debugfs) and thus to wimax_dev->ops.

Reentrancy control is ensured by setting the state to
\ ``__WIMAX_ST_QUIESCING``\ . rfkill operations coming through
wimax_*rfkill*() will be stopped by the quiescing state; ops coming
from the rfkill subsystem will be stopped by the support being
removed by \ :c:func:`wimax_rfkill_rm`\ .

.. This file was automatic generated / don't edit.

