.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk.c

.. _`clk_unprepare`:

clk_unprepare
=============

.. c:function:: void clk_unprepare(struct clk *clk)

    undo preparation of a clock source

    :param struct clk \*clk:
        the clk being unprepared

.. _`clk_unprepare.description`:

Description
-----------

clk_unprepare may sleep, which differentiates it from clk_disable.  In a
simple case, clk_unprepare can be used instead of clk_disable to gate a clk
if the operation may sleep.  One example is a clk which is accessed over
I2c.  In the complex case a clk gate operation may require a fast and a slow
part.  It is this reason that clk_unprepare and clk_disable are not mutually
exclusive.  In fact clk_disable must be called before clk_unprepare.

.. _`clk_prepare`:

clk_prepare
===========

.. c:function:: int clk_prepare(struct clk *clk)

    prepare a clock source

    :param struct clk \*clk:
        the clk being prepared

.. _`clk_prepare.description`:

Description
-----------

clk_prepare may sleep, which differentiates it from clk_enable.  In a simple
case, clk_prepare can be used instead of clk_enable to ungate a clk if the
operation may sleep.  One example is a clk which is accessed over I2c.  In
the complex case a clk ungate operation may require a fast and a slow part.
It is this reason that clk_prepare and clk_enable are not mutually
exclusive.  In fact clk_prepare must be called before clk_enable.
Returns 0 on success, -EERROR otherwise.

.. _`clk_disable`:

clk_disable
===========

.. c:function:: void clk_disable(struct clk *clk)

    gate a clock

    :param struct clk \*clk:
        the clk being gated

.. _`clk_disable.description`:

Description
-----------

clk_disable must not sleep, which differentiates it from clk_unprepare.  In
a simple case, clk_disable can be used instead of clk_unprepare to gate a
clk if the operation is fast and will never sleep.  One example is a
SoC-internal clk which is controlled via simple register writes.  In the
complex case a clk gate operation may require a fast and a slow part.  It is
this reason that clk_unprepare and clk_disable are not mutually exclusive.
In fact clk_disable must be called before clk_unprepare.

.. _`clk_enable`:

clk_enable
==========

.. c:function:: int clk_enable(struct clk *clk)

    ungate a clock

    :param struct clk \*clk:
        the clk being ungated

.. _`clk_enable.description`:

Description
-----------

clk_enable must not sleep, which differentiates it from clk_prepare.  In a
simple case, clk_enable can be used instead of clk_prepare to ungate a clk
if the operation will never sleep.  One example is a SoC-internal clk which
is controlled via simple register writes.  In the complex case a clk ungate
operation may require a fast and a slow part.  It is this reason that
clk_enable and clk_prepare are not mutually exclusive.  In fact clk_prepare
must be called before clk_enable.  Returns 0 on success, -EERROR
otherwise.

.. _`__clk_determine_rate`:

__clk_determine_rate
====================

.. c:function:: int __clk_determine_rate(struct clk_hw *hw, struct clk_rate_request *req)

    get the closest rate actually supported by a clock

    :param struct clk_hw \*hw:
        determine the rate of this clock

    :param struct clk_rate_request \*req:
        *undescribed*

.. _`__clk_determine_rate.description`:

Description
-----------

Useful for clk_ops such as .set_rate and .determine_rate.

.. _`clk_round_rate`:

clk_round_rate
==============

.. c:function:: long clk_round_rate(struct clk *clk, unsigned long rate)

    round the given rate for a clk

    :param struct clk \*clk:
        the clk for which we are rounding a rate

    :param unsigned long rate:
        the rate which is to be rounded

.. _`clk_round_rate.description`:

Description
-----------

Takes in a rate as input and rounds it to a rate that the clk can actually
use which is then returned.  If clk doesn't support round_rate operation
then the parent rate is returned.

.. _`__clk_notify`:

__clk_notify
============

