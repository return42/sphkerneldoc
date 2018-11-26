.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/devlink.c

.. _`devlink_alloc`:

devlink_alloc
=============

.. c:function:: struct devlink *devlink_alloc(const struct devlink_ops *ops, size_t priv_size)

    Allocate new devlink instance resources

    :param ops:
        ops
    :type ops: const struct devlink_ops \*

    :param priv_size:
        size of user private data
    :type priv_size: size_t

.. _`devlink_alloc.description`:

Description
-----------

Allocate new devlink instance resources, including devlink index
and name.

.. _`devlink_register`:

devlink_register
================

.. c:function:: int devlink_register(struct devlink *devlink, struct device *dev)

    Register devlink instance

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`devlink_unregister`:

devlink_unregister
==================

.. c:function:: void devlink_unregister(struct devlink *devlink)

    Unregister devlink instance

    :param devlink:
        devlink
    :type devlink: struct devlink \*

.. _`devlink_free`:

devlink_free
============

.. c:function:: void devlink_free(struct devlink *devlink)

    Free devlink instance resources

    :param devlink:
        devlink
    :type devlink: struct devlink \*

.. _`devlink_port_register`:

devlink_port_register
=====================

.. c:function:: int devlink_port_register(struct devlink *devlink, struct devlink_port *devlink_port, unsigned int port_index)

    Register devlink port

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param devlink_port:
        devlink port
        \ ``port_index``\ 
    :type devlink_port: struct devlink_port \*

    :param port_index:
        *undescribed*
    :type port_index: unsigned int

.. _`devlink_port_register.description`:

Description
-----------

Register devlink port with provided port index. User can use
any indexing, even hw-related one. devlink_port structure
is convenient to be embedded inside user driver private structure.
Note that the caller should take care of zeroing the devlink_port
structure.

.. _`devlink_port_unregister`:

devlink_port_unregister
=======================

.. c:function:: void devlink_port_unregister(struct devlink_port *devlink_port)

    Unregister devlink port

    :param devlink_port:
        devlink port
    :type devlink_port: struct devlink_port \*

.. _`devlink_port_type_eth_set`:

devlink_port_type_eth_set
=========================

.. c:function:: void devlink_port_type_eth_set(struct devlink_port *devlink_port, struct net_device *netdev)

    Set port type to Ethernet

    :param devlink_port:
        devlink port
    :type devlink_port: struct devlink_port \*

    :param netdev:
        related netdevice
    :type netdev: struct net_device \*

.. _`devlink_port_type_ib_set`:

devlink_port_type_ib_set
========================

.. c:function:: void devlink_port_type_ib_set(struct devlink_port *devlink_port, struct ib_device *ibdev)

    Set port type to InfiniBand

    :param devlink_port:
        devlink port
    :type devlink_port: struct devlink_port \*

    :param ibdev:
        related IB device
    :type ibdev: struct ib_device \*

.. _`devlink_port_type_clear`:

devlink_port_type_clear
=======================

.. c:function:: void devlink_port_type_clear(struct devlink_port *devlink_port)

    Clear port type

    :param devlink_port:
        devlink port
    :type devlink_port: struct devlink_port \*

.. _`devlink_port_attrs_set`:

devlink_port_attrs_set
======================

.. c:function:: void devlink_port_attrs_set(struct devlink_port *devlink_port, enum devlink_port_flavour flavour, u32 port_number, bool split, u32 split_subport_number)

    Set port attributes

    :param devlink_port:
        devlink port
    :type devlink_port: struct devlink_port \*

    :param flavour:
        flavour of the port
    :type flavour: enum devlink_port_flavour

    :param port_number:
        number of the port that is facing user, for example
        the front panel port number
    :type port_number: u32

    :param split:
        indicates if this is split port
    :type split: bool

    :param split_subport_number:
        if the port is split, this is the number
        of subport.
    :type split_subport_number: u32

.. _`devlink_dpipe_headers_register`:

devlink_dpipe_headers_register
==============================

.. c:function:: int devlink_dpipe_headers_register(struct devlink *devlink, struct devlink_dpipe_headers *dpipe_headers)

    register dpipe headers

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param dpipe_headers:
        dpipe header array
    :type dpipe_headers: struct devlink_dpipe_headers \*

.. _`devlink_dpipe_headers_register.description`:

Description
-----------

Register the headers supported by hardware.

.. _`devlink_dpipe_headers_unregister`:

devlink_dpipe_headers_unregister
================================

.. c:function:: void devlink_dpipe_headers_unregister(struct devlink *devlink)

    unregister dpipe headers

    :param devlink:
        devlink
    :type devlink: struct devlink \*

.. _`devlink_dpipe_headers_unregister.description`:

Description
-----------

