.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/smack/smack_access.c

.. _`smk_access_entry`:

smk_access_entry
================

.. c:function:: int smk_access_entry(char *subject_label, char *object_label, struct list_head *rule_list)

    look up matching access rule

    :param subject_label:
        a pointer to the subject's Smack label
    :type subject_label: char \*

    :param object_label:
        a pointer to the object's Smack label
    :type object_label: char \*

    :param rule_list:
        the list of rules to search
    :type rule_list: struct list_head \*

.. _`smk_access_entry.description`:

Description
-----------

This function looks up the subject/object pair in the
access rule list and returns the access mode. If no
entry is found returns -ENOENT.

.. _`smk_access_entry.note`:

NOTE
----


Earlier versions of this function allowed for labels that
were not on the label list. This was done to allow for
labels to come over the network that had never been seen
before on this host. Unless the receiving socket has the
star label this will always result in a failure check. The
star labeled socket case is now handled in the networking
hooks so there is no case where the label is not on the
label list. Checking to see if the address of two labels
is the same is now a reliable test.

Do the object check first because that is more
likely to differ.

Allowing write access implies allowing locking.

.. _`smk_access`:

smk_access
==========

.. c:function:: int smk_access(struct smack_known *subject, struct smack_known *object, int request, struct smk_audit_info *a)

    determine if a subject has a specific access to an object

    :param subject:
        a pointer to the subject's Smack label entry
    :type subject: struct smack_known \*

    :param object:
        a pointer to the object's Smack label entry
    :type object: struct smack_known \*

    :param request:
        the access requested, in "MAY" format
    :type request: int

    :param a:
        a pointer to the audit data
    :type a: struct smk_audit_info \*

.. _`smk_access.description`:

Description
-----------

This function looks up the subject/object pair in the
access rule list and returns 0 if the access is permitted,
non zero otherwise.

Smack labels are shared on smack_list

.. _`smk_tskacc`:

smk_tskacc
==========

.. c:function:: int smk_tskacc(struct task_smack *tsp, struct smack_known *obj_known, u32 mode, struct smk_audit_info *a)

    determine if a task has a specific access to an object

    :param tsp:
        a pointer to the subject's task
    :type tsp: struct task_smack \*

    :param obj_known:
        a pointer to the object's label entry
    :type obj_known: struct smack_known \*

    :param mode:
        the access requested, in "MAY" format
    :type mode: u32

    :param a:
        common audit data
    :type a: struct smk_audit_info \*

.. _`smk_tskacc.description`:

Description
-----------

This function checks the subject task's label/object label pair
in the access rule list and returns 0 if the access is permitted,
non zero otherwise. It allows that the task may have the capability
to override the rules.

.. _`smk_curacc`:

smk_curacc
==========

.. c:function:: int smk_curacc(struct smack_known *obj_known, u32 mode, struct smk_audit_info *a)

    determine if current has a specific access to an object

    :param obj_known:
        a pointer to the object's Smack label entry
    :type obj_known: struct smack_known \*

    :param mode:
        the access requested, in "MAY" format
    :type mode: u32

    :param a:
        common audit data
    :type a: struct smk_audit_info \*

.. _`smk_curacc.description`:

Description
-----------

This function checks the current subject label/object label pair
in the access rule list and returns 0 if the access is permitted,
non zero otherwise. It allows that current may have the capability
to override the rules.

.. _`smack_str_from_perm`:

smack_str_from_perm
===================

.. c:function:: void smack_str_from_perm(char *string, int access)

    helper to transalate an int to a readable string

    :param string:
        the string to fill
    :type string: char \*

    :param access:
        the int
    :type access: int

.. _`smack_log_callback`:

smack_log_callback
==================

.. c:function:: void smack_log_callback(struct audit_buffer *ab, void *a)

    SMACK specific information will be called by generic audit code

    :param ab:
        the audit_buffer
    :type ab: struct audit_buffer \*

    :param a:
        audit_data
    :type a: void \*

.. _`smack_log`:

smack_log
=========

