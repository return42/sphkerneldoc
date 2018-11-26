.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/exthdrs.c

.. _`ipv6_renew_options`:

ipv6_renew_options
==================

.. c:function:: struct ipv6_txoptions *ipv6_renew_options(struct sock *sk, struct ipv6_txoptions *opt, int newtype, struct ipv6_opt_hdr *newopt)

    replace a specific ext hdr with a new one.

    :param sk:
        sock from which to allocate memory
    :type sk: struct sock \*

    :param opt:
        original options
    :type opt: struct ipv6_txoptions \*

    :param newtype:
        option type to replace in \ ``opt``\ 
    :type newtype: int

    :param newopt:
        new option of type \ ``newtype``\  to replace (user-mem)
    :type newopt: struct ipv6_opt_hdr \*

.. _`ipv6_renew_options.description`:

Description
-----------

Returns a new set of options which is a copy of \ ``opt``\  with the
option type \ ``newtype``\  replaced with \ ``newopt``\ .

\ ``opt``\  may be NULL, in which case a new set of options is returned
containing just \ ``newopt``\ .

\ ``newopt``\  may be NULL, in which case the specified option type is
not copied into the new set of options.

The new set of options is allocated from the socket option memory
buffer of \ ``sk``\ .

.. _`fl6_update_dst`:

fl6_update_dst
==============

.. c:function:: struct in6_addr *fl6_update_dst(struct flowi6 *fl6, const struct ipv6_txoptions *opt, struct in6_addr *orig)

    update flowi destination address with info given by srcrt option, if any.

    :param fl6:
        flowi6 for which daddr is to be updated
    :type fl6: struct flowi6 \*

    :param opt:
        struct ipv6_txoptions in which to look for srcrt opt
    :type opt: const struct ipv6_txoptions \*

    :param orig:
        copy of original daddr address if modified
    :type orig: struct in6_addr \*

.. _`fl6_update_dst.description`:

Description
-----------

Returns NULL if no txoptions or no srcrt, otherwise returns orig
and initial value of fl6->daddr set in orig

.. This file was automatic generated / don't edit.