.. c:function:: int __clk_notify(struct clk_core *core, unsigned long msg, unsigned long old_rate, unsigned long new_rate)

    call clk notifier chain

    :param struct clk_core \*core:
        clk that is changing rate

    :param unsigned long msg:
        clk notifier type (see include/linux/clk.h)

    :param unsigned long old_rate:
        old clk rate

    :param unsigned long new_rate:
        new clk rate

.. _`__clk_notify.description`:

Description
-----------

Triggers a notifier call chain on the clk rate-change notification
for 'clk'.  Passes a pointer to the struct clk and the previous
and current rates to the notifier callback.  Intended to be called by
internal clock code only.  Returns NOTIFY_DONE from the last driver
called if all went well, or NOTIFY_STOP or NOTIFY_BAD immediately if
a driver returns that.

.. _`__clk_recalc_accuracies`:

__clk_recalc_accuracies
=======================

.. c:function:: void __clk_recalc_accuracies(struct clk_core *core)

    :param struct clk_core \*core:
        first clk in the subtree

.. _`__clk_recalc_accuracies.description`:

Description
-----------

Walks the subtree of clks starting with clk and recalculates accuracies as
it goes.  Note that if a clk does not implement the .recalc_accuracy
callback then it is assumed that the clock will take on the accuracy of its
parent.

.. _`clk_get_accuracy`:

clk_get_accuracy
================

.. c:function:: long clk_get_accuracy(struct clk *clk)

    return the accuracy of clk

    :param struct clk \*clk:
        the clk whose accuracy is being returned

.. _`clk_get_accuracy.description`:

Description
-----------

Simply returns the cached accuracy of the clk, unless
CLK_GET_ACCURACY_NOCACHE flag is set, which means a recalc_rate will be
issued.
If clk is NULL then returns 0.

.. _`__clk_recalc_rates`:

__clk_recalc_rates
==================

.. c:function:: void __clk_recalc_rates(struct clk_core *core, unsigned long msg)

    :param struct clk_core \*core:
        first clk in the subtree

    :param unsigned long msg:
        notification type (see include/linux/clk.h)

.. _`__clk_recalc_rates.description`:

Description
-----------

Walks the subtree of clks starting with clk and recalculates rates as it
goes.  Note that if a clk does not implement the .recalc_rate callback then
it is assumed that the clock will take on the rate of its parent.

clk_recalc_rates also propagates the POST_RATE_CHANGE notification,
if necessary.

.. _`clk_get_rate`:

clk_get_rate
============

.. c:function:: unsigned long clk_get_rate(struct clk *clk)

    return the rate of clk

    :param struct clk \*clk:
        the clk whose rate is being returned

.. _`clk_get_rate.description`:

Description
-----------

Simply returns the cached rate of the clk, unless CLK_GET_RATE_NOCACHE flag
is set, which means a recalc_rate will be issued.
If clk is NULL then returns 0.

.. _`__clk_speculate_rates`:

__clk_speculate_rates
=====================

.. c:function:: int __clk_speculate_rates(struct clk_core *core, unsigned long parent_rate)

    :param struct clk_core \*core:
        first clk in the subtree

    :param unsigned long parent_rate:
        the "future" rate of clk's parent

.. _`__clk_speculate_rates.description`:

Description
-----------

Walks the subtree of clks starting with clk, speculating rates as it
goes and firing off PRE_RATE_CHANGE notifications as necessary.

Unlike clk_recalc_rates, clk_speculate_rates exists only for sending
pre-rate change notifications and returns early if no clks in the
subtree have subscribed to the notifications.  Note that if a clk does not
implement the .recalc_rate callback then it is assumed that the clock will
take on the rate of its parent.

.. _`clk_set_rate`:

clk_set_rate
============

.. c:function:: int clk_set_rate(struct clk *clk, unsigned long rate)

    specify a new rate for clk

    :param struct clk \*clk:
        the clk whose rate is being changed

    :param unsigned long rate:
        the new rate for clk

.. _`clk_set_rate.description`:

Description
-----------

In the simplest case clk_set_rate will only adjust the rate of clk.

