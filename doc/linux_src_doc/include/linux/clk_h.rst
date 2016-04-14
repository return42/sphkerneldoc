.. -*- coding: utf-8; mode: rst -*-

=====
clk.h
=====

.. _`clk-notifier-callback-types`:

clk notifier callback types
===========================

PRE_RATE_CHANGE - called immediately before the clk rate is changed,
to indicate that the rate change will proceed.  Drivers must
immediately terminate any operations that will be affected by the
rate change.  Callbacks may either return NOTIFY_DONE, NOTIFY_OK,
NOTIFY_STOP or NOTIFY_BAD.

ABORT_RATE_CHANGE: called if the rate change failed for some reason
after PRE_RATE_CHANGE.  In this case, all registered notifiers on
the clk will be called with ABORT_RATE_CHANGE. Callbacks must
always return NOTIFY_DONE or NOTIFY_OK.

POST_RATE_CHANGE - called after the clk rate change has successfully
completed.  Callbacks must always return NOTIFY_DONE or NOTIFY_OK.


.. _`clk_notifier`:

struct clk_notifier
===================

.. c:type:: struct clk_notifier

    associate a clk with a notifier



Definition
----------

.. code-block:: c

  struct clk_notifier {
    struct clk * clk;
    struct srcu_notifier_head notifier_head;
    struct list_head node;
  };



Members
-------

:``clk``:
    struct clk * to associate the notifier with

:``notifier_head``:
    a blocking_notifier_head for this clk

:``node``:
    linked list pointers



Description
-----------

A list of struct clk_notifier is maintained by the notifier code.
An entry is created whenever code registers the first notifier on a
particular ``clk``\ .  Future notifiers on that ``clk`` are added to the
``notifier_head``\ .


.. _`clk_notifier_data`:

struct clk_notifier_data
========================

.. c:type:: struct clk_notifier_data

    rate data to pass to the notifier callback



Definition
----------

.. code-block:: c

  struct clk_notifier_data {
    struct clk * clk;
    unsigned long old_rate;
    unsigned long new_rate;
  };



Members
-------

:``clk``:
    struct clk * being changed

:``old_rate``:
    previous rate of this clk

:``new_rate``:
    new rate of this clk



Description
-----------

For a pre-notifier, old_rate is the clk's rate before this rate
change, and new_rate is what the rate will be in the future.  For a
post-notifier, old_rate and new_rate are both set to the clk's
current rate (this was done to optimize the implementation).


.. _`clk_notifier_register`:

clk_notifier_register
=====================

.. c:function:: int clk_notifier_register (struct clk *clk, struct notifier_block *nb)

    change notifier callback

    :param struct clk \*clk:
        clock whose rate we are interested in

    :param struct notifier_block \*nb:
        notifier block with callback function pointer


.. _`clk_notifier_register.description`:

Description
-----------

ProTip: debugging across notifier chains can be frustrating. Make sure that
your notifier callback function prints a nice big warning in case of
failure.


.. _`clk_notifier_unregister`:

clk_notifier_unregister
=======================

.. c:function:: int clk_notifier_unregister (struct clk *clk, struct notifier_block *nb)

    change notifier callback

    :param struct clk \*clk:
        clock whose rate we are no longer interested in

    :param struct notifier_block \*nb:
        notifier block which will be unregistered


.. _`clk_get_accuracy`:

clk_get_accuracy
================

.. c:function:: long clk_get_accuracy (struct clk *clk)

    obtain the clock accuracy in ppb (parts per billion) for a clock source.

    :param struct clk \*clk:
        clock source


.. _`clk_get_accuracy.description`:

Description
-----------

This gets the clock source accuracy expressed in ppb.
A perfect clock returns 0.


.. _`clk_set_phase`:

clk_set_phase
=============

.. c:function:: int clk_set_phase (struct clk *clk, int degrees)

    adjust the phase shift of a clock signal

    :param struct clk \*clk:
        clock signal source

    :param int degrees:
        number of degrees the signal is shifted


.. _`clk_set_phase.description`:

Description
-----------

Shifts the phase of a clock signal by the specified degrees. Returns 0 on
success, -EERROR otherwise.


.. _`clk_get_phase`:

clk_get_phase
=============

.. c:function:: int clk_get_phase (struct clk *clk)

    return the phase shift of a clock signal

    :param struct clk \*clk:
        clock signal source


.. _`clk_get_phase.description`:

Description
-----------

Returns the phase shift of a clock node in degrees, otherwise returns
-EERROR.


.. _`clk_is_match`:

clk_is_match
============

