.. -*- coding: utf-8; mode: rst -*-

===========
nf_tables.h
===========


.. _`nft_registers`:

enum nft_registers
==================

.. c:type:: nft_registers

    nf_tables registers


.. _`nft_registers.definition`:

Definition
----------

.. code-block:: c

    enum nft_registers {
      NFT_REG_VERDICT,
      NFT_REG_1,
      NFT_REG_2,
      NFT_REG_3,
      NFT_REG_4,
      __NFT_REG_MAX,
      NFT_REG32_00,
      MFT_REG32_01,
      NFT_REG32_02,
      NFT_REG32_03,
      NFT_REG32_04,
      NFT_REG32_05,
      NFT_REG32_06,
      NFT_REG32_07,
      NFT_REG32_08,
      NFT_REG32_09,
      NFT_REG32_10,
      NFT_REG32_11,
      NFT_REG32_12,
      NFT_REG32_13,
      NFT_REG32_14,
      NFT_REG32_15
    };


.. _`nft_registers.constants`:

Constants
---------

:``NFT_REG_VERDICT``:
-- undescribed --

:``NFT_REG_1``:
-- undescribed --

:``NFT_REG_2``:
-- undescribed --

:``NFT_REG_3``:
-- undescribed --

:``NFT_REG_4``:
-- undescribed --

:``__NFT_REG_MAX``:
-- undescribed --

:``NFT_REG32_00``:
-- undescribed --

:``MFT_REG32_01``:
-- undescribed --

:``NFT_REG32_02``:
-- undescribed --

:``NFT_REG32_03``:
-- undescribed --

:``NFT_REG32_04``:
-- undescribed --

:``NFT_REG32_05``:
-- undescribed --

:``NFT_REG32_06``:
-- undescribed --

:``NFT_REG32_07``:
-- undescribed --

:``NFT_REG32_08``:
-- undescribed --

:``NFT_REG32_09``:
-- undescribed --

:``NFT_REG32_10``:
-- undescribed --

:``NFT_REG32_11``:
-- undescribed --

:``NFT_REG32_12``:
-- undescribed --

:``NFT_REG32_13``:
-- undescribed --

:``NFT_REG32_14``:
-- undescribed --

:``NFT_REG32_15``:
-- undescribed --


.. _`nft_registers.nf_tables-used-to-have-five-registers`:

nf_tables used to have five registers
-------------------------------------

a verdict register and four data
registers of size 16. The data registers have been changed to 16 registers
of size 4. For compatibility reasons, the NFT_REG_[1-4] registers still
map to areas of size 16, the 4 byte registers are addressed using
NFT_REG32_00 - NFT_REG32_15.



.. _`nft_verdicts`:

enum nft_verdicts
=================

.. c:type:: nft_verdicts

    nf_tables internal verdicts


.. _`nft_verdicts.definition`:

Definition
----------

.. code-block:: c

    enum nft_verdicts {
      NFT_CONTINUE,
      NFT_BREAK,
      NFT_JUMP,
      NFT_GOTO,
      NFT_RETURN
    };


.. _`nft_verdicts.constants`:

Constants
---------

:``NFT_CONTINUE``:
    continue evaluation of the current rule

:``NFT_BREAK``:
    terminate evaluation of the current rule

:``NFT_JUMP``:
    push the current chain on the jump stack and jump to a chain

:``NFT_GOTO``:
    jump to a chain without pushing the current chain on the jump stack

:``NFT_RETURN``:
    return to the topmost chain on the jump stack


.. _`nft_verdicts.description`:

Description
-----------

The nf_tables verdicts share their numeric space with the netfilter verdicts.



.. _`nf_tables_msg_types`:

enum nf_tables_msg_types
========================

.. c:type:: nf_tables_msg_types

    nf_tables netlink message types


.. _`nf_tables_msg_types.definition`:

Definition
----------

.. code-block:: c

    enum nf_tables_msg_types {
      NFT_MSG_NEWTABLE,
      NFT_MSG_GETTABLE,
      NFT_MSG_DELTABLE,
      NFT_MSG_NEWCHAIN,
      NFT_MSG_GETCHAIN,
      NFT_MSG_DELCHAIN,
      NFT_MSG_NEWRULE,
      NFT_MSG_GETRULE,
      NFT_MSG_DELRULE,
      NFT_MSG_NEWSET,
      NFT_MSG_GETSET,
      NFT_MSG_DELSET,
      NFT_MSG_NEWSETELEM,
      NFT_MSG_GETSETELEM,
      NFT_MSG_DELSETELEM,
      NFT_MSG_NEWGEN,
      NFT_MSG_GETGEN,
      NFT_MSG_TRACE,
      NFT_MSG_MAX
    };


.. _`nf_tables_msg_types.constants`:

Constants
---------

:``NFT_MSG_NEWTABLE``:
    create a new table (enum nft_table_attributes)

:``NFT_MSG_GETTABLE``:
    get a table (enum nft_table_attributes)

:``NFT_MSG_DELTABLE``:
    delete a table (enum nft_table_attributes)

:``NFT_MSG_NEWCHAIN``:
    create a new chain (enum nft_chain_attributes)

:``NFT_MSG_GETCHAIN``:
    get a chain (enum nft_chain_attributes)

:``NFT_MSG_DELCHAIN``:
    delete a chain (enum nft_chain_attributes)

:``NFT_MSG_NEWRULE``:
    create a new rule (enum nft_rule_attributes)

:``NFT_MSG_GETRULE``:
    get a rule (enum nft_rule_attributes)

:``NFT_MSG_DELRULE``:
    delete a rule (enum nft_rule_attributes)

:``NFT_MSG_NEWSET``:
    create a new set (enum nft_set_attributes)

:``NFT_MSG_GETSET``:
    get a set (enum nft_set_attributes)

:``NFT_MSG_DELSET``:
    delete a set (enum nft_set_attributes)

:``NFT_MSG_NEWSETELEM``:
    create a new set element (enum nft_set_elem_attributes)

:``NFT_MSG_GETSETELEM``:
    get a set element (enum nft_set_elem_attributes)

:``NFT_MSG_DELSETELEM``:
    delete a set element (enum nft_set_elem_attributes)

:``NFT_MSG_NEWGEN``:
    announce a new generation, only for events (enum nft_gen_attributes)

:``NFT_MSG_GETGEN``:
    get the rule-set generation (enum nft_gen_attributes)

:``NFT_MSG_TRACE``:
    trace event (enum nft_trace_attributes)

:``NFT_MSG_MAX``:
-- undescribed --


.. _`nft_list_attributes`:

enum nft_list_attributes
========================

.. c:type:: nft_list_attributes

    nf_tables generic list netlink attributes


.. _`nft_list_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_list_attributes {
      NFTA_LIST_UNPEC,
      NFTA_LIST_ELEM,
      __NFTA_LIST_MAX
    };


.. _`nft_list_attributes.constants`:

Constants
---------

:``NFTA_LIST_UNPEC``:
-- undescribed --

:``NFTA_LIST_ELEM``:
    list element (NLA_NESTED)

:``__NFTA_LIST_MAX``:
-- undescribed --


.. _`nft_hook_attributes`:

enum nft_hook_attributes
========================

.. c:type:: nft_hook_attributes

    nf_tables netfilter hook netlink attributes


.. _`nft_hook_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_hook_attributes {
      NFTA_HOOK_UNSPEC,
      NFTA_HOOK_HOOKNUM,
      NFTA_HOOK_PRIORITY,
      NFTA_HOOK_DEV,
      __NFTA_HOOK_MAX
    };


.. _`nft_hook_attributes.constants`:

Constants
---------

:``NFTA_HOOK_UNSPEC``:
-- undescribed --

:``NFTA_HOOK_HOOKNUM``:
    netfilter hook number (NLA_U32)

