.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/net/fsm.h

.. _`fsm_debug`:

FSM_DEBUG
=========

.. c:function::  FSM_DEBUG()

.. _`fsm_timer_debug`:

FSM_TIMER_DEBUG
===============

.. c:function::  FSM_TIMER_DEBUG()

    timer handling.

.. _`fsm_debug_history`:

FSM_DEBUG_HISTORY
=================

.. c:function::  FSM_DEBUG_HISTORY()

    Events/Statechanges and print it if a action_function is not found.

.. _`void`:

void
====

.. c:function:: typedef void(*fsm_function_t)

    :param \*fsm_function_t:
        *undescribed*

.. _`init_fsm`:

init_fsm
========

.. c:function:: fsm_instance *init_fsm(char *name, const char **state_names, const char **event_names, int nr_states, int nr_events, const fsm_node *tmpl, int tmpl_len, gfp_t order)

    :param char \*name:
        *undescribed*

    :param const char \*\*state_names:
        *undescribed*

    :param const char \*\*event_names:
        *undescribed*

    :param int nr_states:
        *undescribed*

    :param int nr_events:
        *undescribed*

    :param const fsm_node \*tmpl:
        *undescribed*

    :param int tmpl_len:
        *undescribed*

    :param gfp_t order:
        *undescribed*

.. _`init_fsm.description`:

Description
-----------

\ ``param``\  name        Name of this instance for logging purposes.
\ ``param``\  state_names An array of names for all states for logging purposes.
\ ``param``\  event_names An array of names for all events for logging purposes.
\ ``param``\  nr_states   Number of states for this instance.
\ ``param``\  nr_events   Number of events for this instance.
\ ``param``\  tmpl        An array of fsm_nodes, describing this FSM.
\ ``param``\  tmpl_len    Length of the describing array.
\ ``param``\  order       Parameter for allocation of the FSM data structs.

.. _`kfree_fsm`:

kfree_fsm
=========

.. c:function:: void kfree_fsm(fsm_instance *fi)

    :param fsm_instance \*fi:
        *undescribed*

.. _`kfree_fsm.description`:

Description
-----------

\ ``param``\  fi Pointer to an FSM, previously created with init_fsm.

.. _`fsm_event`:

fsm_event
=========

.. c:function:: int fsm_event(fsm_instance *fi, int event, void *arg)

    If an action function is defined for the current state/event combination, this function is called.

    :param fsm_instance \*fi:
        *undescribed*

    :param int event:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`fsm_event.description`:

Description
-----------

\ ``param``\  fi    Pointer to FSM which should receive the event.
\ ``param``\  event The event do be delivered.
\ ``param``\  arg   A generic argument, handed to the action function.

\ ``return``\       0  on success,
1  if current state or event is out of range
!0 if state and event in range, but no action defined.

.. _`fsm_newstate`:

fsm_newstate
============

.. c:function:: void fsm_newstate(fsm_instance *fi, int newstate)

    This does <em>not</em> trigger an event or calls an action function.

    :param fsm_instance \*fi:
        *undescribed*

    :param int newstate:
        *undescribed*

.. _`fsm_newstate.description`:

Description
-----------

\ ``param``\  fi    Pointer to FSM
\ ``param``\  state The new state for this FSM.

.. _`fsm_getstate`:

fsm_getstate
============

.. c:function:: int fsm_getstate(fsm_instance *fi)

    :param fsm_instance \*fi:
        *undescribed*

.. _`fsm_getstate.description`:

Description
-----------

\ ``param``\  fi Pointer to FSM

\ ``return``\  The current state of the FSM.

.. _`fsm_getstate_str`:

fsm_getstate_str
================

.. c:function:: const char *fsm_getstate_str(fsm_instance *fi)

    :param fsm_instance \*fi:
        *undescribed*

.. _`fsm_getstate_str.description`:

Description
-----------

\ ``param``\  fi Pointer to FSM

\ ``return``\  The current state of the FSM in a human readable form.

.. _`fsm_settimer`:

fsm_settimer
============

.. c:function:: void fsm_settimer(fsm_instance *fi, fsm_timer *)

    This prepares an fsm_timer for usage with fsm_addtimer.

    :param fsm_instance \*fi:
        *undescribed*

    :param fsm_timer \*:
        *undescribed*

.. _`fsm_settimer.description`:

Description
-----------

\ ``param``\  fi    Pointer to FSM
\ ``param``\  timer The timer to be initialized.

.. _`fsm_deltimer`:

fsm_deltimer
============

.. c:function:: void fsm_deltimer(fsm_timer *timer)

    :param fsm_timer \*timer:
        *undescribed*

.. _`fsm_deltimer.description`:

Description
-----------

\ ``param``\  timer The timer to clear.

.. _`fsm_addtimer`:

fsm_addtimer
============

.. c:function:: int fsm_addtimer(fsm_timer *timer, int millisec, int event, void *arg)

    :param fsm_timer \*timer:
        *undescribed*

    :param int millisec:
        *undescribed*

    :param int event:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`fsm_addtimer.description`:

Description
-----------

\ ``param``\  timer    The timer to be added. The field fi of that timer
must have been set to point to the instance.
\ ``param``\  millisec Duration, after which the timer should expire.
\ ``param``\  event    Event, to trigger if timer expires.
\ ``param``\  arg      Generic argument, provided to expiry function.

\ ``return``\          0 on success, -1 if timer is already active.

.. _`fsm_modtimer`:

fsm_modtimer
============

.. c:function:: void fsm_modtimer(fsm_timer *timer, int millisec, int event, void *arg)

    :param fsm_timer \*timer:
        *undescribed*

    :param int millisec:
        *undescribed*

    :param int event:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`fsm_modtimer.description`:

Description
-----------

\ ``param``\  timer    The timer to modify.
\ ``param``\  millisec Duration, after which the timer should expire.
\ ``param``\  event    Event, to trigger if timer expires.
\ ``param``\  arg      Generic argument, provided to expiry function.

.. This file was automatic generated / don't edit.

