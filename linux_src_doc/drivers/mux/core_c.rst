.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mux/core.c

.. _`mux_chip_alloc`:

mux_chip_alloc
==============

.. c:function:: struct mux_chip *mux_chip_alloc(struct device *dev, unsigned int controllers, size_t sizeof_priv)

    Allocate a mux-chip.

    :param struct device \*dev:
        The parent device implementing the mux interface.

    :param unsigned int controllers:
        The number of mux controllers to allocate for this chip.

    :param size_t sizeof_priv:
        Size of extra memory area for private use by the caller.

.. _`mux_chip_alloc.description`:

Description
-----------

After allocating the mux-chip with the desired number of mux controllers
but before registering the chip, the mux driver is required to configure
the number of valid mux states in the mux_chip->mux[N].states members and
the desired idle state in the returned mux_chip->mux[N].idle_state members.
The default idle state is MUX_IDLE_AS_IS. The mux driver also needs to
provide a pointer to the operations struct in the mux_chip->ops member
before registering the mux-chip with mux_chip_register.

.. _`mux_chip_alloc.return`:

Return
------

A pointer to the new mux-chip, or an ERR_PTR with a negative errno.

.. _`mux_chip_register`:

mux_chip_register
=================

.. c:function:: int mux_chip_register(struct mux_chip *mux_chip)

    Register a mux-chip, thus readying the controllers for use.

    :param struct mux_chip \*mux_chip:
        The mux-chip to register.

.. _`mux_chip_register.description`:

Description
-----------

Do not retry registration of the same mux-chip on failure. You should
instead put it away with \ :c:func:`mux_chip_free`\  and allocate a new one, if you
for some reason would like to retry registration.

.. _`mux_chip_register.return`:

Return
------

Zero on success or a negative errno on error.

.. _`mux_chip_unregister`:

mux_chip_unregister
===================

.. c:function:: void mux_chip_unregister(struct mux_chip *mux_chip)

    Take the mux-chip off-line.

    :param struct mux_chip \*mux_chip:
        The mux-chip to unregister.

.. _`mux_chip_unregister.description`:

Description
-----------

mux_chip_unregister() reverses the effects of \ :c:func:`mux_chip_register`\ .
But not completely, you should not try to call \ :c:func:`mux_chip_register`\ 
on a mux-chip that has been registered before.

.. _`mux_chip_free`:

mux_chip_free
=============

.. c:function:: void mux_chip_free(struct mux_chip *mux_chip)

    Free the mux-chip for good.

    :param struct mux_chip \*mux_chip:
        The mux-chip to free.

.. _`mux_chip_free.description`:

Description
-----------

mux_chip_free() reverses the effects of \ :c:func:`mux_chip_alloc`\ .

.. _`devm_mux_chip_alloc`:

devm_mux_chip_alloc
===================

.. c:function:: struct mux_chip *devm_mux_chip_alloc(struct device *dev, unsigned int controllers, size_t sizeof_priv)

    Resource-managed version of \ :c:func:`mux_chip_alloc`\ .

    :param struct device \*dev:
        The parent device implementing the mux interface.

    :param unsigned int controllers:
        The number of mux controllers to allocate for this chip.

    :param size_t sizeof_priv:
        Size of extra memory area for private use by the caller.

.. _`devm_mux_chip_alloc.description`:

Description
-----------

See \ :c:func:`mux_chip_alloc`\  for more details.

.. _`devm_mux_chip_alloc.return`:

Return
------

A pointer to the new mux-chip, or an ERR_PTR with a negative errno.

.. _`devm_mux_chip_register`:

devm_mux_chip_register
======================

.. c:function:: int devm_mux_chip_register(struct device *dev, struct mux_chip *mux_chip)

    Resource-managed version \ :c:func:`mux_chip_register`\ .

    :param struct device \*dev:
        The parent device implementing the mux interface.

    :param struct mux_chip \*mux_chip:
        The mux-chip to register.

.. _`devm_mux_chip_register.description`:

Description
-----------

See \ :c:func:`mux_chip_register`\  for more details.

.. _`devm_mux_chip_register.return`:

Return
------

Zero on success or a negative errno on error.

.. _`mux_control_states`:

mux_control_states
==================

