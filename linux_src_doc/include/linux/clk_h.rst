.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clk.h

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

.. _`clk_notifier.definition`:

Definition
----------

.. code-block:: c

    struct clk_notifier {
        struct clk *clk;
        struct srcu_notifier_head notifier_head;
        struct list_head node;
    }

.. _`clk_notifier.members`:

Members
-------

clk
    struct clk * to associate the notifier with

notifier_head
    a blocking_notifier_head for this clk

node
    linked list pointers

.. _`clk_notifier.description`:

Description
-----------

A list of struct clk_notifier is maintained by the notifier code.
An entry is created whenever code registers the first notifier on a
particular \ ``clk``\ .  Future notifiers on that \ ``clk``\  are added to the
\ ``notifier_head``\ .

.. _`clk_notifier_data`:

struct clk_notifier_data
========================

.. c:type:: struct clk_notifier_data

    rate data to pass to the notifier callback

.. _`clk_notifier_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_notifier_data {
        struct clk *clk;
        unsigned long old_rate;
        unsigned long new_rate;
    }

.. _`clk_notifier_data.members`:

Members
-------

clk
    struct clk * being changed

old_rate
    previous rate of this clk

new_rate
    new rate of this clk

.. _`clk_notifier_data.description`:

Description
-----------

For a pre-notifier, old_rate is the clk's rate before this rate
change, and new_rate is what the rate will be in the future.  For a
post-notifier, old_rate and new_rate are both set to the clk's
current rate (this was done to optimize the implementation).

.. _`clk_bulk_data`:

struct clk_bulk_data
====================

.. c:type:: struct clk_bulk_data

    Data used for bulk clk operations.

.. _`clk_bulk_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_bulk_data {
        const char *id;
        struct clk *clk;
    }

.. _`clk_bulk_data.members`:

Members
-------

id
    clock consumer ID

clk
    struct clk * to store the associated clock

.. _`clk_bulk_data.description`:

Description
-----------

The CLK APIs provide a series of \ :c:func:`clk_bulk_`\  API calls as
a convenience to consumers which require multiple clks.  This
structure is used to manage data for these calls.

.. _`clk_notifier_register`:

clk_notifier_register
=====================

.. c:function:: int clk_notifier_register(struct clk *clk, struct notifier_block *nb)

    register a clock rate-change notifier callback

    :param clk:
        clock whose rate we are interested in
    :type clk: struct clk \*

    :param nb:
        notifier block with callback function pointer
    :type nb: struct notifier_block \*

.. _`clk_notifier_register.description`:

Description
-----------

ProTip: debugging across notifier chains can be frustrating. Make sure that
your notifier callback function prints a nice big warning in case of
failure.

.. _`clk_notifier_unregister`:

clk_notifier_unregister
=======================

.. c:function:: int clk_notifier_unregister(struct clk *clk, struct notifier_block *nb)

    unregister a clock rate-change notifier callback

    :param clk:
        clock whose rate we are no longer interested in
    :type clk: struct clk \*

    :param nb:
        notifier block which will be unregistered
    :type nb: struct notifier_block \*

.. _`clk_get_accuracy`:

clk_get_accuracy
================

