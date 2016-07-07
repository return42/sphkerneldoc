.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/opp/core.c

.. _`_find_opp_table`:

_find_opp_table
===============

.. c:function:: struct opp_table *_find_opp_table(struct device *dev)

    find opp_table struct using device pointer

    :param struct device \*dev:
        device pointer used to lookup OPP table

.. _`_find_opp_table.description`:

Description
-----------

Search OPP table for one containing matching device. Does a RCU reader
operation to grab the pointer needed.

.. _`_find_opp_table.return`:

Return
------

pointer to 'struct opp_table' if found, otherwise -ENODEV or
-EINVAL based on type of error.

.. _`_find_opp_table.locking`:

Locking
-------

For readers, this function must be called under \ :c:func:`rcu_read_lock`\ .
opp_table is a RCU protected pointer, which means that opp_table is valid
as long as we are under RCU lock.

For Writers, this function must be called with opp_table_lock held.

.. _`dev_pm_opp_get_voltage`:

dev_pm_opp_get_voltage
======================

.. c:function:: unsigned long dev_pm_opp_get_voltage(struct dev_pm_opp *opp)

    Gets the voltage corresponding to an opp

    :param struct dev_pm_opp \*opp:
        opp for which voltage has to be returned for

.. _`dev_pm_opp_get_voltage.return`:

Return
------

voltage in micro volt corresponding to the opp, else
return 0

.. _`dev_pm_opp_get_voltage.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. This means that opp which could have been fetched by
opp_find_freq_{exact,ceil,floor} functions is valid as long as we are
under RCU lock. The pointer returned by the opp_find_freq family must be
used in the same section as the usage of this function with the pointer
prior to unlocking with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the
pointer.

.. _`dev_pm_opp_get_freq`:

dev_pm_opp_get_freq
===================

.. c:function:: unsigned long dev_pm_opp_get_freq(struct dev_pm_opp *opp)

    Gets the frequency corresponding to an available opp

    :param struct dev_pm_opp \*opp:
        opp for which frequency has to be returned for

.. _`dev_pm_opp_get_freq.return`:

Return
------

frequency in hertz corresponding to the opp, else
return 0

.. _`dev_pm_opp_get_freq.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. This means that opp which could have been fetched by
opp_find_freq_{exact,ceil,floor} functions is valid as long as we are
under RCU lock. The pointer returned by the opp_find_freq family must be
used in the same section as the usage of this function with the pointer
prior to unlocking with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the
pointer.

.. _`dev_pm_opp_is_turbo`:

dev_pm_opp_is_turbo
===================

.. c:function:: bool dev_pm_opp_is_turbo(struct dev_pm_opp *opp)

    Returns if opp is turbo OPP or not

    :param struct dev_pm_opp \*opp:
        opp for which turbo mode is being verified

.. _`dev_pm_opp_is_turbo.description`:

Description
-----------

Turbo OPPs are not for normal use, and can be enabled (under certain
conditions) for short duration of times to finish high throughput work
quickly. Running on them for longer times may overheat the chip.

.. _`dev_pm_opp_is_turbo.return`:

Return
------

true if opp is turbo opp, else false.

