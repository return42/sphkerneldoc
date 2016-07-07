.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rfkill/core.c

.. _`rfkill_set_block`:

rfkill_set_block
================

.. c:function:: void rfkill_set_block(struct rfkill *rfkill, bool blocked)

    wrapper for set_block method

    :param struct rfkill \*rfkill:
        the rfkill struct to use

    :param bool blocked:
        the new software state

.. _`rfkill_set_block.description`:

Description
-----------

Calls the set_block method (when applicable) and handles notifications
etc. as well.

.. _`__rfkill_switch_all`:

__rfkill_switch_all
===================

.. c:function:: void __rfkill_switch_all(const enum rfkill_type type, bool blocked)

    Toggle state of all switches of given type

    :param const enum rfkill_type type:
        type of interfaces to be affected

    :param bool blocked:
        the new state

.. _`__rfkill_switch_all.description`:

Description
-----------

This function sets the state of all switches of given type,
unless a specific switch is suspended.

Caller must have acquired rfkill_global_mutex.

.. _`rfkill_switch_all`:

rfkill_switch_all
=================

.. c:function:: void rfkill_switch_all(enum rfkill_type type, bool blocked)

    Toggle state of all switches of given type

    :param enum rfkill_type type:
        type of interfaces to be affected

    :param bool blocked:
        the new state

.. _`rfkill_switch_all.description`:

Description
-----------

Acquires rfkill_global_mutex and calls \__rfkill_switch_all(\ ``type``\ , \ ``state``\ ).
Please refer to \\ :c:func:`__rfkill_switch_all`\  for details.

Does nothing if the EPO lock is active.

.. _`rfkill_epo`:

rfkill_epo
==========

.. c:function:: void rfkill_epo( void)

    emergency power off all transmitters

    :param  void:
        no arguments

.. _`rfkill_epo.description`:

Description
-----------

This kicks all non-suspended rfkill devices to RFKILL_STATE_SOFT_BLOCKED,
ignoring everything in its path but rfkill_global_mutex and rfkill->mutex.

The global state before the EPO is saved and can be restored later
using \ :c:func:`rfkill_restore_states`\ .

.. _`rfkill_restore_states`:

rfkill_restore_states
=====================

.. c:function:: void rfkill_restore_states( void)

    restore global states

    :param  void:
        no arguments

.. _`rfkill_restore_states.description`:

Description
-----------

Restore (and sync switches to) the global state from the
states in rfkill_default_states.  This can undo the effects of
a call to \ :c:func:`rfkill_epo`\ .

.. _`rfkill_remove_epo_lock`:

rfkill_remove_epo_lock
======================

.. c:function:: void rfkill_remove_epo_lock( void)

    unlock state changes

    :param  void:
        no arguments

.. _`rfkill_remove_epo_lock.description`:

Description
-----------

Used by rfkill-input manually unlock state changes, when
the EPO switch is deactivated.

.. _`rfkill_is_epo_lock_active`:

rfkill_is_epo_lock_active
=========================

.. c:function:: bool rfkill_is_epo_lock_active( void)

    returns true EPO is active

    :param  void:
        no arguments

.. _`rfkill_is_epo_lock_active.description`:

Description
-----------

Returns 0 (false) if there is NOT an active EPO contidion,
and 1 (true) if there is an active EPO contition, which
locks all radios in one of the BLOCKED states.

Can be called in atomic context.

.. _`rfkill_get_global_sw_state`:

rfkill_get_global_sw_state
==========================

.. c:function:: bool rfkill_get_global_sw_state(const enum rfkill_type type)

    returns global state for a type

    :param const enum rfkill_type type:
        the type to get the global state of

.. _`rfkill_get_global_sw_state.description`:

Description
-----------

Returns the current global state for a given wireless
device type.

.. This file was automatic generated / don't edit.