:``NFTA_HOOK_PRIORITY``:
    netfilter hook priority (NLA_U32)

:``NFTA_HOOK_DEV``:
    netdevice name (NLA_STRING)

:``__NFTA_HOOK_MAX``:
-- undescribed --


.. _`nft_table_flags`:

enum nft_table_flags
====================

.. c:type:: nft_table_flags

    nf_tables table flags


.. _`nft_table_flags.definition`:

Definition
----------

.. code-block:: c

    enum nft_table_flags {
      NFT_TABLE_F_DORMANT
    };


.. _`nft_table_flags.constants`:

Constants
---------

:``NFT_TABLE_F_DORMANT``:
    this table is not active


.. _`nft_table_attributes`:

enum nft_table_attributes
=========================

.. c:type:: nft_table_attributes

    nf_tables table netlink attributes


.. _`nft_table_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_table_attributes {
      NFTA_TABLE_UNSPEC,
      NFTA_TABLE_NAME,
      NFTA_TABLE_FLAGS,
      NFTA_TABLE_USE,
      __NFTA_TABLE_MAX
    };


.. _`nft_table_attributes.constants`:

Constants
---------

:``NFTA_TABLE_UNSPEC``:
-- undescribed --

:``NFTA_TABLE_NAME``:
    name of the table (NLA_STRING)

:``NFTA_TABLE_FLAGS``:
    bitmask of enum nft_table_flags (NLA_U32)

:``NFTA_TABLE_USE``:
    number of chains in this table (NLA_U32)

:``__NFTA_TABLE_MAX``:
-- undescribed --


.. _`nft_chain_attributes`:

enum nft_chain_attributes
=========================

.. c:type:: nft_chain_attributes

    nf_tables chain netlink attributes


.. _`nft_chain_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_chain_attributes {
      NFTA_CHAIN_UNSPEC,
      NFTA_CHAIN_TABLE,
      NFTA_CHAIN_HANDLE,
      NFTA_CHAIN_NAME,
      NFTA_CHAIN_HOOK,
      NFTA_CHAIN_POLICY,
      NFTA_CHAIN_USE,
      NFTA_CHAIN_TYPE,
      NFTA_CHAIN_COUNTERS,
      __NFTA_CHAIN_MAX
    };


.. _`nft_chain_attributes.constants`:

Constants
---------

:``NFTA_CHAIN_UNSPEC``:
-- undescribed --

:``NFTA_CHAIN_TABLE``:
    name of the table containing the chain (NLA_STRING)

:``NFTA_CHAIN_HANDLE``:
    numeric handle of the chain (NLA_U64)

:``NFTA_CHAIN_NAME``:
    name of the chain (NLA_STRING)

:``NFTA_CHAIN_HOOK``:
    hook specification for basechains (NLA_NESTED: nft_hook_attributes)

:``NFTA_CHAIN_POLICY``:
    numeric policy of the chain (NLA_U32)

:``NFTA_CHAIN_USE``:
    number of references to this chain (NLA_U32)

:``NFTA_CHAIN_TYPE``:
    type name of the string (NLA_NUL_STRING)

:``NFTA_CHAIN_COUNTERS``:
    counter specification of the chain (NLA_NESTED: nft_counter_attributes)

:``__NFTA_CHAIN_MAX``:
-- undescribed --


.. _`nft_rule_attributes`:

enum nft_rule_attributes
========================

.. c:type:: nft_rule_attributes

    nf_tables rule netlink attributes


.. _`nft_rule_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_rule_attributes {
      NFTA_RULE_UNSPEC,
      NFTA_RULE_TABLE,
      NFTA_RULE_CHAIN,
      NFTA_RULE_HANDLE,
      NFTA_RULE_EXPRESSIONS,
      NFTA_RULE_COMPAT,
      NFTA_RULE_POSITION,
      NFTA_RULE_USERDATA,
      __NFTA_RULE_MAX
    };


.. _`nft_rule_attributes.constants`:

Constants
---------

:``NFTA_RULE_UNSPEC``:
-- undescribed --

:``NFTA_RULE_TABLE``:
    name of the table containing the rule (NLA_STRING)

:``NFTA_RULE_CHAIN``:
    name of the chain containing the rule (NLA_STRING)

:``NFTA_RULE_HANDLE``:
    numeric handle of the rule (NLA_U64)

:``NFTA_RULE_EXPRESSIONS``:
    list of expressions (NLA_NESTED: nft_expr_attributes)

:``NFTA_RULE_COMPAT``:
    compatibility specifications of the rule (NLA_NESTED: nft_rule_compat_attributes)

:``NFTA_RULE_POSITION``:
    numeric handle of the previous rule (NLA_U64)

:``NFTA_RULE_USERDATA``:
    user data (NLA_BINARY, NFT_USERDATA_MAXLEN)

:``__NFTA_RULE_MAX``:
-- undescribed --


.. _`nft_rule_compat_flags`:

enum nft_rule_compat_flags
==========================

.. c:type:: nft_rule_compat_flags

    nf_tables rule compat flags


.. _`nft_rule_compat_flags.definition`:

Definition
----------

.. code-block:: c

    enum nft_rule_compat_flags {
      NFT_RULE_COMPAT_F_INV,
      NFT_RULE_COMPAT_F_MASK
    };


.. _`nft_rule_compat_flags.constants`:

Constants
---------

:``NFT_RULE_COMPAT_F_INV``:
    invert the check result

:``NFT_RULE_COMPAT_F_MASK``:
-- undescribed --


.. _`nft_rule_compat_attributes`:

enum nft_rule_compat_attributes
===============================

.. c:type:: nft_rule_compat_attributes

    nf_tables rule compat attributes


.. _`nft_rule_compat_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_rule_compat_attributes {
      NFTA_RULE_COMPAT_UNSPEC,
      NFTA_RULE_COMPAT_PROTO,
      NFTA_RULE_COMPAT_FLAGS,
      __NFTA_RULE_COMPAT_MAX
    };


.. _`nft_rule_compat_attributes.constants`:

Constants
---------

:``NFTA_RULE_COMPAT_UNSPEC``:
-- undescribed --

:``NFTA_RULE_COMPAT_PROTO``:
    numerice value of handled protocol (NLA_U32)

:``NFTA_RULE_COMPAT_FLAGS``:
    bitmask of enum nft_rule_compat_flags (NLA_U32)

:``__NFTA_RULE_COMPAT_MAX``:
-- undescribed --


.. _`nft_set_flags`:

enum nft_set_flags
==================

.. c:type:: nft_set_flags

    nf_tables set flags


.. _`nft_set_flags.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_flags {
      NFT_SET_ANONYMOUS,
      NFT_SET_CONSTANT,
      NFT_SET_INTERVAL,
      NFT_SET_MAP,
      NFT_SET_TIMEOUT,
      NFT_SET_EVAL
    };


.. _`nft_set_flags.constants`:

Constants
---------

:``NFT_SET_ANONYMOUS``:
    name allocation, automatic cleanup on unlink

:``NFT_SET_CONSTANT``:
    set contents may not change while bound

:``NFT_SET_INTERVAL``:
    set contains intervals

:``NFT_SET_MAP``:
    set is used as a dictionary

:``NFT_SET_TIMEOUT``:
    set uses timeouts

:``NFT_SET_EVAL``:
    set contains expressions for evaluation


.. _`nft_set_policies`:

enum nft_set_policies
=====================

.. c:type:: nft_set_policies

    set selection policy


.. _`nft_set_policies.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_policies {
      NFT_SET_POL_PERFORMANCE,
      NFT_SET_POL_MEMORY
    };


.. _`nft_set_policies.constants`:

Constants
---------

:``NFT_SET_POL_PERFORMANCE``:
    prefer high performance over low memory use