.. _`dev_pm_opp_is_turbo.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. This means that opp which could have been fetched by
opp_find_freq_{exact,ceil,floor} functions is valid as long as we are
under RCU lock. The pointer returned by the opp_find_freq family must be
used in the same section as the usage of this function with the pointer
prior to unlocking with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the
pointer.

.. _`dev_pm_opp_get_max_clock_latency`:

dev_pm_opp_get_max_clock_latency
================================

.. c:function:: unsigned long dev_pm_opp_get_max_clock_latency(struct device *dev)

    Get max clock latency in nanoseconds

    :param struct device \*dev:
        device for which we do this operation

.. _`dev_pm_opp_get_max_clock_latency.return`:

Return
------

This function returns the max clock latency in nanoseconds.

.. _`dev_pm_opp_get_max_clock_latency.locking`:

Locking
-------

This function takes \ :c:func:`rcu_read_lock`\ .

.. _`dev_pm_opp_get_max_volt_latency`:

dev_pm_opp_get_max_volt_latency
===============================

.. c:function:: unsigned long dev_pm_opp_get_max_volt_latency(struct device *dev)

    Get max voltage latency in nanoseconds

    :param struct device \*dev:
        device for which we do this operation

.. _`dev_pm_opp_get_max_volt_latency.return`:

Return
------

This function returns the max voltage latency in nanoseconds.

.. _`dev_pm_opp_get_max_volt_latency.locking`:

Locking
-------

This function takes \ :c:func:`rcu_read_lock`\ .

.. _`dev_pm_opp_get_max_transition_latency`:

dev_pm_opp_get_max_transition_latency
=====================================

.. c:function:: unsigned long dev_pm_opp_get_max_transition_latency(struct device *dev)

    Get max transition latency in nanoseconds

    :param struct device \*dev:
        device for which we do this operation

.. _`dev_pm_opp_get_max_transition_latency.return`:

Return
------

This function returns the max transition latency, in nanoseconds, to
switch from one OPP to other.

.. _`dev_pm_opp_get_max_transition_latency.locking`:

Locking
-------

This function takes \ :c:func:`rcu_read_lock`\ .

.. _`dev_pm_opp_get_suspend_opp`:

dev_pm_opp_get_suspend_opp
==========================

.. c:function:: struct dev_pm_opp *dev_pm_opp_get_suspend_opp(struct device *dev)

    Get suspend opp

    :param struct device \*dev:
        device for which we do this operation

.. _`dev_pm_opp_get_suspend_opp.return`:

Return
------

This function returns pointer to the suspend opp if it is
defined and available, otherwise it returns NULL.

.. _`dev_pm_opp_get_suspend_opp.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. The reason for the same is that the opp pointer which is
returned will remain valid for use with opp_get_{voltage, freq} only while
under the locked area. The pointer returned must be used prior to unlocking
with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the pointer.

.. _`dev_pm_opp_get_opp_count`:

dev_pm_opp_get_opp_count
========================

.. c:function:: int dev_pm_opp_get_opp_count(struct device *dev)

    Get number of opps available in the opp table

    :param struct device \*dev:
        device for which we do this operation

.. _`dev_pm_opp_get_opp_count.return`:

Return
------

This function returns the number of available opps if there are any,
else returns 0 if none or the corresponding error value.

.. _`dev_pm_opp_get_opp_count.locking`:

Locking
-------

This function takes \ :c:func:`rcu_read_lock`\ .

.. _`dev_pm_opp_find_freq_exact`:

dev_pm_opp_find_freq_exact
==========================

.. c:function:: struct dev_pm_opp *dev_pm_opp_find_freq_exact(struct device *dev, unsigned long freq, bool available)

    search for an exact frequency

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        frequency to search for

    :param bool available:
        true/false - match for available opp

.. _`dev_pm_opp_find_freq_exact.return`:

Return
------

Searches for exact match in the opp table and returns pointer to the
matching opp if found, else returns ERR_PTR in case of error and should
be handled using IS_ERR. Error return values can be:

.. _`dev_pm_opp_find_freq_exact.einval`:

EINVAL
------

for bad pointer

.. _`dev_pm_opp_find_freq_exact.erange`:

ERANGE
------

no match found for search

.. _`dev_pm_opp_find_freq_exact.enodev`:

ENODEV
------

if device not found in list of registered devices

.. _`dev_pm_opp_find_freq_exact.note`:

Note
----

available is a modifier for the search. if available=true, then the
match is for exact matching frequency and is available in the stored OPP
table. if false, the match is for exact frequency which is not available.

This provides a mechanism to enable an opp which is not available currently
or the opposite as well.

