.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/devlink.h

.. _`devlink_dpipe_field`:

struct devlink_dpipe_field
==========================

.. c:type:: struct devlink_dpipe_field

    dpipe field object

.. _`devlink_dpipe_field.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_field {
        const char *name;
        unsigned int id;
        unsigned int bitwidth;
        enum devlink_dpipe_field_mapping_type mapping_type;
    }

.. _`devlink_dpipe_field.members`:

Members
-------

name
    field name

id
    index inside the headers field array

bitwidth
    bitwidth

mapping_type
    mapping type

.. _`devlink_dpipe_header`:

struct devlink_dpipe_header
===========================

.. c:type:: struct devlink_dpipe_header

    dpipe header object

.. _`devlink_dpipe_header.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_header {
        const char *name;
        unsigned int id;
        struct devlink_dpipe_field *fields;
        unsigned int fields_count;
        bool global;
    }

.. _`devlink_dpipe_header.members`:

Members
-------

name
    header name

id
    index, global/local detrmined by global bit

fields
    fields

fields_count
    number of fields

global
    indicates if header is shared like most protocol header
    or driver specific

.. _`devlink_dpipe_match`:

struct devlink_dpipe_match
==========================

.. c:type:: struct devlink_dpipe_match

    represents match operation

.. _`devlink_dpipe_match.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_match {
        enum devlink_dpipe_match_type type;
        unsigned int header_index;
        struct devlink_dpipe_header *header;
        unsigned int field_id;
    }

.. _`devlink_dpipe_match.members`:

Members
-------

type
    type of match

header_index
    header index (packets can have several headers of same
    type like in case of tunnels)

header
    header

field_id
    *undescribed*

.. _`devlink_dpipe_action`:

struct devlink_dpipe_action
===========================

.. c:type:: struct devlink_dpipe_action

    represents action operation

.. _`devlink_dpipe_action.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_action {
        enum devlink_dpipe_action_type type;
        unsigned int header_index;
        struct devlink_dpipe_header *header;
        unsigned int field_id;
    }

.. _`devlink_dpipe_action.members`:

Members
-------

type
    type of action

header_index
    header index (packets can have several headers of same
    type like in case of tunnels)

header
    header

field_id
    *undescribed*

.. _`devlink_dpipe_value`:

struct devlink_dpipe_value
==========================

.. c:type:: struct devlink_dpipe_value

    represents value of match/action

.. _`devlink_dpipe_value.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_value {
        union {
            struct devlink_dpipe_action *action;
            struct devlink_dpipe_match *match;
        } ;
        unsigned int mapping_value;
        bool mapping_valid;
        unsigned int value_size;
        void *value;
        void *mask;
    }

.. _`devlink_dpipe_value.members`:

Members
-------

{unnamed_union}
    anonymous

action
    action

match
    match

mapping_value
    in case the field has some mapping this value
    specified the mapping value

mapping_valid
    specify if mapping value is valid

value_size
    value size

value
    value

mask
    bit mask

.. _`devlink_dpipe_entry`:

struct devlink_dpipe_entry
==========================

.. c:type:: struct devlink_dpipe_entry

    table entry object

.. _`devlink_dpipe_entry.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_entry {
        u64 index;
        struct devlink_dpipe_value *match_values;
        unsigned int match_values_count;
        struct devlink_dpipe_value *action_values;
        unsigned int action_values_count;
        u64 counter;
        bool counter_valid;
    }

.. _`devlink_dpipe_entry.members`:

Members
-------

index
    index of the entry in the table

match_values
    match values

match_values_count
    *undescribed*

action_values
    actions values

action_values_count
    count of actions values

counter
    value of counter

counter_valid
    Specify if value is valid from hardware

.. _`devlink_dpipe_dump_ctx`:

struct devlink_dpipe_dump_ctx
=============================

.. c:type:: struct devlink_dpipe_dump_ctx

    context provided to driver in order to dump

.. _`devlink_dpipe_dump_ctx.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_dump_ctx {
        struct genl_info *info;
        enum devlink_command cmd;
        struct sk_buff *skb;
        struct nlattr *nest;
        void *hdr;
    }

.. _`devlink_dpipe_dump_ctx.members`:

Members
-------

info
    info

cmd
    devlink command

skb
    skb

nest
    top attribute

hdr
    hdr

.. _`devlink_dpipe_table`:

struct devlink_dpipe_table
==========================

.. c:type:: struct devlink_dpipe_table

    table object

.. _`devlink_dpipe_table.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_table {
        void *priv;
        struct list_head list;
        const char *name;
        bool counters_enabled;
        bool counter_control_extern;
        bool resource_valid;
        u64 resource_id;
        u64 resource_units;
        struct devlink_dpipe_table_ops *table_ops;
        struct rcu_head rcu;
    }

