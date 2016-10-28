.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rfkill.h

.. _`rfkill_ops`:

struct rfkill_ops
=================

.. c:type:: struct rfkill_ops

    rfkill driver methods

.. _`rfkill_ops.definition`:

Definition
----------

.. code-block:: c

    struct rfkill_ops {
        void (*poll)(struct rfkill *rfkill, void *data);
        void (*query)(struct rfkill *rfkill, void *data);
        int (*set_block)(void *data, bool blocked);
    }

.. _`rfkill_ops.members`:

Members
-------

poll
    poll the rfkill block state(s) -- only assign this method
    when you need polling. When called, simply call one of the
    rfkill_set{,_hw,_sw}_state family of functions. If the hw
    is getting unblocked you need to take into account the return
    value of those functions to make sure the software block is
    properly used.

query
    query the rfkill block state(s) and call exactly one of the
    rfkill_set{,_hw,_sw}_state family of functions. Assign this
    method if input events can cause hardware state changes to make
    the rfkill core query your driver before setting a requested
    block.

set_block
    turn the transmitter on (blocked == false) or off
    (blocked == true) -- ignore and return 0 when hard blocked.
    This callback must be assigned.

.. _`rfkill_alloc`:

rfkill_alloc
============

.. c:function:: struct rfkill *rfkill_alloc(const char *name, struct device *parent, const enum rfkill_type type, const struct rfkill_ops *ops, void *ops_data)

    allocate rfkill structure

    :param const char \*name:
        name of the struct -- the string is not copied internally

    :param struct device \*parent:
        device that has rf switch on it

    :param const enum rfkill_type type:
        type of the switch (RFKILL_TYPE\_\*)

    :param const struct rfkill_ops \*ops:
        rfkill methods

    :param void \*ops_data:
        data passed to each method

.. _`rfkill_alloc.description`:

Description
-----------

This function should be called by the transmitter driver to allocate an
rfkill structure. Returns \ ``NULL``\  on failure.

.. _`rfkill_register`:

rfkill_register
===============

.. c:function:: int rfkill_register(struct rfkill *rfkill)

    Register a rfkill structure.

    :param struct rfkill \*rfkill:
        rfkill structure to be registered

.. _`rfkill_register.description`:

Description
-----------

This function should be called by the transmitter driver to register
the rfkill structure. Before calling this function the driver needs
to be ready to service method calls from rfkill.

If \ :c:func:`rfkill_init_sw_state`\  is not called before registration,
\ :c:func:`set_block`\  will be called to initialize the software blocked state
to a default value.

If the hardware blocked state is not set before registration,
it is assumed to be unblocked.

.. _`rfkill_pause_polling`:

rfkill_pause_polling
====================

.. c:function:: void rfkill_pause_polling(struct rfkill *rfkill)

    :param struct rfkill \*rfkill:
        *undescribed*

.. _`rfkill_pause_polling.description`:

Description
-----------

Pause polling -- say transmitter is off for other reasons.

.. _`rfkill_pause_polling.note`:

NOTE
----

not necessary for suspend/resume -- in that case the
core stops polling anyway (but will also correctly handle
the case of polling having been paused before suspend.)

.. _`rfkill_resume_polling`:

rfkill_resume_polling
=====================

.. c:function:: void rfkill_resume_polling(struct rfkill *rfkill)

    :param struct rfkill \*rfkill:
        *undescribed*

.. _`rfkill_resume_polling.description`:

Description
-----------

Pause polling -- say transmitter is off for other reasons.

.. _`rfkill_resume_polling.note`:

NOTE
----

not necessary for suspend/resume -- in that case the
core stops polling anyway

.. _`rfkill_unregister`:

rfkill_unregister
=================

.. c:function:: void rfkill_unregister(struct rfkill *rfkill)

    Unregister a rfkill structure.

    :param struct rfkill \*rfkill:
        rfkill structure to be unregistered

.. _`rfkill_unregister.description`:

Description
-----------

This function should be called by the network driver during device
teardown to destroy rfkill structure. Until it returns, the driver
needs to be able to service method calls.

.. _`rfkill_destroy`:

rfkill_destroy
==============

.. c:function:: void rfkill_destroy(struct rfkill *rfkill)

    free rfkill structure

    :param struct rfkill \*rfkill:
        rfkill structure to be destroyed

.. _`rfkill_destroy.description`:

Description
-----------

Destroys the rfkill structure.

.. _`rfkill_set_hw_state`:

