.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_policy.c

.. _`ima_match_rules`:

ima_match_rules
===============

.. c:function:: bool ima_match_rules(struct ima_rule_entry *rule, struct inode *inode, const struct cred *cred, u32 secid, enum ima_hooks func, int mask)

    determine whether an inode matches the measure rule.

    :param rule:
        a pointer to a rule
    :type rule: struct ima_rule_entry \*

    :param inode:
        a pointer to an inode
    :type inode: struct inode \*

    :param cred:
        a pointer to a credentials structure for user validation
    :type cred: const struct cred \*

    :param secid:
        the secid of the task to be validated
    :type secid: u32

    :param func:
        LIM hook identifier
    :type func: enum ima_hooks

    :param mask:
        requested action (MAY_READ \| MAY_WRITE \| MAY_APPEND \| MAY_EXEC)
    :type mask: int

.. _`ima_match_rules.description`:

Description
-----------

Returns true on rule match, false on failure.

.. _`ima_match_policy`:

ima_match_policy
================

.. c:function:: int ima_match_policy(struct inode *inode, const struct cred *cred, u32 secid, enum ima_hooks func, int mask, int flags, int *pcr)

    decision based on LSM and other conditions

    :param inode:
        pointer to an inode for which the policy decision is being made
    :type inode: struct inode \*

    :param cred:
        pointer to a credentials structure for which the policy decision is
        being made
    :type cred: const struct cred \*

    :param secid:
        LSM secid of the task to be validated
    :type secid: u32

    :param func:
        IMA hook identifier
    :type func: enum ima_hooks

    :param mask:
        requested action (MAY_READ \| MAY_WRITE \| MAY_APPEND \| MAY_EXEC)
    :type mask: int

    :param flags:
        *undescribed*
    :type flags: int

    :param pcr:
        set the pcr to extend
    :type pcr: int \*

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

    :param void:
        no arguments
    :type void: 

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

    :param void:
        no arguments
    :type void: 

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

    :param rule:
        *undescribed*
    :type rule: char \*

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

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