.. c:function:: long clk_get_accuracy(struct clk *clk)

    obtain the clock accuracy in ppb (parts per billion) for a clock source.

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_get_accuracy.description`:

Description
-----------

This gets the clock source accuracy expressed in ppb.
A perfect clock returns 0.

.. _`clk_set_phase`:

clk_set_phase
=============

.. c:function:: int clk_set_phase(struct clk *clk, int degrees)

    adjust the phase shift of a clock signal

    :param clk:
        clock signal source
    :type clk: struct clk \*

    :param degrees:
        number of degrees the signal is shifted
    :type degrees: int

.. _`clk_set_phase.description`:

Description
-----------

Shifts the phase of a clock signal by the specified degrees. Returns 0 on
success, -EERROR otherwise.

.. _`clk_get_phase`:

clk_get_phase
=============

.. c:function:: int clk_get_phase(struct clk *clk)

    return the phase shift of a clock signal

    :param clk:
        clock signal source
    :type clk: struct clk \*

.. _`clk_get_phase.description`:

Description
-----------

Returns the phase shift of a clock node in degrees, otherwise returns
-EERROR.

.. _`clk_set_duty_cycle`:

clk_set_duty_cycle
==================

.. c:function:: int clk_set_duty_cycle(struct clk *clk, unsigned int num, unsigned int den)

    adjust the duty cycle ratio of a clock signal

    :param clk:
        clock signal source
    :type clk: struct clk \*

    :param num:
        numerator of the duty cycle ratio to be applied
    :type num: unsigned int

    :param den:
        denominator of the duty cycle ratio to be applied
    :type den: unsigned int

.. _`clk_set_duty_cycle.description`:

Description
-----------

Adjust the duty cycle of a clock signal by the specified ratio. Returns 0 on
success, -EERROR otherwise.

.. _`clk_get_scaled_duty_cycle`:

clk_get_scaled_duty_cycle
=========================

.. c:function:: int clk_get_scaled_duty_cycle(struct clk *clk, unsigned int scale)

    return the duty cycle ratio of a clock signal

    :param clk:
        clock signal source
    :type clk: struct clk \*

    :param scale:
        scaling factor to be applied to represent the ratio as an integer
    :type scale: unsigned int

.. _`clk_get_scaled_duty_cycle.description`:

Description
-----------

Returns the duty cycle ratio multiplied by the scale provided, otherwise
returns -EERROR.

.. _`clk_is_match`:

clk_is_match
============

.. c:function:: bool clk_is_match(const struct clk *p, const struct clk *q)

    check if two clk's point to the same hardware clock

    :param p:
        clk compared against q
    :type p: const struct clk \*

    :param q:
        clk compared against p
    :type q: const struct clk \*

.. _`clk_is_match.description`:

Description
-----------

Returns true if the two struct clk pointers both point to the same hardware
clock node. Put differently, returns true if \ ``p``\  and \ ``q``\ 
share the same \ :c:type:`struct clk_core <clk_core>`\  object.

Returns false otherwise. Note that two NULL clks are treated as matching.

.. _`clk_prepare`:

clk_prepare
===========

.. c:function:: int clk_prepare(struct clk *clk)

    prepare a clock source

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_prepare.description`:

Description
-----------

This prepares the clock source for use.

Must not be called from within atomic context.

.. _`clk_unprepare`:

clk_unprepare
=============

