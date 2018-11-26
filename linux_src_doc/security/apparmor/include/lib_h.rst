.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/lib.h

.. _`aa_strneq`:

aa_strneq
=========

.. c:function:: bool aa_strneq(const char *str, const char *sub, int len)

    compare null terminated \ ``str``\  to a non null terminated substring

    :param str:
        a null terminated string
    :type str: const char \*

    :param sub:
        a substring, not necessarily null terminated
    :type sub: const char \*

    :param len:
        length of \ ``sub``\  to compare
    :type len: int

.. _`aa_strneq.description`:

Description
-----------

The \ ``str``\  string must be full consumed for this to be considered a match

.. _`aa_dfa_null_transition`:

aa_dfa_null_transition
======================

.. c:function:: unsigned int aa_dfa_null_transition(struct aa_dfa *dfa, unsigned int start)

    step to next state after null character

    :param dfa:
        the dfa to match against
    :type dfa: struct aa_dfa \*

    :param start:
        the state of the dfa to start matching in
    :type start: unsigned int

.. _`aa_dfa_null_transition.description`:

Description
-----------

aa_dfa_null_transition transitions to the next state after a null
character which is not used in standard matching and is only
used to separate pairs.

.. _`basename`:

basename
========

.. c:function:: const char *basename(const char *hname)

    find the last component of an hname

    :param hname:
        *undescribed*
    :type hname: const char \*

.. _`basename.return`:

Return
------

the tail (base profile name) name component of an hname

.. _`__policy_find`:

\__policy_find
==============

.. c:function:: struct aa_policy *__policy_find(struct list_head *head, const char *name)

    find a policy by \ ``name``\  on a policy list

    :param head:
        list to search  (NOT NULL)
    :type head: struct list_head \*

    :param name:
        name to search for  (NOT NULL)
    :type name: const char \*

.. _`__policy_find.requires`:

Requires
--------

rcu_read_lock be held

.. _`__policy_find.return`:

Return
------

unrefcounted policy that match \ ``name``\  or NULL if not found

.. _`__policy_strn_find`:

\__policy_strn_find
===================

.. c:function:: struct aa_policy *__policy_strn_find(struct list_head *head, const char *str, int len)

    find a policy that's name matches \ ``len``\  chars of \ ``str``\ 

    :param head:
        list to search  (NOT NULL)
    :type head: struct list_head \*

    :param str:
        string to search for  (NOT NULL)
    :type str: const char \*

    :param len:
        length of match required
    :type len: int

.. _`__policy_strn_find.requires`:

Requires
--------

rcu_read_lock be held

.. _`__policy_strn_find.return`:

Return
------

unrefcounted policy that match \ ``str``\  or NULL if not found

if \ ``len``\  == strlen(@strlen) then this is equiv to \__policy_find
other wise it allows searching for policy by a partial match of name

.. This file was automatic generated / don't edit.