.. c:function:: void smack_log(char *subject_label, char *object_label, int request, int result, struct smk_audit_info *ad)

    Audit the granting or denial of permissions.

    :param subject_label:
        smack label of the requester
    :type subject_label: char \*

    :param object_label:
        smack label of the object being accessed
    :type object_label: char \*

    :param request:
        requested permissions
    :type request: int

    :param result:
        result from smk_access
    :type result: int

    :param ad:
        *undescribed*
    :type ad: struct smk_audit_info \*

.. _`smack_log.description`:

Description
-----------

Audit the granting or denial of permissions in accordance
with the policy.

.. _`smk_insert_entry`:

smk_insert_entry
================

.. c:function:: void smk_insert_entry(struct smack_known *skp)

    insert a smack label into a hash map,

    :param skp:
        *undescribed*
    :type skp: struct smack_known \*

.. _`smk_insert_entry.description`:

Description
-----------

this function must be called under smack_known_lock

.. _`smk_find_entry`:

smk_find_entry
==============

.. c:function:: struct smack_known *smk_find_entry(const char *string)

    find a label on the list, return the list entry

    :param string:
        a text string that might be a Smack label
    :type string: const char \*

.. _`smk_find_entry.description`:

Description
-----------

Returns a pointer to the entry in the label list that
matches the passed string or NULL if not found.

.. _`smk_parse_smack`:

smk_parse_smack
===============

.. c:function:: char *smk_parse_smack(const char *string, int len)

    parse smack label from a text string

    :param string:
        a text string that might contain a Smack label
    :type string: const char \*

    :param len:
        the maximum size, or zero if it is NULL terminated.
    :type len: int

.. _`smk_parse_smack.description`:

Description
-----------

Returns a pointer to the clean label or an error code.

.. _`smk_netlbl_mls`:

smk_netlbl_mls
==============

.. c:function:: int smk_netlbl_mls(int level, char *catset, struct netlbl_lsm_secattr *sap, int len)

    convert a catset to netlabel mls categories

    :param level:
        *undescribed*
    :type level: int

    :param catset:
        the Smack categories
    :type catset: char \*

    :param sap:
        where to put the netlabel categories
    :type sap: struct netlbl_lsm_secattr \*

    :param len:
        *undescribed*
    :type len: int

.. _`smk_netlbl_mls.description`:

Description
-----------

Allocates and fills attr.mls
Returns 0 on success, error code on failure.

.. _`smk_import_entry`:

smk_import_entry
================

.. c:function:: struct smack_known *smk_import_entry(const char *string, int len)

    import a label, return the list entry

    :param string:
        a text string that might be a Smack label
    :type string: const char \*

    :param len:
        the maximum size, or zero if it is NULL terminated.
    :type len: int

.. _`smk_import_entry.description`:

Description
-----------

Returns a pointer to the entry in the label list that
matches the passed string, adding it if necessary,
or an error code.

.. _`smack_from_secid`:

smack_from_secid
================

.. c:function:: struct smack_known *smack_from_secid(const u32 secid)

    find the Smack label associated with a secid

    :param secid:
        an integer that might be associated with a Smack label
    :type secid: const u32

.. _`smack_from_secid.description`:

Description
-----------

Returns a pointer to the appropriate Smack label entry if there is one,
otherwise a pointer to the invalid Smack label.

.. _`smack_privileged_cred`:

smack_privileged_cred
=====================

.. c:function:: bool smack_privileged_cred(int cap, const struct cred *cred)

    are all privilege requirements met by cred

    :param cap:
        The requested capability
    :type cap: int

    :param cred:
        the credential to use
    :type cred: const struct cred \*

.. _`smack_privileged_cred.description`:

Description
-----------

Is the task privileged and allowed to be privileged
by the onlycap rule.

Returns true if the task is allowed to be privileged, false if it's not.

.. _`smack_privileged`:

smack_privileged
================

.. c:function:: bool smack_privileged(int cap)

    are all privilege requirements met

    :param cap:
        The requested capability
    :type cap: int

.. _`smack_privileged.description`:

Description
-----------

Is the task privileged and allowed to be privileged
by the onlycap rule.

Returns true if the task is allowed to be privileged, false if it's not.

.. This file was automatic generated / don't edit.

