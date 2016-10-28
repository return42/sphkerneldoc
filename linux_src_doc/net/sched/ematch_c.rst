.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sched/ematch.c

.. _`tcf_em_register`:

tcf_em_register
===============

.. c:function:: int tcf_em_register(struct tcf_ematch_ops *ops)

    register an extended match

    :param struct tcf_ematch_ops \*ops:
        ematch operations lookup table

.. _`tcf_em_register.description`:

Description
-----------

This function must be called by ematches to announce their presence.
The given \ ``ops``\  must have kind set to a unique identifier and the
callback \ :c:func:`match`\  must be implemented. All other callbacks are optional
and a fallback implementation is used instead.

Returns -EEXISTS if an ematch of the same kind has already registered.

.. _`tcf_em_unregister`:

tcf_em_unregister
=================

.. c:function:: void tcf_em_unregister(struct tcf_ematch_ops *ops)

    unregster and extended match

    :param struct tcf_ematch_ops \*ops:
        ematch operations lookup table

.. _`tcf_em_unregister.description`:

Description
-----------

This function must be called by ematches to announce their disappearance
for examples when the module gets unloaded. The \ ``ops``\  parameter must be
the same as the one used for registration.

Returns -ENOENT if no matching ematch was found.

.. _`tcf_em_tree_validate`:

tcf_em_tree_validate
====================

.. c:function:: int tcf_em_tree_validate(struct tcf_proto *tp, struct nlattr *nla, struct tcf_ematch_tree *tree)

    validate ematch config TLV and build ematch tree

    :param struct tcf_proto \*tp:
        classifier kind handle

    :param struct nlattr \*nla:
        ematch tree configuration TLV

    :param struct tcf_ematch_tree \*tree:
        destination ematch tree variable to store the resulting
        ematch tree.

.. _`tcf_em_tree_validate.description`:

Description
-----------

This function validates the given configuration TLV \ ``nla``\  and builds an
ematch tree in \ ``tree``\ . The resulting tree must later be copied into
the private classifier data using \ :c:func:`tcf_em_tree_change`\ . You MUST NOT
provide the ematch tree variable of the private classifier data directly,
the changes would not be locked properly.

Returns a negative error code if the configuration TLV contains errors.

.. _`tcf_em_tree_destroy`:

tcf_em_tree_destroy
===================

.. c:function:: void tcf_em_tree_destroy(struct tcf_ematch_tree *tree)

    destroy an ematch tree

    :param struct tcf_ematch_tree \*tree:
        ematch tree to be deleted

.. _`tcf_em_tree_destroy.description`:

Description
-----------

This functions destroys an ematch tree previously created by
\ :c:func:`tcf_em_tree_validate`\ /\ :c:func:`tcf_em_tree_change`\ . You must ensure that
the ematch tree is not in use before calling this function.

.. _`tcf_em_tree_dump`:

tcf_em_tree_dump
================

.. c:function:: int tcf_em_tree_dump(struct sk_buff *skb, struct tcf_ematch_tree *tree, int tlv)

    dump ematch tree into a rtnl message

    :param struct sk_buff \*skb:
        skb holding the rtnl message

    :param struct tcf_ematch_tree \*tree:
        *undescribed*

    :param int tlv:
        TLV type to be used to encapsulate the tree

.. _`tcf_em_tree_dump.description`:

Description
-----------

This function dumps a ematch tree into a rtnl message. It is valid to
call this function while the ematch tree is in use.

Returns -1 if the skb tailroom is insufficient.

.. This file was automatic generated / don't edit.

