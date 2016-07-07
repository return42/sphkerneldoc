.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/match.c

.. _`unpack_table`:

unpack_table
============

.. c:function:: struct table_header *unpack_table(char *blob, size_t bsize)

    unpack a dfa table (one of accept, default, base, next check)

    :param char \*blob:
        data to unpack (NOT NULL)

    :param size_t bsize:
        size of blob

.. _`unpack_table.return`:

Return
------

pointer to table else NULL on failure

.. _`unpack_table.note`:

NOTE
----

must be freed by kvfree (not kfree)

.. _`verify_dfa`:

verify_dfa
==========

.. c:function:: int verify_dfa(struct aa_dfa *dfa, int flags)

    verify that transitions and states in the tables are in bounds.

    :param struct aa_dfa \*dfa:
        dfa to test  (NOT NULL)

    :param int flags:
        flags controlling what type of accept table are acceptable

.. _`verify_dfa.description`:

Description
-----------

Assumes dfa has gone through the first pass verification done by unpacking

.. _`verify_dfa.note`:

NOTE
----

this does not valid accept table values

.. _`verify_dfa.return`:

Return
------

\ ``0``\  else error code on failure to verify

.. _`dfa_free`:

dfa_free
========

.. c:function:: void dfa_free(struct aa_dfa *dfa)

    free a dfa allocated by aa_dfa_unpack

    :param struct aa_dfa \*dfa:
        the dfa to free  (MAYBE NULL)

.. _`dfa_free.requires`:

Requires
--------

reference count to dfa == 0

.. _`aa_dfa_free_kref`:

aa_dfa_free_kref
================

.. c:function:: void aa_dfa_free_kref(struct kref *kref)

    free aa_dfa by kref (called by aa_put_dfa)

    :param struct kref \*kref:
        *undescribed*

.. _`aa_dfa_unpack`:

aa_dfa_unpack
=============

.. c:function:: struct aa_dfa *aa_dfa_unpack(void *blob, size_t size, int flags)

    unpack the binary tables of a serialized dfa

    :param void \*blob:
        aligned serialized stream of data to unpack  (NOT NULL)

    :param size_t size:
        size of data to unpack

    :param int flags:
        flags controlling what type of accept tables are acceptable

.. _`aa_dfa_unpack.description`:

Description
-----------

Unpack a dfa that has been serialized.  To find information on the dfa
format look in Documentation/security/apparmor.txt
Assumes the dfa \ ``blob``\  stream has been aligned on a 8 byte boundary

.. _`aa_dfa_unpack.return`:

Return
------

an unpacked dfa ready for matching or ERR_PTR on failure

.. _`aa_dfa_match_len`:

aa_dfa_match_len
================

.. c:function:: unsigned int aa_dfa_match_len(struct aa_dfa *dfa, unsigned int start, const char *str, int len)

    traverse \ ``dfa``\  to find state \ ``str``\  stops at

    :param struct aa_dfa \*dfa:
        the dfa to match \ ``str``\  against  (NOT NULL)

    :param unsigned int start:
        the state of the dfa to start matching in

    :param const char \*str:
        the string of bytes to match against the dfa  (NOT NULL)

    :param int len:
        length of the string of bytes to match

.. _`aa_dfa_match_len.description`:

Description
-----------

aa_dfa_match_len will match \ ``str``\  against the dfa and return the state it
finished matching in. The final state can be used to look up the accepting
label, or as the start state of a continuing match.

This function will happily match again the 0 byte and only finishes
when \ ``len``\  input is consumed.

.. _`aa_dfa_match_len.return`:

Return
------

final state reached after input is consumed

.. _`aa_dfa_match`:

aa_dfa_match
============

.. c:function:: unsigned int aa_dfa_match(struct aa_dfa *dfa, unsigned int start, const char *str)

    traverse \ ``dfa``\  to find state \ ``str``\  stops at

    :param struct aa_dfa \*dfa:
        the dfa to match \ ``str``\  against  (NOT NULL)

    :param unsigned int start:
        the state of the dfa to start matching in

    :param const char \*str:
        the null terminated string of bytes to match against the dfa (NOT NULL)

.. _`aa_dfa_match.description`:

Description
-----------

aa_dfa_match will match \ ``str``\  against the dfa and return the state it
finished matching in. The final state can be used to look up the accepting
label, or as the start state of a continuing match.

.. _`aa_dfa_match.return`:

Return
------

final state reached after input is consumed

.. _`aa_dfa_next`:

aa_dfa_next
===========

.. c:function:: unsigned int aa_dfa_next(struct aa_dfa *dfa, unsigned int state, const char c)

    step one character to the next state in the dfa

    :param struct aa_dfa \*dfa:
        the dfa to tranverse (NOT NULL)

    :param unsigned int state:
        the state to start in

    :param const char c:
        the input character to transition on

.. _`aa_dfa_next.description`:

Description
-----------

aa_dfa_match will step through the dfa by one input character \ ``c``\ 

.. _`aa_dfa_next.return`:

Return
------

state reach after input \ ``c``\ 

.. This file was automatic generated / don't edit.

