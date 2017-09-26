.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/netfilter/nf_tables.h

.. _`nft_verdict`:

struct nft_verdict
==================

.. c:type:: struct nft_verdict

    nf_tables verdict

.. _`nft_verdict.definition`:

Definition
----------

.. code-block:: c

    struct nft_verdict {
        u32 code;
        struct nft_chain *chain;
    }

.. _`nft_verdict.members`:

Members
-------

code
    nf_tables/netfilter verdict code

chain
    destination chain for NFT_JUMP/NFT_GOTO

.. _`nft_regs`:

struct nft_regs
===============

.. c:type:: struct nft_regs

    nf_tables register set

.. _`nft_regs.definition`:

Definition
----------

.. code-block:: c

    struct nft_regs {
        union {
            u32 data[20];
            struct nft_verdict verdict;
        } ;
    }

.. _`nft_regs.members`:

Members
-------

{unnamed_union}
    anonymous

data
    data registers

verdict
    verdict register

.. _`nft_regs.description`:

Description
-----------

The first four data registers alias to the verdict register.

.. _`nft_ctx`:

struct nft_ctx
==============

.. c:type:: struct nft_ctx

    nf_tables rule/set context

.. _`nft_ctx.definition`:

Definition
----------

.. code-block:: c

    struct nft_ctx {
        struct net *net;
        struct nft_af_info *afi;
        struct nft_table *table;
        struct nft_chain *chain;
        const struct nlattr * const *nla;
        u32 portid;
        u32 seq;
        bool report;
    }

.. _`nft_ctx.members`:

Members
-------

net
    net namespace

afi
    address family info

table
    the table the chain is contained in

chain
    the chain the rule is contained in

nla
    netlink attributes

portid
    netlink portID of the original message

seq
    netlink sequence number

report
    notify via unicast netlink message

.. _`nft_userdata`:

struct nft_userdata
===================

.. c:type:: struct nft_userdata

    user defined data associated with an object

.. _`nft_userdata.definition`:

Definition
----------

.. code-block:: c

    struct nft_userdata {
        u8 len;
        unsigned char data[0];
    }

.. _`nft_userdata.members`:

Members
-------

len
    length of the data

data
    content

.. _`nft_userdata.description`:

Description
-----------

The presence of user data is indicated in an object specific fashion,
so a length of zero can't occur and the value "len" indicates data
of length len + 1.

.. _`nft_set_elem`:

struct nft_set_elem
===================

.. c:type:: struct nft_set_elem

    generic representation of set elements

.. _`nft_set_elem.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_elem {
        union {
            u32 buf[NFT_DATA_VALUE_MAXLEN / sizeof(u32)];
            struct nft_data val;
        } key;
        void *priv;
    }

.. _`nft_set_elem.members`:

Members
-------

key
    element key

priv
    element private data and extensions

.. _`nft_set_desc`:

struct nft_set_desc
===================

.. c:type:: struct nft_set_desc

    description of set elements

.. _`nft_set_desc.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_desc {
        unsigned int klen;
        unsigned int dlen;
        unsigned int size;
    }

.. _`nft_set_desc.members`:

Members
-------

klen
    key length

dlen
    data length

size
    number of set elements

.. _`nft_set_class`:

enum nft_set_class
==================

.. c:type:: enum nft_set_class

    performance class

.. _`nft_set_class.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_class {
        NFT_SET_CLASS_O_1,
        NFT_SET_CLASS_O_LOG_N,
        NFT_SET_CLASS_O_N
    };

.. _`nft_set_class.constants`:

Constants
---------

NFT_SET_CLASS_O_1
    *undescribed*

NFT_SET_CLASS_O_LOG_N
    *undescribed*

NFT_SET_CLASS_O_N
    *undescribed*

.. _`nft_set_estimate`:

struct nft_set_estimate
=======================

.. c:type:: struct nft_set_estimate

    estimation of memory and performance characteristics

.. _`nft_set_estimate.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_estimate {
        unsigned int size;
        enum nft_set_class lookup;
        enum nft_set_class space;
    }

.. _`nft_set_estimate.members`:

Members
-------

size
    required memory

lookup
    lookup performance class

space
    memory class

.. _`nft_set_type`:

struct nft_set_type
===================

.. c:type:: struct nft_set_type

    nf_tables set type

