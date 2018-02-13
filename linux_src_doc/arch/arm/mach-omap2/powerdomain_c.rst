.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/powerdomain.c

.. _`_pwrdm_register`:

\_pwrdm_register
================

.. c:function:: int _pwrdm_register(struct powerdomain *pwrdm)

    register a powerdomain

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to register

.. _`_pwrdm_register.description`:

Description
-----------

Adds a powerdomain to the internal powerdomain list.  Returns
-EINVAL if given a null pointer, -EEXIST if a powerdomain is
already registered by the provided name, or 0 upon success.

.. _`_pwrdm_save_clkdm_state_and_activate`:

\_pwrdm_save_clkdm_state_and_activate
=====================================

.. c:function:: u8 _pwrdm_save_clkdm_state_and_activate(struct powerdomain *pwrdm, u8 curr_pwrst, u8 pwrst)

    prepare for power state change

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to operate on

    :param u8 curr_pwrst:
        current power state of \ ``pwrdm``\ 

    :param u8 pwrst:
        power state to switch to

.. _`_pwrdm_save_clkdm_state_and_activate.description`:

Description
-----------

Determine whether the powerdomain needs to be turned on before
attempting to switch power states.  Called by
\ :c:func:`omap_set_pwrdm_state`\ .  NOTE that if the powerdomain contains
multiple clockdomains, this code assumes that the first clockdomain
supports software-supervised wakeup mode - potentially a problem.
Returns the power state switch mode currently in use (see the
"Types of sleep_switch" comment above).

.. _`_pwrdm_restore_clkdm_state`:

\_pwrdm_restore_clkdm_state
===========================

.. c:function:: void _pwrdm_restore_clkdm_state(struct powerdomain *pwrdm, u8 sleep_switch)

    restore the clkdm hwsup state after pwrst change

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to operate on

    :param u8 sleep_switch:
        return value from \_pwrdm_save_clkdm_state_and_activate()

.. _`_pwrdm_restore_clkdm_state.description`:

Description
-----------

Restore the clockdomain state perturbed by
\_pwrdm_save_clkdm_state_and_activate(), and call the power state
bookkeeping code.  Called by \ :c:func:`omap_set_pwrdm_state`\ .  NOTE that if
the powerdomain contains multiple clockdomains, this assumes that
the first associated clockdomain supports either
hardware-supervised idle control in the register, or
software-supervised sleep.  No return value.

.. _`pwrdm_register_platform_funcs`:

pwrdm_register_platform_funcs
=============================

.. c:function:: int pwrdm_register_platform_funcs(struct pwrdm_ops *po)

    register powerdomain implementation fns

    :param struct pwrdm_ops \*po:
        func pointers for arch specific implementations

.. _`pwrdm_register_platform_funcs.description`:

Description
-----------

Register the list of function pointers used to implement the
powerdomain functions on different OMAP SoCs.  Should be called
before any other pwrdm_register\*() function.  Returns -EINVAL if
\ ``po``\  is null, -EEXIST if platform functions have already been
registered, or 0 upon success.

.. _`pwrdm_register_pwrdms`:

pwrdm_register_pwrdms
=====================

.. c:function:: int pwrdm_register_pwrdms(struct powerdomain **ps)

    register SoC powerdomains

    :param struct powerdomain \*\*ps:
        pointer to an array of struct powerdomain to register

.. _`pwrdm_register_pwrdms.description`:

Description
-----------

Register the powerdomains available on a particular OMAP SoC.  Must
be called after \ :c:func:`pwrdm_register_platform_funcs`\ .  May be called
multiple times.  Returns -EACCES if called before
\ :c:func:`pwrdm_register_platform_funcs`\ ; -EINVAL if the argument \ ``ps``\  is
null; or 0 upon success.

.. _`pwrdm_complete_init`:

pwrdm_complete_init
===================

.. c:function:: int pwrdm_complete_init( void)

    set up the powerdomain layer

    :param  void:
        no arguments

.. _`pwrdm_complete_init.description`:

Description
-----------

Do whatever is necessary to initialize registered powerdomains and
powerdomain code.  Currently, this programs the next power state
for each powerdomain to ON.  This prevents powerdomains from
unexpectedly losing context or entering high wakeup latency modes
with non-power-management-enabled kernels.  Must be called after
\ :c:func:`pwrdm_register_pwrdms`\ .  Returns -EACCES if called before
\ :c:func:`pwrdm_register_pwrdms`\ , or 0 upon success.

