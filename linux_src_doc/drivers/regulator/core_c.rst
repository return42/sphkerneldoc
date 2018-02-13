.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/core.c

.. _`regulator_lock_supply`:

regulator_lock_supply
=====================

.. c:function:: void regulator_lock_supply(struct regulator_dev *rdev)

    lock a regulator and its supplies

    :param struct regulator_dev \*rdev:
        regulator source

.. _`regulator_unlock_supply`:

regulator_unlock_supply
=======================

.. c:function:: void regulator_unlock_supply(struct regulator_dev *rdev)

    unlock a regulator and its supplies

    :param struct regulator_dev \*rdev:
        regulator source

.. _`of_get_regulator`:

of_get_regulator
================

.. c:function:: struct device_node *of_get_regulator(struct device *dev, const char *supply)

    get a regulator device node based on supply name

    :param struct device \*dev:
        Device pointer for the consumer (of regulator) device

    :param const char \*supply:
        regulator supply name

.. _`of_get_regulator.description`:

Description
-----------

Extract the regulator device node corresponding to the supply name.
returns the device node corresponding to the regulator if found, else
returns NULL.

.. _`set_machine_constraints`:

set_machine_constraints
=======================

.. c:function:: int set_machine_constraints(struct regulator_dev *rdev, const struct regulation_constraints *constraints)

    sets regulator constraints

    :param struct regulator_dev \*rdev:
        regulator source

    :param const struct regulation_constraints \*constraints:
        constraints to apply

.. _`set_machine_constraints.description`:

Description
-----------

Allows platform initialisation code to define and constrain
regulator circuits e.g. valid voltage/current ranges, etc.  NOTE:
Constraints *must* be set by platform code in order for some
regulator operations to proceed i.e. set_voltage, set_current_limit,
set_mode.

.. _`set_supply`:

set_supply
==========

.. c:function:: int set_supply(struct regulator_dev *rdev, struct regulator_dev *supply_rdev)

    set regulator supply regulator

    :param struct regulator_dev \*rdev:
        regulator name

    :param struct regulator_dev \*supply_rdev:
        supply regulator name

.. _`set_supply.description`:

Description
-----------

Called by platform initialisation code to set the supply regulator for this
regulator. This ensures that a regulators supply will also be enabled by the
core if it's child is enabled.

.. _`set_consumer_device_supply`:

set_consumer_device_supply
==========================

.. c:function:: int set_consumer_device_supply(struct regulator_dev *rdev, const char *consumer_dev_name, const char *supply)

    Bind a regulator to a symbolic supply

    :param struct regulator_dev \*rdev:
        regulator source

    :param const char \*consumer_dev_name:
        \ :c:func:`dev_name`\  string for device supply applies to

    :param const char \*supply:
        symbolic name for supply

.. _`set_consumer_device_supply.description`:

Description
-----------

Allows platform initialisation code to map physical regulator
sources to symbolic names for supplies for use by devices.  Devices
should use these symbolic names to request regulators, avoiding the
need to provide board-specific regulator names as platform data.

.. _`regulator_dev_lookup`:

regulator_dev_lookup
====================

.. c:function:: struct regulator_dev *regulator_dev_lookup(struct device *dev, const char *supply)

    lookup a regulator device.

    :param struct device \*dev:
        device for regulator "consumer".

    :param const char \*supply:
        Supply name or regulator ID.

.. _`regulator_dev_lookup.description`:

Description
-----------

If successful, returns a struct regulator_dev that corresponds to the name
\ ``supply``\  and with the embedded struct device refcount incremented by one.
The refcount must be dropped by calling \ :c:func:`put_device`\ .
On failure one of the following ERR-PTR-encoded values is returned:
-ENODEV if lookup fails permanently, -EPROBE_DEFER if lookup could succeed
in the future.

.. _`regulator_get`:

regulator_get
=============

.. c:function:: struct regulator *regulator_get(struct device *dev, const char *id)

    lookup and obtain a reference to a regulator.

    :param struct device \*dev:
        device for regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID.