Setting the CLK_SET_RATE_PARENT flag allows the rate change operation to
propagate up to clk's parent; whether or not this happens depends on the
outcome of clk's .round_rate implementation.  If \*parent_rate is unchanged
after calling .round_rate then upstream parent propagation is ignored.  If
\*parent_rate comes back with a new rate for clk's parent then we propagate
up to clk's parent and set its rate.  Upward propagation will continue
until either a clk does not support the CLK_SET_RATE_PARENT flag or
.round_rate stops requesting changes to clk's parent_rate.

Rate changes are accomplished via tree traversal that also recalculates the
rates for the clocks and fires off POST_RATE_CHANGE notifiers.

Returns 0 on success, -EERROR otherwise.

.. _`clk_set_rate_range`:

clk_set_rate_range
==================

.. c:function:: int clk_set_rate_range(struct clk *clk, unsigned long min, unsigned long max)

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

.. c:function:: int clk_set_min_rate(struct clk *clk, unsigned long rate)

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

.. c:function:: int clk_set_max_rate(struct clk *clk, unsigned long rate)

    set a maximum clock rate for a clock source

    :param struct clk \*clk:
        clock source

    :param unsigned long rate:
        desired maximum clock rate in Hz, inclusive

.. _`clk_set_max_rate.description`:

Description
-----------

Returns success (0) or negative errno.

.. _`clk_get_parent`:

clk_get_parent
==============

.. c:function:: struct clk *clk_get_parent(struct clk *clk)

    return the parent of a clk

    :param struct clk \*clk:
        the clk whose parent gets returned

.. _`clk_get_parent.description`:

Description
-----------

Simply returns clk->parent.  Returns NULL if clk is NULL.

.. _`clk_has_parent`:

clk_has_parent
==============

.. c:function:: bool clk_has_parent(struct clk *clk, struct clk *parent)

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

Returns true if \ ``parent``\  is a possible parent for \ ``clk``\ , false otherwise.

.. _`clk_set_parent`:

clk_set_parent
==============

.. c:function:: int clk_set_parent(struct clk *clk, struct clk *parent)

    switch the parent of a mux clk

    :param struct clk \*clk:
        the mux clk whose input we are switching

    :param struct clk \*parent:
        the new input to clk

.. _`clk_set_parent.description`:

Description
-----------

Re-parent clk to use parent as its new input source.  If clk is in
prepared state, the clk will get enabled for the duration of this call. If
that's not acceptable for a specific clk (Eg: the consumer can't handle
that, the reparenting is glitchy in hardware, etc), use the
CLK_SET_PARENT_GATE flag to allow reparenting only when clk is unprepared.

After successfully changing clk's parent clk_set_parent will update the
clk topology, sysfs topology and propagate rate recalculation via
\__clk_recalc_rates.

Returns 0 on success, -EERROR otherwise.

.. _`clk_set_phase`:

clk_set_phase
=============

.. c:function:: int clk_set_phase(struct clk *clk, int degrees)

    adjust the phase shift of a clock signal

    :param struct clk \*clk:
        clock signal source

    :param int degrees:
        number of degrees the signal is shifted

.. _`clk_set_phase.description`:

Description
-----------

Shifts the phase of a clock signal by the specified
degrees. Returns 0 on success, -EERROR otherwise.

This function makes no distinction about the input or reference
signal that we adjust the clock signal phase against. For example
phase locked-loop clock signal generators we may shift phase with
respect to feedback clock signal input, but for other cases the
clock phase may be shifted with respect to some other, unspecified
signal.

Additionally the concept of phase shift does not propagate through
the clock tree hierarchy, which sets it apart from clock rates and
clock accuracy. A parent clock phase attribute does not have an
impact on the phase attribute of a child clock.

.. _`clk_get_phase`:

clk_get_phase
=============

.. c:function:: int clk_get_phase(struct clk *clk)

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

.. c:function:: bool clk_is_match(const struct clk *p, const struct clk *q)

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

.. _`clk_debug_register`:

clk_debug_register
==================

.. c:function:: int clk_debug_register(struct clk_core *core)

    add a clk node to the debugfs clk directory

    :param struct clk_core \*core:
        the clk being added to the debugfs clk directory