.. c:function:: void clk_unprepare(struct clk *clk)

    undo preparation of a clock source

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_unprepare.description`:

Description
-----------

This undoes a previously prepared clock.  The caller must balance
the number of prepare and unprepare calls.

Must not be called from within atomic context.

.. _`clk_get`:

clk_get
=======

.. c:function:: struct clk *clk_get(struct device *dev, const char *id)

    lookup and obtain a reference to a clock producer.

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param id:
        clock consumer ID
    :type id: const char \*

.. _`clk_get.description`:

Description
-----------

Returns a struct clk corresponding to the clock producer, or
valid \ :c:func:`IS_ERR`\  condition containing errno.  The implementation
uses \ ``dev``\  and \ ``id``\  to determine the clock consumer, and thereby
the clock producer.  (IOW, \ ``id``\  may be identical strings, but
clk_get may return different clock producers depending on \ ``dev``\ .)

Drivers must assume that the clock source is not enabled.

clk_get should not be called from within interrupt context.

.. _`clk_bulk_get`:

clk_bulk_get
============

.. c:function:: int clk_bulk_get(struct device *dev, int num_clks, struct clk_bulk_data *clks)

    lookup and obtain a number of references to clock producer.

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table of consumer
    :type clks: struct clk_bulk_data \*

.. _`clk_bulk_get.description`:

Description
-----------

This helper function allows drivers to get several clk consumers in one
operation. If any of the clk cannot be acquired then any clks
that were obtained will be freed before returning to the caller.

Returns 0 if all clocks specified in clk_bulk_data table are obtained
successfully, or valid \ :c:func:`IS_ERR`\  condition containing errno.
The implementation uses \ ``dev``\  and \ ``clk_bulk_data.id``\  to determine the
clock consumer, and thereby the clock producer.
The clock returned is stored in each \ ``clk_bulk_data.clk``\  field.

Drivers must assume that the clock source is not enabled.

clk_bulk_get should not be called from within interrupt context.

.. _`clk_bulk_get_all`:

clk_bulk_get_all
================

.. c:function:: int clk_bulk_get_all(struct device *dev, struct clk_bulk_data **clks)

    lookup and obtain all available references to clock producer.

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param clks:
        pointer to the clk_bulk_data table of consumer
    :type clks: struct clk_bulk_data \*\*

.. _`clk_bulk_get_all.description`:

Description
-----------

This helper function allows drivers to get all clk consumers in one
operation. If any of the clk cannot be acquired then any clks
that were obtained will be freed before returning to the caller.

Returns a positive value for the number of clocks obtained while the
clock references are stored in the clk_bulk_data table in \ ``clks``\  field.
Returns 0 if there're none and a negative value if something failed.

Drivers must assume that the clock source is not enabled.

clk_bulk_get should not be called from within interrupt context.

.. _`devm_clk_bulk_get`:

devm_clk_bulk_get
=================

.. c:function:: int devm_clk_bulk_get(struct device *dev, int num_clks, struct clk_bulk_data *clks)

    managed get multiple clk consumers

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table of consumer
    :type clks: struct clk_bulk_data \*

.. _`devm_clk_bulk_get.description`:

Description
-----------

Return 0 on success, an errno on failure.

This helper function allows drivers to get several clk
consumers in one operation with management, the clks will
automatically be freed when the device is unbound.

.. _`devm_clk_bulk_get_all`:

devm_clk_bulk_get_all
=====================

.. c:function:: int devm_clk_bulk_get_all(struct device *dev, struct clk_bulk_data **clks)

    managed get multiple clk consumers

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param clks:
        pointer to the clk_bulk_data table of consumer
    :type clks: struct clk_bulk_data \*\*

.. _`devm_clk_bulk_get_all.description`:

Description
-----------

Returns a positive value for the number of clocks obtained while the
clock references are stored in the clk_bulk_data table in \ ``clks``\  field.
Returns 0 if there're none and a negative value if something failed.

This helper function allows drivers to get several clk
consumers in one operation with management, the clks will
automatically be freed when the device is unbound.

.. _`devm_clk_get`:

devm_clk_get
============

.. c:function:: struct clk *devm_clk_get(struct device *dev, const char *id)

    lookup and obtain a managed reference to a clock producer.

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param id:
        clock consumer ID
    :type id: const char \*

.. _`devm_clk_get.description`:

Description
-----------

Returns a struct clk corresponding to the clock producer, or
valid \ :c:func:`IS_ERR`\  condition containing errno.  The implementation
uses \ ``dev``\  and \ ``id``\  to determine the clock consumer, and thereby
the clock producer.  (IOW, \ ``id``\  may be identical strings, but
clk_get may return different clock producers depending on \ ``dev``\ .)

Drivers must assume that the clock source is not enabled.

devm_clk_get should not be called from within interrupt context.

The clock will automatically be freed when the device is unbound
from the bus.

.. _`devm_get_clk_from_child`:

devm_get_clk_from_child
=======================

.. c:function:: struct clk *devm_get_clk_from_child(struct device *dev, struct device_node *np, const char *con_id)

    lookup and obtain a managed reference to a clock producer from child node.

    :param dev:
        device for clock "consumer"
    :type dev: struct device \*

    :param np:
        pointer to clock consumer node
    :type np: struct device_node \*

    :param con_id:
        clock consumer ID
    :type con_id: const char \*

.. _`devm_get_clk_from_child.description`:

Description
-----------

This function parses the clocks, and uses them to look up the
struct clk from the registered list of clock providers by using
\ ``np``\  and \ ``con_id``\ 

The clock will automatically be freed when the device is unbound
from the bus.

.. _`clk_rate_exclusive_get`:

clk_rate_exclusive_get
======================

.. c:function:: int clk_rate_exclusive_get(struct clk *clk)

    get exclusivity over the rate control of a producer

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_rate_exclusive_get.description`:

Description
-----------

This function allows drivers to get exclusive control over the rate of a
provider. It prevents any other consumer to execute, even indirectly,
opereation which could alter the rate of the provider or cause glitches

If exlusivity is claimed more than once on clock, even by the same driver,
the rate effectively gets locked as exclusivity can't be preempted.

Must not be called from within atomic context.

Returns success (0) or negative errno.

.. _`clk_rate_exclusive_put`:

clk_rate_exclusive_put
======================

.. c:function:: void clk_rate_exclusive_put(struct clk *clk)

    release exclusivity over the rate control of a producer

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_rate_exclusive_put.description`:

Description
-----------

This function allows drivers to release the exclusivity it previously got
from \ :c:func:`clk_rate_exclusive_get`\ 

The caller must balance the number of \ :c:func:`clk_rate_exclusive_get`\  and
\ :c:func:`clk_rate_exclusive_put`\  calls.

Must not be called from within atomic context.

.. _`clk_enable`:

clk_enable
==========

.. c:function:: int clk_enable(struct clk *clk)

    inform the system when the clock source should be running.

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_enable.description`:

Description
-----------

If the clock can not be enabled/disabled, this should return success.

May be called from atomic contexts.

Returns success (0) or negative errno.

.. _`clk_bulk_enable`:

clk_bulk_enable
===============

.. c:function:: int clk_bulk_enable(int num_clks, const struct clk_bulk_data *clks)

    inform the system when the set of clks should be running.

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table of consumer
    :type clks: const struct clk_bulk_data \*

.. _`clk_bulk_enable.description`:

Description
-----------

May be called from atomic contexts.

Returns success (0) or negative errno.

.. _`clk_disable`:

clk_disable
===========

.. c:function:: void clk_disable(struct clk *clk)

    inform the system when the clock source is no longer required.

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_disable.description`:

Description
-----------

Inform the system that a clock source is no longer required by
a driver and may be shut down.

May be called from atomic contexts.

Implementation detail: if the clock source is shared between
multiple drivers, \ :c:func:`clk_enable`\  calls must be balanced by the
same number of \ :c:func:`clk_disable`\  calls for the clock source to be
disabled.

.. _`clk_bulk_disable`:

clk_bulk_disable
================

.. c:function:: void clk_bulk_disable(int num_clks, const struct clk_bulk_data *clks)

    inform the system when the set of clks is no longer required.

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table of consumer
    :type clks: const struct clk_bulk_data \*

.. _`clk_bulk_disable.description`:

Description
-----------

Inform the system that a set of clks is no longer required by
a driver and may be shut down.

May be called from atomic contexts.

Implementation detail: if the set of clks is shared between
multiple drivers, \ :c:func:`clk_bulk_enable`\  calls must be balanced by the
same number of \ :c:func:`clk_bulk_disable`\  calls for the clock source to be
disabled.

.. _`clk_get_rate`:

clk_get_rate
============

.. c:function:: unsigned long clk_get_rate(struct clk *clk)

    obtain the current clock rate (in Hz) for a clock source. This is only valid once the clock source has been enabled.

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_put`:

clk_put
=======