.. _`regulator_get.description`:

Description
-----------

Returns a struct regulator corresponding to the regulator producer,
or \ :c:func:`IS_ERR`\  condition containing errno.

Use of supply names configured via \ :c:func:`regulator_set_device_supply`\  is
strongly encouraged.  It is recommended that the supply name used
should match the name used for the supply and/or the relevant
device pins in the datasheet.

.. _`regulator_get_exclusive`:

regulator_get_exclusive
=======================

.. c:function:: struct regulator *regulator_get_exclusive(struct device *dev, const char *id)

    obtain exclusive access to a regulator.

    :param struct device \*dev:
        device for regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID.

.. _`regulator_get_exclusive.description`:

Description
-----------

Returns a struct regulator corresponding to the regulator producer,
or \ :c:func:`IS_ERR`\  condition containing errno.  Other consumers will be
unable to obtain this regulator while this reference is held and the
use count for the regulator will be initialised to reflect the current
state of the regulator.

This is intended for use by consumers which cannot tolerate shared
use of the regulator such as those which need to force the
regulator off for correct operation of the hardware they are
controlling.

Use of supply names configured via \ :c:func:`regulator_set_device_supply`\  is
strongly encouraged.  It is recommended that the supply name used
should match the name used for the supply and/or the relevant
device pins in the datasheet.

.. _`regulator_get_optional`:

regulator_get_optional
======================

.. c:function:: struct regulator *regulator_get_optional(struct device *dev, const char *id)

    obtain optional access to a regulator.

    :param struct device \*dev:
        device for regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID.

.. _`regulator_get_optional.description`:

Description
-----------

Returns a struct regulator corresponding to the regulator producer,
or \ :c:func:`IS_ERR`\  condition containing errno.

This is intended for use by consumers for devices which can have
some supplies unconnected in normal use, such as some MMC devices.
It can allow the regulator core to provide stub supplies for other
supplies requested using normal \ :c:func:`regulator_get`\  calls without
disrupting the operation of drivers that can handle absent
supplies.

Use of supply names configured via \ :c:func:`regulator_set_device_supply`\  is
strongly encouraged.  It is recommended that the supply name used
should match the name used for the supply and/or the relevant
device pins in the datasheet.

.. _`regulator_put`:

regulator_put
=============

