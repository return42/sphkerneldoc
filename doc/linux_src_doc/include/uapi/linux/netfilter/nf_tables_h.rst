.. -*- coding: utf-8; mode: rst -*-

===========
nf_tables.h
===========

.. _`nft_registers`:

enum nft_registers
==================

.. c:type:: enum nft_registers

    nf_tables registers



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


Description
-----------


nf_tables used to have five registers: a verdict register and four data
registers of size 16. The data registers have been changed to 16 registers
of size 4. For compatibility reasons, the NFT_REG_[1-4] registers still
map to areas of size 16, the 4 byte registers are addressed using
NFT_REG32_00 - NFT_REG32_15.


.. _`nft_verdicts`:

enum nft_verdicts
=================

.. c:type:: enum nft_verdicts

    nf_tables internal verdicts



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


Description
-----------

The nf_tables verdicts share their numeric space with the netfilter verdicts.


.. _`nf_tables_msg_types`:

enum nf_tables_msg_types
========================

.. c:type:: enum nf_tables_msg_types

    nf_tables netlink message types



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

.. c:type:: enum nft_list_attributes

    nf_tables generic list netlink attributes



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

.. c:type:: enum nft_hook_attributes

    nf_tables netfilter hook netlink attributes



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

.. c:type:: enum nft_table_flags

    nf_tables table flags



Constants
---------

:``NFT_TABLE_F_DORMANT``:
    this table is not active


.. _`nft_table_attributes`:

enum nft_table_attributes
=========================

.. c:type:: enum nft_table_attributes

    nf_tables table netlink attributes



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

.. c:type:: enum nft_chain_attributes

    nf_tables chain netlink attributes



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

.. c:type:: enum nft_rule_attributes

    nf_tables rule netlink attributes



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

.. c:type:: enum nft_rule_compat_flags

    nf_tables rule compat flags



Constants
---------

:``NFT_RULE_COMPAT_F_INV``:
    invert the check result

:``NFT_RULE_COMPAT_F_MASK``:
    -- undescribed --


.. _`nft_rule_compat_attributes`:

enum nft_rule_compat_attributes
===============================

.. c:type:: enum nft_rule_compat_attributes

    nf_tables rule compat attributes



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

.. c:type:: enum nft_set_flags

    nf_tables set flags



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

.. c:type:: enum nft_set_policies

    set selection policy



Constants
---------

:``NFT_SET_POL_PERFORMANCE``:
    prefer high performance over low memory use

:``NFT_SET_POL_MEMORY``:
    prefer low memory use over high performance


.. _`nft_set_desc_attributes`:

enum nft_set_desc_attributes
============================

.. c:type:: enum nft_set_desc_attributes

    set element description



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

.. c:type:: enum nft_set_attributes

    nf_tables set netlink attributes



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

.. c:type:: enum nft_set_elem_flags

    nf_tables set element flags



Constants
---------

:``NFT_SET_ELEM_INTERVAL_END``:
    element ends the previous interval


.. _`nft_set_elem_attributes`:

enum nft_set_elem_attributes
============================

.. c:type:: enum nft_set_elem_attributes

    nf_tables set element netlink attributes



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

.. c:type:: enum nft_set_elem_list_attributes

    nf_tables set element list netlink attributes



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

.. c:type:: enum nft_data_types

    nf_tables data types



Constants
---------

:``NFT_DATA_VALUE``:
    generic data

:``NFT_DATA_VERDICT``:
    netfilter verdict


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

.. c:type:: enum nft_data_attributes

    nf_tables data netlink attributes



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

.. c:type:: enum nft_verdict_attributes

    nf_tables verdict netlink attributes



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

.. c:type:: enum nft_expr_attributes

    nf_tables expression netlink attributes



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

.. c:type:: enum nft_immediate_attributes

    nf_tables immediate expression netlink attributes



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

.. c:type:: enum nft_bitwise_attributes

    nf_tables bitwise expression netlink attributes



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


Description
-----------

The bitwise expression performs the following operation:

dreg = (sreg & mask) ^ xor

which allow to express all bitwise operations::

                mask        xor

NOT:                1        1
OR:                0        x
XOR:                1        x
AND:                x        0


.. _`nft_byteorder_ops`:

enum nft_byteorder_ops
======================

.. c:type:: enum nft_byteorder_ops

    nf_tables byteorder operators



Constants
---------

:``NFT_BYTEORDER_NTOH``:
    network to host operator

:``NFT_BYTEORDER_HTON``:
    host to network opertaor


.. _`nft_byteorder_attributes`:

enum nft_byteorder_attributes
=============================

.. c:type:: enum nft_byteorder_attributes

    nf_tables byteorder expression netlink attributes



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