.. _`pwrdm_lock`:

pwrdm_lock
==========

.. c:function:: void pwrdm_lock(struct powerdomain *pwrdm)

    acquire a Linux spinlock on a powerdomain

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to lock

.. _`pwrdm_lock.description`:

Description
-----------

Acquire the powerdomain spinlock on \ ``pwrdm``\ .  No return value.

.. _`pwrdm_unlock`:

pwrdm_unlock
============

.. c:function:: void pwrdm_unlock(struct powerdomain *pwrdm)

    release a Linux spinlock on a powerdomain

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to unlock

.. _`pwrdm_unlock.description`:

Description
-----------

Release the powerdomain spinlock on \ ``pwrdm``\ .  No return value.

.. _`pwrdm_lookup`:

pwrdm_lookup
============

.. c:function:: struct powerdomain *pwrdm_lookup(const char *name)

    look up a powerdomain by name, return a pointer

    :param const char \*name:
        name of powerdomain

.. _`pwrdm_lookup.description`:

Description
-----------

Find a registered powerdomain by its name \ ``name``\ .  Returns a pointer
to the struct powerdomain if found, or NULL otherwise.

.. _`pwrdm_for_each`:

pwrdm_for_each
==============

.. c:function:: int pwrdm_for_each(int (*fn)(struct powerdomain *pwrdm, void *user), void *user)

    call function on each registered clockdomain

    :param int (\*fn)(struct powerdomain \*pwrdm, void \*user):
        callback function \*

    :param void \*user:
        *undescribed*

.. _`pwrdm_for_each.description`:

Description
-----------

Call the supplied function \ ``fn``\  for each registered powerdomain.
The callback function \ ``fn``\  can return anything but 0 to bail out
early from the iterator.  Returns the last return value of the
callback function, which should be 0 for success or anything else
to indicate failure; or -EINVAL if the function pointer is null.

.. _`pwrdm_add_clkdm`:

pwrdm_add_clkdm
===============

.. c:function:: int pwrdm_add_clkdm(struct powerdomain *pwrdm, struct clockdomain *clkdm)

    add a clockdomain to a powerdomain

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to add the clockdomain to

    :param struct clockdomain \*clkdm:
        struct clockdomain \* to associate with a powerdomain

.. _`pwrdm_add_clkdm.description`:

Description
-----------

Associate the clockdomain \ ``clkdm``\  with a powerdomain \ ``pwrdm``\ .  This
enables the use of \ :c:func:`pwrdm_for_each_clkdm`\ .  Returns -EINVAL if
presented with invalid pointers; -ENOMEM if memory could not be allocated;
or 0 upon success.

.. _`pwrdm_get_mem_bank_count`:

pwrdm_get_mem_bank_count
========================

.. c:function:: int pwrdm_get_mem_bank_count(struct powerdomain *pwrdm)

    get number of memory banks in this powerdomain

    :param struct powerdomain \*pwrdm:
        struct powerdomain \*

.. _`pwrdm_get_mem_bank_count.description`:

Description
-----------

Return the number of controllable memory banks in powerdomain \ ``pwrdm``\ ,
starting with 1.  Returns -EINVAL if the powerdomain pointer is null.

.. _`pwrdm_set_next_pwrst`:

pwrdm_set_next_pwrst
====================

.. c:function:: int pwrdm_set_next_pwrst(struct powerdomain *pwrdm, u8 pwrst)

    set next powerdomain power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to set

    :param u8 pwrst:
        one of the PWRDM_POWER\_\* macros

.. _`pwrdm_set_next_pwrst.description`:

Description
-----------

Set the powerdomain \ ``pwrdm``\ 's next power state to \ ``pwrst``\ .  The powerdomain
may not enter this state immediately if the preconditions for this state
have not been satisfied.  Returns -EINVAL if the powerdomain pointer is
null or if the power state is invalid for the powerdomin, or returns 0
upon success.

.. _`pwrdm_read_next_pwrst`:

pwrdm_read_next_pwrst
=====================

.. c:function:: int pwrdm_read_next_pwrst(struct powerdomain *pwrdm)

    get next powerdomain power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get power state

.. _`pwrdm_read_next_pwrst.description`:

Description
-----------

Return the powerdomain \ ``pwrdm``\ 's next power state.  Returns -EINVAL
if the powerdomain pointer is null or returns the next power state
upon success.

.. _`pwrdm_read_pwrst`:

pwrdm_read_pwrst
================

.. c:function:: int pwrdm_read_pwrst(struct powerdomain *pwrdm)

    get current powerdomain power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get power state

.. _`pwrdm_read_pwrst.description`:

Description
-----------

Return the powerdomain \ ``pwrdm``\ 's current power state. Returns -EINVAL
if the powerdomain pointer is null or returns the current power state
upon success. Note that if the power domain only supports the ON state
then just return ON as the current state.

.. _`pwrdm_read_prev_pwrst`:

pwrdm_read_prev_pwrst
=====================

.. c:function:: int pwrdm_read_prev_pwrst(struct powerdomain *pwrdm)

    get previous powerdomain power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get previous power state

.. _`pwrdm_read_prev_pwrst.description`:

Description
-----------

Return the powerdomain \ ``pwrdm``\ 's previous power state.  Returns -EINVAL
if the powerdomain pointer is null or returns the previous power state
upon success.

.. _`pwrdm_set_logic_retst`:

pwrdm_set_logic_retst
=====================

.. c:function:: int pwrdm_set_logic_retst(struct powerdomain *pwrdm, u8 pwrst)

    set powerdomain logic power state upon retention

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to set

    :param u8 pwrst:
        one of the PWRDM_POWER\_\* macros

.. _`pwrdm_set_logic_retst.description`:

Description
-----------

Set the next power state \ ``pwrst``\  that the logic portion of the
powerdomain \ ``pwrdm``\  will enter when the powerdomain enters retention.
This will be either RETENTION or OFF, if supported.  Returns
-EINVAL if the powerdomain pointer is null or the target power
state is not not supported, or returns 0 upon success.

.. _`pwrdm_set_mem_onst`:

pwrdm_set_mem_onst
==================

.. c:function:: int pwrdm_set_mem_onst(struct powerdomain *pwrdm, u8 bank, u8 pwrst)

    set memory power state while powerdomain ON

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to set

    :param u8 bank:
        memory bank number to set (0-3)

    :param u8 pwrst:
        one of the PWRDM_POWER\_\* macros

.. _`pwrdm_set_mem_onst.description`:

Description
-----------

Set the next power state \ ``pwrst``\  that memory bank \ ``bank``\  of the
powerdomain \ ``pwrdm``\  will enter when the powerdomain enters the ON
state.  \ ``bank``\  will be a number from 0 to 3, and represents different
types of memory, depending on the powerdomain.  Returns -EINVAL if
the powerdomain pointer is null or the target power state is not
not supported for this memory bank, -EEXIST if the target memory
bank does not exist or is not controllable, or returns 0 upon
success.

.. _`pwrdm_set_mem_retst`:

pwrdm_set_mem_retst
===================

.. c:function:: int pwrdm_set_mem_retst(struct powerdomain *pwrdm, u8 bank, u8 pwrst)

    set memory power state while powerdomain in RET

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to set

    :param u8 bank:
        memory bank number to set (0-3)

    :param u8 pwrst:
        one of the PWRDM_POWER\_\* macros

.. _`pwrdm_set_mem_retst.description`:

Description
-----------

Set the next power state \ ``pwrst``\  that memory bank \ ``bank``\  of the
powerdomain \ ``pwrdm``\  will enter when the powerdomain enters the
RETENTION state.  Bank will be a number from 0 to 3, and represents
different types of memory, depending on the powerdomain.  \ ``pwrst``\ 
will be either RETENTION or OFF, if supported.  Returns -EINVAL if
the powerdomain pointer is null or the target power state is not
not supported for this memory bank, -EEXIST if the target memory
bank does not exist or is not controllable, or returns 0 upon
success.

.. _`pwrdm_read_logic_pwrst`:

pwrdm_read_logic_pwrst
======================

.. c:function:: int pwrdm_read_logic_pwrst(struct powerdomain *pwrdm)

    get current powerdomain logic retention power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get current logic retention power state

.. _`pwrdm_read_logic_pwrst.description`:

Description
-----------

Return the power state that the logic portion of powerdomain \ ``pwrdm``\ 
will enter when the powerdomain enters retention.  Returns -EINVAL
if the powerdomain pointer is null or returns the logic retention
power state upon success.

.. _`pwrdm_read_prev_logic_pwrst`:

pwrdm_read_prev_logic_pwrst
===========================

.. c:function:: int pwrdm_read_prev_logic_pwrst(struct powerdomain *pwrdm)

    get previous powerdomain logic power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get previous logic power state