.. _`dev_pm_opp_find_freq_exact.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. The reason for the same is that the opp pointer which is
returned will remain valid for use with opp_get_{voltage, freq} only while
under the locked area. The pointer returned must be used prior to unlocking
with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the pointer.

.. _`dev_pm_opp_find_freq_ceil`:

dev_pm_opp_find_freq_ceil
=========================

.. c:function:: struct dev_pm_opp *dev_pm_opp_find_freq_ceil(struct device *dev, unsigned long *freq)

    Search for an rounded ceil freq

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long \*freq:
        Start frequency

.. _`dev_pm_opp_find_freq_ceil.description`:

Description
-----------

Search for the matching ceil \*available\* OPP from a starting freq
for a device.

.. _`dev_pm_opp_find_freq_ceil.return`:

Return
------

matching \*opp and refreshes \*freq accordingly, else returns
ERR_PTR in case of error and should be handled using IS_ERR. Error return

.. _`dev_pm_opp_find_freq_ceil.einval`:

EINVAL
------

for bad pointer

.. _`dev_pm_opp_find_freq_ceil.erange`:

ERANGE
------

no match found for search

.. _`dev_pm_opp_find_freq_ceil.enodev`:

ENODEV
------

if device not found in list of registered devices

.. _`dev_pm_opp_find_freq_ceil.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. The reason for the same is that the opp pointer which is
returned will remain valid for use with opp_get_{voltage, freq} only while
under the locked area. The pointer returned must be used prior to unlocking
with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the pointer.

.. _`dev_pm_opp_find_freq_floor`:

dev_pm_opp_find_freq_floor
==========================

.. c:function:: struct dev_pm_opp *dev_pm_opp_find_freq_floor(struct device *dev, unsigned long *freq)

    Search for a rounded floor freq

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long \*freq:
        Start frequency

.. _`dev_pm_opp_find_freq_floor.description`:

Description
-----------

Search for the matching floor \*available\* OPP from a starting freq
for a device.

.. _`dev_pm_opp_find_freq_floor.return`:

Return
------

matching \*opp and refreshes \*freq accordingly, else returns
ERR_PTR in case of error and should be handled using IS_ERR. Error return

.. _`dev_pm_opp_find_freq_floor.einval`:

EINVAL
------

for bad pointer

.. _`dev_pm_opp_find_freq_floor.erange`:

ERANGE
------

no match found for search

.. _`dev_pm_opp_find_freq_floor.enodev`:

ENODEV
------

if device not found in list of registered devices

.. _`dev_pm_opp_find_freq_floor.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp is a rcu
protected pointer. The reason for the same is that the opp pointer which is
returned will remain valid for use with opp_get_{voltage, freq} only while
under the locked area. The pointer returned must be used prior to unlocking
with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the pointer.

.. _`dev_pm_opp_set_rate`:

dev_pm_opp_set_rate
===================

.. c:function:: int dev_pm_opp_set_rate(struct device *dev, unsigned long target_freq)

    Configure new OPP based on frequency

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long target_freq:
        frequency to achieve

.. _`dev_pm_opp_set_rate.description`:

Description
-----------

This configures the power-supplies and clock source to the levels specified
by the OPP corresponding to the target_freq.

.. _`dev_pm_opp_set_rate.locking`:

Locking
-------

This function takes \ :c:func:`rcu_read_lock`\ .

.. _`_add_opp_table`:

_add_opp_table
==============

.. c:function:: struct opp_table *_add_opp_table(struct device *dev)

    Find OPP table or allocate a new one

    :param struct device \*dev:
        device for which we do this operation

.. _`_add_opp_table.description`:

Description
-----------

It tries to find an existing table first, if it couldn't find one, it
allocates a new OPP table and returns that.

.. _`_add_opp_table.return`:

Return
------

valid opp_table pointer if success, else NULL.

.. _`_kfree_device_rcu`:

_kfree_device_rcu
=================

.. c:function:: void _kfree_device_rcu(struct rcu_head *head)

    Free opp_table RCU handler

    :param struct rcu_head \*head:
        RCU head

.. _`_remove_opp_table`:

_remove_opp_table
=================

.. c:function:: void _remove_opp_table(struct opp_table *opp_table)

    Removes a OPP table

    :param struct opp_table \*opp_table:
        OPP table to be removed.

.. _`_remove_opp_table.description`:

Description
-----------

Removes/frees OPP table if it doesn't contain any OPPs.

.. _`_kfree_opp_rcu`:

_kfree_opp_rcu
==============

.. c:function:: void _kfree_opp_rcu(struct rcu_head *head)

    Free OPP RCU handler

    :param struct rcu_head \*head:
        RCU head

.. _`_opp_remove`:

_opp_remove
===========

.. c:function:: void _opp_remove(struct opp_table *opp_table, struct dev_pm_opp *opp, bool notify)

    Remove an OPP from a table definition

    :param struct opp_table \*opp_table:
        points back to the opp_table struct this opp belongs to

    :param struct dev_pm_opp \*opp:
        pointer to the OPP to remove

    :param bool notify:
        OPP_EVENT_REMOVE notification should be sent or not

.. _`_opp_remove.description`:

Description
-----------

This function removes an opp definition from the opp table.

.. _`_opp_remove.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
It is assumed that the caller holds required mutex for an RCU updater
strategy.

