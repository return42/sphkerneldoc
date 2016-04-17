.. -*- coding: utf-8; mode: rst -*-

==========
powercap.h
==========


.. _`powercap_control_type_ops`:

struct powercap_control_type_ops
================================

.. c:type:: powercap_control_type_ops

    Define control type callbacks


.. _`powercap_control_type_ops.definition`:

Definition
----------

.. code-block:: c

  struct powercap_control_type_ops {
    int (* set_enable) (struct powercap_control_type *, bool mode);
    int (* get_enable) (struct powercap_control_type *, bool *mode);
    int (* release) (struct powercap_control_type *);
  };


.. _`powercap_control_type_ops.members`:

Members
-------

:``set_enable``:
    Enable/Disable whole control type.
    Default is enabled. But this callback allows all zones
    to be in disable state and remove any applied power
    limits. If disabled power zone can only be monitored
    not controlled.

:``get_enable``:
    get Enable/Disable status.

:``release``:
    Callback to inform that last reference to this
    control type is closed. So it is safe to free data
    structure associated with this control type.
    This callback is mandatory if the client own memory
    for the control type.




.. _`powercap_control_type_ops.description`:

Description
-----------

This structure defines control type callbacks to be implemented by client
drivers



.. _`powercap_control_type`:

struct powercap_control_type
============================

.. c:type:: powercap_control_type

    Defines a powercap control_type


.. _`powercap_control_type.definition`:

Definition
----------

.. code-block:: c

  struct powercap_control_type {
    struct device dev;
    struct idr idr;
    const struct powercap_control_type_ops * ops;
    bool allocated;
  };


.. _`powercap_control_type.members`:

Members
-------

:``dev``:
    device for this control_type

:``idr``:
    idr to have unique id for its child

:``ops``:
    Pointer to callback struct

:``allocated``:
    This is possible that client owns the memory
    used by this structure. In this case
    this flag is set to false by framework to
    prevent deallocation during release process.
    Otherwise this flag is set to true.




.. _`powercap_control_type.description`:

Description
-----------

Defines powercap control_type. This acts as a container for power
zones, which use same method to control power. E.g. RAPL, RAPL-PCI etc.
All fields are private and should not be used by client drivers.



.. _`powercap_zone_ops`:

struct powercap_zone_ops
========================

.. c:type:: powercap_zone_ops

    Define power zone callbacks


.. _`powercap_zone_ops.definition`:

Definition
----------

.. code-block:: c

  struct powercap_zone_ops {
    int (* get_max_energy_range_uj) (struct powercap_zone *, u64 *);
    int (* get_energy_uj) (struct powercap_zone *, u64 *);
    int (* reset_energy_uj) (struct powercap_zone *);
    int (* get_max_power_range_uw) (struct powercap_zone *, u64 *);
    int (* get_power_uw) (struct powercap_zone *, u64 *);
    int (* set_enable) (struct powercap_zone *, bool mode);
    int (* get_enable) (struct powercap_zone *, bool *mode);
    int (* release) (struct powercap_zone *);
  };


.. _`powercap_zone_ops.members`:

Members
-------

:``get_max_energy_range_uj``:
    Get maximum range of energy counter in
    micro-joules.

:``get_energy_uj``:
    Get current energy counter in micro-joules.

:``reset_energy_uj``:
    Reset micro-joules energy counter.

:``get_max_power_range_uw``:
    Get maximum range of power counter in
    micro-watts.

:``get_power_uw``:
    Get current power counter in micro-watts.

:``set_enable``:
    Enable/Disable power zone controls.
    Default is enabled.

:``get_enable``:
    get Enable/Disable status.

:``release``:
    Callback to inform that last reference to this
    control type is closed. So it is safe to free
    data structure associated with this
    control type. Mandatory, if client driver owns
    the power_zone memory.




.. _`powercap_zone_ops.description`:

Description
-----------

This structure defines zone callbacks to be implemented by client drivers.
Client drives can define both energy and power related callbacks. But at
the least one type (either power or energy) is mandatory. Client drivers
should handle mutual exclusion, if required in callbacks.



.. _`powercap_zone`:

struct powercap_zone
====================

.. c:type:: powercap_zone

    Defines instance of a power cap zone


.. _`powercap_zone.definition`:

Definition
----------