.. _`pwrdm_read_prev_logic_pwrst.description`:

Description
-----------

Return the powerdomain \ ``pwrdm``\ 's previous logic power state.  Returns
-EINVAL if the powerdomain pointer is null or returns the previous
logic power state upon success.

.. _`pwrdm_read_logic_retst`:

pwrdm_read_logic_retst
======================

.. c:function:: int pwrdm_read_logic_retst(struct powerdomain *pwrdm)

    get next powerdomain logic power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get next logic power state

.. _`pwrdm_read_logic_retst.description`:

Description
-----------

Return the powerdomain pwrdm's logic power state.  Returns -EINVAL
if the powerdomain pointer is null or returns the next logic
power state upon success.

.. _`pwrdm_read_mem_pwrst`:

pwrdm_read_mem_pwrst
====================

.. c:function:: int pwrdm_read_mem_pwrst(struct powerdomain *pwrdm, u8 bank)

    get current memory bank power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get current memory bank power state

    :param u8 bank:
        memory bank number (0-3)

.. _`pwrdm_read_mem_pwrst.description`:

Description
-----------

Return the powerdomain \ ``pwrdm``\ 's current memory power state for bank
\ ``bank``\ .  Returns -EINVAL if the powerdomain pointer is null, -EEXIST if
the target memory bank does not exist or is not controllable, or
returns the current memory power state upon success.

.. _`pwrdm_read_prev_mem_pwrst`:

pwrdm_read_prev_mem_pwrst
=========================

.. c:function:: int pwrdm_read_prev_mem_pwrst(struct powerdomain *pwrdm, u8 bank)

    get previous memory bank power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get previous memory bank power state

    :param u8 bank:
        memory bank number (0-3)

.. _`pwrdm_read_prev_mem_pwrst.description`:

Description
-----------

Return the powerdomain \ ``pwrdm``\ 's previous memory power state for
bank \ ``bank``\ .  Returns -EINVAL if the powerdomain pointer is null,
-EEXIST if the target memory bank does not exist or is not
controllable, or returns the previous memory power state upon
success.

.. _`pwrdm_read_mem_retst`:

pwrdm_read_mem_retst
====================

.. c:function:: int pwrdm_read_mem_retst(struct powerdomain *pwrdm, u8 bank)

    get next memory bank power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to get mext memory bank power state

    :param u8 bank:
        memory bank number (0-3)

.. _`pwrdm_read_mem_retst.description`:

Description
-----------

Return the powerdomain pwrdm's next memory power state for bank
x.  Returns -EINVAL if the powerdomain pointer is null, -EEXIST if
the target memory bank does not exist or is not controllable, or
returns the next memory power state upon success.

.. _`pwrdm_clear_all_prev_pwrst`:

pwrdm_clear_all_prev_pwrst
==========================

.. c:function:: int pwrdm_clear_all_prev_pwrst(struct powerdomain *pwrdm)

    clear previous powerstate register for a pwrdm

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to clear

.. _`pwrdm_clear_all_prev_pwrst.description`:

Description
-----------

Clear the powerdomain's previous power state register \ ``pwrdm``\ .
Clears the entire register, including logic and memory bank
previous power states.  Returns -EINVAL if the powerdomain pointer
is null, or returns 0 upon success.

.. _`pwrdm_enable_hdwr_sar`:

pwrdm_enable_hdwr_sar
=====================

.. c:function:: int pwrdm_enable_hdwr_sar(struct powerdomain *pwrdm)

    enable automatic hardware SAR for a pwrdm

    :param struct powerdomain \*pwrdm:
        struct powerdomain \*

.. _`pwrdm_enable_hdwr_sar.description`:

Description
-----------

Enable automatic context save-and-restore upon power state change
for some devices in the powerdomain \ ``pwrdm``\ .  Warning: this only
affects a subset of devices in a powerdomain; check the TRM
closely.  Returns -EINVAL if the powerdomain pointer is null or if
the powerdomain does not support automatic save-and-restore, or
returns 0 upon success.

.. _`pwrdm_disable_hdwr_sar`:

pwrdm_disable_hdwr_sar
======================

.. c:function:: int pwrdm_disable_hdwr_sar(struct powerdomain *pwrdm)

    disable automatic hardware SAR for a pwrdm

    :param struct powerdomain \*pwrdm:
        struct powerdomain \*

.. _`pwrdm_disable_hdwr_sar.description`:

Description
-----------

