.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/include/audit.h

.. _`selinux_audit_rule_init`:

selinux_audit_rule_init
=======================

.. c:function:: int selinux_audit_rule_init(u32 field, u32 op, char *rulestr, void **rule)

    alloc/init an selinux audit rule structure.

    :param field:
        the field this rule refers to
    :type field: u32

    :param op:
        the operater the rule uses
    :type op: u32

    :param rulestr:
        the text "target" of the rule
    :type rulestr: char \*

    :param rule:
        pointer to the new rule structure returned via this
    :type rule: void \*\*

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

    :param rule:
        pointer to the audit rule to be freed
    :type rule: void \*

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

    :param sid:
        the context ID to check
    :type sid: u32

    :param field:
        the field this rule refers to
    :type field: u32

    :param op:
        the operater the rule uses
    :type op: u32

    :param rule:
        pointer to the audit rule to check against
    :type rule: void \*

    :param actx:
        the audit context (can be NULL) associated with the check
    :type actx: struct audit_context \*

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

    :param krule:
        *undescribed*
    :type krule: struct audit_krule \*

.. This file was automatic generated / don't edit.