rfkill_set_hw_state
===================

.. c:function:: bool rfkill_set_hw_state(struct rfkill *rfkill, bool blocked)

    Set the internal rfkill hardware block state

    :param struct rfkill \*rfkill:
        pointer to the rfkill class to modify.

    :param bool blocked:
        *undescribed*

.. _`rfkill_set_hw_state.description`:

Description
-----------

rfkill drivers that get events when the hard-blocked state changes
use this function to notify the rfkill core (and through that also
userspace) of the current state.  They should also use this after
resume if the state could have changed.

You need not (but may) call this function if poll_state is assigned.

This function can be called in any context, even from within rfkill
callbacks.

The function returns the combined block state (true if transmitter
should be blocked) so that drivers need not keep track of the soft
block state -- which they might not be able to.

.. _`rfkill_set_sw_state`:

rfkill_set_sw_state
===================

.. c:function:: bool rfkill_set_sw_state(struct rfkill *rfkill, bool blocked)

    Set the internal rfkill software block state

    :param struct rfkill \*rfkill:
        pointer to the rfkill class to modify.

    :param bool blocked:
        *undescribed*

.. _`rfkill_set_sw_state.description`:

Description
-----------

rfkill drivers that get events when the soft-blocked state changes
(yes, some platforms directly act on input but allow changing again)
use this function to notify the rfkill core (and through that also
userspace) of the current state.

Drivers should also call this function after resume if the state has
been changed by the user.  This only makes sense for "persistent"
devices (see \ :c:func:`rfkill_init_sw_state`\ ).

This function can be called in any context, even from within rfkill
callbacks.

The function returns the combined block state (true if transmitter
should be blocked).

.. _`rfkill_init_sw_state`:

rfkill_init_sw_state
====================

.. c:function:: void rfkill_init_sw_state(struct rfkill *rfkill, bool blocked)

    Initialize persistent software block state

    :param struct rfkill \*rfkill:
        pointer to the rfkill class to modify.

    :param bool blocked:
        *undescribed*

.. _`rfkill_init_sw_state.description`:

Description
-----------

rfkill drivers that preserve their software block state over power off
use this function to notify the rfkill core (and through that also
userspace) of their initial state.  It should only be used before
registration.

In addition, it marks the device as "persistent", an attribute which
can be read by userspace.  Persistent devices are expected to preserve
their own state when suspended.

.. _`rfkill_set_states`:

rfkill_set_states
=================

.. c:function:: void rfkill_set_states(struct rfkill *rfkill, bool sw, bool hw)

    Set the internal rfkill block states

    :param struct rfkill \*rfkill:
        pointer to the rfkill class to modify.

    :param bool sw:
        the current software block state to set

    :param bool hw:
        the current hardware block state to set

.. _`rfkill_set_states.description`:

Description
-----------

This function can be called in any context, even from within rfkill
callbacks.

.. _`rfkill_blocked`:

rfkill_blocked
==============

.. c:function:: bool rfkill_blocked(struct rfkill *rfkill)

    query rfkill block

    :param struct rfkill \*rfkill:
        rfkill struct to query

.. _`rfkill_find_type`:

rfkill_find_type
================

.. c:function:: enum rfkill_type rfkill_find_type(const char *name)

    Helpper for finding rfkill type by name

    :param const char \*name:
        the name of the type

.. _`rfkill_find_type.description`:

Description
-----------

Returns enum rfkill_type that conrresponds the name.

.. _`rfkill_get_led_trigger_name`:

rfkill_get_led_trigger_name
===========================

.. c:function:: const char *rfkill_get_led_trigger_name(struct rfkill *rfkill)

    Get the LED trigger name for the button's LED. This function might return a NULL pointer if registering of the LED trigger failed. Use this as "default_trigger" for the LED.

    :param struct rfkill \*rfkill:
        *undescribed*

.. _`rfkill_set_led_trigger_name`:

rfkill_set_led_trigger_name
===========================

.. c:function:: void rfkill_set_led_trigger_name(struct rfkill *rfkill, const char *name)

    - set the LED trigger name

    :param struct rfkill \*rfkill:
        rfkill struct

    :param const char \*name:
        LED trigger name

.. _`rfkill_set_led_trigger_name.description`:

Description
-----------

This function sets the LED trigger name of the radio LED
trigger that rfkill creates. It is optional, but if called
must be called before \ :c:func:`rfkill_register`\  to be effective.

.. This file was automatic generated / don't edit.

