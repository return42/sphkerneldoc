.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/pkt_cls.h

.. _`tcf_exts_has_actions`:

tcf_exts_has_actions
====================

.. c:function:: bool tcf_exts_has_actions(struct tcf_exts *exts)

    check if at least one action is present

    :param struct tcf_exts \*exts:
        tc filter extensions handle

.. _`tcf_exts_has_actions.description`:

Description
-----------

Returns true if at least one action is present.

.. _`tcf_exts_has_one_action`:

tcf_exts_has_one_action
=======================

.. c:function:: bool tcf_exts_has_one_action(struct tcf_exts *exts)

    check if exactly one action is present

    :param struct tcf_exts \*exts:
        tc filter extensions handle

.. _`tcf_exts_has_one_action.description`:

Description
-----------

Returns true if exactly one action is present.

.. _`tcf_exts_exec`:

tcf_exts_exec
=============

.. c:function:: int tcf_exts_exec(struct sk_buff *skb, struct tcf_exts *exts, struct tcf_result *res)

    execute tc filter extensions

    :param struct sk_buff \*skb:
        socket buffer

    :param struct tcf_exts \*exts:
        tc filter extensions handle

    :param struct tcf_result \*res:
        desired result

.. _`tcf_exts_exec.description`:

Description
-----------

Executes all configured extensions. Returns TC_ACT_OK on a normal execution,
a negative number if the filter must be considered unmatched or
a positive action code (TC_ACT\_\*) which must be returned to the
underlying layer.

.. _`tcf_pkt_info`:

struct tcf_pkt_info
===================

.. c:type:: struct tcf_pkt_info

    packet information

.. _`tcf_pkt_info.definition`:

Definition
----------

.. code-block:: c

    struct tcf_pkt_info {
        unsigned char *ptr;
        int nexthdr;
    }

.. _`tcf_pkt_info.members`:

Members
-------

ptr
    *undescribed*

nexthdr
    *undescribed*

.. _`tcf_ematch`:

struct tcf_ematch
=================

.. c:type:: struct tcf_ematch

    extended match (ematch)

.. _`tcf_ematch.definition`:

Definition
----------

.. code-block:: c

    struct tcf_ematch {
        struct tcf_ematch_ops *ops;
        unsigned long data;
        unsigned int datalen;
        u16 matchid;
        u16 flags;
        struct net *net;
    }

.. _`tcf_ematch.members`:

Members
-------

ops
    the operations lookup table of the corresponding ematch module

data
    ematch specific data

datalen
    length of the ematch specific configuration data

matchid
    identifier to allow userspace to reidentify a match

flags
    flags specifying attributes and the relation to other matches

net
    *undescribed*

.. _`tcf_ematch_tree`:

struct tcf_ematch_tree
======================

.. c:type:: struct tcf_ematch_tree

    ematch tree handle

.. _`tcf_ematch_tree.definition`:

Definition
----------

.. code-block:: c

    struct tcf_ematch_tree {
        struct tcf_ematch_tree_hdr hdr;
        struct tcf_ematch *matches;
    }

.. _`tcf_ematch_tree.members`:

Members
-------

hdr
    ematch tree header supplied by userspace

matches
    array of ematches

.. _`tcf_ematch_ops`:

struct tcf_ematch_ops
=====================

.. c:type:: struct tcf_ematch_ops

    ematch module operations

.. _`tcf_ematch_ops.definition`:

Definition
----------

.. code-block:: c

    struct tcf_ematch_ops {
        int kind;
        int datalen;
        int (*change)(struct net *net, void *, int, struct tcf_ematch *);
        int (*match)(struct sk_buff *, struct tcf_ematch *, struct tcf_pkt_info *);
        void (*destroy)(struct tcf_ematch *);
        int (*dump)(struct sk_buff *, struct tcf_ematch *);
        struct module *owner;
        struct list_head link;
    }

.. _`tcf_ematch_ops.members`:

Members
-------

kind
    identifier (kind) of this ematch module

datalen
    length of expected configuration data (optional)

change
    called during validation (optional)

match
    called during ematch tree evaluation, must return 1/0

destroy
    called during destroyage (optional)

dump
    called during dumping process (optional)

owner
    owner, must be set to THIS_MODULE

link
    link to previous/next ematch module (internal use)

.. _`tcf_em_tree_match`:

tcf_em_tree_match
=================

.. c:function:: int tcf_em_tree_match(struct sk_buff *skb, struct tcf_ematch_tree *tree, struct tcf_pkt_info *info)

    evaulate an ematch tree

    :param struct sk_buff \*skb:
        socket buffer of the packet in question

    :param struct tcf_ematch_tree \*tree:
        ematch tree to be used for evaluation

    :param struct tcf_pkt_info \*info:
        packet information examined by classifier

.. _`tcf_em_tree_match.description`:

Description
-----------

This function matches \ ``skb``\  against the ematch tree in \ ``tree``\  by going
through all ematches respecting their logic relations returning
as soon as the result is obvious.

Returns 1 if the ematch tree as-one matches, no ematches are configured
or ematch is not enabled in the kernel, otherwise 0 is returned.

.. This file was automatic generated / don't edit.