.. c:function:: void regulator_put(struct regulator *regulator)

    "free" the regulator source

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_put.note`:

Note
----

drivers must ensure that all regulator_enable calls made on this
regulator source are balanced by regulator_disable calls prior to calling
this function.

.. _`regulator_register_supply_alias`:

regulator_register_supply_alias
===============================

.. c:function:: int regulator_register_supply_alias(struct device *dev, const char *id, struct device *alias_dev, const char *alias_id)

    Provide device alias for supply lookup

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID

    :param struct device \*alias_dev:
        device that should be used to lookup the supply

    :param const char \*alias_id:
        Supply name or regulator ID that should be used to lookup the
        supply

.. _`regulator_register_supply_alias.description`:

Description
-----------

All lookups for id on dev will instead be conducted for alias_id on
alias_dev.

.. _`regulator_unregister_supply_alias`:

regulator_unregister_supply_alias
=================================

.. c:function:: void regulator_unregister_supply_alias(struct device *dev, const char *id)

    Remove device alias

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const char \*id:
        Supply name or regulator ID

.. _`regulator_unregister_supply_alias.description`:

Description
-----------

Remove a lookup alias if one exists for id on dev.

.. _`regulator_bulk_register_supply_alias`:

regulator_bulk_register_supply_alias
====================================

.. c:function:: int regulator_bulk_register_supply_alias(struct device *dev, const char *const *id, struct device *alias_dev, const char *const *alias_id, int num_id)

    register multiple aliases

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const char \*const \*id:
        List of supply names or regulator IDs

    :param struct device \*alias_dev:
        device that should be used to lookup the supply

    :param const char \*const \*alias_id:
        List of supply names or regulator IDs that should be used to
        lookup the supply

    :param int num_id:
        Number of aliases to register

.. _`regulator_bulk_register_supply_alias.description`:

Description
-----------

\ ``return``\  0 on success, an errno on failure.

This helper function allows drivers to register several supply
aliases in one operation.  If any of the aliases cannot be
registered any aliases that were registered will be removed
before returning to the caller.

.. _`regulator_bulk_unregister_supply_alias`:

regulator_bulk_unregister_supply_alias
======================================

.. c:function:: void regulator_bulk_unregister_supply_alias(struct device *dev, const char *const *id, int num_id)

    unregister multiple aliases

    :param struct device \*dev:
        device that will be given as the regulator "consumer"

    :param const char \*const \*id:
        List of supply names or regulator IDs

    :param int num_id:
        Number of aliases to unregister

.. _`regulator_bulk_unregister_supply_alias.description`:

Description
-----------

This helper function allows drivers to unregister several supply
aliases in one operation.

.. _`regulator_ena_gpio_ctrl`:

regulator_ena_gpio_ctrl
=======================

.. c:function:: int regulator_ena_gpio_ctrl(struct regulator_dev *rdev, bool enable)

    balance enable_count of each GPIO and actual GPIO pin control

    :param struct regulator_dev \*rdev:
        regulator_dev structure

    :param bool enable:
        enable GPIO at initial use?

.. _`regulator_ena_gpio_ctrl.description`:

Description
-----------

GPIO is enabled in case of initial use. (enable_count is 0)
GPIO is disabled when it is not shared any more. (enable_count <= 1)

.. _`_regulator_enable_delay`:

_regulator_enable_delay
=======================

.. c:function:: void _regulator_enable_delay(unsigned int delay)

    a delay helper function

    :param unsigned int delay:
        time to delay in microseconds

.. _`_regulator_enable_delay.delay-for-the-requested-amount-of-time-as-per-the-guidelines-in`:

Delay for the requested amount of time as per the guidelines in
---------------------------------------------------------------


    Documentation/timers/timers-howto.txt

The assumption here is that regulators will never be enabled in
atomic context and therefore sleeping functions can be used.

.. _`regulator_enable`:

regulator_enable
================

.. c:function:: int regulator_enable(struct regulator *regulator)

    enable regulator output

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_enable.description`:

Description
-----------

Request that the regulator be enabled with the regulator output at
the predefined voltage or current value.  Calls to \ :c:func:`regulator_enable`\ 
must be balanced with calls to \ :c:func:`regulator_disable`\ .

.. _`regulator_enable.note`:

NOTE
----

the output value can be set by other drivers, boot loader or may be
hardwired in the regulator.

.. _`regulator_disable`:

regulator_disable
=================

.. c:function:: int regulator_disable(struct regulator *regulator)

    disable regulator output

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_disable.description`:

Description
-----------

Disable the regulator output voltage or current.  Calls to
\ :c:func:`regulator_enable`\  must be balanced with calls to
\ :c:func:`regulator_disable`\ .

.. _`regulator_disable.note`:

NOTE
----

this will only disable the regulator output if no other consumer
devices have it enabled, the regulator device supports disabling and
machine constraints permit this operation.

.. _`regulator_force_disable`:

regulator_force_disable
=======================

.. c:function:: int regulator_force_disable(struct regulator *regulator)

    force disable regulator output

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_force_disable.description`:

Description
-----------

Forcibly disable the regulator output voltage or current.

.. _`regulator_force_disable.note`:

NOTE
----

this *will* disable the regulator output even if other consumer
devices have it enabled. This should be used for situations when device
damage will likely occur if the regulator is not disabled (e.g. over temp).

.. _`regulator_disable_deferred`:

regulator_disable_deferred
==========================