Disable automatic context save-and-restore upon power state change
for some devices in the powerdomain \ ``pwrdm``\ .  Warning: this only
affects a subset of devices in a powerdomain; check the TRM
closely.  Returns -EINVAL if the powerdomain pointer is null or if
the powerdomain does not support automatic save-and-restore, or
returns 0 upon success.

.. _`pwrdm_has_hdwr_sar`:

pwrdm_has_hdwr_sar
==================

.. c:function:: bool pwrdm_has_hdwr_sar(struct powerdomain *pwrdm)

    test whether powerdomain supports hardware SAR

    :param struct powerdomain \*pwrdm:
        struct powerdomain \*

.. _`pwrdm_has_hdwr_sar.description`:

Description
-----------

Returns 1 if powerdomain \ ``pwrdm``\  supports hardware save-and-restore
for some devices, or 0 if it does not.

.. _`pwrdm_get_valid_lp_state`:

pwrdm_get_valid_lp_state
========================

.. c:function:: u8 pwrdm_get_valid_lp_state(struct powerdomain *pwrdm, bool is_logic_state, u8 req_state)

    Find best match deep power state

    :param struct powerdomain \*pwrdm:
        power domain for which we want to find best match

    :param bool is_logic_state:
        Are we looking for logic state match here? Should
        be one of PWRDM_xxx macro values

    :param u8 req_state:
        requested power state

.. _`pwrdm_get_valid_lp_state.return`:

Return
------

closest match for requested power state. default fallback
is RET for logic state and ON for power state.

This does a search from the power domain data looking for the
closest valid power domain state that the hardware can achieve.
PRCM definitions for PWRSTCTRL allows us to program whatever
configuration we'd like, and PRCM will actually attempt such
a transition, however if the powerdomain does not actually support it,
we endup with a hung system. The valid power domain states are already
available in our powerdomain data files. So this function tries to do

.. _`pwrdm_get_valid_lp_state.the-following`:

the following
-------------

a) find if we have an exact match to the request - no issues.
b) else find if a deeper power state is possible.
c) failing which, it tries to find closest higher power state for the
request.

.. _`omap_set_pwrdm_state`:

omap_set_pwrdm_state
====================

.. c:function:: int omap_set_pwrdm_state(struct powerdomain *pwrdm, u8 pwrst)

    change a powerdomain's current power state

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to change the power state of

    :param u8 pwrst:
        power state to change to

.. _`omap_set_pwrdm_state.description`:

Description
-----------

Change the current hardware power state of the powerdomain
represented by \ ``pwrdm``\  to the power state represented by \ ``pwrst``\ .
Returns -EINVAL if \ ``pwrdm``\  is null or invalid or if the
powerdomain's current power state could not be read, or returns 0
upon success or if \ ``pwrdm``\  does not support \ ``pwrst``\  or any
lower-power state.  XXX Should not return 0 if the \ ``pwrdm``\  does not
support \ ``pwrst``\  or any lower-power state: this should be an error.

.. _`pwrdm_get_context_loss_count`:

pwrdm_get_context_loss_count
============================

.. c:function:: int pwrdm_get_context_loss_count(struct powerdomain *pwrdm)

    get powerdomain's context loss count

    :param struct powerdomain \*pwrdm:
        struct powerdomain \* to wait for

.. _`pwrdm_get_context_loss_count.description`:

Description
-----------

Context loss count is the sum of powerdomain off-mode counter, the
logic off counter and the per-bank memory off counter.  Returns negative
(and WARNs) upon error, otherwise, returns the context loss count.

.. _`pwrdm_can_ever_lose_context`:

pwrdm_can_ever_lose_context
===========================

.. c:function:: bool pwrdm_can_ever_lose_context(struct powerdomain *pwrdm)

    can this powerdomain ever lose context?

    :param struct powerdomain \*pwrdm:
        struct powerdomain \*

.. _`pwrdm_can_ever_lose_context.description`:

Description
-----------

Given a struct powerdomain \* \ ``pwrdm``\ , returns 1 if the powerdomain
can lose either memory or logic context or if \ ``pwrdm``\  is invalid, or
returns 0 otherwise.  This function is not concerned with how the
powerdomain registers are programmed (i.e., to go off or not); it's
concerned with whether it's ever possible for this powerdomain to
go off while some other part of the chip is active.  This function
assumes that every powerdomain can go to either ON or INACTIVE.

.. This file was automatic generated / don't edit.