Unregister the headers supported by hardware.

.. _`devlink_dpipe_table_counter_enabled`:

devlink_dpipe_table_counter_enabled
===================================

.. c:function:: bool devlink_dpipe_table_counter_enabled(struct devlink *devlink, const char *table_name)

    check if counter allocation required

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param table_name:
        tables name
    :type table_name: const char \*

.. _`devlink_dpipe_table_counter_enabled.description`:

Description
-----------

Used by driver to check if counter allocation is required.
After counter allocation is turned on the table entries
are updated to include counter statistics.

After that point on the driver must respect the counter
state so that each entry added to the table is added
with a counter.

.. _`devlink_dpipe_table_register`:

devlink_dpipe_table_register
============================

.. c:function:: int devlink_dpipe_table_register(struct devlink *devlink, const char *table_name, struct devlink_dpipe_table_ops *table_ops, void *priv, bool counter_control_extern)

    register dpipe table

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param table_name:
        table name
    :type table_name: const char \*

    :param table_ops:
        table ops
    :type table_ops: struct devlink_dpipe_table_ops \*

    :param priv:
        priv
    :type priv: void \*

    :param counter_control_extern:
        external control for counters
    :type counter_control_extern: bool

.. _`devlink_dpipe_table_unregister`:

devlink_dpipe_table_unregister
==============================

.. c:function:: void devlink_dpipe_table_unregister(struct devlink *devlink, const char *table_name)

    unregister dpipe table

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param table_name:
        table name
    :type table_name: const char \*

.. _`devlink_resource_register`:

devlink_resource_register
=========================

.. c:function:: int devlink_resource_register(struct devlink *devlink, const char *resource_name, u64 resource_size, u64 resource_id, u64 parent_resource_id, const struct devlink_resource_size_params *size_params)

    devlink resource register

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param resource_name:
        resource's name
    :type resource_name: const char \*

    :param resource_size:
        resource's size
    :type resource_size: u64

    :param resource_id:
        resource's id
    :type resource_id: u64

    :param parent_resource_id:
        *undescribed*
    :type parent_resource_id: u64

    :param size_params:
        *undescribed*
    :type size_params: const struct devlink_resource_size_params \*

.. _`devlink_resources_unregister`:

devlink_resources_unregister
============================

.. c:function:: void devlink_resources_unregister(struct devlink *devlink, struct devlink_resource *resource)

    free all resources

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param resource:
        resource
    :type resource: struct devlink_resource \*

.. _`devlink_resource_size_get`:

devlink_resource_size_get
=========================

.. c:function:: int devlink_resource_size_get(struct devlink *devlink, u64 resource_id, u64 *p_resource_size)

    get and update size

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param resource_id:
        the requested resource id
    :type resource_id: u64

    :param p_resource_size:
        ptr to update
    :type p_resource_size: u64 \*

.. _`devlink_dpipe_table_resource_set`:

devlink_dpipe_table_resource_set
================================

.. c:function:: int devlink_dpipe_table_resource_set(struct devlink *devlink, const char *table_name, u64 resource_id, u64 resource_units)

    set the resource id

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param table_name:
        table name
    :type table_name: const char \*

    :param resource_id:
        resource id
    :type resource_id: u64

    :param resource_units:
        number of resource's units consumed per table's entry
    :type resource_units: u64

.. _`devlink_resource_occ_get_register`:

devlink_resource_occ_get_register
=================================

.. c:function:: void devlink_resource_occ_get_register(struct devlink *devlink, u64 resource_id, devlink_resource_occ_get_t *occ_get, void *occ_get_priv)

    register occupancy getter

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param resource_id:
        resource id
    :type resource_id: u64

    :param occ_get:
        occupancy getter callback
    :type occ_get: devlink_resource_occ_get_t \*

    :param occ_get_priv:
        occupancy getter callback priv
    :type occ_get_priv: void \*

.. _`devlink_resource_occ_get_unregister`:

devlink_resource_occ_get_unregister
===================================

.. c:function:: void devlink_resource_occ_get_unregister(struct devlink *devlink, u64 resource_id)

    unregister occupancy getter

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param resource_id:
        resource id
    :type resource_id: u64

.. _`devlink_params_register`:

devlink_params_register
=======================

.. c:function:: int devlink_params_register(struct devlink *devlink, const struct devlink_param *params, size_t params_count)

    register configuration parameters

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param params:
        configuration parameters array
    :type params: const struct devlink_param \*

    :param params_count:
        number of parameters provided
    :type params_count: size_t

.. _`devlink_params_register.description`:

Description
-----------

Register the configuration parameters supported by the driver.

.. _`devlink_params_unregister`:

devlink_params_unregister
=========================

