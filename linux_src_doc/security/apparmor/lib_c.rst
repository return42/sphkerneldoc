.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/lib.c

.. _`aa_split_fqname`:

aa_split_fqname
===============

.. c:function:: char *aa_split_fqname(char *fqname, char **ns_name)

    split a fqname into a profile and namespace name

    :param char \*fqname:
        a full qualified name in namespace profile format (NOT NULL)

    :param char \*\*ns_name:
        pointer to portion of the string containing the ns name (NOT NULL)

.. _`aa_split_fqname.return`:

Return
------

profile name or NULL if one is not specified

Split a namespace name from a profile name (see policy.c for naming
description).  If a portion of the name is missing it returns NULL for
that portion.

.. _`aa_split_fqname.note`:

NOTE
----

may modify the \ ``fqname``\  string.  The pointers returned point
into the \ ``fqname``\  string.

.. _`skipn_spaces`:

skipn_spaces
============

.. c:function:: const char *skipn_spaces(const char *str, size_t n)

    Removes leading whitespace from \ ``str``\ .

    :param const char \*str:
        The string to be stripped.

    :param size_t n:
        *undescribed*

.. _`skipn_spaces.description`:

Description
-----------

Returns a pointer to the first non-whitespace character in \ ``str``\ .
if all whitespace will return NULL

.. _`aa_info_message`:

aa_info_message
===============

.. c:function:: void aa_info_message(const char *str)

    log a none profile related status message

    :param const char \*str:
        message to log

.. _`aa_policy_init`:

aa_policy_init
==============

.. c:function:: bool aa_policy_init(struct aa_policy *policy, const char *prefix, const char *name, gfp_t gfp)

    initialize a policy structure

    :param struct aa_policy \*policy:
        policy to initialize  (NOT NULL)

    :param const char \*prefix:
        prefix name if any is required.  (MAYBE NULL)

    :param const char \*name:
        name of the policy, init will make a copy of it  (NOT NULL)

    :param gfp_t gfp:
        *undescribed*

.. _`aa_policy_init.note`:

Note
----

this fn creates a copy of strings passed in

.. _`aa_policy_init.return`:

Return
------

true if policy init successful

.. _`aa_policy_destroy`:

aa_policy_destroy
=================

.. c:function:: void aa_policy_destroy(struct aa_policy *policy)

    free the elements referenced by \ ``policy``\ 

    :param struct aa_policy \*policy:
        policy that is to have its elements freed  (NOT NULL)

.. This file was automatic generated / don't edit.