.. c:function:: void clk_put(struct clk *clk)

    "free" the clock source

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_put.note`:

Note
----

drivers must ensure that all clk_enable calls made on this
clock source are balanced by clk_disable calls prior to calling
this function.

clk_put should not be called from within interrupt context.

.. _`clk_bulk_put`:

clk_bulk_put
============

.. c:function:: void clk_bulk_put(int num_clks, struct clk_bulk_data *clks)

    "free" the clock source

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table of consumer
    :type clks: struct clk_bulk_data \*

.. _`clk_bulk_put.note`:

Note
----

drivers must ensure that all clk_bulk_enable calls made on this
clock source are balanced by clk_bulk_disable calls prior to calling
this function.

clk_bulk_put should not be called from within interrupt context.

.. _`clk_bulk_put_all`:

clk_bulk_put_all
================

.. c:function:: void clk_bulk_put_all(int num_clks, struct clk_bulk_data *clks)

    "free" all the clock source

    :param num_clks:
        the number of clk_bulk_data
    :type num_clks: int

    :param clks:
        the clk_bulk_data table of consumer
    :type clks: struct clk_bulk_data \*

.. _`clk_bulk_put_all.note`:

Note
----

drivers must ensure that all clk_bulk_enable calls made on this
clock source are balanced by clk_bulk_disable calls prior to calling
this function.

clk_bulk_put_all should not be called from within interrupt context.

.. _`devm_clk_put`:

devm_clk_put
============

.. c:function:: void devm_clk_put(struct device *dev, struct clk *clk)

    "free" a managed clock source

    :param dev:
        device used to acquire the clock
    :type dev: struct device \*

    :param clk:
        clock source acquired with \ :c:func:`devm_clk_get`\ 
    :type clk: struct clk \*

.. _`devm_clk_put.note`:

Note
----

drivers must ensure that all clk_enable calls made on this
clock source are balanced by clk_disable calls prior to calling
this function.

clk_put should not be called from within interrupt context.

.. _`clk_round_rate`:

clk_round_rate
==============

.. c:function:: long clk_round_rate(struct clk *clk, unsigned long rate)

    adjust a rate to the exact rate a clock can provide

    :param clk:
        clock source
    :type clk: struct clk \*

    :param rate:
        desired clock rate in Hz
    :type rate: unsigned long

.. _`clk_round_rate.description`:

Description
-----------

This answers the question "if I were to pass \ ``rate``\  to \ :c:func:`clk_set_rate`\ ,
what clock rate would I end up with?" without changing the hardware
in any way.  In other words:

  rate = clk_round_rate(clk, r);

.. _`clk_round_rate.and`:

and
---


  clk_set_rate(clk, r);
  rate = clk_get_rate(clk);

are equivalent except the former does not modify the clock hardware
in any way.

Returns rounded clock rate in Hz, or negative errno.

.. _`clk_set_rate`:

clk_set_rate
============

.. c:function:: int clk_set_rate(struct clk *clk, unsigned long rate)

    set the clock rate for a clock source

    :param clk:
        clock source
    :type clk: struct clk \*

    :param rate:
        desired clock rate in Hz
    :type rate: unsigned long

.. _`clk_set_rate.description`:

Description
-----------

Returns success (0) or negative errno.

.. _`clk_set_rate_exclusive`:

clk_set_rate_exclusive
======================

.. c:function:: int clk_set_rate_exclusive(struct clk *clk, unsigned long rate)

    set the clock rate and claim exclusivity over clock source

    :param clk:
        clock source
    :type clk: struct clk \*

    :param rate:
        desired clock rate in Hz
    :type rate: unsigned long

.. _`clk_set_rate_exclusive.description`:

Description
-----------

This helper function allows drivers to atomically set the rate of a producer
and claim exclusivity over the rate control of the producer.

It is essentially a combination of \ :c:func:`clk_set_rate`\  and
\ :c:func:`clk_rate_exclusite_get`\ . Caller must balance this call with a call to
\ :c:func:`clk_rate_exclusive_put`\ 

Returns success (0) or negative errno.

.. _`clk_has_parent`:

clk_has_parent
==============

.. c:function:: bool clk_has_parent(struct clk *clk, struct clk *parent)

    check if a clock is a possible parent for another

    :param clk:
        clock source
    :type clk: struct clk \*

    :param parent:
        parent clock source
    :type parent: struct clk \*

.. _`clk_has_parent.description`:

Description
-----------

This function can be used in drivers that need to check that a clock can be
the parent of another without actually changing the parent.

Returns true if \ ``parent``\  is a possible parent for \ ``clk``\ , false otherwise.

.. _`clk_set_rate_range`:

clk_set_rate_range
==================

.. c:function:: int clk_set_rate_range(struct clk *clk, unsigned long min, unsigned long max)

    set a rate range for a clock source

    :param clk:
        clock source
    :type clk: struct clk \*

    :param min:
        desired minimum clock rate in Hz, inclusive
    :type min: unsigned long

    :param max:
        desired maximum clock rate in Hz, inclusive
    :type max: unsigned long

.. _`clk_set_rate_range.description`:

Description
-----------

Returns success (0) or negative errno.

.. _`clk_set_min_rate`:

clk_set_min_rate
================

.. c:function:: int clk_set_min_rate(struct clk *clk, unsigned long rate)

    set a minimum clock rate for a clock source

    :param clk:
        clock source
    :type clk: struct clk \*

    :param rate:
        desired minimum clock rate in Hz, inclusive
    :type rate: unsigned long

.. _`clk_set_min_rate.description`:

Description
-----------

Returns success (0) or negative errno.

.. _`clk_set_max_rate`:

clk_set_max_rate
================

.. c:function:: int clk_set_max_rate(struct clk *clk, unsigned long rate)

    set a maximum clock rate for a clock source

    :param clk:
        clock source
    :type clk: struct clk \*

    :param rate:
        desired maximum clock rate in Hz, inclusive
    :type rate: unsigned long

.. _`clk_set_max_rate.description`:

Description
-----------

Returns success (0) or negative errno.

.. _`clk_set_parent`:

clk_set_parent
==============

.. c:function:: int clk_set_parent(struct clk *clk, struct clk *parent)

    set the parent clock source for this clock

    :param clk:
        clock source
    :type clk: struct clk \*

    :param parent:
        parent clock source
    :type parent: struct clk \*

.. _`clk_set_parent.description`:

Description
-----------

Returns success (0) or negative errno.

.. _`clk_get_parent`:

clk_get_parent
==============

.. c:function:: struct clk *clk_get_parent(struct clk *clk)

    get the parent clock source for this clock

    :param clk:
        clock source
    :type clk: struct clk \*

.. _`clk_get_parent.description`:

Description
-----------

Returns struct clk corresponding to parent clock source, or
valid \ :c:func:`IS_ERR`\  condition containing errno.

.. _`clk_get_sys`:

clk_get_sys
===========

.. c:function:: struct clk *clk_get_sys(const char *dev_id, const char *con_id)

    get a clock based upon the device name

    :param dev_id:
        device name
    :type dev_id: const char \*

    :param con_id:
        connection ID
    :type con_id: const char \*

.. _`clk_get_sys.description`:

Description
-----------

Returns a struct clk corresponding to the clock producer, or
valid \ :c:func:`IS_ERR`\  condition containing errno.  The implementation
uses \ ``dev_id``\  and \ ``con_id``\  to determine the clock consumer, and
thereby the clock producer. In contrast to \ :c:func:`clk_get`\  this function
takes the device name instead of the device itself for identification.

Drivers must assume that the clock source is not enabled.

clk_get_sys should not be called from within interrupt context.

.. _`clk_save_context`:

clk_save_context
================

.. c:function:: int clk_save_context( void)

    save clock context for poweroff

    :param void:
        no arguments
    :type void: 

.. _`clk_save_context.description`:

Description
-----------

Saves the context of the clock register for powerstates in which the
contents of the registers will be lost. Occurs deep within the suspend
code so locking is not necessary.

.. _`clk_restore_context`:

clk_restore_context
===================

.. c:function:: void clk_restore_context( void)

    restore clock context after poweroff

    :param void:
        no arguments
    :type void: 

.. _`clk_restore_context.description`:

Description
-----------

This occurs with all clocks enabled. Occurs deep within the resume code
so locking is not necessary.

.. This file was automatic generated / don't edit.

