.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/block/drbd/drbd_state.c

.. _`cl_wide_st_chg`:

cl_wide_st_chg
==============

.. c:function:: int cl_wide_st_chg(struct drbd_device *device, union drbd_state os, union drbd_state ns)

    true if the state change is a cluster wide one

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param os:
        old (current) state.
    :type os: union drbd_state

    :param ns:
        new (wanted) state.
    :type ns: union drbd_state

.. _`drbd_force_state`:

drbd_force_state
================

.. c:function:: void drbd_force_state(struct drbd_device *device, union drbd_state mask, union drbd_state val)

    Impose a change which happens outside our control on our state

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param mask:
        mask of state bits to change.
    :type mask: union drbd_state

    :param val:
        value of new state bits.
    :type val: union drbd_state

.. _`drbd_req_state`:

drbd_req_state
==============

.. c:function:: enum drbd_state_rv drbd_req_state(struct drbd_device *device, union drbd_state mask, union drbd_state val, enum chg_state_flags f)

    Perform an eventually cluster wide state change

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param mask:
        mask of state bits to change.
    :type mask: union drbd_state

    :param val:
        value of new state bits.
    :type val: union drbd_state

    :param f:
        flags
    :type f: enum chg_state_flags

.. _`drbd_req_state.description`:

Description
-----------

Should not be called directly, use \ :c:func:`drbd_request_state`\  or
\_drbd_request_state().

.. _`_drbd_request_state`:

\_drbd_request_state
====================

.. c:function:: enum drbd_state_rv _drbd_request_state(struct drbd_device *device, union drbd_state mask, union drbd_state val, enum chg_state_flags f)

    Request a state change (with flags)

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param mask:
        mask of state bits to change.
    :type mask: union drbd_state

    :param val:
        value of new state bits.
    :type val: union drbd_state

    :param f:
        flags
    :type f: enum chg_state_flags

.. _`_drbd_request_state.description`:

Description
-----------

Cousin of \ :c:func:`drbd_request_state`\ , useful with the CS_WAIT_COMPLETE
flag, or when logging of failed state change requests is not desired.

.. _`is_valid_state`:

is_valid_state
==============

.. c:function:: enum drbd_state_rv is_valid_state(struct drbd_device *device, union drbd_state ns)

    Returns an SS\_ error code if ns is not valid

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param ns:
        State to consider.
    :type ns: union drbd_state

.. _`is_valid_soft_transition`:

is_valid_soft_transition
========================

.. c:function:: enum drbd_state_rv is_valid_soft_transition(union drbd_state os, union drbd_state ns, struct drbd_connection *connection)

    Returns an SS\_ error code if the state transition is not possible This function limits state transitions that may be declined by DRBD. I.e. user requests (aka soft transitions).

    :param os:
        old state.
    :type os: union drbd_state

    :param ns:
        new state.
    :type ns: union drbd_state

    :param connection:
        *undescribed*
    :type connection: struct drbd_connection \*

.. _`is_valid_transition`:

is_valid_transition
===================

.. c:function:: enum drbd_state_rv is_valid_transition(union drbd_state os, union drbd_state ns)

    Returns an SS\_ error code if the state transition is not possible This limits hard state transitions. Hard state transitions are facts there are imposed on DRBD by the environment. E.g. disk broke or network broke down. But those hard state transitions are still not allowed to do everything.

    :param os:
        old state.
    :type os: union drbd_state

    :param ns:
        new state.
    :type ns: union drbd_state

.. _`sanitize_state`:

sanitize_state
==============

.. c:function:: union drbd_state sanitize_state(struct drbd_device *device, union drbd_state os, union drbd_state ns, enum sanitize_state_warnings *warn)

    Resolves implicitly necessary additional changes to a state transition

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param os:
        old state.
    :type os: union drbd_state

    :param ns:
        new state.
    :type ns: union drbd_state

    :param warn:
        *undescribed*
    :type warn: enum sanitize_state_warnings \*

.. _`sanitize_state.description`:

Description
-----------

When we loose connection, we have to set the state of the peers disk (pdsk)
to D_UNKNOWN. This rule and many more along those lines are in this function.

.. _`_drbd_set_state`:

\_drbd_set_state
================

.. c:function:: enum drbd_state_rv _drbd_set_state(struct drbd_device *device, union drbd_state ns, enum chg_state_flags flags, struct completion *done)

    Set a new DRBD state

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param ns:
        new state.
    :type ns: union drbd_state

    :param flags:
        Flags
    :type flags: enum chg_state_flags

    :param done:
        Optional completion, that will get completed after the \ :c:func:`after_state_ch`\  finished
    :type done: struct completion \*

.. _`_drbd_set_state.description`:

Description
-----------

Caller needs to hold req_lock. Do not call directly.

.. _`after_state_ch`:

after_state_ch
==============

.. c:function:: void after_state_ch(struct drbd_device *device, union drbd_state os, union drbd_state ns, enum chg_state_flags flags, struct drbd_state_change *state_change)

    Perform after state change actions that may sleep

    :param device:
        DRBD device.
    :type device: struct drbd_device \*

    :param os:
        old state.
    :type os: union drbd_state

    :param ns:
        new state.
    :type ns: union drbd_state

    :param flags:
        Flags
    :type flags: enum chg_state_flags

    :param state_change:
        *undescribed*
    :type state_change: struct drbd_state_change \*

.. This file was automatic generated / don't edit.