.. code-block:: c

  struct powercap_zone {
    int id;
    char * name;
    void * control_type_inst;
    const struct powercap_zone_ops * ops;
    struct device dev;
    int const_id_cnt;
    struct idr idr;
    struct idr * parent_idr;
    void * private_data;
    struct attribute ** zone_dev_attrs;
    int zone_attr_count;
    struct attribute_group dev_zone_attr_group;
    const struct attribute_group * dev_attr_groups[2];
    bool allocated;
  };


.. _`powercap_zone.members`:

Members
-------

:``id``:
    Unique id

:``name``:
    Power zone name.

:``control_type_inst``:
    Control type instance for this zone.

:``ops``:
    Pointer to the zone operation structure.

:``dev``:
    Instance of a device.

:``const_id_cnt``:
    Number of constraint defined.

:``idr``:
    Instance to an idr entry for children zones.

:``parent_idr``:
    To remove reference from the parent idr.

:``private_data``:
    Private data pointer if any for this zone.

:``zone_dev_attrs``:
    Attributes associated with this device.

:``zone_attr_count``:
    Attribute count.

:``dev_zone_attr_group``:
    Attribute group for attributes.

:``dev_attr_groups[2]``:
    Attribute group store to register with device.

:``allocated``:
    This is possible that client owns the memory
    used by this structure. In this case
    this flag is set to false by framework to
    prevent deallocation during release process.
    Otherwise this flag is set to true.




.. _`powercap_zone.description`:

Description
-----------

This defines a power zone instance. The fields of this structure are
private, and should not be used by client drivers.



.. _`powercap_zone_constraint_ops`:

struct powercap_zone_constraint_ops
===================================

.. c:type:: powercap_zone_constraint_ops

    Define constraint callbacks


.. _`powercap_zone_constraint_ops.definition`:

Definition
----------

.. code-block:: c

  struct powercap_zone_constraint_ops {
    int (* set_power_limit_uw) (struct powercap_zone *, int, u64);
    int (* get_power_limit_uw) (struct powercap_zone *, int, u64 *);
    int (* set_time_window_us) (struct powercap_zone *, int, u64);
    int (* get_time_window_us) (struct powercap_zone *, int, u64 *);
    int (* get_max_power_uw) (struct powercap_zone *, int, u64 *);
    int (* get_min_power_uw) (struct powercap_zone *, int, u64 *);
    int (* get_max_time_window_us) (struct powercap_zone *, int, u64 *);
    int (* get_min_time_window_us) (struct powercap_zone *, int, u64 *);
    const char *(* get_name) (struct powercap_zone *, int);
  };


.. _`powercap_zone_constraint_ops.members`:

Members
-------

:``set_power_limit_uw``:
    Set power limit in micro-watts.

:``get_power_limit_uw``:
    Get power limit in micro-watts.

:``set_time_window_us``:
    Set time window in micro-seconds.

:``get_time_window_us``:
    Get time window in micro-seconds.

:``get_max_power_uw``:
    Get max power allowed in micro-watts.

:``get_min_power_uw``:
    Get min power allowed in micro-watts.

:``get_max_time_window_us``:
    Get max time window allowed in micro-seconds.

:``get_min_time_window_us``:
    Get min time window allowed in micro-seconds.

:``get_name``:
    Get the name of constraint




.. _`powercap_zone_constraint_ops.description`:

Description
-----------

This structure is used to define the constraint callbacks for the client
drivers. The following callbacks are mandatory and can't be NULL::

 set_power_limit_uw
 get_power_limit_uw
 set_time_window_us
 get_time_window_us
 get_name
 Client drivers should handle mutual exclusion, if required in callbacks.



.. _`powercap_zone_constraint`:

struct powercap_zone_constraint
===============================

.. c:type:: powercap_zone_constraint

    Defines instance of a constraint


.. _`powercap_zone_constraint.definition`:

Definition
----------

.. code-block:: c

  struct powercap_zone_constraint {
    int id;
    struct powercap_zone * power_zone;
    const struct powercap_zone_constraint_ops * ops;
  };


.. _`powercap_zone_constraint.members`:

Members
-------

:``id``:
    Instance Id of this constraint.

:``power_zone``:
    Pointer to the power zone for this constraint.

:``ops``:
    Pointer to the constraint callbacks.




.. _`powercap_zone_constraint.description`:

Description
-----------

This defines a constraint instance.



.. _`powercap_set_zone_data`:

powercap_set_zone_data
======================

.. c:function:: void powercap_set_zone_data (struct powercap_zone *power_zone, void *pdata)

    Set private data for a zone

    :param struct powercap_zone \*power_zone:
        A pointer to the valid zone instance.

    :param void \*pdata:
        A pointer to the user private data.