:``NFT_SET_POL_MEMORY``:
    prefer low memory use over high performance


.. _`nft_set_desc_attributes`:

enum nft_set_desc_attributes
============================

.. c:type:: nft_set_desc_attributes

    set element description


.. _`nft_set_desc_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_desc_attributes {
      NFTA_SET_DESC_UNSPEC,
      NFTA_SET_DESC_SIZE,
      __NFTA_SET_DESC_MAX
    };


.. _`nft_set_desc_attributes.constants`:

Constants
---------

:``NFTA_SET_DESC_UNSPEC``:
-- undescribed --

:``NFTA_SET_DESC_SIZE``:
    number of elements in set (NLA_U32)

:``__NFTA_SET_DESC_MAX``:
-- undescribed --


.. _`nft_set_attributes`:

enum nft_set_attributes
=======================

.. c:type:: nft_set_attributes

    nf_tables set netlink attributes


.. _`nft_set_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_attributes {
      NFTA_SET_UNSPEC,
      NFTA_SET_TABLE,
      NFTA_SET_NAME,
      NFTA_SET_FLAGS,
      NFTA_SET_KEY_TYPE,
      NFTA_SET_KEY_LEN,
      NFTA_SET_DATA_TYPE,
      NFTA_SET_DATA_LEN,
      NFTA_SET_POLICY,
      NFTA_SET_DESC,
      NFTA_SET_ID,
      NFTA_SET_TIMEOUT,
      NFTA_SET_GC_INTERVAL,
      NFTA_SET_USERDATA,
      __NFTA_SET_MAX
    };


.. _`nft_set_attributes.constants`:

Constants
---------

:``NFTA_SET_UNSPEC``:
-- undescribed --

:``NFTA_SET_TABLE``:
    table name (NLA_STRING)

:``NFTA_SET_NAME``:
    set name (NLA_STRING)

:``NFTA_SET_FLAGS``:
    bitmask of enum nft_set_flags (NLA_U32)

:``NFTA_SET_KEY_TYPE``:
    key data type, informational purpose only (NLA_U32)

:``NFTA_SET_KEY_LEN``:
    key data length (NLA_U32)

:``NFTA_SET_DATA_TYPE``:
    mapping data type (NLA_U32)

:``NFTA_SET_DATA_LEN``:
    mapping data length (NLA_U32)

:``NFTA_SET_POLICY``:
    selection policy (NLA_U32)

:``NFTA_SET_DESC``:
    set description (NLA_NESTED)

:``NFTA_SET_ID``:
    uniquely identifies a set in a transaction (NLA_U32)

:``NFTA_SET_TIMEOUT``:
    default timeout value (NLA_U64)

:``NFTA_SET_GC_INTERVAL``:
    garbage collection interval (NLA_U32)

:``NFTA_SET_USERDATA``:
    user data (NLA_BINARY)

:``__NFTA_SET_MAX``:
-- undescribed --


.. _`nft_set_elem_flags`:

enum nft_set_elem_flags
=======================

.. c:type:: nft_set_elem_flags

    nf_tables set element flags


.. _`nft_set_elem_flags.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_elem_flags {
      NFT_SET_ELEM_INTERVAL_END
    };


.. _`nft_set_elem_flags.constants`:

Constants
---------

:``NFT_SET_ELEM_INTERVAL_END``:
    element ends the previous interval


.. _`nft_set_elem_attributes`:

enum nft_set_elem_attributes
============================

.. c:type:: nft_set_elem_attributes

    nf_tables set element netlink attributes


.. _`nft_set_elem_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_elem_attributes {
      NFTA_SET_ELEM_UNSPEC,
      NFTA_SET_ELEM_KEY,
      NFTA_SET_ELEM_DATA,
      NFTA_SET_ELEM_FLAGS,
      NFTA_SET_ELEM_TIMEOUT,
      NFTA_SET_ELEM_EXPIRATION,
      NFTA_SET_ELEM_USERDATA,
      NFTA_SET_ELEM_EXPR,
      __NFTA_SET_ELEM_MAX
    };


.. _`nft_set_elem_attributes.constants`:

Constants
---------

:``NFTA_SET_ELEM_UNSPEC``:
-- undescribed --

:``NFTA_SET_ELEM_KEY``:
    key value (NLA_NESTED: nft_data)

:``NFTA_SET_ELEM_DATA``:
    data value of mapping (NLA_NESTED: nft_data_attributes)

:``NFTA_SET_ELEM_FLAGS``:
    bitmask of nft_set_elem_flags (NLA_U32)

:``NFTA_SET_ELEM_TIMEOUT``:
    timeout value (NLA_U64)

:``NFTA_SET_ELEM_EXPIRATION``:
    expiration time (NLA_U64)

:``NFTA_SET_ELEM_USERDATA``:
    user data (NLA_BINARY)

:``NFTA_SET_ELEM_EXPR``:
    expression (NLA_NESTED: nft_expr_attributes)

:``__NFTA_SET_ELEM_MAX``:
-- undescribed --


.. _`nft_set_elem_list_attributes`:

enum nft_set_elem_list_attributes
=================================

.. c:type:: nft_set_elem_list_attributes

    nf_tables set element list netlink attributes


.. _`nft_set_elem_list_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_elem_list_attributes {
      NFTA_SET_ELEM_LIST_UNSPEC,
      NFTA_SET_ELEM_LIST_TABLE,
      NFTA_SET_ELEM_LIST_SET,
      NFTA_SET_ELEM_LIST_ELEMENTS,
      NFTA_SET_ELEM_LIST_SET_ID,
      __NFTA_SET_ELEM_LIST_MAX
    };


.. _`nft_set_elem_list_attributes.constants`:

Constants
---------

:``NFTA_SET_ELEM_LIST_UNSPEC``:
-- undescribed --

:``NFTA_SET_ELEM_LIST_TABLE``:
    table of the set to be changed (NLA_STRING)

:``NFTA_SET_ELEM_LIST_SET``:
    name of the set to be changed (NLA_STRING)

:``NFTA_SET_ELEM_LIST_ELEMENTS``:
    list of set elements (NLA_NESTED: nft_set_elem_attributes)

:``NFTA_SET_ELEM_LIST_SET_ID``:
    uniquely identifies a set in a transaction (NLA_U32)

:``__NFTA_SET_ELEM_LIST_MAX``:
-- undescribed --


.. _`nft_data_types`:

enum nft_data_types
===================

.. c:type:: nft_data_types

    nf_tables data types


.. _`nft_data_types.definition`:

Definition
----------

.. code-block:: c

    enum nft_data_types {
      NFT_DATA_VALUE,
      NFT_DATA_VERDICT
    };


.. _`nft_data_types.constants`:

Constants
---------

:``NFT_DATA_VALUE``:
    generic data

:``NFT_DATA_VERDICT``:
    netfilter verdict


.. _`nft_data_types.description`:

Description
-----------

The type of data is usually determined by the kernel directly and is not
explicitly specified by userspace. The only difference are sets, where
userspace specifies the key and mapping data types.

The values 0xffffff00-0xffffffff are reserved for internally used types.
The remaining range can be freely used by userspace to encode types, all
values are equivalent to NFT_DATA_VALUE.



.. _`nft_data_attributes`:

enum nft_data_attributes
========================

.. c:type:: nft_data_attributes

    nf_tables data netlink attributes


.. _`nft_data_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_data_attributes {
      NFTA_DATA_UNSPEC,
      NFTA_DATA_VALUE,
      NFTA_DATA_VERDICT,
      __NFTA_DATA_MAX
    };


.. _`nft_data_attributes.constants`:

Constants
---------

:``NFTA_DATA_UNSPEC``:
-- undescribed --

:``NFTA_DATA_VALUE``:
    generic data (NLA_BINARY)