.. _`nft_set_type.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_type {
        const struct nft_set_ops *(*select_ops)(const struct nft_ctx *,const struct nft_set_desc *desc, u32 flags);
        const struct nft_set_ops *ops;
        struct list_head list;
        struct module *owner;
    }

.. _`nft_set_type.members`:

Members
-------

select_ops
    function to select nft_set_ops

ops
    default ops, used when no select_ops functions is present

list
    used internally

owner
    module reference

.. _`nft_set_ops`:

struct nft_set_ops
==================

.. c:type:: struct nft_set_ops

    nf_tables set operations

.. _`nft_set_ops.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_ops {
        bool (*lookup)(const struct net *net,const struct nft_set *set,const u32 *key, const struct nft_set_ext **ext);
        bool (*update)(struct nft_set *set,const u32 *key,void *(*new)(struct nft_set *,const struct nft_expr *,struct nft_regs *),const struct nft_expr *expr,struct nft_regs *regs, const struct nft_set_ext **ext);
        int (*insert)(const struct net *net,const struct nft_set *set,const struct nft_set_elem *elem, struct nft_set_ext **ext);
        void (*activate)(const struct net *net,const struct nft_set *set, const struct nft_set_elem *elem);
        void * (*deactivate)(const struct net *net,const struct nft_set *set, const struct nft_set_elem *elem);
        bool (*flush)(const struct net *net,const struct nft_set *set, void *priv);
        void (*remove)(const struct net *net,const struct nft_set *set, const struct nft_set_elem *elem);
        void (*walk)(const struct nft_ctx *ctx,struct nft_set *set, struct nft_set_iter *iter);
        unsigned int (*privsize)(const struct nlattr * const nla[], const struct nft_set_desc *desc);
        bool (*estimate)(const struct nft_set_desc *desc,u32 features, struct nft_set_estimate *est);
        int (*init)(const struct nft_set *set,const struct nft_set_desc *desc, const struct nlattr * const nla[]);
        void (*destroy)(const struct nft_set *set);
        unsigned int elemsize;
        u32 features;
        const struct nft_set_type *type;
    }

.. _`nft_set_ops.members`:

Members
-------

lookup
    look up an element within the set

update
    *undescribed*

insert
    insert new element into set

activate
    activate new element in the next generation

deactivate
    lookup for element and deactivate it in the next generation

flush
    deactivate element in the next generation

remove
    remove element from set

walk
    iterate over all set elemeennts

privsize
    function to return size of set private data

estimate
    *undescribed*

init
    initialize private data of new set instance

destroy
    destroy private data of set instance

elemsize
    element private size

features
    features supported by the implementation

type
    *undescribed*

.. _`nft_set`:

struct nft_set
==============

.. c:type:: struct nft_set

    nf_tables set instance

.. _`nft_set.definition`:

Definition
----------

.. code-block:: c

    struct nft_set {
        struct list_head list;
        struct list_head bindings;
        char *name;
        u32 ktype;
        u32 dtype;
        u32 objtype;
        u32 size;
        atomic_t nelems;
        u32 ndeact;
        u64 timeout;
        u32 gc_int;
        u16 policy;
        u16 udlen;
        unsigned char *udata;
        const struct nft_set_ops *ops ____cacheline_aligned;
        u16 flags:14, genmask:2;
        u8 klen;
        u8 dlen;
        unsigned char data[] __attribute__((aligned(__alignof__(u64))));
    }

.. _`nft_set.members`:

Members
-------

list
    table set list node

bindings
    list of set bindings

name
    name of the set

ktype
    key type (numeric type defined by userspace, not used in the kernel)

dtype
    data type (verdict or numeric type defined by userspace)

objtype
    object type (see NFT_OBJECT\_\* definitions)

size
    maximum set size

nelems
    number of elements

ndeact
    number of deactivated elements queued for removal

timeout
    default timeout value in jiffies

gc_int
    garbage collection interval in msecs

policy
    set parameterization (see enum nft_set_policies)

udlen
    user data length

udata
    user data

____cacheline_aligned
    *undescribed*

flags
    set flags

genmask
    generation mask

klen
    key length

dlen
    data length

data
    private set data

.. _`nft_set_binding`:

struct nft_set_binding
======================

.. c:type:: struct nft_set_binding

    nf_tables set binding