.. c:function:: int regulator_disable_deferred(struct regulator *regulator, int ms)

    disable regulator output with delay

    :param struct regulator \*regulator:
        regulator source

    :param int ms:
        miliseconds until the regulator is disabled

.. _`regulator_disable_deferred.description`:

Description
-----------

Execute \ :c:func:`regulator_disable`\  on the regulator after a delay.  This
is intended for use with devices that require some time to quiesce.

.. _`regulator_disable_deferred.note`:

NOTE
----

this will only disable the regulator output if no other consumer
devices have it enabled, the regulator device supports disabling and
machine constraints permit this operation.

.. _`regulator_is_enabled`:

regulator_is_enabled
====================

.. c:function:: int regulator_is_enabled(struct regulator *regulator)

    is the regulator output enabled

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_is_enabled.description`:

Description
-----------

Returns positive if the regulator driver backing the source/client
has requested that the device be enabled, zero if it hasn't, else a
negative errno code.

Note that the device backing this regulator handle can have multiple
users, so it might be enabled even if \ :c:func:`regulator_enable`\  was never
called for this particular source.

.. _`regulator_count_voltages`:

regulator_count_voltages
========================

.. c:function:: int regulator_count_voltages(struct regulator *regulator)

    count \ :c:func:`regulator_list_voltage`\  selectors

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_count_voltages.description`:

Description
-----------

Returns number of selectors, or negative errno.  Selectors are
numbered starting at zero, and typically correspond to bitfields
in hardware registers.

.. _`regulator_list_voltage`:

regulator_list_voltage
======================

.. c:function:: int regulator_list_voltage(struct regulator *regulator, unsigned selector)

    enumerate supported voltages

    :param struct regulator \*regulator:
        regulator source

    :param unsigned selector:
        identify voltage to list

.. _`regulator_list_voltage.context`:

Context
-------

can sleep

.. _`regulator_list_voltage.description`:

Description
-----------

Returns a voltage that can be passed to \ ``regulator_set_voltage``\ (),
zero if this selector code can't be used on this system, or a
negative errno.

.. _`regulator_get_regmap`:

regulator_get_regmap
====================

.. c:function:: struct regmap *regulator_get_regmap(struct regulator *regulator)

    get the regulator's register map

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_get_regmap.description`:

Description
-----------

Returns the register map for the given regulator, or an ERR_PTR value
if the regulator doesn't use regmap.

.. _`regulator_get_hardware_vsel_register`:

regulator_get_hardware_vsel_register
====================================

.. c:function:: int regulator_get_hardware_vsel_register(struct regulator *regulator, unsigned *vsel_reg, unsigned *vsel_mask)

    get the HW voltage selector register

    :param struct regulator \*regulator:
        regulator source

    :param unsigned \*vsel_reg:
        voltage selector register, output parameter

    :param unsigned \*vsel_mask:
        mask for voltage selector bitfield, output parameter

.. _`regulator_get_hardware_vsel_register.description`:

Description
-----------

Returns the hardware register offset and bitmask used for setting the
regulator voltage. This might be useful when configuring voltage-scaling
hardware or firmware that can make I2C requests behind the kernel's back,
for example.

On success, the output parameters \ ``vsel_reg``\  and \ ``vsel_mask``\  are filled in
and 0 is returned, otherwise a negative errno is returned.

.. _`regulator_list_hardware_vsel`:

regulator_list_hardware_vsel
============================

.. c:function:: int regulator_list_hardware_vsel(struct regulator *regulator, unsigned selector)

    get the HW-specific register value for a selector

    :param struct regulator \*regulator:
        regulator source

    :param unsigned selector:
        identify voltage to list

.. _`regulator_list_hardware_vsel.description`:

Description
-----------

Converts the selector to a hardware-specific voltage selector that can be
directly written to the regulator registers. The address of the voltage
register can be determined by calling \ ``regulator_get_hardware_vsel_register``\ .

On error a negative errno is returned.

.. _`regulator_get_linear_step`:

regulator_get_linear_step
=========================

.. c:function:: unsigned int regulator_get_linear_step(struct regulator *regulator)

    return the voltage step size between VSEL values

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_get_linear_step.description`:

Description
-----------

Returns the voltage step size between VSEL values for linear
regulators, or return 0 if the regulator isn't a linear regulator.

.. _`regulator_is_supported_voltage`:

regulator_is_supported_voltage
==============================

.. c:function:: int regulator_is_supported_voltage(struct regulator *regulator, int min_uV, int max_uV)

    check if a voltage range can be supported

    :param struct regulator \*regulator:
        Regulator to check.

    :param int min_uV:
        Minimum required voltage in uV.

    :param int max_uV:
        Maximum required voltage in uV.

.. _`regulator_is_supported_voltage.description`:

Description
-----------

Returns a boolean or a negative error code.

.. _`regulator_set_voltage`:

regulator_set_voltage
=====================

.. c:function:: int regulator_set_voltage(struct regulator *regulator, int min_uV, int max_uV)

    set regulator output voltage

    :param struct regulator \*regulator:
        regulator source

    :param int min_uV:
        Minimum required voltage in uV

    :param int max_uV:
        Maximum acceptable voltage in uV

.. _`regulator_set_voltage.description`:

Description
-----------

Sets a voltage regulator to the desired output voltage. This can be set
during any regulator state. IOW, regulator can be disabled or enabled.

If the regulator is enabled then the voltage will change to the new value
immediately otherwise if the regulator is disabled the regulator will
output at the new voltage when enabled.

.. _`regulator_set_voltage.note`:

NOTE
----

If the regulator is shared between several devices then the lowest
request voltage that meets the system constraints will be used.
Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.

.. _`regulator_set_voltage_time`:

regulator_set_voltage_time
==========================

.. c:function:: int regulator_set_voltage_time(struct regulator *regulator, int old_uV, int new_uV)

    get raise/fall time

    :param struct regulator \*regulator:
        regulator source

    :param int old_uV:
        starting voltage in microvolts

    :param int new_uV:
        target voltage in microvolts

.. _`regulator_set_voltage_time.description`:

Description
-----------

Provided with the starting and ending voltage, this function attempts to
calculate the time in microseconds required to rise or fall to this new
voltage.

.. _`regulator_set_voltage_time_sel`:

regulator_set_voltage_time_sel
==============================

.. c:function:: int regulator_set_voltage_time_sel(struct regulator_dev *rdev, unsigned int old_selector, unsigned int new_selector)

    get raise/fall time

    :param struct regulator_dev \*rdev:
        regulator source device

    :param unsigned int old_selector:
        selector for starting voltage

    :param unsigned int new_selector:
        selector for target voltage

.. _`regulator_set_voltage_time_sel.description`:

Description
-----------

Provided with the starting and target voltage selectors, this function
returns time in microseconds required to rise or fall to this new voltage

Drivers providing ramp_delay in regulation_constraints can use this as their
\ :c:func:`set_voltage_time_sel`\  operation.

.. _`regulator_sync_voltage`:

regulator_sync_voltage
======================

.. c:function:: int regulator_sync_voltage(struct regulator *regulator)

    re-apply last regulator output voltage

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_sync_voltage.description`:

Description
-----------

Re-apply the last configured voltage.  This is intended to be used
where some external control source the consumer is cooperating with
has caused the configured voltage to change.

.. _`regulator_get_voltage`:

regulator_get_voltage
=====================

.. c:function:: int regulator_get_voltage(struct regulator *regulator)

    get regulator output voltage

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_get_voltage.description`:

Description
-----------

This returns the current regulator voltage in uV.

.. _`regulator_get_voltage.note`:

NOTE
----

If the regulator is disabled it will return the voltage value. This
function should not be used to determine regulator state.

.. _`regulator_set_current_limit`:

regulator_set_current_limit
===========================