:``NFTA_DATA_VERDICT``:
    nf_tables verdict (NLA_NESTED: nft_verdict_attributes)

:``__NFTA_DATA_MAX``:
-- undescribed --


.. _`nft_verdict_attributes`:

enum nft_verdict_attributes
===========================

.. c:type:: nft_verdict_attributes

    nf_tables verdict netlink attributes


.. _`nft_verdict_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_verdict_attributes {
      NFTA_VERDICT_UNSPEC,
      NFTA_VERDICT_CODE,
      NFTA_VERDICT_CHAIN,
      __NFTA_VERDICT_MAX
    };


.. _`nft_verdict_attributes.constants`:

Constants
---------

:``NFTA_VERDICT_UNSPEC``:
-- undescribed --

:``NFTA_VERDICT_CODE``:
    nf_tables verdict (NLA_U32: enum nft_verdicts)

:``NFTA_VERDICT_CHAIN``:
    jump target chain name (NLA_STRING)

:``__NFTA_VERDICT_MAX``:
-- undescribed --


.. _`nft_expr_attributes`:

enum nft_expr_attributes
========================

.. c:type:: nft_expr_attributes

    nf_tables expression netlink attributes


.. _`nft_expr_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_expr_attributes {
      NFTA_EXPR_UNSPEC,
      NFTA_EXPR_NAME,
      NFTA_EXPR_DATA,
      __NFTA_EXPR_MAX
    };


.. _`nft_expr_attributes.constants`:

Constants
---------

:``NFTA_EXPR_UNSPEC``:
-- undescribed --

:``NFTA_EXPR_NAME``:
    name of the expression type (NLA_STRING)

:``NFTA_EXPR_DATA``:
    type specific data (NLA_NESTED)

:``__NFTA_EXPR_MAX``:
-- undescribed --


.. _`nft_immediate_attributes`:

enum nft_immediate_attributes
=============================

.. c:type:: nft_immediate_attributes

    nf_tables immediate expression netlink attributes


.. _`nft_immediate_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_immediate_attributes {
      NFTA_IMMEDIATE_UNSPEC,
      NFTA_IMMEDIATE_DREG,
      NFTA_IMMEDIATE_DATA,
      __NFTA_IMMEDIATE_MAX
    };


.. _`nft_immediate_attributes.constants`:

Constants
---------

:``NFTA_IMMEDIATE_UNSPEC``:
-- undescribed --

:``NFTA_IMMEDIATE_DREG``:
    destination register to load data into (NLA_U32)

:``NFTA_IMMEDIATE_DATA``:
    data to load (NLA_NESTED: nft_data_attributes)

:``__NFTA_IMMEDIATE_MAX``:
-- undescribed --


.. _`nft_bitwise_attributes`:

enum nft_bitwise_attributes
===========================

.. c:type:: nft_bitwise_attributes

    nf_tables bitwise expression netlink attributes


.. _`nft_bitwise_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_bitwise_attributes {
      NFTA_BITWISE_UNSPEC,
      NFTA_BITWISE_SREG,
      NFTA_BITWISE_DREG,
      NFTA_BITWISE_LEN,
      NFTA_BITWISE_MASK,
      NFTA_BITWISE_XOR,
      __NFTA_BITWISE_MAX
    };


.. _`nft_bitwise_attributes.constants`:

Constants
---------

:``NFTA_BITWISE_UNSPEC``:
-- undescribed --

:``NFTA_BITWISE_SREG``:
    source register (NLA_U32: nft_registers)

:``NFTA_BITWISE_DREG``:
    destination register (NLA_U32: nft_registers)

:``NFTA_BITWISE_LEN``:
    length of operands (NLA_U32)

:``NFTA_BITWISE_MASK``:
    mask value (NLA_NESTED: nft_data_attributes)

:``NFTA_BITWISE_XOR``:
    xor value (NLA_NESTED: nft_data_attributes)

:``__NFTA_BITWISE_MAX``:
-- undescribed --


.. _`nft_bitwise_attributes.the-bitwise-expression-performs-the-following-operation`:

The bitwise expression performs the following operation
-------------------------------------------------------


dreg = (sreg & mask) ^ xor



.. _`nft_bitwise_attributes.which-allow-to-express-all-bitwise-operations`:

which allow to express all bitwise operations
---------------------------------------------


mask        xor



.. _`nft_bitwise_attributes.not`:

NOT
---

1        1



.. _`nft_bitwise_attributes.or`:

OR
--

0        x



.. _`nft_bitwise_attributes.xor`:

XOR
---

1        x



.. _`nft_bitwise_attributes.and`:

AND
---

x        0



.. _`nft_byteorder_ops`:

enum nft_byteorder_ops
======================

.. c:type:: nft_byteorder_ops

    nf_tables byteorder operators


.. _`nft_byteorder_ops.definition`:

Definition
----------

.. code-block:: c

    enum nft_byteorder_ops {
      NFT_BYTEORDER_NTOH,
      NFT_BYTEORDER_HTON
    };


.. _`nft_byteorder_ops.constants`:

Constants
---------

:``NFT_BYTEORDER_NTOH``:
    network to host operator

:``NFT_BYTEORDER_HTON``:
    host to network opertaor


.. _`nft_byteorder_attributes`:

enum nft_byteorder_attributes
=============================

.. c:type:: nft_byteorder_attributes

    nf_tables byteorder expression netlink attributes


.. _`nft_byteorder_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_byteorder_attributes {
      NFTA_BYTEORDER_UNSPEC,
      NFTA_BYTEORDER_SREG,
      NFTA_BYTEORDER_DREG,
      NFTA_BYTEORDER_OP,
      NFTA_BYTEORDER_LEN,
      NFTA_BYTEORDER_SIZE,
      __NFTA_BYTEORDER_MAX
    };


.. _`nft_byteorder_attributes.constants`:

Constants
---------

:``NFTA_BYTEORDER_UNSPEC``:
-- undescribed --

:``NFTA_BYTEORDER_SREG``:
    source register (NLA_U32: nft_registers)

:``NFTA_BYTEORDER_DREG``:
    destination register (NLA_U32: nft_registers)

:``NFTA_BYTEORDER_OP``:
    operator (NLA_U32: enum nft_byteorder_ops)

:``NFTA_BYTEORDER_LEN``:
    length of the data (NLA_U32)

:``NFTA_BYTEORDER_SIZE``:
    data size in bytes (NLA_U32: 2 or 4)

:``__NFTA_BYTEORDER_MAX``:
-- undescribed --


.. _`nft_cmp_ops`:

enum nft_cmp_ops
================

.. c:type:: nft_cmp_ops

    nf_tables relational operator


.. _`nft_cmp_ops.definition`:

Definition
----------

.. code-block:: c

    enum nft_cmp_ops {
      NFT_CMP_EQ,
      NFT_CMP_NEQ,
      NFT_CMP_LT,
      NFT_CMP_LTE,
      NFT_CMP_GT,
      NFT_CMP_GTE
    };


.. _`nft_cmp_ops.constants`:

Constants
---------

:``NFT_CMP_EQ``:
    equal

:``NFT_CMP_NEQ``:
    not equal

:``NFT_CMP_LT``:
    less than

:``NFT_CMP_LTE``:
    less than or equal to

:``NFT_CMP_GT``:
    greater than

:``NFT_CMP_GTE``:
    greater than or equal to


.. _`nft_cmp_attributes`:

enum nft_cmp_attributes
=======================

.. c:type:: nft_cmp_attributes

    nf_tables cmp expression netlink attributes


.. _`nft_cmp_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_cmp_attributes {
      NFTA_CMP_UNSPEC,
      NFTA_CMP_SREG,
      NFTA_CMP_OP,
      NFTA_CMP_DATA,
      __NFTA_CMP_MAX
    };


.. _`nft_cmp_attributes.constants`:

Constants
---------

:``NFTA_CMP_UNSPEC``:
-- undescribed --

:``NFTA_CMP_SREG``:
    source register of data to compare (NLA_U32: nft_registers)

:``NFTA_CMP_OP``:
    cmp operation (NLA_U32: nft_cmp_ops)

:``NFTA_CMP_DATA``:
    data to compare against (NLA_NESTED: nft_data_attributes)

:``__NFTA_CMP_MAX``:
-- undescribed --


.. _`nft_lookup_attributes`:

enum nft_lookup_attributes
==========================

.. c:type:: nft_lookup_attributes

    nf_tables set lookup expression netlink attributes


.. _`nft_lookup_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_lookup_attributes {
      NFTA_LOOKUP_UNSPEC,
      NFTA_LOOKUP_SET,
      NFTA_LOOKUP_SREG,
      NFTA_LOOKUP_DREG,
      NFTA_LOOKUP_SET_ID,
      __NFTA_LOOKUP_MAX
    };


.. _`nft_lookup_attributes.constants`:

Constants
---------

:``NFTA_LOOKUP_UNSPEC``:
-- undescribed --

:``NFTA_LOOKUP_SET``:
    name of the set where to look for (NLA_STRING)

:``NFTA_LOOKUP_SREG``:
    source register of the data to look for (NLA_U32: nft_registers)

:``NFTA_LOOKUP_DREG``:
    destination register (NLA_U32: nft_registers)

:``NFTA_LOOKUP_SET_ID``:
    uniquely identifies a set in a transaction (NLA_U32)

:``__NFTA_LOOKUP_MAX``:
-- undescribed --


.. _`nft_dynset_attributes`:

enum nft_dynset_attributes
==========================

.. c:type:: nft_dynset_attributes

    dynset expression attributes


.. _`nft_dynset_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_dynset_attributes {
      NFTA_DYNSET_UNSPEC,
      NFTA_DYNSET_SET_NAME,
      NFTA_DYNSET_SET_ID,
      NFTA_DYNSET_OP,
      NFTA_DYNSET_SREG_KEY,
      NFTA_DYNSET_SREG_DATA,
      NFTA_DYNSET_TIMEOUT,
      NFTA_DYNSET_EXPR,
      __NFTA_DYNSET_MAX
    };


.. _`nft_dynset_attributes.constants`:

Constants
---------

:``NFTA_DYNSET_UNSPEC``:
-- undescribed --

:``NFTA_DYNSET_SET_NAME``:
    name of set the to add data to (NLA_STRING)

:``NFTA_DYNSET_SET_ID``:
    uniquely identifier of the set in the transaction (NLA_U32)

:``NFTA_DYNSET_OP``:
    operation (NLA_U32)

:``NFTA_DYNSET_SREG_KEY``:
    source register of the key (NLA_U32)

:``NFTA_DYNSET_SREG_DATA``:
    source register of the data (NLA_U32)

:``NFTA_DYNSET_TIMEOUT``:
    timeout value for the new element (NLA_U64)

:``NFTA_DYNSET_EXPR``:
    expression (NLA_NESTED: nft_expr_attributes)

:``__NFTA_DYNSET_MAX``:
-- undescribed --


.. _`nft_payload_bases`:

enum nft_payload_bases
======================

.. c:type:: nft_payload_bases

    nf_tables payload expression offset bases


.. _`nft_payload_bases.definition`:

Definition
----------

.. code-block:: c

    enum nft_payload_bases {
      NFT_PAYLOAD_LL_HEADER,
      NFT_PAYLOAD_NETWORK_HEADER,
      NFT_PAYLOAD_TRANSPORT_HEADER
    };


.. _`nft_payload_bases.constants`:

Constants
---------

:``NFT_PAYLOAD_LL_HEADER``:
    link layer header

:``NFT_PAYLOAD_NETWORK_HEADER``:
    network header

:``NFT_PAYLOAD_TRANSPORT_HEADER``:
    transport header


.. _`nft_payload_csum_types`:

enum nft_payload_csum_types
===========================

.. c:type:: nft_payload_csum_types

    nf_tables payload expression checksum types


.. _`nft_payload_csum_types.definition`:

Definition
----------

.. code-block:: c

    enum nft_payload_csum_types {
      NFT_PAYLOAD_CSUM_NONE,
      NFT_PAYLOAD_CSUM_INET
    };


.. _`nft_payload_csum_types.constants`:

Constants
---------

:``NFT_PAYLOAD_CSUM_NONE``:
    no checksumming

:``NFT_PAYLOAD_CSUM_INET``:
    internet checksum (RFC 791)


.. _`nft_payload_attributes`:

enum nft_payload_attributes
===========================

.. c:type:: nft_payload_attributes

    nf_tables payload expression netlink attributes


.. _`nft_payload_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_payload_attributes {
      NFTA_PAYLOAD_UNSPEC,
      NFTA_PAYLOAD_DREG,
      NFTA_PAYLOAD_BASE,
      NFTA_PAYLOAD_OFFSET,
      NFTA_PAYLOAD_LEN,
      NFTA_PAYLOAD_SREG,
      NFTA_PAYLOAD_CSUM_TYPE,
      NFTA_PAYLOAD_CSUM_OFFSET,
      __NFTA_PAYLOAD_MAX
    };


.. _`nft_payload_attributes.constants`:

Constants
---------

:``NFTA_PAYLOAD_UNSPEC``:
-- undescribed --

:``NFTA_PAYLOAD_DREG``:
    destination register to load data into (NLA_U32: nft_registers)

:``NFTA_PAYLOAD_BASE``:
    payload base (NLA_U32: nft_payload_bases)

:``NFTA_PAYLOAD_OFFSET``:
    payload offset relative to base (NLA_U32)

:``NFTA_PAYLOAD_LEN``:
    payload length (NLA_U32)

:``NFTA_PAYLOAD_SREG``:
    source register to load data from (NLA_U32: nft_registers)

:``NFTA_PAYLOAD_CSUM_TYPE``:
    checksum type (NLA_U32)

:``NFTA_PAYLOAD_CSUM_OFFSET``:
    checksum offset relative to base (NLA_U32)

:``__NFTA_PAYLOAD_MAX``:
-- undescribed --


.. _`nft_exthdr_attributes`:

enum nft_exthdr_attributes
==========================

.. c:type:: nft_exthdr_attributes

    nf_tables IPv6 extension header expression netlink attributes


.. _`nft_exthdr_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_exthdr_attributes {
      NFTA_EXTHDR_UNSPEC,
      NFTA_EXTHDR_DREG,
      NFTA_EXTHDR_TYPE,
      NFTA_EXTHDR_OFFSET,
      NFTA_EXTHDR_LEN,
      __NFTA_EXTHDR_MAX
    };


.. _`nft_exthdr_attributes.constants`:

Constants
---------

:``NFTA_EXTHDR_UNSPEC``:
-- undescribed --

:``NFTA_EXTHDR_DREG``:
    destination register (NLA_U32: nft_registers)

:``NFTA_EXTHDR_TYPE``:
    extension header type (NLA_U8)

:``NFTA_EXTHDR_OFFSET``:
    extension header offset (NLA_U32)

:``NFTA_EXTHDR_LEN``:
    extension header length (NLA_U32)

:``__NFTA_EXTHDR_MAX``:
-- undescribed --


.. _`nft_meta_keys`:

enum nft_meta_keys
==================

.. c:type:: nft_meta_keys

    nf_tables meta expression keys


.. _`nft_meta_keys.definition`:

Definition
----------