.. _`devlink_dpipe_table.members`:

Members
-------

priv
    private

list
    *undescribed*

name
    table name

counters_enabled
    indicates if counters are active

counter_control_extern
    indicates if counter control is in dpipe or
    external tool

resource_valid
    Indicate that the resource id is valid

resource_id
    relative resource this table is related to

resource_units
    number of resource's unit consumed per table's entry

table_ops
    table operations

rcu
    rcu

.. _`devlink_dpipe_table_ops`:

struct devlink_dpipe_table_ops
==============================

.. c:type:: struct devlink_dpipe_table_ops

    dpipe_table ops \ ``actions_dump``\  - dumps all tables actions \ ``matches_dump``\  - dumps all tables matches \ ``entries_dump``\  - dumps all active entries in the table \ ``counters_set_update``\  - when changing the counter status hardware sync maybe needed to allocate/free counter related resources \ ``size_get``\  - get size

.. _`devlink_dpipe_table_ops.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_table_ops {
        int (*actions_dump)(void *priv, struct sk_buff *skb);
        int (*matches_dump)(void *priv, struct sk_buff *skb);
        int (*entries_dump)(void *priv, bool counters_enabled, struct devlink_dpipe_dump_ctx *dump_ctx);
        int (*counters_set_update)(void *priv, bool enable);
        u64 (*size_get)(void *priv);
    }

.. _`devlink_dpipe_table_ops.members`:

Members
-------

actions_dump
    *undescribed*

matches_dump
    *undescribed*

entries_dump
    *undescribed*

counters_set_update
    *undescribed*

size_get
    *undescribed*

.. _`devlink_dpipe_headers`:

struct devlink_dpipe_headers
============================

.. c:type:: struct devlink_dpipe_headers

    dpipe headers \ ``headers``\  - header array can be shared (global bit) or driver specific \ ``headers_count``\  - count of headers

.. _`devlink_dpipe_headers.definition`:

Definition
----------

.. code-block:: c

    struct devlink_dpipe_headers {
        struct devlink_dpipe_header **headers;
        unsigned int headers_count;
    }

.. _`devlink_dpipe_headers.members`:

Members
-------

headers
    *undescribed*

headers_count
    *undescribed*

.. _`devlink_resource_ops`:

struct devlink_resource_ops
===========================

.. c:type:: struct devlink_resource_ops

    resource ops

.. _`devlink_resource_ops.definition`:

Definition
----------

.. code-block:: c

    struct devlink_resource_ops {
        u64 (*occ_get)(struct devlink *devlink);
        int (*size_validate)(struct devlink *devlink, u64 size, struct netlink_ext_ack *extack);
    }

.. _`devlink_resource_ops.members`:

Members
-------

occ_get
    get the occupied size

size_validate
    validate the size of the resource before update, reload
    is needed for changes to take place

.. _`devlink_resource_size_params`:

struct devlink_resource_size_params
===================================

.. c:type:: struct devlink_resource_size_params

    resource's size parameters

.. _`devlink_resource_size_params.definition`:

Definition
----------

.. code-block:: c

    struct devlink_resource_size_params {
        u64 size_min;
        u64 size_max;
        u64 size_granularity;
        enum devlink_resource_unit unit;
    }

.. _`devlink_resource_size_params.members`:

Members
-------

size_min
    minimum size which can be set

size_max
    maximum size which can be set

size_granularity
    size granularity

unit
    *undescribed*

.. _`devlink_resource`:

struct devlink_resource
=======================

.. c:type:: struct devlink_resource

    devlink resource

.. _`devlink_resource.definition`:

Definition
----------

.. code-block:: c

    struct devlink_resource {
        const char *name;
        u64 id;
        u64 size;
        u64 size_new;
        bool size_valid;
        struct devlink_resource *parent;
        struct devlink_resource_size_params *size_params;
        struct list_head list;
        struct list_head resource_list;
        const struct devlink_resource_ops *resource_ops;
    }

.. _`devlink_resource.members`:

Members
-------

name
    name of the resource

id
    id, per devlink instance

size
    size of the resource

size_new
    updated size of the resource, reload is needed

size_valid
    valid in case the total size of the resource is valid
    including its children

parent
    parent resource

size_params
    size parameters

list
    parent list

resource_list
    list of child resources

resource_ops
    resource ops

.. This file was automatic generated / don't edit.