.. _`clk_debug_register.description`:

Description
-----------

Dynamically adds a clk to the debugfs clk directory if debugfs has been
initialized.  Otherwise it bails out early since the debugfs clk directory
will be created lazily by clk_debug_init as part of a late_initcall.

.. _`clk_debug_init`:

clk_debug_init
==============

.. c:function:: int clk_debug_init( void)

    lazily populate the debugfs clk directory

    :param  void:
        no arguments

.. _`clk_debug_init.description`:

Description
-----------

clks are often initialized very early during boot before memory can be
dynamically allocated and well before debugfs is setup. This function
populates the debugfs clk directory once at boot-time when we know that
debugfs is setup. It should only be called once at boot-time, all other clks
added dynamically will be done so with clk_debug_register.

.. _`__clk_core_init`:

__clk_core_init
===============

.. c:function:: int __clk_core_init(struct clk_core *core)

    initialize the data structures in a struct clk_core

    :param struct clk_core \*core:
        clk_core being initialized

.. _`__clk_core_init.description`:

Description
-----------

Initializes the lists in struct clk_core, queries the hardware for the
parent and rate and sets them both.

.. _`clk_register`:

clk_register
============

.. c:function:: struct clk *clk_register(struct device *dev, struct clk_hw *hw)

    allocate a new clock, register it and return an opaque cookie

    :param struct device \*dev:
        device that is registering this clock

    :param struct clk_hw \*hw:
        link to hardware-specific clock data

.. _`clk_register.description`:

Description
-----------

clk_register is the primary interface for populating the clock tree with new
clock nodes.  It returns a pointer to the newly allocated struct clk which
cannot be dereferenced by driver code but may be used in conjunction with the
rest of the clock API.  In the event of an error clk_register will return an
error code; drivers must test for an error code after calling clk_register.

.. _`clk_hw_register`:

clk_hw_register
===============

.. c:function:: int clk_hw_register(struct device *dev, struct clk_hw *hw)

    register a clk_hw and return an error code

    :param struct device \*dev:
        device that is registering this clock

    :param struct clk_hw \*hw:
        link to hardware-specific clock data

.. _`clk_hw_register.description`:

Description
-----------

clk_hw_register is the primary interface for populating the clock tree with
new clock nodes. It returns an integer equal to zero indicating success or
less than zero indicating failure. Drivers must test for an error code after
calling \ :c:func:`clk_hw_register`\ .

.. _`clk_unregister`:

clk_unregister
==============

.. c:function:: void clk_unregister(struct clk *clk)

    unregister a currently registered clock

    :param struct clk \*clk:
        clock to unregister

.. _`clk_hw_unregister`:

clk_hw_unregister
=================

.. c:function:: void clk_hw_unregister(struct clk_hw *hw)

    unregister a currently registered clk_hw

    :param struct clk_hw \*hw:
        hardware-specific clock data to unregister

.. _`devm_clk_register`:

devm_clk_register
=================

.. c:function:: struct clk *devm_clk_register(struct device *dev, struct clk_hw *hw)

    resource managed \ :c:func:`clk_register`\ 

    :param struct device \*dev:
        device that is registering this clock

    :param struct clk_hw \*hw:
        link to hardware-specific clock data

.. _`devm_clk_register.description`:

Description
-----------

Managed \ :c:func:`clk_register`\ . Clocks returned from this function are
automatically \ :c:func:`clk_unregister`\ ed on driver detach. See \ :c:func:`clk_register`\  for
more information.

.. _`devm_clk_hw_register`:

devm_clk_hw_register
====================

.. c:function:: int devm_clk_hw_register(struct device *dev, struct clk_hw *hw)

    resource managed \ :c:func:`clk_hw_register`\ 

    :param struct device \*dev:
        device that is registering this clock

    :param struct clk_hw \*hw:
        link to hardware-specific clock data

.. _`devm_clk_hw_register.description`:

Description
-----------

Managed \ :c:func:`clk_hw_register`\ . Clocks registered by this function are
automatically \ :c:func:`clk_hw_unregister`\ ed on driver detach. See \ :c:func:`clk_hw_register`\ 
for more information.