.. _`dev_pm_opp_remove`:

dev_pm_opp_remove
=================

.. c:function:: void dev_pm_opp_remove(struct device *dev, unsigned long freq)

    Remove an OPP from OPP table

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        OPP to remove with matching 'freq'

.. _`dev_pm_opp_remove.description`:

Description
-----------

This function removes an opp from the opp table.

.. _`dev_pm_opp_remove.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`_opp_add_v1`:

_opp_add_v1
===========

.. c:function:: int _opp_add_v1(struct device *dev, unsigned long freq, long u_volt, bool dynamic)

    Allocate a OPP based on v1 bindings.

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        Frequency in Hz for this OPP

    :param long u_volt:
        Voltage in uVolts for this OPP

    :param bool dynamic:
        Dynamically added OPPs.

.. _`_opp_add_v1.description`:

Description
-----------

This function adds an opp definition to the opp table and returns status.
The opp is made available by default and it can be controlled using
dev_pm_opp_enable/disable functions and may be removed by dev_pm_opp_remove.

.. _`_opp_add_v1.note`:

NOTE
----

"dynamic" parameter impacts OPPs added by the dev_pm_opp_of_add_table
and freed by dev_pm_opp_of_remove_table.

.. _`_opp_add_v1.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`_opp_add_v1.return`:

Return
------

0            On success OR
Duplicate OPPs (both freq and volt are same) and opp->available
-EEXIST      Freq are same and volt are different OR
Duplicate OPPs (both freq and volt are same) and !opp->available
-ENOMEM      Memory allocation failure

.. _`dev_pm_opp_set_supported_hw`:

dev_pm_opp_set_supported_hw
===========================

.. c:function:: int dev_pm_opp_set_supported_hw(struct device *dev, const u32 *versions, unsigned int count)

    Set supported platforms

    :param struct device \*dev:
        Device for which supported-hw has to be set.

    :param const u32 \*versions:
        Array of hierarchy of versions to match.

    :param unsigned int count:
        Number of elements in the array.

.. _`dev_pm_opp_set_supported_hw.description`:

Description
-----------

This is required only for the V2 bindings, and it enables a platform to
specify the hierarchy of versions it supports. OPP layer will then enable
OPPs, which are available for those versions, based on its 'opp-supported-hw'
property.

.. _`dev_pm_opp_set_supported_hw.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_put_supported_hw`:

dev_pm_opp_put_supported_hw
===========================

.. c:function:: void dev_pm_opp_put_supported_hw(struct device *dev)

    Releases resources blocked for supported hw

    :param struct device \*dev:
        Device for which supported-hw has to be put.

.. _`dev_pm_opp_put_supported_hw.description`:

Description
-----------

