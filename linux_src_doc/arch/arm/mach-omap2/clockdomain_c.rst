.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clockdomain.c

.. _`_clkdm_register`:

_clkdm_register
===============

.. c:function:: int _clkdm_register(struct clockdomain *clkdm)

    register a clockdomain

    :param struct clockdomain \*clkdm:
        struct clockdomain \* to register

.. _`_clkdm_register.description`:

Description
-----------

Adds a clockdomain to the internal clockdomain list.
Returns -EINVAL if given a null pointer, -EEXIST if a clockdomain is
already registered by the provided name, or 0 upon success.

.. _`_autodep_lookup`:

_autodep_lookup
===============

.. c:function:: void _autodep_lookup(struct clkdm_autodep *autodep)

    resolve autodep clkdm names to clkdm pointers; store

    :param struct clkdm_autodep \*autodep:
        struct clkdm_autodep \* to resolve

.. _`_autodep_lookup.description`:

Description
-----------

Resolve autodep clockdomain names to clockdomain pointers via
\ :c:func:`clkdm_lookup`\  and store the pointers in the autodep structure.  An
"autodep" is a clockdomain sleep/wakeup dependency that is
automatically added and removed whenever clocks in the associated
clockdomain are enabled or disabled (respectively) when the
clockdomain is in hardware-supervised mode.  Meant to be called
once at clockdomain layer initialization, since these should remain
fixed for a particular architecture.  No return value.

XXX autodeps are deprecated and should be removed at the earliest
opportunity

.. _`_resolve_clkdm_deps`:

_resolve_clkdm_deps
===================

.. c:function:: void _resolve_clkdm_deps(struct clockdomain *clkdm, struct clkdm_dep *clkdm_deps)

    resolve clkdm_names in \ ``clkdm_deps``\  to clkdms

    :param struct clockdomain \*clkdm:
        clockdomain that we are resolving dependencies for

    :param struct clkdm_dep \*clkdm_deps:
        ptr to array of struct clkdm_deps to resolve

.. _`_resolve_clkdm_deps.description`:

Description
-----------

Iterates through \ ``clkdm_deps``\ , looking up the struct clockdomain named by
clkdm_name and storing the clockdomain pointer in the struct clkdm_dep.
No return value.

.. _`_clkdm_add_wkdep`:

_clkdm_add_wkdep
================

