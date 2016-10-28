.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/include/audit.h

.. _`selinux_audit_rule_init`:

selinux_audit_rule_init
=======================

.. c:function:: int selinux_audit_rule_init(u32 field, u32 op, char *rulestr, void **rule)

    alloc/init an selinux audit rule structure.

    :param u32 field:
        the field this rule refers to

    :param u32 op:
        the operater the rule uses

    :param char \*rulestr:
        the text "target" of the rule

    :param void \*\*rule:
        pointer to the new rule structure returned via this

.. _`selinux_audit_rule_init.description`:

Description
-----------

Returns 0 if successful, -errno if not.  On success, the rule structure
will be allocated internally.  The caller must free this structure with
\ :c:func:`selinux_audit_rule_free`\  after use.

.. _`selinux_audit_rule_free`:

selinux_audit_rule_free
=======================

.. c:function:: void selinux_audit_rule_free(void *rule)

    free an selinux audit rule structure.

    :param void \*rule:
        pointer to the audit rule to be freed

.. _`selinux_audit_rule_free.description`:

Description
-----------

This will free all memory associated with the given rule.
If \ ``rule``\  is NULL, no operation is performed.

.. _`selinux_audit_rule_match`:

selinux_audit_rule_match
========================

.. c:function:: int selinux_audit_rule_match(u32 sid, u32 field, u32 op, void *rule, struct audit_context *actx)

    determine if a context ID matches a rule.

    :param u32 sid:
        the context ID to check

    :param u32 field:
        the field this rule refers to

    :param u32 op:
        the operater the rule uses

    :param void \*rule:
        pointer to the audit rule to check against

    :param struct audit_context \*actx:
        the audit context (can be NULL) associated with the check

.. _`selinux_audit_rule_match.description`:

Description
-----------

Returns 1 if the context id matches the rule, 0 if it does not, and
-errno on failure.

.. _`selinux_audit_rule_known`:

selinux_audit_rule_known
========================

.. c:function:: int selinux_audit_rule_known(struct audit_krule *krule)

    check to see if rule contains selinux fields.

    :param struct audit_krule \*krule:
        *undescribed*

.. This file was automatic generated / don't edit.