.. code-block:: c

    enum nft_meta_keys {
      NFT_META_LEN,
      NFT_META_PROTOCOL,
      NFT_META_PRIORITY,
      NFT_META_MARK,
      NFT_META_IIF,
      NFT_META_OIF,
      NFT_META_IIFNAME,
      NFT_META_OIFNAME,
      NFT_META_IIFTYPE,
      NFT_META_OIFTYPE,
      NFT_META_SKUID,
      NFT_META_SKGID,
      NFT_META_NFTRACE,
      NFT_META_RTCLASSID,
      NFT_META_SECMARK,
      NFT_META_NFPROTO,
      NFT_META_L4PROTO,
      NFT_META_BRI_IIFNAME,
      NFT_META_BRI_OIFNAME,
      NFT_META_PKTTYPE,
      NFT_META_CPU,
      NFT_META_IIFGROUP,
      NFT_META_OIFGROUP,
      NFT_META_CGROUP,
      NFT_META_PRANDOM
    };


.. _`nft_meta_keys.constants`:

Constants
---------

:``NFT_META_LEN``:
    packet length (skb->len)

:``NFT_META_PROTOCOL``:
    packet ethertype protocol (skb->protocol), invalid in OUTPUT

:``NFT_META_PRIORITY``:
    packet priority (skb->priority)

:``NFT_META_MARK``:
    packet mark (skb->mark)

:``NFT_META_IIF``:
    packet input interface index (dev->ifindex)

:``NFT_META_OIF``:
    packet output interface index (dev->ifindex)

:``NFT_META_IIFNAME``:
    packet input interface name (dev->name)

:``NFT_META_OIFNAME``:
    packet output interface name (dev->name)

:``NFT_META_IIFTYPE``:
    packet input interface type (dev->type)

:``NFT_META_OIFTYPE``:
    packet output interface type (dev->type)

:``NFT_META_SKUID``:
    originating socket UID (fsuid)

:``NFT_META_SKGID``:
    originating socket GID (fsgid)

:``NFT_META_NFTRACE``:
    packet nftrace bit

:``NFT_META_RTCLASSID``:
    realm value of packet's route (skb->dst->tclassid)

:``NFT_META_SECMARK``:
    packet secmark (skb->secmark)

:``NFT_META_NFPROTO``:
    netfilter protocol

:``NFT_META_L4PROTO``:
    layer 4 protocol number

:``NFT_META_BRI_IIFNAME``:
    packet input bridge interface name

:``NFT_META_BRI_OIFNAME``:
    packet output bridge interface name

:``NFT_META_PKTTYPE``:
    packet type (skb->pkt_type), special handling for loopback

:``NFT_META_CPU``:
    cpu id through :c:func:`smp_processor_id`

:``NFT_META_IIFGROUP``:
    packet input interface group

:``NFT_META_OIFGROUP``:
    packet output interface group

:``NFT_META_CGROUP``:
    socket control group (skb->sk->sk_classid)

:``NFT_META_PRANDOM``:
    a 32bit pseudo-random number


.. _`nft_meta_attributes`:

enum nft_meta_attributes
========================

.. c:type:: nft_meta_attributes

    nf_tables meta expression netlink attributes


.. _`nft_meta_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_meta_attributes {
      NFTA_META_UNSPEC,
      NFTA_META_DREG,
      NFTA_META_KEY,
      NFTA_META_SREG,
      __NFTA_META_MAX
    };


.. _`nft_meta_attributes.constants`:

Constants
---------

:``NFTA_META_UNSPEC``:
-- undescribed --

:``NFTA_META_DREG``:
    destination register (NLA_U32)

:``NFTA_META_KEY``:
    meta data item to load (NLA_U32: nft_meta_keys)

:``NFTA_META_SREG``:
    source register (NLA_U32)

:``__NFTA_META_MAX``:
-- undescribed --


.. _`nft_ct_keys`:

enum nft_ct_keys
================

.. c:type:: nft_ct_keys

    nf_tables ct expression keys


.. _`nft_ct_keys.definition`:

Definition
----------

.. code-block:: c

    enum nft_ct_keys {
      NFT_CT_STATE,
      NFT_CT_DIRECTION,
      NFT_CT_STATUS,
      NFT_CT_MARK,
      NFT_CT_SECMARK,
      NFT_CT_EXPIRATION,
      NFT_CT_HELPER,
      NFT_CT_L3PROTOCOL,
      NFT_CT_SRC,
      NFT_CT_DST,
      NFT_CT_PROTOCOL,
      NFT_CT_PROTO_SRC,
      NFT_CT_PROTO_DST,
      NFT_CT_LABELS,
      NFT_CT_PKTS,
      NFT_CT_BYTES
    };


.. _`nft_ct_keys.constants`:

Constants
---------

:``NFT_CT_STATE``:
    conntrack state (bitmask of enum ip_conntrack_info)

:``NFT_CT_DIRECTION``:
    conntrack direction (enum ip_conntrack_dir)

:``NFT_CT_STATUS``:
    conntrack status (bitmask of enum ip_conntrack_status)

:``NFT_CT_MARK``:
    conntrack mark value

:``NFT_CT_SECMARK``:
    conntrack secmark value

:``NFT_CT_EXPIRATION``:
    relative conntrack expiration time in ms

:``NFT_CT_HELPER``:
    connection tracking helper assigned to conntrack

:``NFT_CT_L3PROTOCOL``:
    conntrack layer 3 protocol

:``NFT_CT_SRC``:
    conntrack layer 3 protocol source (IPv4/IPv6 address)

:``NFT_CT_DST``:
    conntrack layer 3 protocol destination (IPv4/IPv6 address)

:``NFT_CT_PROTOCOL``:
    conntrack layer 4 protocol

:``NFT_CT_PROTO_SRC``:
    conntrack layer 4 protocol source

:``NFT_CT_PROTO_DST``:
    conntrack layer 4 protocol destination

:``NFT_CT_LABELS``:
-- undescribed --

:``NFT_CT_PKTS``:
-- undescribed --

:``NFT_CT_BYTES``:
-- undescribed --


.. _`nft_ct_attributes`:

enum nft_ct_attributes
======================

.. c:type:: nft_ct_attributes

    nf_tables ct expression netlink attributes


.. _`nft_ct_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_ct_attributes {
      NFTA_CT_UNSPEC,
      NFTA_CT_DREG,
      NFTA_CT_KEY,
      NFTA_CT_DIRECTION,
      NFTA_CT_SREG,
      __NFTA_CT_MAX
    };


.. _`nft_ct_attributes.constants`:

Constants
---------

:``NFTA_CT_UNSPEC``:
-- undescribed --

:``NFTA_CT_DREG``:
    destination register (NLA_U32)

:``NFTA_CT_KEY``:
    conntrack data item to load (NLA_U32: nft_ct_keys)

:``NFTA_CT_DIRECTION``:
    direction in case of directional keys (NLA_U8)

:``NFTA_CT_SREG``:
    source register (NLA_U32)

:``__NFTA_CT_MAX``:
-- undescribed --


.. _`nft_limit_attributes`:

enum nft_limit_attributes
=========================

.. c:type:: nft_limit_attributes

    nf_tables limit expression netlink attributes


.. _`nft_limit_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_limit_attributes {
      NFTA_LIMIT_UNSPEC,
      NFTA_LIMIT_RATE,
      NFTA_LIMIT_UNIT,
      NFTA_LIMIT_BURST,
      NFTA_LIMIT_TYPE,
      NFTA_LIMIT_FLAGS,
      __NFTA_LIMIT_MAX
    };


.. _`nft_limit_attributes.constants`:

Constants
---------

:``NFTA_LIMIT_UNSPEC``:
-- undescribed --

:``NFTA_LIMIT_RATE``:
    refill rate (NLA_U64)

:``NFTA_LIMIT_UNIT``:
    refill unit (NLA_U64)

:``NFTA_LIMIT_BURST``:
    burst (NLA_U32)

:``NFTA_LIMIT_TYPE``:
    type of limit (NLA_U32: enum nft_limit_type)

:``NFTA_LIMIT_FLAGS``:
    flags (NLA_U32: enum nft_limit_flags)

:``__NFTA_LIMIT_MAX``:
-- undescribed --


.. _`nft_counter_attributes`:

enum nft_counter_attributes
===========================

.. c:type:: nft_counter_attributes

    nf_tables counter expression netlink attributes


.. _`nft_counter_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_counter_attributes {
      NFTA_COUNTER_UNSPEC,
      NFTA_COUNTER_BYTES,
      NFTA_COUNTER_PACKETS,
      __NFTA_COUNTER_MAX
    };