.. c:function:: int _clkdm_add_wkdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    add a wakeup dependency from clkdm2 to clkdm1 (lockless)

    :param struct clockdomain \*clkdm1:
        wake this struct clockdomain \* up (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* wakes up (source)

.. _`_clkdm_add_wkdep.description`:

Description
-----------

When the clockdomain represented by \ ``clkdm2``\  wakes up, wake up
\ ``clkdm1``\ . Implemented in hardware on the OMAP, this feature is
designed to reduce wakeup latency of the dependent clockdomain \ ``clkdm1``\ .
Returns -EINVAL if presented with invalid clockdomain pointers,
-ENOENT if \ ``clkdm2``\  cannot wake up clkdm1 in hardware, or 0 upon
success.

.. _`_clkdm_del_wkdep`:

_clkdm_del_wkdep
================

.. c:function:: int _clkdm_del_wkdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    remove a wakeup dep from clkdm2 to clkdm1 (lockless)

    :param struct clockdomain \*clkdm1:
        wake this struct clockdomain \* up (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* wakes up (source)

.. _`_clkdm_del_wkdep.description`:

Description
-----------

Remove a wakeup dependency causing \ ``clkdm1``\  to wake up when \ ``clkdm2``\ 
wakes up.  Returns -EINVAL if presented with invalid clockdomain
pointers, -ENOENT if \ ``clkdm2``\  cannot wake up clkdm1 in hardware, or
0 upon success.

.. _`_clkdm_add_sleepdep`:

_clkdm_add_sleepdep
===================

.. c:function:: int _clkdm_add_sleepdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    add a sleep dependency from clkdm2 to clkdm1 (lockless)

    :param struct clockdomain \*clkdm1:
        prevent this struct clockdomain \* from sleeping (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* is active (source)

.. _`_clkdm_add_sleepdep.description`:

Description
-----------

Prevent \ ``clkdm1``\  from automatically going inactive (and then to
retention or off) if \ ``clkdm2``\  is active.  Returns -EINVAL if
presented with invalid clockdomain pointers or called on a machine
that does not support software-configurable hardware sleep
dependencies, -ENOENT if the specified dependency cannot be set in
hardware, or 0 upon success.

.. _`_clkdm_del_sleepdep`:

_clkdm_del_sleepdep
===================

.. c:function:: int _clkdm_del_sleepdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    remove a sleep dep from clkdm2 to clkdm1 (lockless)

    :param struct clockdomain \*clkdm1:
        prevent this struct clockdomain \* from sleeping (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* is active (source)

.. _`_clkdm_del_sleepdep.description`:

Description
-----------

Allow \ ``clkdm1``\  to automatically go inactive (and then to retention or
off), independent of the activity state of \ ``clkdm2``\ .  Returns -EINVAL
if presented with invalid clockdomain pointers or called on a machine
that does not support software-configurable hardware sleep dependencies,
-ENOENT if the specified dependency cannot be cleared in hardware, or
0 upon success.

.. _`clkdm_register_platform_funcs`:

clkdm_register_platform_funcs
=============================

.. c:function:: int clkdm_register_platform_funcs(struct clkdm_ops *co)

    register clockdomain implementation fns

    :param struct clkdm_ops \*co:
        func pointers for arch specific implementations

.. _`clkdm_register_platform_funcs.description`:

Description
-----------

Register the list of function pointers used to implement the
clockdomain functions on different OMAP SoCs.  Should be called
before any other clkdm_register\*() function.  Returns -EINVAL if
\ ``co``\  is null, -EEXIST if platform functions have already been
registered, or 0 upon success.

.. _`clkdm_register_clkdms`:

clkdm_register_clkdms
=====================

.. c:function:: int clkdm_register_clkdms(struct clockdomain **cs)

    register SoC clockdomains

    :param struct clockdomain \*\*cs:
        pointer to an array of struct clockdomain to register

.. _`clkdm_register_clkdms.description`:

Description
-----------

Register the clockdomains available on a particular OMAP SoC.  Must
be called after \ :c:func:`clkdm_register_platform_funcs`\ .  May be called
multiple times.  Returns -EACCES if called before
\ :c:func:`clkdm_register_platform_funcs`\ ; -EINVAL if the argument \ ``cs``\  is
null; or 0 upon success.

.. _`clkdm_register_autodeps`:

clkdm_register_autodeps
=======================

.. c:function:: int clkdm_register_autodeps(struct clkdm_autodep *ia)

    register autodeps (if required)

    :param struct clkdm_autodep \*ia:
        pointer to a static array of struct clkdm_autodep to register

.. _`clkdm_register_autodeps.description`:

Description
-----------

Register clockdomain "automatic dependencies."  These are
clockdomain wakeup and sleep dependencies that are automatically
added whenever the first clock inside a clockdomain is enabled, and
removed whenever the last clock inside a clockdomain is disabled.
These are currently only used on OMAP3 devices, and are deprecated,
since they waste energy.  However, until the OMAP2/3 IP block
enable/disable sequence can be converted to match the OMAP4
sequence, they are needed.

Must be called only after all of the SoC clockdomains are
registered, since the function will resolve autodep clockdomain
names into clockdomain pointers.

The struct clkdm_autodep \ ``ia``\  array must be static, as this function
does not copy the array elements.

Returns -EACCES if called before any clockdomains have been
registered, -EINVAL if called with a null \ ``ia``\  argument, -EEXIST if
autodeps have already been registered, or 0 upon success.

.. _`clkdm_complete_init`:

clkdm_complete_init
===================

.. c:function:: int clkdm_complete_init( void)

    set up the clockdomain layer

    :param  void:
        no arguments

.. _`clkdm_complete_init.description`:

Description
-----------

Put all clockdomains into software-supervised mode; PM code should
later enable hardware-supervised mode as appropriate.  Must be
called after \ :c:func:`clkdm_register_clkdms`\ .  Returns -EACCES if called
before \ :c:func:`clkdm_register_clkdms`\ , or 0 upon success.

.. _`clkdm_lookup`:

clkdm_lookup
============

.. c:function:: struct clockdomain *clkdm_lookup(const char *name)

    look up a clockdomain by name, return a pointer

    :param const char \*name:
        name of clockdomain

.. _`clkdm_lookup.description`:

Description
-----------

Find a registered clockdomain by its name \ ``name``\ .  Returns a pointer
to the struct clockdomain if found, or NULL otherwise.

.. _`clkdm_for_each`:

clkdm_for_each
==============

.. c:function:: int clkdm_for_each(int (*fn)(struct clockdomain *clkdm, void *user), void *user)

    call function on each registered clockdomain

    :param int (\*fn)(struct clockdomain \*clkdm, void \*user):
        callback function \*

    :param void \*user:
        *undescribed*

.. _`clkdm_for_each.description`:

Description
-----------

Call the supplied function \ ``fn``\  for each registered clockdomain.
The callback function \ ``fn``\  can return anything but 0 to bail
out early from the iterator.  The callback function is called with
the clkdm_mutex held, so no clockdomain structure manipulation
functions should be called from the callback, although hardware
clockdomain control functions are fine.  Returns the last return
value of the callback function, which should be 0 for success or
anything else to indicate failure; or -EINVAL if the function pointer
is null.

.. _`clkdm_get_pwrdm`:

clkdm_get_pwrdm
===============

.. c:function:: struct powerdomain *clkdm_get_pwrdm(struct clockdomain *clkdm)

    return a ptr to the pwrdm that this clkdm resides in

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_get_pwrdm.description`:

Description
-----------

Return a pointer to the struct powerdomain that the specified clockdomain
\ ``clkdm``\  exists in, or returns NULL if \ ``clkdm``\  is NULL.

.. _`clkdm_add_wkdep`:

clkdm_add_wkdep
===============

.. c:function:: int clkdm_add_wkdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    add a wakeup dependency from clkdm2 to clkdm1

    :param struct clockdomain \*clkdm1:
        wake this struct clockdomain \* up (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* wakes up (source)

.. _`clkdm_add_wkdep.description`:

Description
-----------

When the clockdomain represented by \ ``clkdm2``\  wakes up, wake up
\ ``clkdm1``\ . Implemented in hardware on the OMAP, this feature is
designed to reduce wakeup latency of the dependent clockdomain \ ``clkdm1``\ .
Returns -EINVAL if presented with invalid clockdomain pointers,
-ENOENT if \ ``clkdm2``\  cannot wake up clkdm1 in hardware, or 0 upon
success.

.. _`clkdm_del_wkdep`:

clkdm_del_wkdep
===============

.. c:function:: int clkdm_del_wkdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    remove a wakeup dependency from clkdm2 to clkdm1

    :param struct clockdomain \*clkdm1:
        wake this struct clockdomain \* up (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* wakes up (source)

.. _`clkdm_del_wkdep.description`:

Description
-----------

Remove a wakeup dependency causing \ ``clkdm1``\  to wake up when \ ``clkdm2``\ 
wakes up.  Returns -EINVAL if presented with invalid clockdomain
pointers, -ENOENT if \ ``clkdm2``\  cannot wake up clkdm1 in hardware, or
0 upon success.

.. _`clkdm_read_wkdep`:

clkdm_read_wkdep
================

.. c:function:: int clkdm_read_wkdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    read wakeup dependency state from clkdm2 to clkdm1

    :param struct clockdomain \*clkdm1:
        wake this struct clockdomain \* up (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* wakes up (source)

.. _`clkdm_read_wkdep.description`:

Description
-----------

Return 1 if a hardware wakeup dependency exists wherein \ ``clkdm1``\  will be
awoken when \ ``clkdm2``\  wakes up; 0 if dependency is not set; -EINVAL
if either clockdomain pointer is invalid; or -ENOENT if the hardware
is incapable.

.. _`clkdm_read_wkdep.revisit`:

REVISIT
-------

Currently this function only represents software-controllable
wakeup dependencies.  Wakeup dependencies fixed in hardware are not
yet handled here.

.. _`clkdm_clear_all_wkdeps`:

clkdm_clear_all_wkdeps
======================

.. c:function:: int clkdm_clear_all_wkdeps(struct clockdomain *clkdm)

    remove all wakeup dependencies from target clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \* to remove all wakeup dependencies from

.. _`clkdm_clear_all_wkdeps.description`:

Description
-----------

Remove all inter-clockdomain wakeup dependencies that could cause
\ ``clkdm``\  to wake.  Intended to be used during boot to initialize the
PRCM to a known state, after all clockdomains are put into swsup idle
and woken up.  Returns -EINVAL if \ ``clkdm``\  pointer is invalid, or
0 upon success.

.. _`clkdm_add_sleepdep`:

clkdm_add_sleepdep
==================

.. c:function:: int clkdm_add_sleepdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    add a sleep dependency from clkdm2 to clkdm1

    :param struct clockdomain \*clkdm1:
        prevent this struct clockdomain \* from sleeping (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* is active (source)

.. _`clkdm_add_sleepdep.description`:

Description
-----------

Prevent \ ``clkdm1``\  from automatically going inactive (and then to
retention or off) if \ ``clkdm2``\  is active.  Returns -EINVAL if
presented with invalid clockdomain pointers or called on a machine
that does not support software-configurable hardware sleep
dependencies, -ENOENT if the specified dependency cannot be set in
hardware, or 0 upon success.

.. _`clkdm_del_sleepdep`:

clkdm_del_sleepdep
==================

.. c:function:: int clkdm_del_sleepdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    remove a sleep dependency from clkdm2 to clkdm1

    :param struct clockdomain \*clkdm1:
        prevent this struct clockdomain \* from sleeping (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* is active (source)

.. _`clkdm_del_sleepdep.description`:

Description
-----------

Allow \ ``clkdm1``\  to automatically go inactive (and then to retention or
off), independent of the activity state of \ ``clkdm2``\ .  Returns -EINVAL
if presented with invalid clockdomain pointers or called on a machine
that does not support software-configurable hardware sleep dependencies,
-ENOENT if the specified dependency cannot be cleared in hardware, or
0 upon success.

.. _`clkdm_read_sleepdep`:

clkdm_read_sleepdep
===================

.. c:function:: int clkdm_read_sleepdep(struct clockdomain *clkdm1, struct clockdomain *clkdm2)

    read sleep dependency state from clkdm2 to clkdm1

    :param struct clockdomain \*clkdm1:
        prevent this struct clockdomain \* from sleeping (dependent)

    :param struct clockdomain \*clkdm2:
        when this struct clockdomain \* is active (source)

.. _`clkdm_read_sleepdep.description`:

Description
-----------

Return 1 if a hardware sleep dependency exists wherein \ ``clkdm1``\  will
not be allowed to automatically go inactive if \ ``clkdm2``\  is active;
0 if \ ``clkdm1``\ 's automatic power state inactivity transition is independent
of \ ``clkdm2``\ 's; -EINVAL if either clockdomain pointer is invalid or called
on a machine that does not support software-configurable hardware sleep
dependencies; or -ENOENT if the hardware is incapable.

.. _`clkdm_read_sleepdep.revisit`:

REVISIT
-------

Currently this function only represents software-controllable
sleep dependencies.  Sleep dependencies fixed in hardware are not
yet handled here.

.. _`clkdm_clear_all_sleepdeps`:

clkdm_clear_all_sleepdeps
=========================

.. c:function:: int clkdm_clear_all_sleepdeps(struct clockdomain *clkdm)

    remove all sleep dependencies from target clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \* to remove all sleep dependencies from

.. _`clkdm_clear_all_sleepdeps.description`:

Description
-----------

Remove all inter-clockdomain sleep dependencies that could prevent
\ ``clkdm``\  from idling.  Intended to be used during boot to initialize the
PRCM to a known state, after all clockdomains are put into swsup idle
and woken up.  Returns -EINVAL if \ ``clkdm``\  pointer is invalid, or
0 upon success.

.. _`clkdm_sleep_nolock`:

clkdm_sleep_nolock
==================

.. c:function:: int clkdm_sleep_nolock(struct clockdomain *clkdm)

    force clockdomain sleep transition (lockless)

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_sleep_nolock.description`:

Description
-----------

Instruct the CM to force a sleep transition on the specified
clockdomain \ ``clkdm``\ .  Only for use by the powerdomain code.  Returns
-EINVAL if \ ``clkdm``\  is NULL or if clockdomain does not support
software-initiated sleep; 0 upon success.

.. _`clkdm_sleep`:

clkdm_sleep
===========

.. c:function:: int clkdm_sleep(struct clockdomain *clkdm)

    force clockdomain sleep transition

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_sleep.description`:

Description
-----------

Instruct the CM to force a sleep transition on the specified
clockdomain \ ``clkdm``\ .  Returns -EINVAL if \ ``clkdm``\  is NULL or if
clockdomain does not support software-initiated sleep; 0 upon
success.

.. _`clkdm_wakeup_nolock`:

clkdm_wakeup_nolock
===================

.. c:function:: int clkdm_wakeup_nolock(struct clockdomain *clkdm)

    force clockdomain wakeup transition (lockless)

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_wakeup_nolock.description`:

Description
-----------

Instruct the CM to force a wakeup transition on the specified
clockdomain \ ``clkdm``\ .  Only for use by the powerdomain code.  Returns
-EINVAL if \ ``clkdm``\  is NULL or if the clockdomain does not support
software-controlled wakeup; 0 upon success.

.. _`clkdm_wakeup`:

clkdm_wakeup
============

.. c:function:: int clkdm_wakeup(struct clockdomain *clkdm)

    force clockdomain wakeup transition

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_wakeup.description`:

Description
-----------

Instruct the CM to force a wakeup transition on the specified
clockdomain \ ``clkdm``\ .  Returns -EINVAL if \ ``clkdm``\  is NULL or if the
clockdomain does not support software-controlled wakeup; 0 upon
success.

.. _`clkdm_allow_idle_nolock`:

clkdm_allow_idle_nolock
=======================

.. c:function:: void clkdm_allow_idle_nolock(struct clockdomain *clkdm)

    enable hwsup idle transitions for clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_allow_idle_nolock.description`:

Description
-----------

Allow the hardware to automatically switch the clockdomain \ ``clkdm``\ 
into active or idle states, as needed by downstream clocks.  If the
clockdomain has any downstream clocks enabled in the clock
framework, wkdep/sleepdep autodependencies are added; this is so
device drivers can read and write to the device.  Only for use by
the powerdomain code.  No return value.

.. _`clkdm_allow_idle`:

clkdm_allow_idle
================

.. c:function:: void clkdm_allow_idle(struct clockdomain *clkdm)

    enable hwsup idle transitions for clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_allow_idle.description`:

Description
-----------

Allow the hardware to automatically switch the clockdomain \ ``clkdm``\  into
active or idle states, as needed by downstream clocks.  If the
clockdomain has any downstream clocks enabled in the clock
framework, wkdep/sleepdep autodependencies are added; this is so
device drivers can read and write to the device.  No return value.

.. _`clkdm_deny_idle_nolock`:

clkdm_deny_idle_nolock
======================

.. c:function:: void clkdm_deny_idle_nolock(struct clockdomain *clkdm)

    disable hwsup idle transitions for clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_deny_idle_nolock.description`:

Description
-----------

Prevent the hardware from automatically switching the clockdomain
\ ``clkdm``\  into inactive or idle states.  If the clockdomain has
downstream clocks enabled in the clock framework, wkdep/sleepdep
autodependencies are removed.  Only for use by the powerdomain
code.  No return value.

.. _`clkdm_deny_idle`:

clkdm_deny_idle
===============

.. c:function:: void clkdm_deny_idle(struct clockdomain *clkdm)

    disable hwsup idle transitions for clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_deny_idle.description`:

Description
-----------

Prevent the hardware from automatically switching the clockdomain
\ ``clkdm``\  into inactive or idle states.  If the clockdomain has
downstream clocks enabled in the clock framework, wkdep/sleepdep
autodependencies are removed.  No return value.

.. _`clkdm_in_hwsup`:

clkdm_in_hwsup
==============

.. c:function:: bool clkdm_in_hwsup(struct clockdomain *clkdm)

    is clockdomain \ ``clkdm``\  have hardware-supervised idle enabled?

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_in_hwsup.description`:

Description
-----------

Returns true if clockdomain \ ``clkdm``\  currently has
hardware-supervised idle enabled, or false if it does not or if
\ ``clkdm``\  is NULL.  It is only valid to call this function after
\ :c:func:`clkdm_init`\  has been called.  This function does not actually read
bits from the hardware; it instead tests an in-memory flag that is
changed whenever the clockdomain code changes the auto-idle mode.

.. _`clkdm_missing_idle_reporting`:

clkdm_missing_idle_reporting
============================

.. c:function:: bool clkdm_missing_idle_reporting(struct clockdomain *clkdm)

    can \ ``clkdm``\  enter autoidle even if in use?

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_missing_idle_reporting.description`:

Description
-----------

Returns true if clockdomain \ ``clkdm``\  has the
CLKDM_MISSING_IDLE_REPORTING flag set, or false if not or \ ``clkdm``\  is
null.  More information is available in the documentation for the
CLKDM_MISSING_IDLE_REPORTING macro.

.. _`clkdm_add_autodeps`:

clkdm_add_autodeps
==================

.. c:function:: void clkdm_add_autodeps(struct clockdomain *clkdm)

    add auto sleepdeps/wkdeps to clkdm upon clock enable

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_add_autodeps.description`:

Description
-----------

Add the "autodep" sleep & wakeup dependencies to clockdomain 'clkdm'
in hardware-supervised mode.  Meant to be called from clock framework
when a clock inside clockdomain 'clkdm' is enabled.  No return value.

XXX autodeps are deprecated and should be removed at the earliest
opportunity

.. _`clkdm_del_autodeps`:

clkdm_del_autodeps
==================

.. c:function:: void clkdm_del_autodeps(struct clockdomain *clkdm)

    remove auto sleepdeps/wkdeps from clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

.. _`clkdm_del_autodeps.description`:

Description
-----------

Remove the "autodep" sleep & wakeup dependencies from clockdomain 'clkdm'
in hardware-supervised mode.  Meant to be called from clock framework
when a clock inside clockdomain 'clkdm' is disabled.  No return value.

XXX autodeps are deprecated and should be removed at the earliest
opportunity

.. _`clkdm_clk_enable`:

clkdm_clk_enable
================

.. c:function:: int clkdm_clk_enable(struct clockdomain *clkdm, struct clk *clk)

    add an enabled downstream clock to this clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

    :param struct clk \*clk:
        struct clk \* of the enabled downstream clock

.. _`clkdm_clk_enable.description`:

Description
-----------

Increment the usecount of the clockdomain \ ``clkdm``\  and ensure that it
is awake before \ ``clk``\  is enabled.  Intended to be called by
\ :c:func:`clk_enable`\  code.  If the clockdomain is in software-supervised
idle mode, force the clockdomain to wake.  If the clockdomain is in
hardware-supervised idle mode, add clkdm-pwrdm autodependencies, to
ensure that devices in the clockdomain can be read from/written to
by on-chip processors.  Returns -EINVAL if passed null pointers;
returns 0 upon success or if the clockdomain is in hwsup idle mode.

.. _`clkdm_clk_disable`:

clkdm_clk_disable
=================

.. c:function:: int clkdm_clk_disable(struct clockdomain *clkdm, struct clk *clk)

    remove an enabled downstream clock from this clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

    :param struct clk \*clk:
        struct clk \* of the disabled downstream clock

.. _`clkdm_clk_disable.description`:

Description
-----------

Decrement the usecount of this clockdomain \ ``clkdm``\  when \ ``clk``\  is
disabled.  Intended to be called by \ :c:func:`clk_disable`\  code.  If the
clockdomain usecount goes to 0, put the clockdomain to sleep
(software-supervised mode) or remove the clkdm autodependencies
(hardware-supervised mode).  Returns -EINVAL if passed null
pointers; -ERANGE if the \ ``clkdm``\  usecount underflows; or returns 0
upon success or if the clockdomain is in hwsup idle mode.

.. _`clkdm_hwmod_enable`:

clkdm_hwmod_enable
==================

.. c:function:: int clkdm_hwmod_enable(struct clockdomain *clkdm, struct omap_hwmod *oh)

    add an enabled downstream hwmod to this clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* of the enabled downstream hwmod

.. _`clkdm_hwmod_enable.description`:

Description
-----------

Increment the usecount of the clockdomain \ ``clkdm``\  and ensure that it
is awake before \ ``oh``\  is enabled. Intended to be called by
\ :c:func:`module_enable`\  code.
If the clockdomain is in software-supervised idle mode, force the
clockdomain to wake.  If the clockdomain is in hardware-supervised idle
mode, add clkdm-pwrdm autodependencies, to ensure that devices in the
clockdomain can be read from/written to by on-chip processors.
Returns -EINVAL if passed null pointers;
returns 0 upon success or if the clockdomain is in hwsup idle mode.

.. _`clkdm_hwmod_disable`:

clkdm_hwmod_disable
===================

.. c:function:: int clkdm_hwmod_disable(struct clockdomain *clkdm, struct omap_hwmod *oh)

    remove an enabled downstream hwmod from this clkdm

    :param struct clockdomain \*clkdm:
        struct clockdomain \*

    :param struct omap_hwmod \*oh:
        struct omap_hwmod \* of the disabled downstream hwmod

.. _`clkdm_hwmod_disable.description`:

Description
-----------

Decrement the usecount of this clockdomain \ ``clkdm``\  when \ ``oh``\  is
disabled. Intended to be called by \ :c:func:`module_disable`\  code.
If the clockdomain usecount goes to 0, put the clockdomain to sleep
(software-supervised mode) or remove the clkdm autodependencies
(hardware-supervised mode).
Returns -EINVAL if passed null pointers; -ERANGE if the \ ``clkdm``\  usecount
underflows; or returns 0 upon success or if the clockdomain is in hwsup
idle mode.

.. This file was automatic generated / don't edit.