.. c:function:: bool clk_is_match (const struct clk *p, const struct clk *q)

    check if two clk's point to the same hardware clock

    :param const struct clk \*p:
        clk compared against q

    :param const struct clk \*q:
        clk compared against p


.. _`clk_is_match.description`:

Description
-----------

Returns true if the two struct clk pointers both point to the same hardware
clock node. Put differently, returns true if struct clk \*p and struct clk \*q
share the same struct clk_core object.

Returns false otherwise. Note that two NULL clks are treated as matching.


.. _`clk_prepare`:

clk_prepare
===========

.. c:function:: int clk_prepare (struct clk *clk)

    prepare a clock source

    :param struct clk \*clk:
        clock source


.. _`clk_prepare.description`:

Description
-----------

This prepares the clock source for use.

Must not be called from within atomic context.


.. _`clk_unprepare`:

clk_unprepare
=============

.. c:function:: void clk_unprepare (struct clk *clk)

    undo preparation of a clock source

    :param struct clk \*clk:
        clock source


.. _`clk_unprepare.description`:

Description
-----------

This undoes a previously prepared clock.  The caller must balance
the number of prepare and unprepare calls.

Must not be called from within atomic context.


.. _`clk_get`:

clk_get
=======

.. c:function:: struct clk *clk_get (struct device *dev, const char *id)

    lookup and obtain a reference to a clock producer.

    :param struct device \*dev:
        device for clock "consumer"

    :param const char \*id:
        clock consumer ID


.. _`clk_get.description`:

Description
-----------

Returns a struct clk corresponding to the clock producer, or
valid :c:func:`IS_ERR` condition containing errno.  The implementation
uses ``dev`` and ``id`` to determine the clock consumer, and thereby
the clock producer.  (IOW, ``id`` may be identical strings, but
clk_get may return different clock producers depending on ``dev``\ .)

Drivers must assume that the clock source is not enabled.

clk_get should not be called from within interrupt context.


.. _`devm_clk_get`:

devm_clk_get
============

.. c:function:: struct clk *devm_clk_get (struct device *dev, const char *id)

    lookup and obtain a managed reference to a clock producer.

    :param struct device \*dev:
        device for clock "consumer"

    :param const char \*id:
        clock consumer ID


.. _`devm_clk_get.description`:

Description
-----------

Returns a struct clk corresponding to the clock producer, or
valid :c:func:`IS_ERR` condition containing errno.  The implementation
uses ``dev`` and ``id`` to determine the clock consumer, and thereby
the clock producer.  (IOW, ``id`` may be identical strings, but
clk_get may return different clock producers depending on ``dev``\ .)

Drivers must assume that the clock source is not enabled.

devm_clk_get should not be called from within interrupt context.

The clock will automatically be freed when the device is unbound
from the bus.


.. _`clk_enable`:

clk_enable
==========

.. c:function:: int clk_enable (struct clk *clk)

    inform the system when the clock source should be running.

    :param struct clk \*clk:
        clock source


.. _`clk_enable.description`:

Description
-----------

If the clock can not be enabled/disabled, this should return success.

May be called from atomic contexts.

Returns success (0) or negative errno.


.. _`clk_disable`:

clk_disable
===========

.. c:function:: void clk_disable (struct clk *clk)

    inform the system when the clock source is no longer required.

    :param struct clk \*clk:
        clock source


.. _`clk_disable.description`:

Description
-----------

Inform the system that a clock source is no longer required by
a driver and may be shut down.

May be called from atomic contexts.

Implementation detail: if the clock source is shared between
multiple drivers, :c:func:`clk_enable` calls must be balanced by the
same number of :c:func:`clk_disable` calls for the clock source to be
disabled.


.. _`clk_get_rate`:

clk_get_rate
============

.. c:function:: unsigned long clk_get_rate (struct clk *clk)

    obtain the current clock rate (in Hz) for a clock source. This is only valid once the clock source has been enabled.

    :param struct clk \*clk:
        clock source


.. _`clk_put`:

clk_put
=======

.. c:function:: void clk_put (struct clk *clk)

    "free" the clock source

    :param struct clk \*clk:
        clock source


.. _`clk_put.description`:

Description
-----------

Note: drivers must ensure that all clk_enable calls made on this
clock source are balanced by clk_disable calls prior to calling
this function.

clk_put should not be called from within interrupt context.


.. _`devm_clk_put`:

devm_clk_put
============

.. c:function:: void devm_clk_put (struct device *dev, struct clk *clk)

    "free" a managed clock source

    :param struct device \*dev:
        device used to acquire the clock

    :param struct clk \*clk:
        clock source acquired with :c:func:`devm_clk_get`


.. _`devm_clk_put.description`:

Description
-----------

