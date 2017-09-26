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

.. This file was automatic generated / don't edit.