.. _`nft_set_binding.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_binding {
        struct list_head list;
        const struct nft_chain *chain;
        u32 flags;
    }

.. _`nft_set_binding.members`:

Members
-------

list
    set bindings list node

chain
    chain containing the rule bound to the set

flags
    set action flags

.. _`nft_set_binding.description`:

Description
-----------

A set binding contains all information necessary for validation
of new elements added to a bound set.

.. _`nft_set_extensions`:

enum nft_set_extensions
=======================

.. c:type:: enum nft_set_extensions

    set extension type IDs

.. _`nft_set_extensions.definition`:

Definition
----------

.. code-block:: c

    enum nft_set_extensions {
        NFT_SET_EXT_KEY,
        NFT_SET_EXT_DATA,
        NFT_SET_EXT_FLAGS,
        NFT_SET_EXT_TIMEOUT,
        NFT_SET_EXT_EXPIRATION,
        NFT_SET_EXT_USERDATA,
        NFT_SET_EXT_EXPR,
        NFT_SET_EXT_OBJREF,
        NFT_SET_EXT_NUM
    };

.. _`nft_set_extensions.constants`:

Constants
---------

NFT_SET_EXT_KEY
    element key

NFT_SET_EXT_DATA
    mapping data

NFT_SET_EXT_FLAGS
    element flags

NFT_SET_EXT_TIMEOUT
    element timeout

NFT_SET_EXT_EXPIRATION
    element expiration time

NFT_SET_EXT_USERDATA
    user data associated with the element

NFT_SET_EXT_EXPR
    expression assiociated with the element

NFT_SET_EXT_OBJREF
    stateful object reference associated with element

NFT_SET_EXT_NUM
    number of extension types

.. _`nft_set_ext_type`:

struct nft_set_ext_type
=======================

.. c:type:: struct nft_set_ext_type

    set extension type

.. _`nft_set_ext_type.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_ext_type {
        u8 len;
        u8 align;
    }

.. _`nft_set_ext_type.members`:

Members
-------

len
    fixed part length of the extension

align
    alignment requirements of the extension

.. _`nft_set_ext_tmpl`:

struct nft_set_ext_tmpl
=======================

.. c:type:: struct nft_set_ext_tmpl

    set extension template

.. _`nft_set_ext_tmpl.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_ext_tmpl {
        u16 len;
        u8 offset[NFT_SET_EXT_NUM];
    }

.. _`nft_set_ext_tmpl.members`:

Members
-------

len
    length of extension area

offset
    offsets of individual extension types

.. _`nft_set_ext`:

struct nft_set_ext
==================

.. c:type:: struct nft_set_ext

    set extensions

.. _`nft_set_ext.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_ext {
        u8 genmask;
        u8 offset[NFT_SET_EXT_NUM];
        char data[0];
    }

.. _`nft_set_ext.members`:

Members
-------

genmask
    generation mask

offset
    offsets of individual extension types

data
    beginning of extension data

.. _`nft_set_gc_batch_head`:

struct nft_set_gc_batch_head
============================

.. c:type:: struct nft_set_gc_batch_head

    nf_tables set garbage collection batch

