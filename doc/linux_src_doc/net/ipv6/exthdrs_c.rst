.. -*- coding: utf-8; mode: rst -*-

=========
exthdrs.c
=========


.. _`fl6_update_dst`:

fl6_update_dst
==============

.. c:function:: struct in6_addr *fl6_update_dst (struct flowi6 *fl6, const struct ipv6_txoptions *opt, struct in6_addr *orig)

    update flowi destination address with info given by srcrt option, if any.

    :param struct flowi6 \*fl6:
        flowi6 for which daddr is to be updated

    :param const struct ipv6_txoptions \*opt:
        struct ipv6_txoptions in which to look for srcrt opt

    :param struct in6_addr \*orig:
        copy of original daddr address if modified



.. _`fl6_update_dst.description`:

Description
-----------

Returns NULL if no txoptions or no srcrt, otherwise returns orig
and initial value of fl6->daddr set in orig