This is required only for the V2 bindings, and is called for a matching
\ :c:func:`dev_pm_opp_set_supported_hw`\ . Until this is called, the opp_table structure
will not be freed.

.. _`dev_pm_opp_put_supported_hw.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_set_prop_name`:

dev_pm_opp_set_prop_name
========================

.. c:function:: int dev_pm_opp_set_prop_name(struct device *dev, const char *name)

    Set prop-extn name

    :param struct device \*dev:
        Device for which the prop-name has to be set.

    :param const char \*name:
        name to postfix to properties.

.. _`dev_pm_opp_set_prop_name.description`:

Description
-----------

This is required only for the V2 bindings, and it enables a platform to
specify the extn to be used for certain property names. The properties to
which the extension will apply are opp-microvolt and opp-microamp. OPP core
should postfix the property name with -<name> while looking for them.

.. _`dev_pm_opp_set_prop_name.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_put_prop_name`:

dev_pm_opp_put_prop_name
========================

.. c:function:: void dev_pm_opp_put_prop_name(struct device *dev)

    Releases resources blocked for prop-name

    :param struct device \*dev:
        Device for which the prop-name has to be put.

.. _`dev_pm_opp_put_prop_name.description`:

Description
-----------

This is required only for the V2 bindings, and is called for a matching
\ :c:func:`dev_pm_opp_set_prop_name`\ . Until this is called, the opp_table structure
will not be freed.

.. _`dev_pm_opp_put_prop_name.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_set_regulator`:

dev_pm_opp_set_regulator
========================

.. c:function:: int dev_pm_opp_set_regulator(struct device *dev, const char *name)

    Set regulator name for the device

    :param struct device \*dev:
        Device for which regulator name is being set.

    :param const char \*name:
        Name of the regulator.

.. _`dev_pm_opp_set_regulator.description`:

Description
-----------

In order to support OPP switching, OPP layer needs to know the name of the
device's regulator, as the core would be required to switch voltages as well.

This must be called before any OPPs are initialized for the device.

.. _`dev_pm_opp_set_regulator.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_put_regulator`:

dev_pm_opp_put_regulator
========================

.. c:function:: void dev_pm_opp_put_regulator(struct device *dev)

    Releases resources blocked for regulator

    :param struct device \*dev:
        Device for which regulator was set.

.. _`dev_pm_opp_put_regulator.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_add`:

dev_pm_opp_add
==============

.. c:function:: int dev_pm_opp_add(struct device *dev, unsigned long freq, unsigned long u_volt)

    Add an OPP table from a table definitions

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        Frequency in Hz for this OPP

    :param unsigned long u_volt:
        Voltage in uVolts for this OPP

.. _`dev_pm_opp_add.description`:

Description
-----------

This function adds an opp definition to the opp table and returns status.
The opp is made available by default and it can be controlled using
dev_pm_opp_enable/disable functions.

.. _`dev_pm_opp_add.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. _`dev_pm_opp_add.return`:

Return
------

0            On success OR
Duplicate OPPs (both freq and volt are same) and opp->available
-EEXIST      Freq are same and volt are different OR
Duplicate OPPs (both freq and volt are same) and !opp->available
-ENOMEM      Memory allocation failure

.. _`_opp_set_availability`:

_opp_set_availability
=====================

.. c:function:: int _opp_set_availability(struct device *dev, unsigned long freq, bool availability_req)

    helper to set the availability of an opp

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        OPP frequency to modify availability

    :param bool availability_req:
        availability status requested for this opp

.. _`_opp_set_availability.description`:

Description
-----------

Set the availability of an OPP with an RCU operation, opp_{enable,disable}
share a common logic which is isolated here.

.. _`_opp_set_availability.return`:

Return
------

-EINVAL for bad pointers, -ENOMEM if no memory available for the
copy operation, returns 0 if no modification was done OR modification was
successful.

.. _`_opp_set_availability.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function internally uses RCU updater strategy with mutex locks to
keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex locking or \ :c:func:`synchronize_rcu`\  blocking calls cannot be used.