.. _`nft_counter_attributes.constants`:

Constants
---------

:``NFTA_COUNTER_UNSPEC``:
-- undescribed --

:``NFTA_COUNTER_BYTES``:
    number of bytes (NLA_U64)

:``NFTA_COUNTER_PACKETS``:
    number of packets (NLA_U64)

:``__NFTA_COUNTER_MAX``:
-- undescribed --


.. _`nft_log_attributes`:

enum nft_log_attributes
=======================

.. c:type:: nft_log_attributes

    nf_tables log expression netlink attributes


.. _`nft_log_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_log_attributes {
      NFTA_LOG_UNSPEC,
      NFTA_LOG_GROUP,
      NFTA_LOG_PREFIX,
      NFTA_LOG_SNAPLEN,
      NFTA_LOG_QTHRESHOLD,
      NFTA_LOG_LEVEL,
      NFTA_LOG_FLAGS,
      __NFTA_LOG_MAX
    };


.. _`nft_log_attributes.constants`:

Constants
---------

:``NFTA_LOG_UNSPEC``:
-- undescribed --

:``NFTA_LOG_GROUP``:
    netlink group to send messages to (NLA_U32)

:``NFTA_LOG_PREFIX``:
    prefix to prepend to log messages (NLA_STRING)

:``NFTA_LOG_SNAPLEN``:
    length of payload to include in netlink message (NLA_U32)

:``NFTA_LOG_QTHRESHOLD``:
    queue threshold (NLA_U32)

:``NFTA_LOG_LEVEL``:
    log level (NLA_U32)

:``NFTA_LOG_FLAGS``:
    logging flags (NLA_U32)

:``__NFTA_LOG_MAX``:
-- undescribed --


.. _`nft_queue_attributes`:

enum nft_queue_attributes
=========================

.. c:type:: nft_queue_attributes

    nf_tables queue expression netlink attributes


.. _`nft_queue_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_queue_attributes {
      NFTA_QUEUE_UNSPEC,
      NFTA_QUEUE_NUM,
      NFTA_QUEUE_TOTAL,
      NFTA_QUEUE_FLAGS,
      __NFTA_QUEUE_MAX
    };


.. _`nft_queue_attributes.constants`:

Constants
---------

:``NFTA_QUEUE_UNSPEC``:
-- undescribed --

:``NFTA_QUEUE_NUM``:
    netlink queue to send messages to (NLA_U16)

:``NFTA_QUEUE_TOTAL``:
    number of queues to load balance packets on (NLA_U16)

:``NFTA_QUEUE_FLAGS``:
    various flags (NLA_U16)

:``__NFTA_QUEUE_MAX``:
-- undescribed --


.. _`nft_reject_types`:

enum nft_reject_types
=====================

.. c:type:: nft_reject_types

    nf_tables reject expression reject types


.. _`nft_reject_types.definition`:

Definition
----------

.. code-block:: c

    enum nft_reject_types {
      NFT_REJECT_ICMP_UNREACH,
      NFT_REJECT_TCP_RST,
      NFT_REJECT_ICMPX_UNREACH
    };


.. _`nft_reject_types.constants`:

Constants
---------

:``NFT_REJECT_ICMP_UNREACH``:
    reject using ICMP unreachable

:``NFT_REJECT_TCP_RST``:
    reject using TCP RST

:``NFT_REJECT_ICMPX_UNREACH``:
    abstracted ICMP unreachable for bridge and inet


.. _`nft_reject_inet_code`:

enum nft_reject_inet_code
=========================

.. c:type:: nft_reject_inet_code

    Generic reject codes for IPv4/IPv6


.. _`nft_reject_inet_code.definition`:

Definition
----------

.. code-block:: c

    enum nft_reject_inet_code {
      NFT_REJECT_ICMPX_NO_ROUTE,
      NFT_REJECT_ICMPX_PORT_UNREACH,
      NFT_REJECT_ICMPX_HOST_UNREACH,
      NFT_REJECT_ICMPX_ADMIN_PROHIBITED,
      __NFT_REJECT_ICMPX_MAX
    };


.. _`nft_reject_inet_code.constants`:

Constants
---------

:``NFT_REJECT_ICMPX_NO_ROUTE``:
    no route to host / network unreachable

:``NFT_REJECT_ICMPX_PORT_UNREACH``:
    port unreachable

:``NFT_REJECT_ICMPX_HOST_UNREACH``:
    host unreachable

:``NFT_REJECT_ICMPX_ADMIN_PROHIBITED``:
    administratively prohibited

:``__NFT_REJECT_ICMPX_MAX``:
-- undescribed --


.. _`nft_reject_inet_code.description`:

Description
-----------

These codes are mapped to real ICMP and ICMPv6 codes.



.. _`nft_reject_attributes`:

enum nft_reject_attributes
==========================

.. c:type:: nft_reject_attributes

    nf_tables reject expression netlink attributes


.. _`nft_reject_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_reject_attributes {
      NFTA_REJECT_UNSPEC,
      NFTA_REJECT_TYPE,
      NFTA_REJECT_ICMP_CODE,
      __NFTA_REJECT_MAX
    };


.. _`nft_reject_attributes.constants`:

Constants
---------

:``NFTA_REJECT_UNSPEC``:
-- undescribed --

:``NFTA_REJECT_TYPE``:
    packet type to use (NLA_U32: nft_reject_types)

:``NFTA_REJECT_ICMP_CODE``:
    ICMP code to use (NLA_U8)

:``__NFTA_REJECT_MAX``:
-- undescribed --


.. _`nft_nat_types`:

enum nft_nat_types
==================

.. c:type:: nft_nat_types

    nf_tables nat expression NAT types


.. _`nft_nat_types.definition`:

Definition
----------

.. code-block:: c

    enum nft_nat_types {
      NFT_NAT_SNAT,
      NFT_NAT_DNAT
    };


.. _`nft_nat_types.constants`:

Constants
---------

:``NFT_NAT_SNAT``:
    source NAT

:``NFT_NAT_DNAT``:
    destination NAT


.. _`nft_nat_attributes`:

enum nft_nat_attributes
=======================

.. c:type:: nft_nat_attributes

    nf_tables nat expression netlink attributes


.. _`nft_nat_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_nat_attributes {
      NFTA_NAT_UNSPEC,
      NFTA_NAT_TYPE,
      NFTA_NAT_FAMILY,
      NFTA_NAT_REG_ADDR_MIN,
      NFTA_NAT_REG_ADDR_MAX,
      NFTA_NAT_REG_PROTO_MIN,
      NFTA_NAT_REG_PROTO_MAX,
      NFTA_NAT_FLAGS,
      __NFTA_NAT_MAX
    };


.. _`nft_nat_attributes.constants`:

Constants
---------

:``NFTA_NAT_UNSPEC``:
-- undescribed --

:``NFTA_NAT_TYPE``:
    NAT type (NLA_U32: nft_nat_types)

:``NFTA_NAT_FAMILY``:
    NAT family (NLA_U32)

:``NFTA_NAT_REG_ADDR_MIN``:
    source register of address range start (NLA_U32: nft_registers)