.. _`devm_clk_unregister`:

devm_clk_unregister
===================

.. c:function:: void devm_clk_unregister(struct device *dev, struct clk *clk)

    resource managed \ :c:func:`clk_unregister`\ 

    :param struct device \*dev:
        *undescribed*

    :param struct clk \*clk:
        clock to unregister

.. _`devm_clk_unregister.description`:

Description
-----------

Deallocate a clock allocated with \ :c:func:`devm_clk_register`\ . Normally
this function will not need to be called and the resource management
code will ensure that the resource is freed.

.. _`devm_clk_hw_unregister`:

devm_clk_hw_unregister
======================

.. c:function:: void devm_clk_hw_unregister(struct device *dev, struct clk_hw *hw)

    resource managed \ :c:func:`clk_hw_unregister`\ 

    :param struct device \*dev:
        device that is unregistering the hardware-specific clock data

    :param struct clk_hw \*hw:
        link to hardware-specific clock data

.. _`devm_clk_hw_unregister.description`:

Description
-----------

Unregister a clk_hw registered with \ :c:func:`devm_clk_hw_register`\ . Normally
this function will not need to be called and the resource management
code will ensure that the resource is freed.

.. _`clk_notifier_register`:

clk_notifier_register
=====================

.. c:function:: int clk_notifier_register(struct clk *clk, struct notifier_block *nb)

    add a clk rate change notifier

    :param struct clk \*clk:
        struct clk \* to watch

    :param struct notifier_block \*nb:
        struct notifier_block \* with callback info

.. _`clk_notifier_register.description`:

Description
-----------

Request notification when clk's rate changes.  This uses an SRCU
notifier because we want it to block and notifier unregistrations are
uncommon.  The callbacks associated with the notifier must not
re-enter into the clk framework by calling any top-level clk APIs;
this will cause a nested prepare_lock mutex.

In all notification cases (pre, post and abort rate change) the original
clock rate is passed to the callback via struct clk_notifier_data.old_rate
and the new frequency is passed via struct clk_notifier_data.new_rate.

\ :c:func:`clk_notifier_register`\  must be called from non-atomic context.
Returns -EINVAL if called with null arguments, -ENOMEM upon
allocation failure; otherwise, passes along the return value of
\ :c:func:`srcu_notifier_chain_register`\ .

.. _`clk_notifier_unregister`:

clk_notifier_unregister
=======================

.. c:function:: int clk_notifier_unregister(struct clk *clk, struct notifier_block *nb)

    remove a clk rate change notifier

    :param struct clk \*clk:
        struct clk \*

    :param struct notifier_block \*nb:
        struct notifier_block \* with callback info

.. _`clk_notifier_unregister.description`:

Description
-----------

Request no further notification for changes to 'clk' and frees memory
allocated in clk_notifier_register.

Returns -EINVAL if called with null arguments; otherwise, passes
along the return value of \ :c:func:`srcu_notifier_chain_unregister`\ .

.. _`of_clk_provider`:

struct of_clk_provider
======================

.. c:type:: struct of_clk_provider

    Clock provider registration structure

.. _`of_clk_provider.definition`:

Definition
----------

.. code-block:: c

    struct of_clk_provider {
        struct list_head link;
        struct device_node *node;
        struct clk *(*get)(struct of_phandle_args *clkspec, void *data);
        struct clk_hw *(*get_hw)(struct of_phandle_args *clkspec, void *data);
        void *data;
    }

.. _`of_clk_provider.members`:

Members
-------

link
    Entry in global list of clock providers

node
    Pointer to device tree node of clock provider

get
    Get clock callback.  Returns NULL or a struct clk for the
    given clock specifier

get_hw
    *undescribed*

data
    context pointer to be passed into \ ``get``\  callback

.. _`of_clk_add_provider`:

of_clk_add_provider
===================