.. _`dev_pm_opp_enable`:

dev_pm_opp_enable
=================

.. c:function:: int dev_pm_opp_enable(struct device *dev, unsigned long freq)

    Enable a specific OPP

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        OPP frequency to enable

.. _`dev_pm_opp_enable.description`:

Description
-----------

Enables a provided opp. If the operation is valid, this returns 0, else the
corresponding error value. It is meant to be used for users an OPP available
after being temporarily made unavailable with dev_pm_opp_disable.

.. _`dev_pm_opp_enable.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function indirectly uses RCU and mutex locks to keep the
integrity of the internal data structures. Callers should ensure that
this function is \*NOT\* called under RCU protection or in contexts where
mutex locking or \ :c:func:`synchronize_rcu`\  blocking calls cannot be used.

.. _`dev_pm_opp_enable.return`:

Return
------

-EINVAL for bad pointers, -ENOMEM if no memory available for the
copy operation, returns 0 if no modification was done OR modification was
successful.

.. _`dev_pm_opp_disable`:

dev_pm_opp_disable
==================

.. c:function:: int dev_pm_opp_disable(struct device *dev, unsigned long freq)

    Disable a specific OPP

    :param struct device \*dev:
        device for which we do this operation

    :param unsigned long freq:
        OPP frequency to disable

.. _`dev_pm_opp_disable.description`:

Description
-----------

Disables a provided opp. If the operation is valid, this returns
0, else the corresponding error value. It is meant to be a temporary
control by users to make this OPP not available until the circumstances are
right to make it available again (with a call to dev_pm_opp_enable).

.. _`dev_pm_opp_disable.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function indirectly uses RCU and mutex locks to keep the
integrity of the internal data structures. Callers should ensure that
this function is \*NOT\* called under RCU protection or in contexts where
mutex locking or \ :c:func:`synchronize_rcu`\  blocking calls cannot be used.

.. _`dev_pm_opp_disable.return`:

Return
------

-EINVAL for bad pointers, -ENOMEM if no memory available for the
copy operation, returns 0 if no modification was done OR modification was
successful.

.. _`dev_pm_opp_get_notifier`:

dev_pm_opp_get_notifier
=======================

.. c:function:: struct srcu_notifier_head *dev_pm_opp_get_notifier(struct device *dev)

    find notifier_head of the device with opp

    :param struct device \*dev:
        device pointer used to lookup OPP table.

.. _`dev_pm_opp_get_notifier.return`:

Return
------

pointer to  notifier head if found, otherwise -ENODEV or
-EINVAL based on type of error casted as pointer. value must be checked
with IS_ERR to determine valid pointer or error result.

.. _`dev_pm_opp_get_notifier.locking`:

Locking
-------

This function must be called under \ :c:func:`rcu_read_lock`\ . opp_table is a
RCU protected pointer. The reason for the same is that the opp pointer which
is returned will remain valid for use with opp_get_{voltage, freq} only while
under the locked area. The pointer returned must be used prior to unlocking
with \ :c:func:`rcu_read_unlock`\  to maintain the integrity of the pointer.

.. _`dev_pm_opp_remove_table`:

dev_pm_opp_remove_table
=======================

.. c:function:: void dev_pm_opp_remove_table(struct device *dev)

    Free all OPPs associated with the device

    :param struct device \*dev:
        device pointer used to lookup OPP table.

.. _`dev_pm_opp_remove_table.description`:

Description
-----------

Free both OPPs created using static entries present in DT and the
dynamically added entries.

.. _`dev_pm_opp_remove_table.locking`:

Locking
-------

The internal opp_table and opp structures are RCU protected.
Hence this function indirectly uses RCU updater strategy with mutex locks
to keep the integrity of the internal data structures. Callers should ensure
that this function is \*NOT\* called under RCU protection or in contexts where
mutex cannot be locked.

.. This file was automatic generated / don't edit.