.. c:function:: int regulator_set_current_limit(struct regulator *regulator, int min_uA, int max_uA)

    set regulator output current limit

    :param struct regulator \*regulator:
        regulator source

    :param int min_uA:
        Minimum supported current in uA

    :param int max_uA:
        Maximum supported current in uA

.. _`regulator_set_current_limit.description`:

Description
-----------

Sets current sink to the desired output current. This can be set during
any regulator state. IOW, regulator can be disabled or enabled.

If the regulator is enabled then the current will change to the new value
immediately otherwise if the regulator is disabled the regulator will
output at the new current when enabled.

.. _`regulator_set_current_limit.note`:

NOTE
----

Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.

.. _`regulator_get_current_limit`:

regulator_get_current_limit
===========================

.. c:function:: int regulator_get_current_limit(struct regulator *regulator)

    get regulator output current

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_get_current_limit.description`:

Description
-----------

This returns the current supplied by the specified current sink in uA.

.. _`regulator_get_current_limit.note`:

NOTE
----

If the regulator is disabled it will return the current value. This
function should not be used to determine regulator state.

.. _`regulator_set_mode`:

regulator_set_mode
==================

.. c:function:: int regulator_set_mode(struct regulator *regulator, unsigned int mode)

    set regulator operating mode

    :param struct regulator \*regulator:
        regulator source

    :param unsigned int mode:
        operating mode - one of the REGULATOR_MODE constants

.. _`regulator_set_mode.description`:

Description
-----------

Set regulator operating mode to increase regulator efficiency or improve
regulation performance.

.. _`regulator_set_mode.note`:

NOTE
----

Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.

.. _`regulator_get_mode`:

regulator_get_mode
==================

.. c:function:: unsigned int regulator_get_mode(struct regulator *regulator)

    get regulator operating mode

    :param struct regulator \*regulator:
        regulator source

.. _`regulator_get_mode.description`:

Description
-----------

Get the current regulator operating mode.

.. _`regulator_get_error_flags`:

regulator_get_error_flags
=========================

.. c:function:: int regulator_get_error_flags(struct regulator *regulator, unsigned int *flags)

    get regulator error information

    :param struct regulator \*regulator:
        regulator source

    :param unsigned int \*flags:
        pointer to store error flags

.. _`regulator_get_error_flags.description`:

Description
-----------

Get the current regulator error information.

.. _`regulator_set_load`:

regulator_set_load
==================

.. c:function:: int regulator_set_load(struct regulator *regulator, int uA_load)

    set regulator load

    :param struct regulator \*regulator:
        regulator source

    :param int uA_load:
        load current

.. _`regulator_set_load.description`:

Description
-----------

Notifies the regulator core of a new device load. This is then used by
DRMS (if enabled by constraints) to set the most efficient regulator
operating mode for the new regulator loading.

Consumer devices notify their supply regulator of the maximum power
they will require (can be taken from device datasheet in the power
consumption tables) when they change operational status and hence power
state. Examples of operational state changes that can affect power
consumption are :-

   o Device is opened / closed.
   o Device I/O is about to begin or has just finished.
   o Device is idling in between work.

This information is also exported via sysfs to userspace.

DRMS will sum the total requested load on the regulator and change
to the most efficient operating mode if platform constraints allow.

On error a negative errno is returned.

.. _`regulator_allow_bypass`:

regulator_allow_bypass
======================

.. c:function:: int regulator_allow_bypass(struct regulator *regulator, bool enable)

    allow the regulator to go into bypass mode

    :param struct regulator \*regulator:
        Regulator to configure

    :param bool enable:
        enable or disable bypass mode

.. _`regulator_allow_bypass.description`:

Description
-----------

Allow the regulator to go into bypass mode if all other consumers
for the regulator also enable bypass mode and the machine
constraints allow this.  Bypass mode means that the regulator is
simply passing the input directly to the output with no regulation.

.. _`regulator_register_notifier`:

regulator_register_notifier
===========================

.. c:function:: int regulator_register_notifier(struct regulator *regulator, struct notifier_block *nb)

    register regulator event notifier

    :param struct regulator \*regulator:
        regulator source

    :param struct notifier_block \*nb:
        notifier block

.. _`regulator_register_notifier.description`:

Description
-----------

Register notifier block to receive regulator events.

.. _`regulator_unregister_notifier`:

regulator_unregister_notifier
=============================

.. c:function:: int regulator_unregister_notifier(struct regulator *regulator, struct notifier_block *nb)

    unregister regulator event notifier

    :param struct regulator \*regulator:
        regulator source

    :param struct notifier_block \*nb:
        notifier block

.. _`regulator_unregister_notifier.description`:

Description
-----------

Unregister regulator event notifier block.

.. _`regulator_bulk_get`:

regulator_bulk_get
==================

.. c:function:: int regulator_bulk_get(struct device *dev, int num_consumers, struct regulator_bulk_data *consumers)

    get multiple regulator consumers

    :param struct device \*dev:
        Device to supply

    :param int num_consumers:
        Number of consumers to register

    :param struct regulator_bulk_data \*consumers:
        Configuration of consumers; clients are stored here.

.. _`regulator_bulk_get.description`:

Description
-----------

\ ``return``\  0 on success, an errno on failure.

This helper function allows drivers to get several regulator
consumers in one operation.  If any of the regulators cannot be
acquired then any regulators that were allocated will be freed
before returning to the caller.

.. _`regulator_bulk_enable`:

regulator_bulk_enable
=====================

.. c:function:: int regulator_bulk_enable(int num_consumers, struct regulator_bulk_data *consumers)

    enable multiple regulator consumers

    :param int num_consumers:
        Number of consumers

    :param struct regulator_bulk_data \*consumers:
        Consumer data; clients are stored here.
        \ ``return``\          0 on success, an errno on failure

.. _`regulator_bulk_enable.description`:

Description
-----------

This convenience API allows consumers to enable multiple regulator
clients in a single API call.  If any consumers cannot be enabled
then any others that were enabled will be disabled again prior to
return.

.. _`regulator_bulk_disable`:

regulator_bulk_disable
======================

.. c:function:: int regulator_bulk_disable(int num_consumers, struct regulator_bulk_data *consumers)

    disable multiple regulator consumers

    :param int num_consumers:
        Number of consumers

    :param struct regulator_bulk_data \*consumers:
        Consumer data; clients are stored here.
        \ ``return``\          0 on success, an errno on failure

.. _`regulator_bulk_disable.description`:

Description
-----------

This convenience API allows consumers to disable multiple regulator
clients in a single API call.  If any consumers cannot be disabled
then any others that were disabled will be enabled again prior to
return.

.. _`regulator_bulk_force_disable`:

regulator_bulk_force_disable
============================

.. c:function:: int regulator_bulk_force_disable(int num_consumers, struct regulator_bulk_data *consumers)

    force disable multiple regulator consumers

    :param int num_consumers:
        Number of consumers

    :param struct regulator_bulk_data \*consumers:
        Consumer data; clients are stored here.
        \ ``return``\          0 on success, an errno on failure

.. _`regulator_bulk_force_disable.description`:

Description
-----------

This convenience API allows consumers to forcibly disable multiple regulator
clients in a single API call.

.. _`regulator_bulk_force_disable.note`:

NOTE
----

This should be used for situations when device damage will
likely occur if the regulators are not disabled (e.g. over temp).
Although regulator_force_disable function call for some consumers can
return error numbers, the function is called for all consumers.

.. _`regulator_bulk_free`:

regulator_bulk_free
===================

.. c:function:: void regulator_bulk_free(int num_consumers, struct regulator_bulk_data *consumers)

    free multiple regulator consumers

    :param int num_consumers:
        Number of consumers

    :param struct regulator_bulk_data \*consumers:
        Consumer data; clients are stored here.

.. _`regulator_bulk_free.description`:

Description
-----------

This convenience API allows consumers to free multiple regulator
clients in a single API call.

.. _`regulator_notifier_call_chain`:

regulator_notifier_call_chain
=============================

.. c:function:: int regulator_notifier_call_chain(struct regulator_dev *rdev, unsigned long event, void *data)

    call regulator event notifier

    :param struct regulator_dev \*rdev:
        regulator source

    :param unsigned long event:
        notifier block

    :param void \*data:
        callback-specific data.

.. _`regulator_notifier_call_chain.description`:

Description
-----------

Called by regulator drivers to notify clients a regulator event has
occurred. We also notify regulator clients downstream.
Note lock must be held by caller.

.. _`regulator_mode_to_status`:

regulator_mode_to_status
========================

.. c:function:: int regulator_mode_to_status(unsigned int mode)

    convert a regulator mode into a status

    :param unsigned int mode:
        Mode to convert

.. _`regulator_mode_to_status.description`:

Description
-----------

Convert a regulator mode into a status.

.. _`regulator_register`:

regulator_register
==================

.. c:function:: struct regulator_dev *regulator_register(const struct regulator_desc *regulator_desc, const struct regulator_config *cfg)

    register regulator

    :param const struct regulator_desc \*regulator_desc:
        regulator to register

    :param const struct regulator_config \*cfg:
        runtime configuration for regulator

.. _`regulator_register.description`:

Description
-----------

Called by regulator drivers to register a regulator.
Returns a valid pointer to struct regulator_dev on success
or an \ :c:func:`ERR_PTR`\  on error.

.. _`regulator_unregister`:

regulator_unregister
====================

.. c:function:: void regulator_unregister(struct regulator_dev *rdev)

    unregister regulator

    :param struct regulator_dev \*rdev:
        regulator to unregister

.. _`regulator_unregister.description`:

Description
-----------

Called by regulator drivers to unregister a regulator.

.. _`regulator_suspend_late`:

regulator_suspend_late
======================

.. c:function:: int regulator_suspend_late(struct device *dev)

    prepare regulators for system wide suspend

    :param struct device \*dev:
        *undescribed*

.. _`regulator_suspend_late.description`:

Description
-----------

Configure each regulator with it's suspend operating parameters for state.

.. _`regulator_has_full_constraints`:

regulator_has_full_constraints
==============================

.. c:function:: void regulator_has_full_constraints( void)

    the system has fully specified constraints

    :param  void:
        no arguments

.. _`regulator_has_full_constraints.description`:

Description
-----------

Calling this function will cause the regulator API to disable all
regulators which have a zero use count and don't have an always_on
constraint in a late_initcall.

The intention is that this will become the default behaviour in a
future kernel release so users are encouraged to use this facility
now.

.. _`rdev_get_drvdata`:

rdev_get_drvdata
================

.. c:function:: void *rdev_get_drvdata(struct regulator_dev *rdev)

    get rdev regulator driver data

    :param struct regulator_dev \*rdev:
        regulator

.. _`rdev_get_drvdata.description`:

Description
-----------

Get rdev regulator driver private data. This call can be used in the
regulator driver context.

.. _`regulator_get_drvdata`:

regulator_get_drvdata
=====================

.. c:function:: void *regulator_get_drvdata(struct regulator *regulator)

    get regulator driver data

    :param struct regulator \*regulator:
        regulator

.. _`regulator_get_drvdata.description`:

Description
-----------

Get regulator driver private data. This call can be used in the consumer
driver context when non API regulator specific functions need to be called.

.. _`regulator_set_drvdata`:

regulator_set_drvdata
=====================

.. c:function:: void regulator_set_drvdata(struct regulator *regulator, void *data)

    set regulator driver data

    :param struct regulator \*regulator:
        regulator

    :param void \*data:
        data

.. _`rdev_get_id`:

rdev_get_id
===========

.. c:function:: int rdev_get_id(struct regulator_dev *rdev)

    get regulator ID

    :param struct regulator_dev \*rdev:
        regulator

.. This file was automatic generated / don't edit.

