.. -*- coding: utf-8; mode: rst -*-

=========
pkt_cls.h
=========


.. _`tcf_exts_is_predicative`:

tcf_exts_is_predicative
=======================

.. c:function:: int tcf_exts_is_predicative (struct tcf_exts *exts)

    check if a predicative extension is present

    :param struct tcf_exts \*exts:
        tc filter extensions handle



.. _`tcf_exts_is_predicative.description`:

Description
-----------

Returns 1 if a predicative extension is present, i.e. an extension which
might cause further actions and thus overrule the regular tcf_result.



.. _`tcf_exts_is_available`:

tcf_exts_is_available
=====================

.. c:function:: int tcf_exts_is_available (struct tcf_exts *exts)

    check if at least one extension is present

    :param struct tcf_exts \*exts:
        tc filter extensions handle



.. _`tcf_exts_is_available.description`:

Description
-----------

Returns 1 if at least one extension is present.



.. _`tcf_exts_exec`:

tcf_exts_exec
=============

.. c:function:: int tcf_exts_exec (struct sk_buff *skb, struct tcf_exts *exts, struct tcf_result *res)

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

Executes all configured extensions. Returns 0 on a normal execution,
a negative number if the filter must be considered unmatched or
a positive action code (TC_ACT\_\*) which must be returned to the
underlying layer.



.. _`tcf_pkt_info`:

struct tcf_pkt_info
===================

.. c:type:: tcf_pkt_info

    packet information


.. _`tcf_pkt_info.definition`:

Definition
----------

.. code-block:: c

  struct tcf_pkt_info {
  };


.. _`tcf_pkt_info.members`:

Members
-------




.. _`tcf_ematch`:

struct tcf_ematch
=================

.. c:type:: tcf_ematch

    extended match (ematch)


.. _`tcf_ematch.definition`:

Definition
----------

.. code-block:: c

  struct tcf_ematch {
    struct tcf_ematch_ops * ops;
    unsigned long data;
    unsigned int datalen;
    u16 matchid;
    u16 flags;
  };


.. _`tcf_ematch.members`:

Members
-------

:``ops``:
    the operations lookup table of the corresponding ematch module

:``data``:
    ematch specific data

:``datalen``:
    length of the ematch specific configuration data

:``matchid``:
    identifier to allow userspace to reidentify a match

:``flags``:
    flags specifying attributes and the relation to other matches




.. _`tcf_ematch_tree`:

struct tcf_ematch_tree
======================

.. c:type:: tcf_ematch_tree

    ematch tree handle


.. _`tcf_ematch_tree.definition`:

Definition
----------

.. code-block:: c

  struct tcf_ematch_tree {
    struct tcf_ematch_tree_hdr hdr;
    struct tcf_ematch * matches;
  };


.. _`tcf_ematch_tree.members`:

Members
-------

:``hdr``:
    ematch tree header supplied by userspace

:``matches``:
    array of ematches




.. _`tcf_ematch_ops`:

struct tcf_ematch_ops
=====================

.. c:type:: tcf_ematch_ops

    ematch module operations


.. _`tcf_ematch_ops.definition`:

Definition
----------

.. code-block:: c

  struct tcf_ematch_ops {
    int kind;
    int datalen;
    int (* change) (struct net *net, void *,int, struct tcf_ematch *);
    int (* match) (struct sk_buff *, struct tcf_ematch *,struct tcf_pkt_info *);
    void (* destroy) (struct tcf_ematch *);
    int (* dump) (struct sk_buff *, struct tcf_ematch *);
    struct module * owner;
    struct list_head link;
  };


.. _`tcf_ematch_ops.members`:

Members
-------

:``kind``:
    identifier (kind) of this ematch module

:``datalen``:
    length of expected configuration data (optional)

:``change``:
    called during validation (optional)

:``match``:
    called during ematch tree evaluation, must return 1/0

:``destroy``:
    called during destroyage (optional)

:``dump``:
    called during dumping process (optional)

:``owner``:
    owner, must be set to THIS_MODULE

:``link``:
    link to previous/next ematch module (internal use)




.. _`tcf_em_tree_change`:

tcf_em_tree_change
==================

.. c:function:: void tcf_em_tree_change (struct tcf_proto *tp, struct tcf_ematch_tree *dst, struct tcf_ematch_tree *src)

    replace ematch tree of a running classifier

    :param struct tcf_proto \*tp:
        classifier kind handle

    :param struct tcf_ematch_tree \*dst:
        destination ematch tree variable

    :param struct tcf_ematch_tree \*src:
        source ematch tree (temporary tree from tcf_em_tree_validate)



.. _`tcf_em_tree_change.description`:

Description
-----------

This functions replaces the ematch tree in ``dst`` with the ematch
tree in ``src``\ . The classifier in charge of the ematch tree may be
running.



.. _`tcf_em_tree_match`:

tcf_em_tree_match
=================

.. c:function:: int tcf_em_tree_match (struct sk_buff *skb, struct tcf_ematch_tree *tree, struct tcf_pkt_info *info)

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

This function matches ``skb`` against the ematch tree in ``tree`` by going
through all ematches respecting their logic relations returning
as soon as the result is obvious.

Returns 1 if the ematch tree as-one matches, no ematches are configured
or ematch is not enabled in the kernel, otherwise 0 is returned.