.. c:type:: enum nft_cmp_ops

    nf_tables relational operator



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

.. c:type:: enum nft_cmp_attributes

    nf_tables cmp expression netlink attributes



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

.. c:type:: enum nft_lookup_attributes

    nf_tables set lookup expression netlink attributes



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

.. c:type:: enum nft_dynset_attributes

    dynset expression attributes



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

.. c:type:: enum nft_payload_bases

    nf_tables payload expression offset bases



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

.. c:type:: enum nft_payload_csum_types

    nf_tables payload expression checksum types



Constants
---------

:``NFT_PAYLOAD_CSUM_NONE``:
    no checksumming

:``NFT_PAYLOAD_CSUM_INET``:
    internet checksum (RFC 791)


.. _`nft_payload_attributes`:

enum nft_payload_attributes
===========================

.. c:type:: enum nft_payload_attributes

    nf_tables payload expression netlink attributes



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

.. c:type:: enum nft_exthdr_attributes

    nf_tables IPv6 extension header expression netlink attributes



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

.. c:type:: enum nft_meta_keys

    nf_tables meta expression keys



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

.. c:type:: enum nft_meta_attributes

    nf_tables meta expression netlink attributes



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

.. c:type:: enum nft_ct_keys

    nf_tables ct expression keys



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

.. c:type:: enum nft_ct_attributes

    nf_tables ct expression netlink attributes



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

.. c:type:: enum nft_limit_attributes

    nf_tables limit expression netlink attributes



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

.. c:type:: enum nft_counter_attributes

    nf_tables counter expression netlink attributes



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

.. c:type:: enum nft_log_attributes

    nf_tables log expression netlink attributes



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

.. c:type:: enum nft_queue_attributes

    nf_tables queue expression netlink attributes



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

.. c:type:: enum nft_reject_types

    nf_tables reject expression reject types



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

.. c:type:: enum nft_reject_inet_code

    Generic reject codes for IPv4/IPv6



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


Description
-----------

These codes are mapped to real ICMP and ICMPv6 codes.


.. _`nft_reject_attributes`:

enum nft_reject_attributes
==========================

.. c:type:: enum nft_reject_attributes

    nf_tables reject expression netlink attributes



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

.. c:type:: enum nft_nat_types

    nf_tables nat expression NAT types



Constants
---------

:``NFT_NAT_SNAT``:
    source NAT

:``NFT_NAT_DNAT``:
    destination NAT


.. _`nft_nat_attributes`:

enum nft_nat_attributes
=======================

.. c:type:: enum nft_nat_attributes

    nf_tables nat expression netlink attributes



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
    NAT flags (see NF_NAT_RANGE_\* in linux/netfilter/nf_nat.h) (NLA_U32)

:``__NFTA_NAT_MAX``:
    -- undescribed --


.. _`nft_masq_attributes`:

enum nft_masq_attributes
========================

.. c:type:: enum nft_masq_attributes

    nf_tables masquerade expression attributes



Constants
---------

:``NFTA_MASQ_UNSPEC``:
    -- undescribed --

:``NFTA_MASQ_FLAGS``:
    NAT flags (see NF_NAT_RANGE_\* in linux/netfilter/nf_nat.h) (NLA_U32)

:``NFTA_MASQ_REG_PROTO_MIN``:
    source register of proto range start (NLA_U32: nft_registers)

:``NFTA_MASQ_REG_PROTO_MAX``:
    source register of proto range end (NLA_U32: nft_registers)

:``__NFTA_MASQ_MAX``:
    -- undescribed --


.. _`nft_redir_attributes`:

enum nft_redir_attributes
=========================

.. c:type:: enum nft_redir_attributes

    nf_tables redirect expression netlink attributes



Constants
---------

:``NFTA_REDIR_UNSPEC``:
    -- undescribed --

:``NFTA_REDIR_REG_PROTO_MIN``:
    source register of proto range start (NLA_U32: nft_registers)

:``NFTA_REDIR_REG_PROTO_MAX``:
    source register of proto range end (NLA_U32: nft_registers)

:``NFTA_REDIR_FLAGS``:
    NAT flags (see NF_NAT_RANGE_\* in linux/netfilter/nf_nat.h) (NLA_U32)

:``__NFTA_REDIR_MAX``:
    -- undescribed --


.. _`nft_dup_attributes`:

enum nft_dup_attributes
=======================

.. c:type:: enum nft_dup_attributes

    nf_tables dup expression netlink attributes



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

.. c:type:: enum nft_fwd_attributes

    nf_tables fwd expression netlink attributes



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

.. c:type:: enum nft_gen_attributes

    nf_tables ruleset generation attributes



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

.. c:type:: enum nft_trace_attibutes

    nf_tables trace netlink attributes



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