.. c:function:: void devlink_params_unregister(struct devlink *devlink, const struct devlink_param *params, size_t params_count)

    unregister configuration parameters

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param params:
        configuration parameters to unregister
    :type params: const struct devlink_param \*

    :param params_count:
        number of parameters provided
    :type params_count: size_t

.. _`devlink_param_driverinit_value_get`:

devlink_param_driverinit_value_get
==================================

.. c:function:: int devlink_param_driverinit_value_get(struct devlink *devlink, u32 param_id, union devlink_param_value *init_val)

    get configuration parameter value for driver initializing

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param param_id:
        parameter ID
    :type param_id: u32

    :param init_val:
        value of parameter in driverinit configuration mode
    :type init_val: union devlink_param_value \*

.. _`devlink_param_driverinit_value_get.description`:

Description
-----------

This function should be used by the driver to get driverinit
configuration for initialization after reload command.

.. _`devlink_param_driverinit_value_set`:

devlink_param_driverinit_value_set
==================================

.. c:function:: int devlink_param_driverinit_value_set(struct devlink *devlink, u32 param_id, union devlink_param_value init_val)

    set value of configuration parameter for driverinit configuration mode

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param param_id:
        parameter ID
    :type param_id: u32

    :param init_val:
        value of parameter to set for driverinit configuration mode
    :type init_val: union devlink_param_value

.. _`devlink_param_driverinit_value_set.description`:

Description
-----------

This function should be used by the driver to set driverinit
configuration mode default value.

.. _`devlink_param_value_changed`:

devlink_param_value_changed
===========================

.. c:function:: void devlink_param_value_changed(struct devlink *devlink, u32 param_id)

    notify devlink on a parameter's value change. Should be called by the driver right after the change.

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param param_id:
        parameter ID
    :type param_id: u32

.. _`devlink_param_value_changed.description`:

Description
-----------

This function should be used by the driver to notify devlink on value
change, excluding driverinit configuration mode.
For driverinit configuration mode driver should use the function
\ :c:func:`devlink_param_driverinit_value_set`\  instead.

.. _`devlink_param_value_str_fill`:

devlink_param_value_str_fill
============================

.. c:function:: void devlink_param_value_str_fill(union devlink_param_value *dst_val, const char *src)

    Safely fill-up the string preventing from overflow of the preallocated buffer

    :param dst_val:
        destination devlink_param_value
    :type dst_val: union devlink_param_value \*

    :param src:
        source buffer
    :type src: const char \*

.. _`devlink_region_create`:

devlink_region_create
=====================

.. c:function:: struct devlink_region *devlink_region_create(struct devlink *devlink, const char *region_name, u32 region_max_snapshots, u64 region_size)

    create a new address region

    :param devlink:
        devlink
    :type devlink: struct devlink \*

    :param region_name:
        region name
    :type region_name: const char \*

    :param region_max_snapshots:
        Maximum supported number of snapshots for region
    :type region_max_snapshots: u32

    :param region_size:
        size of region
    :type region_size: u64

.. _`devlink_region_destroy`:

devlink_region_destroy
======================

.. c:function:: void devlink_region_destroy(struct devlink_region *region)

    destroy address region

    :param region:
        devlink region to destroy
    :type region: struct devlink_region \*

.. _`devlink_region_shapshot_id_get`:

devlink_region_shapshot_id_get
==============================

.. c:function:: u32 devlink_region_shapshot_id_get(struct devlink *devlink)

    get snapshot ID

    :param devlink:
        devlink
    :type devlink: struct devlink \*

.. _`devlink_region_shapshot_id_get.description`:

Description
-----------

This callback should be called when adding a new snapshot,
Driver should use the same id for multiple snapshots taken
on multiple regions at the same time/by the same trigger.

.. _`devlink_region_snapshot_create`:

devlink_region_snapshot_create
==============================

.. c:function:: int devlink_region_snapshot_create(struct devlink_region *region, u64 data_len, u8 *data, u32 snapshot_id, devlink_snapshot_data_dest_t *data_destructor)

    create a new snapshot This will add a new snapshot of a region. The snapshot will be stored on the region struct and can be accessed from devlink. This is useful for future analyses of snapshots. Multiple snapshots can be created on a region. The \ ``snapshot_id``\  should be obtained using the getter function.

    :param region:
        *undescribed*
    :type region: struct devlink_region \*

    :param data_len:
        size of snapshot data
    :type data_len: u64

    :param data:
        snapshot data
    :type data: u8 \*

    :param snapshot_id:
        snapshot id to be created
    :type snapshot_id: u32

    :param data_destructor:
        pointer to destructor function to free data
    :type data_destructor: devlink_snapshot_data_dest_t \*

.. This file was automatic generated / don't edit.