.. c:function:: unsigned int mux_control_states(struct mux_control *mux)

    Query the number of multiplexer states.

    :param struct mux_control \*mux:
        The mux-control to query.

.. _`mux_control_states.return`:

Return
------

The number of multiplexer states.

.. _`mux_control_select`:

mux_control_select
==================

.. c:function:: int mux_control_select(struct mux_control *mux, unsigned int state)

    Select the given multiplexer state.

    :param struct mux_control \*mux:
        The mux-control to request a change of state from.

    :param unsigned int state:
        The new requested state.

.. _`mux_control_select.description`:

Description
-----------

On successfully selecting the mux-control state, it will be locked until
there is a call to \ :c:func:`mux_control_deselect`\ . If the mux-control is already
selected when \ :c:func:`mux_control_select`\  is called, the caller will be blocked
until \ :c:func:`mux_control_deselect`\  is called (by someone else).

Therefore, make sure to call \ :c:func:`mux_control_deselect`\  when the operation is
complete and the mux-control is free for others to use, but do not call
\ :c:func:`mux_control_deselect`\  if \ :c:func:`mux_control_select`\  fails.

.. _`mux_control_select.return`:

Return
------

0 when the mux-control state has the requested state or a negative
errno on error.

.. _`mux_control_try_select`:

mux_control_try_select
======================

.. c:function:: int mux_control_try_select(struct mux_control *mux, unsigned int state)

    Try to select the given multiplexer state.

    :param struct mux_control \*mux:
        The mux-control to request a change of state from.

    :param unsigned int state:
        The new requested state.

.. _`mux_control_try_select.description`:

Description
-----------

On successfully selecting the mux-control state, it will be locked until
\ :c:func:`mux_control_deselect`\  called.

Therefore, make sure to call \ :c:func:`mux_control_deselect`\  when the operation is
complete and the mux-control is free for others to use, but do not call
\ :c:func:`mux_control_deselect`\  if \ :c:func:`mux_control_try_select`\  fails.

.. _`mux_control_try_select.return`:

Return
------

0 when the mux-control state has the requested state or a negative
errno on error. Specifically -EBUSY if the mux-control is contended.

.. _`mux_control_deselect`:

mux_control_deselect
====================

.. c:function:: int mux_control_deselect(struct mux_control *mux)

    Deselect the previously selected multiplexer state.

    :param struct mux_control \*mux:
        The mux-control to deselect.

.. _`mux_control_deselect.description`:

Description
-----------

It is required that a single call is made to \ :c:func:`mux_control_deselect`\  for
each and every successful call made to either of \ :c:func:`mux_control_select`\  or
\ :c:func:`mux_control_try_select`\ .

.. _`mux_control_deselect.return`:

Return
------

0 on success and a negative errno on error. An error can only
occur if the mux has an idle state. Note that even if an error occurs, the
mux-control is unlocked and is thus free for the next access.

.. _`mux_control_get`:

mux_control_get
===============

.. c:function:: struct mux_control *mux_control_get(struct device *dev, const char *mux_name)

    Get the mux-control for a device.

    :param struct device \*dev:
        The device that needs a mux-control.

    :param const char \*mux_name:
        The name identifying the mux-control.

.. _`mux_control_get.return`:

Return
------

A pointer to the mux-control, or an ERR_PTR with a negative errno.

.. _`mux_control_put`:

mux_control_put
===============

.. c:function:: void mux_control_put(struct mux_control *mux)

    Put away the mux-control for good.

    :param struct mux_control \*mux:
        The mux-control to put away.

.. _`mux_control_put.description`:

Description
-----------

mux_control_put() reverses the effects of \ :c:func:`mux_control_get`\ .

.. _`devm_mux_control_get`:

devm_mux_control_get
====================

.. c:function:: struct mux_control *devm_mux_control_get(struct device *dev, const char *mux_name)

    Get the mux-control for a device, with resource management.

    :param struct device \*dev:
        The device that needs a mux-control.

    :param const char \*mux_name:
        The name identifying the mux-control.

.. _`devm_mux_control_get.return`:

Return
------

Pointer to the mux-control, or an ERR_PTR with a negative errno.

.. This file was automatic generated / don't edit.