.. c:function:: int of_clk_add_provider(struct device_node *np, struct clk *(*clk_src_get)(struct of_phandle_args *clkspec, void *data), void *data)

    Register a clock provider for a node

    :param struct device_node \*np:
        Device node pointer associated with clock provider

    :param struct clk \*(\*clk_src_get)(struct of_phandle_args \*clkspec, void \*data):
        callback for decoding clock

    :param void \*data:
        context pointer for \ ``clk_src_get``\  callback.

.. _`of_clk_add_hw_provider`:

of_clk_add_hw_provider
======================

.. c:function:: int of_clk_add_hw_provider(struct device_node *np, struct clk_hw *(*get)(struct of_phandle_args *clkspec, void *data), void *data)

    Register a clock provider for a node

    :param struct device_node \*np:
        Device node pointer associated with clock provider

    :param struct clk_hw \*(\*get)(struct of_phandle_args \*clkspec, void \*data):
        callback for decoding clk_hw

    :param void \*data:
        context pointer for \ ``get``\  callback.

.. _`of_clk_del_provider`:

of_clk_del_provider
===================

.. c:function:: void of_clk_del_provider(struct device_node *np)

    Remove a previously registered clock provider

    :param struct device_node \*np:
        Device node pointer associated with clock provider

.. _`of_clk_get_from_provider`:

of_clk_get_from_provider
========================

.. c:function:: struct clk *of_clk_get_from_provider(struct of_phandle_args *clkspec)

    Lookup a clock from a clock provider

    :param struct of_phandle_args \*clkspec:
        pointer to a clock specifier data structure

.. _`of_clk_get_from_provider.description`:

Description
-----------

This function looks up a struct clk from the registered list of clock
providers, an input is a clock specifier data structure as returned
from the \ :c:func:`of_parse_phandle_with_args`\  function call.

.. _`of_clk_get_parent_count`:

of_clk_get_parent_count
=======================

.. c:function:: unsigned int of_clk_get_parent_count(struct device_node *np)

    Count the number of clocks a device node has

    :param struct device_node \*np:
        device node to count

.. _`of_clk_get_parent_count.return`:

Return
------

The number of clocks that are possible parents of this node

.. _`of_clk_parent_fill`:

of_clk_parent_fill
==================

.. c:function:: int of_clk_parent_fill(struct device_node *np, const char **parents, unsigned int size)

    Fill \ ``parents``\  with names of \ ``np``\ 's parents and return number of parents

    :param struct device_node \*np:
        Device node pointer associated with clock provider

    :param const char \*\*parents:
        pointer to char array that hold the parents' names

    :param unsigned int size:
        size of the \ ``parents``\  array

.. _`of_clk_parent_fill.return`:

Return
------

number of parents for the clock node.

.. _`of_clk_detect_critical`:

of_clk_detect_critical
======================

.. c:function:: int of_clk_detect_critical(struct device_node *np, int index, unsigned long *flags)

    set CLK_IS_CRITICAL flag from Device Tree

    :param struct device_node \*np:
        Device node pointer associated with clock provider

    :param int index:
        clock index

    :param unsigned long \*flags:
        pointer to clk_core->flags

.. _`of_clk_detect_critical.description`:

Description
-----------

Detects if the clock-critical property exists and, if so, sets the
corresponding CLK_IS_CRITICAL flag.

Do not use this function. It exists only for legacy Device Tree
bindings, such as the one-clock-per-node style that are outdated.
Those bindings typically put all clock data into .dts and the Linux
driver has no clock data, thus making it impossible to set this flag
correctly from the driver. Only those drivers may call
of_clk_detect_critical from their setup functions.

.. _`of_clk_detect_critical.return`:

Return
------

error code or zero on success

.. _`of_clk_init`:

of_clk_init
===========

.. c:function:: void of_clk_init(const struct of_device_id *matches)

    Scan and init clock providers from the DT

    :param const struct of_device_id \*matches:
        array of compatible values and init functions for providers.

.. _`of_clk_init.description`:

Description
-----------

This function scans the device tree for matching clock providers
and calls their initialization functions. It also does it by trying
to follow the dependencies.

.. This file was automatic generated / don't edit.