.. _`powercap_set_zone_data.description`:

Description
-----------

Allows client drivers to associate some private data to zone instance.



.. _`powercap_get_zone_data`:

powercap_get_zone_data
======================

.. c:function:: void *powercap_get_zone_data (struct powercap_zone *power_zone)

    Get private data for a zone

    :param struct powercap_zone \*power_zone:
        A pointer to the valid zone instance.



.. _`powercap_get_zone_data.description`:

Description
-----------

Allows client drivers to get private data associate with a zone,
using call to powercap_set_zone_data.



.. _`powercap_register_control_type`:

powercap_register_control_type
==============================

.. c:function:: struct powercap_control_type *powercap_register_control_type (struct powercap_control_type *control_type, const char *name, const struct powercap_control_type_ops *ops)

    Register a control_type with framework

    :param struct powercap_control_type \*control_type:
        Pointer to client allocated memory for the control type
        structure storage. If this is NULL, powercap framework
        will allocate memory and own it.
        Advantage of this parameter is that client can embed
        this data in its data structures and allocate in a
        single call, preventing multiple allocations.

    :param const char \*name:

        *undescribed*

    :param const struct powercap_control_type_ops \*ops:
        Callbacks for control type. This parameter is optional.



.. _`powercap_register_control_type.description`:

Description
-----------

Used to create a control_type with the power capping class. Here control_type
can represent a type of technology, which can control a range of power zones.
For example a control_type can be RAPL (Running Average Power Limit)
Intel® 64 and IA-32 Processor Architectures. The name can be any string
which must be unique, otherwise this function returns NULL.
A pointer to the control_type instance is returned on success.



.. _`powercap_unregister_control_type`:

powercap_unregister_control_type
================================

.. c:function:: int powercap_unregister_control_type (struct powercap_control_type *instance)

    Unregister a control_type from framework

    :param struct powercap_control_type \*instance:
        A pointer to the valid control_type instance.



.. _`powercap_unregister_control_type.description`:

Description
-----------

Used to unregister a control_type with the power capping class.
All power zones registered under this control type have to be unregistered
before calling this function, or it will fail with an error code.



.. _`powercap_register_zone`:

powercap_register_zone
======================

.. c:function:: struct powercap_zone *powercap_register_zone (struct powercap_zone *power_zone, struct powercap_control_type *control_type, const char *name, struct powercap_zone *parent, const struct powercap_zone_ops *ops, int nr_constraints, const struct powercap_zone_constraint_ops *const_ops)

    Register a power zone

    :param struct powercap_zone \*power_zone:
        Pointer to client allocated memory for the power zone structure
        storage. If this is NULL, powercap framework will allocate
        memory and own it. Advantage of this parameter is that client
        can embed this data in its data structures and allocate in a
        single call, preventing multiple allocations.

    :param struct powercap_control_type \*control_type:
        A control_type instance under which this zone operates.

    :param const char \*name:
        A name for this zone.

    :param struct powercap_zone \*parent:
        A pointer to the parent power zone instance if any or NULL

    :param const struct powercap_zone_ops \*ops:
        Pointer to zone operation callback structure.

    :param int nr_constraints:

        *undescribed*

    :param const struct powercap_zone_constraint_ops \*const_ops:
        Pointer to constraint callback structure



.. _`powercap_register_zone.description`:

Description
-----------

Register a power zone under a given control type. A power zone must register
a pointer to a structure representing zone callbacks.
A power zone can be located under a parent power zone, in which case ``parent``
should point to it.  Otherwise, if ``parent`` is NULL, the new power zone will
be located directly under the given control type
For each power zone there may be a number of constraints that appear in the
sysfs under that zone as attributes with unique numeric IDs.
Returns pointer to the power_zone on success.



.. _`powercap_unregister_zone`:

powercap_unregister_zone
========================

.. c:function:: int powercap_unregister_zone (struct powercap_control_type *control_type, struct powercap_zone *power_zone)

    Unregister a zone device

    :param struct powercap_control_type \*control_type:
        A pointer to the valid instance of a control_type.

    :param struct powercap_zone \*power_zone:
        A pointer to the valid zone instance for a control_type



.. _`powercap_unregister_zone.description`:

Description
-----------

Used to unregister a zone device for a control_type.  Caller should
make sure that children for this zone are unregistered first.

