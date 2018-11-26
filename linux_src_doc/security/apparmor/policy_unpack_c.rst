.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/policy_unpack.c

.. _`audit_iface`:

audit_iface
===========

.. c:function:: int audit_iface(struct aa_profile *new, const char *ns_name, const char *name, const char *info, struct aa_ext *e, int error)

    do audit message for policy unpacking/load/replace/remove

    :param new:
        profile if it has been allocated (MAYBE NULL)
    :type new: struct aa_profile \*

    :param ns_name:
        name of the ns the profile is to be loaded to (MAY BE NULL)
    :type ns_name: const char \*

    :param name:
        name of the profile being manipulated (MAYBE NULL)
    :type name: const char \*

    :param info:
        any extra info about the failure (MAYBE NULL)
    :type info: const char \*

    :param e:
        buffer position info
    :type e: struct aa_ext \*

    :param error:
        error code
    :type error: int

.. _`audit_iface.return`:

Return
------

\ ``0``\  or error

.. _`unpack_u16_chunk`:

unpack_u16_chunk
================

.. c:function:: size_t unpack_u16_chunk(struct aa_ext *e, char **chunk)

    test and do bounds checking for a u16 size based chunk

    :param e:
        serialized data read head (NOT NULL)
    :type e: struct aa_ext \*

    :param chunk:
        start address for chunk of data (NOT NULL)
    :type chunk: char \*\*

.. _`unpack_u16_chunk.return`:

Return
------

the size of chunk found with the read head at the end of the chunk.

.. _`unpack_namex`:

unpack_nameX
============

.. c:function:: bool unpack_nameX(struct aa_ext *e, enum aa_code code, const char *name)

    check is the next element is of type X with a name of \ ``name``\ 

    :param e:
        serialized data extent information  (NOT NULL)
    :type e: struct aa_ext \*

    :param code:
        type code
    :type code: enum aa_code

    :param name:
        name to match to the serialized element.  (MAYBE NULL)
    :type name: const char \*

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

.. _`unpack_dfa`:

unpack_dfa
==========

.. c:function:: struct aa_dfa *unpack_dfa(struct aa_ext *e)

    unpack a file rule dfa

    :param e:
        serialized data extent information (NOT NULL)
    :type e: struct aa_ext \*

.. _`unpack_dfa.description`:

Description
-----------

returns dfa or ERR_PTR or NULL if no dfa

.. _`unpack_trans_table`:

unpack_trans_table
==================

.. c:function:: bool unpack_trans_table(struct aa_ext *e, struct aa_profile *profile)

    unpack a profile transition table

    :param e:
        serialized data extent information  (NOT NULL)
    :type e: struct aa_ext \*

    :param profile:
        profile to add the accept table to (NOT NULL)
    :type profile: struct aa_profile \*

.. _`unpack_trans_table.return`:

Return
------

1 if table successfully unpacked

.. _`unpack_profile`:

unpack_profile
==============

.. c:function:: struct aa_profile *unpack_profile(struct aa_ext *e, char **ns_name)

    unpack a serialized profile

    :param e:
        serialized data extent information (NOT NULL)
    :type e: struct aa_ext \*

    :param ns_name:
        *undescribed*
    :type ns_name: char \*\*

.. _`unpack_profile.note`:

NOTE
----

unpack profile sets audit struct if there is a failure

.. _`verify_header`:

verify_header
=============

.. c:function:: int verify_header(struct aa_ext *e, int required, const char **ns)

    unpack serialized stream header

    :param e:
        serialized data read head (NOT NULL)
    :type e: struct aa_ext \*

    :param required:
        whether the header is required or optional
    :type required: int

    :param ns:
        Returns - namespace if one is specified else NULL (NOT NULL)
    :type ns: const char \*\*

.. _`verify_header.return`:

Return
------

error or 0 if header is good

.. _`verify_profile`:

verify_profile
==============

.. c:function:: int verify_profile(struct aa_profile *profile)

    Do post unpack analysis to verify profile consistency

    :param profile:
        profile to verify (NOT NULL)
    :type profile: struct aa_profile \*

.. _`verify_profile.return`:

Return
------

0 if passes verification else error

.. _`aa_unpack`:

aa_unpack
=========

.. c:function:: int aa_unpack(struct aa_loaddata *udata, struct list_head *lh, const char **ns)

    unpack packed binary profile(s) data loaded from user space

    :param udata:
        user data copied to kmem  (NOT NULL)
    :type udata: struct aa_loaddata \*

    :param lh:
        list to place unpacked profiles in a aa_repl_ws
    :type lh: struct list_head \*

    :param ns:
        Returns namespace profile is in if specified else NULL (NOT NULL)
    :type ns: const char \*\*

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

