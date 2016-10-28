.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/policy_unpack.c

.. _`audit_iface`:

audit_iface
===========

.. c:function:: int audit_iface(struct aa_profile *new, const char *name, const char *info, struct aa_ext *e, int error)

    do audit message for policy unpacking/load/replace/remove

    :param struct aa_profile \*new:
        profile if it has been allocated (MAYBE NULL)

    :param const char \*name:
        name of the profile being manipulated (MAYBE NULL)

    :param const char \*info:
        any extra info about the failure (MAYBE NULL)

    :param struct aa_ext \*e:
        buffer position info

    :param int error:
        error code

.. _`audit_iface.return`:

Return
------

\ ``0``\  or error

.. _`unpack_u16_chunk`:

unpack_u16_chunk
================

.. c:function:: size_t unpack_u16_chunk(struct aa_ext *e, char **chunk)

    test and do bounds checking for a u16 size based chunk

    :param struct aa_ext \*e:
        serialized data read head (NOT NULL)

    :param char \*\*chunk:
        start address for chunk of data (NOT NULL)

.. _`unpack_u16_chunk.return`:

Return
------

the size of chunk found with the read head at the end of the chunk.

.. _`unpack_namex`:

unpack_nameX
============

.. c:function:: bool unpack_nameX(struct aa_ext *e, enum aa_code code, const char *name)

    check is the next element is of type X with a name of \ ``name``\ 

    :param struct aa_ext \*e:
        serialized data extent information  (NOT NULL)

    :param enum aa_code code:
        type code

    :param const char \*name:
        name to match to the serialized element.  (MAYBE NULL)

.. _`unpack_namex.description`:

Description
-----------

check that the next serialized data element is of type X and has a tag
name \ ``name``\ .  If \ ``name``\  is specified then there must be a matching
name element in the stream.  If \ ``name``\  is NULL any name element will be
skipped and only the typecode will be tested.

Returns 1 on success (both type code and name tests match) and the read
head is advanced past the headers

.. _`unpack_namex.return`:

Return
------

0 if either match fails, the read head does not move

.. _`verify_accept`:

verify_accept
=============

.. c:function:: bool verify_accept(struct aa_dfa *dfa, int flags)

    verify the accept tables of a dfa

    :param struct aa_dfa \*dfa:
        dfa to verify accept tables of (NOT NULL)

    :param int flags:
        flags governing dfa

.. _`verify_accept.return`:

Return
------

1 if valid accept tables else 0 if error

.. _`unpack_dfa`:

unpack_dfa
==========

.. c:function:: struct aa_dfa *unpack_dfa(struct aa_ext *e)

    unpack a file rule dfa

    :param struct aa_ext \*e:
        serialized data extent information (NOT NULL)

.. _`unpack_dfa.description`:

Description
-----------

returns dfa or ERR_PTR or NULL if no dfa

.. _`unpack_trans_table`:

unpack_trans_table
==================

.. c:function:: bool unpack_trans_table(struct aa_ext *e, struct aa_profile *profile)

    unpack a profile transition table

    :param struct aa_ext \*e:
        serialized data extent information  (NOT NULL)

    :param struct aa_profile \*profile:
        profile to add the accept table to (NOT NULL)

.. _`unpack_trans_table.return`:

Return
------

1 if table successfully unpacked

.. _`unpack_profile`:

unpack_profile
==============

.. c:function:: struct aa_profile *unpack_profile(struct aa_ext *e)

    unpack a serialized profile

    :param struct aa_ext \*e:
        serialized data extent information (NOT NULL)

.. _`unpack_profile.note`:

NOTE
----

unpack profile sets audit struct if there is a failure

.. _`verify_header`:

verify_header
=============

.. c:function:: int verify_header(struct aa_ext *e, int required, const char **ns)

    unpack serialized stream header

    :param struct aa_ext \*e:
        serialized data read head (NOT NULL)

    :param int required:
        whether the header is required or optional

    :param const char \*\*ns:
        Returns - namespace if one is specified else NULL (NOT NULL)

.. _`verify_header.return`:

Return
------

error or 0 if header is good

.. _`verify_profile`:

verify_profile
==============

.. c:function:: int verify_profile(struct aa_profile *profile)

    Do post unpack analysis to verify profile consistency

    :param struct aa_profile \*profile:
        profile to verify (NOT NULL)

.. _`verify_profile.return`:

Return
------

0 if passes verification else error

.. _`aa_unpack`:

aa_unpack
=========

.. c:function:: int aa_unpack(void *udata, size_t size, struct list_head *lh, const char **ns)

    unpack packed binary profile(s) data loaded from user space

    :param void \*udata:
        user data copied to kmem  (NOT NULL)

    :param size_t size:
        the size of the user data

    :param struct list_head \*lh:
        list to place unpacked profiles in a aa_repl_ws

    :param const char \*\*ns:
        Returns namespace profile is in if specified else NULL (NOT NULL)

.. _`aa_unpack.description`:

Description
-----------

Unpack user data and return refcounted allocated profile(s) stored in
\ ``lh``\  in order of discovery, with the list chain stored in base.list
or error

.. _`aa_unpack.return`:

Return
------

profile(s) on \ ``lh``\  else error pointer if fails to unpack

.. This file was automatic generated / don't edit.