.. _`nft_set_gc_batch_head.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_gc_batch_head {
        struct rcu_head rcu;
        const struct nft_set *set;
        unsigned int cnt;
    }

.. _`nft_set_gc_batch_head.members`:

Members
-------

rcu
    rcu head

set
    set the elements belong to

cnt
    count of elements

.. _`nft_set_gc_batch`:

struct nft_set_gc_batch
=======================

.. c:type:: struct nft_set_gc_batch

    nf_tables set garbage collection batch

.. _`nft_set_gc_batch.definition`:

Definition
----------

.. code-block:: c

    struct nft_set_gc_batch {
        struct nft_set_gc_batch_head head;
        void *elems[NFT_SET_GC_BATCH_SIZE];
    }

.. _`nft_set_gc_batch.members`:

Members
-------

head
    GC batch head

elems
    garbage collection elements

.. _`nft_expr_type`:

struct nft_expr_type
====================

.. c:type:: struct nft_expr_type

    nf_tables expression type

.. _`nft_expr_type.definition`:

Definition
----------

.. code-block:: c

    struct nft_expr_type {
        const struct nft_expr_ops *(*select_ops)(const struct nft_ctx *, const struct nlattr * const tb[]);
        const struct nft_expr_ops *ops;
        struct list_head list;
        const char *name;
        struct module *owner;
        const struct nla_policy *policy;
        unsigned int maxattr;
        u8 family;
        u8 flags;
    }

.. _`nft_expr_type.members`:

Members
-------

select_ops
    function to select nft_expr_ops

ops
    default ops, used when no select_ops functions is present

list
    used internally

name
    Identifier

owner
    module reference

policy
    netlink attribute policy

maxattr
    highest netlink attribute number

family
    address family for AF-specific types

flags
    expression type flags

.. _`nft_expr`:

struct nft_expr
===============

.. c:type:: struct nft_expr

    nf_tables expression

.. _`nft_expr.definition`:

Definition
----------

.. code-block:: c

    struct nft_expr {
        const struct nft_expr_ops *ops;
        unsigned char data[];
    }

.. _`nft_expr.members`:

Members
-------

ops
    expression ops

data
    expression private data

.. _`nft_rule`:

struct nft_rule
===============

.. c:type:: struct nft_rule

    nf_tables rule

.. _`nft_rule.definition`:

Definition
----------

.. code-block:: c

    struct nft_rule {
        struct list_head list;
        u64 handle:42,genmask:2,dlen:12, udata:1;
        unsigned char data[] __attribute__((aligned(__alignof__(struct nft_expr))));
    }

.. _`nft_rule.members`:

Members
-------

list
    used internally

handle
    rule handle

genmask
    generation mask

dlen
    length of expression data

udata
    user data is appended to the rule

data
    expression data

.. _`nft_chain`:

struct nft_chain
================

.. c:type:: struct nft_chain

    nf_tables chain

.. _`nft_chain.definition`:

Definition
----------

.. code-block:: c

    struct nft_chain {
        struct list_head rules;
        struct list_head list;
        struct nft_table *table;
        u64 handle;
        u32 use;
        u16 level;
        u8 flags:6, genmask:2;
        char *name;
    }

.. _`nft_chain.members`:

Members
-------

rules
    list of rules in the chain

list
    used internally

table
    table that this chain belongs to

handle
    chain handle

use
    number of jump references to this chain

level
    length of longest path to this chain

flags
    bitmask of enum nft_chain_flags

genmask
    *undescribed*

name
    name of the chain

.. _`nf_chain_type`:

struct nf_chain_type
====================

.. c:type:: struct nf_chain_type

    nf_tables chain type info

.. _`nf_chain_type.definition`:

Definition
----------

.. code-block:: c

    struct nf_chain_type {
        const char *name;
        enum nft_chain_type type;
        int family;
        struct module *owner;
        unsigned int hook_mask;
        nf_hookfn *hooks[NF_MAX_HOOKS];
    }

.. _`nf_chain_type.members`:

Members
-------

name
    name of the type

type
    numeric identifier

family
    address family

owner
    module owner

hook_mask
    mask of valid hooks

hooks
    hookfn overrides

.. _`nft_base_chain`:

struct nft_base_chain
=====================

.. c:type:: struct nft_base_chain

    nf_tables base chain

.. _`nft_base_chain.definition`:

Definition
----------

.. code-block:: c

    struct nft_base_chain {
        struct nf_hook_ops ops[NFT_HOOK_OPS_MAX];
        const struct nf_chain_type *type;
        u8 policy;
        u8 flags;
        struct nft_stats __percpu *stats;
        struct nft_chain chain;
        char dev_name[IFNAMSIZ];
    }

.. _`nft_base_chain.members`:

Members
-------

ops
    netfilter hook ops

type
    chain type

policy
    default policy

flags
    *undescribed*

stats
    per-cpu chain stats

chain
    the chain

dev_name
    device name that this base chain is attached to (if any)

.. _`nft_table`:

struct nft_table
================

.. c:type:: struct nft_table

    nf_tables table

.. _`nft_table.definition`:

Definition
----------

.. code-block:: c

    struct nft_table {
        struct list_head list;
        struct list_head chains;
        struct list_head sets;
        struct list_head objects;
        u64 hgenerator;
        u32 use;
        u16 flags:14, genmask:2;
        char *name;
    }

.. _`nft_table.members`:

Members
-------

list
    used internally

chains
    chains in the table

sets
    sets in the table

objects
    stateful objects in the table

hgenerator
    handle generator state

use
    number of chain references to this table

flags
    table flag (see enum nft_table_flags)

genmask
    generation mask

name
    name of the table

.. _`nft_af_info`:

struct nft_af_info
==================

.. c:type:: struct nft_af_info

    nf_tables address family info

.. _`nft_af_info.definition`:

Definition
----------

.. code-block:: c

    struct nft_af_info {
        struct list_head list;
        int family;
        unsigned int nhooks;
        struct module *owner;
        struct list_head tables;
        u32 flags;
        unsigned int nops;
        void (*hook_ops_init)(struct nf_hook_ops *, unsigned int);
        nf_hookfn *hooks[NF_MAX_HOOKS];
    }

.. _`nft_af_info.members`:

Members
-------

list
    used internally

family
    address family

nhooks
    number of hooks in this family

owner
    module owner

tables
    used internally

flags
    family flags

nops
    number of hook ops in this family

hook_ops_init
    initialization function for chain hook ops

hooks
    hookfn overrides for packet validation

.. _`nft_object`:

struct nft_object
=================

.. c:type:: struct nft_object

    nf_tables stateful object

.. _`nft_object.definition`:

Definition
----------

.. code-block:: c

    struct nft_object {
        struct list_head list;
        char *name;
        struct nft_table *table;
        u32 genmask:2, use:30;
        const struct nft_object_ops *ops ____cacheline_aligned;
        unsigned char data[] __attribute__((aligned(__alignof__(u64))));
    }

.. _`nft_object.members`:

Members
-------

list
    table stateful object list node

name
    name of this stateful object

table
    table this object belongs to

genmask
    generation mask

use
    number of references to this stateful object

____cacheline_aligned
    *undescribed*

data
    pointer to object data

.. _`nft_object_type`:

struct nft_object_type
======================

.. c:type:: struct nft_object_type

    stateful object type

.. _`nft_object_type.definition`:

Definition
----------

.. code-block:: c

    struct nft_object_type {
        const struct nft_object_ops *(*select_ops)(const struct nft_ctx *, const struct nlattr * const tb[]);
        const struct nft_object_ops *ops;
        struct list_head list;
        u32 type;
        unsigned int maxattr;
        struct module *owner;
        const struct nla_policy *policy;
    }

.. _`nft_object_type.members`:

Members
-------

select_ops
    function to select nft_object_ops

ops
    default ops, used when no select_ops functions is present

list
    list node in list of object types

type
    stateful object numeric type

maxattr
    maximum netlink attribute

owner
    module owner

policy
    netlink attribute policy

.. _`nft_object_ops`:

struct nft_object_ops
=====================

.. c:type:: struct nft_object_ops

    stateful object operations

.. _`nft_object_ops.definition`:

Definition
----------

.. code-block:: c

    struct nft_object_ops {
        void (*eval)(struct nft_object *obj,struct nft_regs *regs, const struct nft_pktinfo *pkt);
        unsigned int size;
        int (*init)(const struct nft_ctx *ctx,const struct nlattr *const tb[], struct nft_object *obj);
        void (*destroy)(struct nft_object *obj);
        int (*dump)(struct sk_buff *skb,struct nft_object *obj, bool reset);
        const struct nft_object_type *type;
    }

.. _`nft_object_ops.members`:

Members
-------

eval
    stateful object evaluation function

size
    stateful object size

init
    initialize object from netlink attributes

destroy
    release existing stateful object

dump
    netlink dump stateful object

type
    *undescribed*

.. _`nft_traceinfo`:

struct nft_traceinfo
====================

.. c:type:: struct nft_traceinfo

    nft tracing information and state

.. _`nft_traceinfo.definition`:

Definition
----------

.. code-block:: c

    struct nft_traceinfo {
        const struct nft_pktinfo *pkt;
        const struct nft_base_chain *basechain;
        const struct nft_chain *chain;
        const struct nft_rule *rule;
        const struct nft_verdict *verdict;
        enum nft_trace_types type;
        bool packet_dumped;
        bool trace;
    }

.. _`nft_traceinfo.members`:

Members
-------

pkt
    pktinfo currently processed

basechain
    base chain currently processed

chain
    chain currently processed

rule
    rule that was evaluated

verdict
    verdict given by rule

type
    event type (enum nft_trace_types)

packet_dumped
    packet headers sent in a previous traceinfo message

trace
    other struct members are initialised

.. _`nft_trans`:

struct nft_trans
================

.. c:type:: struct nft_trans

    nf_tables object update in transaction

.. _`nft_trans.definition`:

Definition
----------

.. code-block:: c

    struct nft_trans {
        struct list_head list;
        int msg_type;
        struct nft_ctx ctx;
        char data[0];
    }

.. _`nft_trans.members`:

Members
-------

list
    used internally

msg_type
    message type

ctx
    transaction context

data
    internal information related to the transaction

.. This file was automatic generated / don't edit.