Note: drivers must ensure that all clk_enable calls made on this
clock source are balanced by clk_disable calls prior to calling
this function.

clk_put should not be called from within interrupt context.


.. _`clk_round_rate`:

clk_round_rate
==============

.. c:function:: long clk_round_rate (struct clk *clk, unsigned long rate)

    adjust a rate to the exact rate a clock can provide

    :param struct clk \*clk:
        clock source

    :param unsigned long rate:
        desired clock rate in Hz


.. _`clk_round_rate.description`:

Description
-----------

This answers the question "if I were to pass ``rate`` to :c:func:`clk_set_rate`,
what clock rate would I end up with?" without changing the hardware
in any way.  In other words::

  rate = clk_round_rate(clk, r);

and::

  clk_set_rate(clk, r);
  rate = clk_get_rate(clk);

are equivalent except the former does not modify the clock hardware
in any way.

Returns rounded clock rate in Hz, or negative errno.


.. _`clk_set_rate`:

clk_set_rate
============

.. c:function:: int clk_set_rate (struct clk *clk, unsigned long rate)

    set the clock rate for a clock source

    :param struct clk \*clk:
        clock source

    :param unsigned long rate:
        desired clock rate in Hz


.. _`clk_set_rate.description`:

Description
-----------

Returns success (0) or negative errno.


.. _`clk_has_parent`:

clk_has_parent
==============

.. c:function:: bool clk_has_parent (struct clk *clk, struct clk *parent)

    check if a clock is a possible parent for another

    :param struct clk \*clk:
        clock source

    :param struct clk \*parent:
        parent clock source


.. _`clk_has_parent.description`:

Description
-----------

This function can be used in drivers that need to check that a clock can be
the parent of another without actually changing the parent.

Returns true if ``parent`` is a possible parent for ``clk``\ , false otherwise.


.. _`clk_set_rate_range`:

clk_set_rate_range
==================

.. c:function:: int clk_set_rate_range (struct clk *clk, unsigned long min, unsigned long max)

    set a rate range for a clock source

    :param struct clk \*clk:
        clock source

    :param unsigned long min:
        desired minimum clock rate in Hz, inclusive

    :param unsigned long max:
        desired maximum clock rate in Hz, inclusive


.. _`clk_set_rate_range.description`:

Description
-----------

Returns success (0) or negative errno.


.. _`clk_set_min_rate`:

clk_set_min_rate
================

.. c:function:: int clk_set_min_rate (struct clk *clk, unsigned long rate)

    set a minimum clock rate for a clock source

    :param struct clk \*clk:
        clock source

    :param unsigned long rate:
        desired minimum clock rate in Hz, inclusive


.. _`clk_set_min_rate.description`:

Description
-----------

Returns success (0) or negative errno.


.. _`clk_set_max_rate`:

clk_set_max_rate
================

.. c:function:: int clk_set_max_rate (struct clk *clk, unsigned long rate)

    set a maximum clock rate for a clock source

    :param struct clk \*clk:
        clock source

    :param unsigned long rate:
        desired maximum clock rate in Hz, inclusive


.. _`clk_set_max_rate.description`:

Description
-----------

Returns success (0) or negative errno.


.. _`clk_set_parent`:

clk_set_parent
==============

.. c:function:: int clk_set_parent (struct clk *clk, struct clk *parent)

    set the parent clock source for this clock

    :param struct clk \*clk:
        clock source

    :param struct clk \*parent:
        parent clock source


.. _`clk_set_parent.description`:

Description
-----------

Returns success (0) or negative errno.


.. _`clk_get_parent`:

clk_get_parent
==============

.. c:function:: struct clk *clk_get_parent (struct clk *clk)

    get the parent clock source for this clock

    :param struct clk \*clk:
        clock source


.. _`clk_get_parent.description`:

Description
-----------

Returns struct clk corresponding to parent clock source, or
valid :c:func:`IS_ERR` condition containing errno.


.. _`clk_get_sys`:

clk_get_sys
===========

.. c:function:: struct clk *clk_get_sys (const char *dev_id, const char *con_id)

    get a clock based upon the device name

    :param const char \*dev_id:
        device name

    :param const char \*con_id:
        connection ID


.. _`clk_get_sys.description`:

Description
-----------

Returns a struct clk corresponding to the clock producer, or
valid :c:func:`IS_ERR` condition containing errno.  The implementation
uses ``dev_id`` and ``con_id`` to determine the clock consumer, and
thereby the clock producer. In contrast to :c:func:`clk_get` this function
takes the device name instead of the device itself for identification.

Drivers must assume that the clock source is not enabled.

clk_get_sys should not be called from within interrupt context.