:``NFTA_NAT_REG_ADDR_MAX``:
    source register of address range end (NLA_U32: nft_registers)

:``NFTA_NAT_REG_PROTO_MIN``:
    source register of proto range start (NLA_U32: nft_registers)

:``NFTA_NAT_REG_PROTO_MAX``:
    source register of proto range end (NLA_U32: nft_registers)

:``NFTA_NAT_FLAGS``:
    NAT flags (see NF_NAT_RANGE\_\* in linux/netfilter/nf_nat.h) (NLA_U32)

:``__NFTA_NAT_MAX``:
-- undescribed --


.. _`nft_masq_attributes`:

enum nft_masq_attributes
========================

.. c:type:: nft_masq_attributes

    nf_tables masquerade expression attributes


.. _`nft_masq_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_masq_attributes {
      NFTA_MASQ_UNSPEC,
      NFTA_MASQ_FLAGS,
      NFTA_MASQ_REG_PROTO_MIN,
      NFTA_MASQ_REG_PROTO_MAX,
      __NFTA_MASQ_MAX
    };


.. _`nft_masq_attributes.constants`:

Constants
---------

:``NFTA_MASQ_UNSPEC``:
-- undescribed --

:``NFTA_MASQ_FLAGS``:
    NAT flags (see NF_NAT_RANGE\_\* in linux/netfilter/nf_nat.h) (NLA_U32)

:``NFTA_MASQ_REG_PROTO_MIN``:
    source register of proto range start (NLA_U32: nft_registers)

:``NFTA_MASQ_REG_PROTO_MAX``:
    source register of proto range end (NLA_U32: nft_registers)

:``__NFTA_MASQ_MAX``:
-- undescribed --


.. _`nft_redir_attributes`:

enum nft_redir_attributes
=========================

.. c:type:: nft_redir_attributes

    nf_tables redirect expression netlink attributes


.. _`nft_redir_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_redir_attributes {
      NFTA_REDIR_UNSPEC,
      NFTA_REDIR_REG_PROTO_MIN,
      NFTA_REDIR_REG_PROTO_MAX,
      NFTA_REDIR_FLAGS,
      __NFTA_REDIR_MAX
    };


.. _`nft_redir_attributes.constants`:

Constants
---------

:``NFTA_REDIR_UNSPEC``:
-- undescribed --

:``NFTA_REDIR_REG_PROTO_MIN``:
    source register of proto range start (NLA_U32: nft_registers)

:``NFTA_REDIR_REG_PROTO_MAX``:
    source register of proto range end (NLA_U32: nft_registers)

:``NFTA_REDIR_FLAGS``:
    NAT flags (see NF_NAT_RANGE\_\* in linux/netfilter/nf_nat.h) (NLA_U32)

:``__NFTA_REDIR_MAX``:
-- undescribed --


.. _`nft_dup_attributes`:

enum nft_dup_attributes
=======================

.. c:type:: nft_dup_attributes

    nf_tables dup expression netlink attributes


.. _`nft_dup_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_dup_attributes {
      NFTA_DUP_UNSPEC,
      NFTA_DUP_SREG_ADDR,
      NFTA_DUP_SREG_DEV,
      __NFTA_DUP_MAX
    };


.. _`nft_dup_attributes.constants`:

Constants
---------

:``NFTA_DUP_UNSPEC``:
-- undescribed --

:``NFTA_DUP_SREG_ADDR``:
    source register of address (NLA_U32: nft_registers)

:``NFTA_DUP_SREG_DEV``:
    source register of output interface (NLA_U32: nft_register)

:``__NFTA_DUP_MAX``:
-- undescribed --


.. _`nft_fwd_attributes`:

enum nft_fwd_attributes
=======================

.. c:type:: nft_fwd_attributes

    nf_tables fwd expression netlink attributes


.. _`nft_fwd_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_fwd_attributes {
      NFTA_FWD_UNSPEC,
      NFTA_FWD_SREG_DEV,
      __NFTA_FWD_MAX
    };


.. _`nft_fwd_attributes.constants`:

Constants
---------

:``NFTA_FWD_UNSPEC``:
-- undescribed --

:``NFTA_FWD_SREG_DEV``:
    source register of output interface (NLA_U32: nft_register)

:``__NFTA_FWD_MAX``:
-- undescribed --


.. _`nft_gen_attributes`:

enum nft_gen_attributes
=======================

.. c:type:: nft_gen_attributes

    nf_tables ruleset generation attributes


.. _`nft_gen_attributes.definition`:

Definition
----------

.. code-block:: c

    enum nft_gen_attributes {
      NFTA_GEN_UNSPEC,
      NFTA_GEN_ID,
      __NFTA_GEN_MAX
    };


.. _`nft_gen_attributes.constants`:

Constants
---------

:``NFTA_GEN_UNSPEC``:
-- undescribed --

:``NFTA_GEN_ID``:
    Ruleset generation ID (NLA_U32)

:``__NFTA_GEN_MAX``:
-- undescribed --


.. _`nft_trace_attibutes`:

enum nft_trace_attibutes
========================

.. c:type:: nft_trace_attibutes

    nf_tables trace netlink attributes


.. _`nft_trace_attibutes.definition`:

Definition
----------

.. code-block:: c

    enum nft_trace_attibutes {
      NFTA_TRACE_UNSPEC,
      NFTA_TRACE_TABLE,
      NFTA_TRACE_CHAIN,
      NFTA_TRACE_RULE_HANDLE,
      NFTA_TRACE_TYPE,
      NFTA_TRACE_VERDICT,
      NFTA_TRACE_ID,
      NFTA_TRACE_LL_HEADER,
      NFTA_TRACE_NETWORK_HEADER,
      NFTA_TRACE_TRANSPORT_HEADER,
      NFTA_TRACE_IIF,
      NFTA_TRACE_IIFTYPE,
      NFTA_TRACE_OIF,
      NFTA_TRACE_OIFTYPE,
      NFTA_TRACE_MARK,
      NFTA_TRACE_NFPROTO,
      NFTA_TRACE_POLICY,
      __NFTA_TRACE_MAX
    };


.. _`nft_trace_attibutes.constants`:

Constants
---------

:``NFTA_TRACE_UNSPEC``:
-- undescribed --

:``NFTA_TRACE_TABLE``:
    name of the table (NLA_STRING)

:``NFTA_TRACE_CHAIN``:
    name of the chain (NLA_STRING)

:``NFTA_TRACE_RULE_HANDLE``:
    numeric handle of the rule (NLA_U64)

:``NFTA_TRACE_TYPE``:
    type of the event (NLA_U32: nft_trace_types)

:``NFTA_TRACE_VERDICT``:
    verdict returned by hook (NLA_NESTED: nft_verdicts)

:``NFTA_TRACE_ID``:
    pseudo-id, same for each skb traced (NLA_U32)

:``NFTA_TRACE_LL_HEADER``:
    linklayer header (NLA_BINARY)

:``NFTA_TRACE_NETWORK_HEADER``:
    network header (NLA_BINARY)

:``NFTA_TRACE_TRANSPORT_HEADER``:
    transport header (NLA_BINARY)

:``NFTA_TRACE_IIF``:
    indev ifindex (NLA_U32)

:``NFTA_TRACE_IIFTYPE``:
    netdev->type of indev (NLA_U16)

:``NFTA_TRACE_OIF``:
    outdev ifindex (NLA_U32)

:``NFTA_TRACE_OIFTYPE``:
    netdev->type of outdev (NLA_U16)

:``NFTA_TRACE_MARK``:
    nfmark (NLA_U32)

:``NFTA_TRACE_NFPROTO``:
    nf protocol processed (NLA_U32)

:``NFTA_TRACE_POLICY``:
    policy that decided fate of packet (NLA_U32)

:``__NFTA_TRACE_MAX``:
-- undescribed --
