.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/apparmor.h

.. _`aa_strneq`:

aa_strneq
=========

.. c:function:: bool aa_strneq(const char *str, const char *sub, int len)

    compare null terminated \ ``str``\  to a non null terminated substring

    :param const char \*str:
        a null terminated string

    :param const char \*sub:
        a substring, not necessarily null terminated

    :param int len:
        length of \ ``sub``\  to compare

.. _`aa_strneq.description`:

Description
-----------

The \ ``str``\  string must be full consumed for this to be considered a match

.. _`aa_dfa_null_transition`:

aa_dfa_null_transition
======================

.. c:function:: unsigned int aa_dfa_null_transition(struct aa_dfa *dfa, unsigned int start)

    step to next state after null character

    :param struct aa_dfa \*dfa:
        the dfa to match against

    :param unsigned int start:
        the state of the dfa to start matching in

.. _`aa_dfa_null_transition.description`:

Description
-----------

aa_dfa_null_transition transitions to the next state after a null
character which is not used in standard matching and is only
used to separate pairs.

.. This file was automatic generated / don't edit.

