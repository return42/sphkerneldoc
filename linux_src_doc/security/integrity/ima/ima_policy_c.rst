.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_policy.c

.. _`ima_match_rules`:

ima_match_rules
===============

.. c:function:: bool ima_match_rules(struct ima_rule_entry *rule, struct inode *inode, enum ima_hooks func, int mask)

    determine whether an inode matches the measure rule.

    :param struct ima_rule_entry \*rule:
        a pointer to a rule

    :param struct inode \*inode:
        a pointer to an inode

    :param enum ima_hooks func:
        LIM hook identifier

    :param int mask:
        requested action (MAY_READ \| MAY_WRITE \| MAY_APPEND \| MAY_EXEC)

.. _`ima_match_rules.description`:

Description
-----------

Returns true on rule match, false on failure.

.. _`ima_match_policy`:

ima_match_policy
================

.. c:function:: int ima_match_policy(struct inode *inode, enum ima_hooks func, int mask, int flags, int *pcr)

    decision based on LSM and other conditions

    :param struct inode \*inode:
        pointer to an inode for which the policy decision is being made

    :param enum ima_hooks func:
        IMA hook identifier

    :param int mask:
        requested action (MAY_READ \| MAY_WRITE \| MAY_APPEND \| MAY_EXEC)

    :param int flags:
        *undescribed*

    :param int \*pcr:
        set the pcr to extend

.. _`ima_match_policy.description`:

Description
-----------

Measure decision based on func/mask/fsmagic and LSM(subj/obj/type)
conditions.

Since the IMA policy may be updated multiple times we need to lock the
list when walking it.  Reads are many orders of magnitude more numerous
than writes so \ :c:func:`ima_match_policy`\  is classical RCU candidate.

.. _`ima_init_policy`:

ima_init_policy
===============

.. c:function:: void ima_init_policy( void)

    initialize the default measure rules.

    :param  void:
        no arguments

.. _`ima_init_policy.description`:

Description
-----------

ima_rules points to either the ima_default_rules or the
the new ima_policy_rules.

.. _`ima_update_policy`:

ima_update_policy
=================

.. c:function:: void ima_update_policy( void)

    update default_rules with new measure rules

    :param  void:
        no arguments

.. _`ima_update_policy.description`:

Description
-----------

Called on file .release to update the default rules with a complete new
policy.  What we do here is to splice ima_policy_rules and ima_temp_rules so
they make a queue.  The policy may be updated multiple times and this is the
RCU updater.

Policy rules are never deleted so ima_policy_flag gets zeroed only once when
we switch from the default policy to user defined.

.. _`ima_parse_add_rule`:

ima_parse_add_rule
==================

.. c:function:: ssize_t ima_parse_add_rule(char *rule)

    add a rule to ima_policy_rules \ ``rule``\  - ima measurement policy rule

    :param char \*rule:
        *undescribed*

.. _`ima_parse_add_rule.description`:

Description
-----------

Avoid locking by allowing just one writer at a time in \ :c:func:`ima_write_policy`\ 
Returns the length of the rule parsed, an error code on failure

.. _`ima_delete_rules`:

ima_delete_rules
================

.. c:function:: void ima_delete_rules( void)

    flight policy. We don't need locking as we operate on the temp list, which is different from the active one.  There is also only one user of \ :c:func:`ima_delete_rules`\  at a time.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

